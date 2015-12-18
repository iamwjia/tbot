# This file is part of tbot.  tbot is free software: you can
# redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, version 2.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc., 51
# Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# start with
# python2.7 src/common/tbot.py -c tbot_aristainetos2.cfg -t tc_ub_aristainetos2_ubi.py
# ubi testcases for the aristainetos2 board
#
import time
from tbotlib import tbot

#set board state for which the tc is valid
tb.set_board_state("u-boot")

#this board needs some time to settle
time.sleep(10)

#load ub tbot environment
tb.eof_call_tc("tc_ub_load_board_env.py")

# probe spi nor
tb.eof_write_con("sf probe")

#nand tests
tb.tc_ub_ubi_prep_offset = '4096'
tb.tc_ub_ubi_prep_partname = 'ubi'
tb.eof_call_tc("tc_ub_ubi_prepare.py")

#check if rootfs volume exists
tb.tc_ub_ubifs_vol_exist_name = 'rootfs'
tb.eof_call_tc("tc_ub_ubifs_check_vol_exist.py")
if tb.tc_return:
    print("EXISTING")
else:
    print("NOT EXISTING")
#  delete it
#  check if rootfs volume exists, must fail
#and create it
#check if rootfs volume exists

#get file
tb.tc_ub_tftp_file_addr = tb.tc_ub_ubi_write_addr
tb.tc_ub_tftp_file_name = '/tftpboot/aristainetos/tbot/rootfs-minimal.ubifs'
tb.eof_call_tc("tc_ub_tftp_file.py")

#write it in ubi volume
tb.tc_ub_ubi_write_len = '0xc00000'
tb.tc_ub_ubi_write_vol_name = 'rootfs'
tb.eof_call_tc("tc_ub_ubi_write.py")

#read file from ubi volume
tb.tc_ub_ubi_read_addr = '11000000'
tb.tc_ub_ubi_read_vol_name = tb.tc_ub_ubi_write_vol_name
tb.tc_ub_ubi_read_len = tb.tc_ub_ubi_write_len
tb.eof_call_tc("tc_ub_ubi_read.py")

#cmp if all bytes are the same
tmp = 'cmp.b ' + tb.tc_ub_ubi_load_addr + ' ' + tb.tc_ub_ubi_write_addr + ' ' + tb.tc_ub_ubi_write_len
tb.eof_write_con(tmp)
tb.eof_search_str_in_readline_end_con("!=")
tb.eof_read_end_state_con(1)

#mount ubifs
tb.eof_call_tc("tc_ub_ubifs_mount.py")
#ls "/"
tb.tc_ub_ubifs_ls_dir = '/'
tb.eof_call_tc("tc_ub_ubifs_ls.py")

#nor tests
tb.tc_ub_ubi_prep_offset = '64'
tb.tc_ub_ubi_prep_partname = 'rescue-system'
tb.tc_ub_ubi_load_name = 'kernel'
tb.eof_call_tc("tc_ub_ubi_prepare.py")
tb.eof_call_tc("tc_ub_ubi_check_volume.py")

#write file into kernel volume
tb.tftp_addr_r = tb.tc_ub_ubi_write_addr
tb.tftp_file = '/tftpboot/aristainetos/tbot/aristainetos2.itb'
tb.eof_call_tc("tc_ub_tftp_file.py")

read_line_retry_save=tb.read_line_retry
tb.read_line_retry=1000
tb.tc_ub_ubi_write_vol_name = 'kernel'
tb.eof_call_tc("tc_ub_ubi_write.py")

#read file from kernel partition
tb.tc_ub_ubi_load_addr = '11000000'
tb.eof_call_tc("tc_ub_ubi_load.py")

#compare it with original
#tmp = "cmp.b 11000000 14000000 ${filesize}"
# does not work ... console hangs
tmp = "run tbot_cmp_ubi"
tb.eof_write_con(tmp)
tb.eof_search_str_in_readline_end_con("!=")
tb.read_line_retry=read_line_retry_save
tb.eof_read_end_state_con(1)

# power off board at the end
tb.eof_call_tc("tc_lab_poweroff.py")
tb.end_tc(True)
