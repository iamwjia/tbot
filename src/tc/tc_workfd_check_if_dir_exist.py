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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_workfd_check_if_dir_exist.py
# check if a dir in tbot workdir exist
# this tc returns always true, but sets
# tb.tc_return True or False, because we may not
# want to end testcase failed, if dir not exists.
from tbotlib import tbot

logging.info("args: workfd %s %s", tb.workfd, tb.tc_workfd_check_if_dir_exists_name)

tb.eof_call_tc("tc_workfd_goto_tbot_workdir.py")
tmp = 'test -d ' + tb.tc_workfd_check_if_dir_exists_name
tb.eof_write(tb.workfd, tmp)
tb.eof_read_end_state(tb.workfd, 1)
tb.eof_write(tb.workfd, "if [ $? -ne 0 ]; then echo 'FAILED'; fi")
ret = tb.eof_search_str_in_readline(tb.workfd, "FAILED", 0)
if ret == True:
    tb.tc_return = False
if ret == None:
    tb.tc_return = False
if ret == False:
    tb.tc_return = True

tb.eof_read_end_state(tb.workfd, 1)
tb.end_tc(tb.tc_return)
