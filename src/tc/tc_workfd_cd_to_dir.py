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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_workfd_cd_to_dir.py
# simple cd into a directory
#
from tbotlib import tbot

logging.info("args: workfd %s %s", tb.workfd, tb.tc_workfd_cd_name)

tb.tc_workfd_check_if_dir_exists_name = tb.tc_workfd_cd_name
tb.eof_call_tc("tc_workfd_check_if_dir_exist.py")
tmp = "cd " + tb.tc_workfd_cd_name
tb.eof_write(tb.workfd, tmp)
tb.eof_read_end_state(tb.workfd, 1)
tb.eof_call_tc("tc_workfd_check_cmd_success.py")

tb.end_tc(True)