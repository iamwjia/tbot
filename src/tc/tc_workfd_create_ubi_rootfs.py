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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_workfd_create_ubi_rootfs.py
# create a ubifs rootfs
from tbotlib import tbot

logging.info("args: workdfd: %s %s", tb.workfd, tb.tc_workfd_create_ubi_rootfs_path)
logging.info("%s", tb.tc_workfd_create_ubi_rootfs_target)

tb.eof_write(tb.workfd, "su")
tb.eof_search_str_in_readline(tb.workfd, "Password", 1)
tb.write_stream_passwd(tb.workfd, "root", "lab")
tb.set_prompt(tb.workfd, tb.linux_prompt, 'export PS1="\u@\h [\$(date +%k:%M:%S)] ', ' >"')

tmp = "date > " + tb.tc_workfd_create_ubi_rootfs_path + "/creation_time"
tb.eof_write_lx_cmd_check(tb.workfd, tmp)
tmp = "cat " + tb.tc_workfd_create_ubi_rootfs_path + "/creation_time"
tb.eof_write_lx_cmd_check(tb.workfd, tmp)

tmp = "mkfs.ubifs --root=" + tb.tc_workfd_create_ubi_rootfs_path + " --min-io-size=" + tb.tc_ubi_min_io_size + " --leb-size=" + tb.tc_ubi_leb_size + " --max-leb-cnt=" + tb.tc_ubi_max_leb_cnt + " -F --output=" + tb.tc_workfd_create_ubi_rootfs_target
tb.eof_write_lx_cmd_check(tb.workfd, tmp)
tb.eof_write_cmd(tb.workfd, "exit")
tb.end_tc(True)
