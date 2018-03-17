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
# Description:
#
# go into git source tree tb.config.tc_workfd_git_rebase_git_src_path
# checkout branch tb.config.tc_workfd_git_rebase_git_base_branch
# call "git fetch" and "git pull"
# checkout branch tb.config.tc_workfd_git_rebase_git_work_branch
# and rebase tb.config.tc_workfd_git_rebase_git_work_branch with
# tb.config.tc_workfd_git_rebase_git_base_branch
#
# End:

from tbotlib import tbot

try:
    tb.config.tc_workfd_git_rebase_git_src_path
except:
    logging.error("tb.config.tc_workfd_git_rebase_git_src_path not set")
    tb.end_tc(False)

try:
    tb.config.tc_workfd_git_rebase_git_base_branch
except:
    logging.error("tb.config.tc_workfd_git_rebase_git_base_branch not set")
    tb.end_tc(False)

try:
    tb.config.tc_workfd_git_rebase_git_work_branch
except:
    logging.error("tb.config.tc_workfd_git_rebase_git_work_branch not set")
    tb.end_tc(False)

# always add some logging info for example which variables
# your testcase uses
# don;t forget to define a default value for a new config variable
# if it makes sense
logging.info("arg: %s", tb.workfd.name)
logging.info("arg: src path: %s", tb.config.tc_workfd_git_rebase_git_src_path)
logging.info("arg: base branch: %s", tb.config.tc_workfd_git_rebase_git_base_branch)
logging.info("arg: work branch: %s", tb.config.tc_workfd_git_rebase_git_work_branch)

# save current pwd ?

base = os.path.basename(tb.config.tc_workfd_git_rebase_git_src_path)
tb.event.create_event('main', 'tc_workfd_git_rebase.py', 'SET_DOC_FILENAME_NOIRQ', 'git_rebase_' + base)
tb.write_lx_cmd_check(tb.workfd, 'cd ' + tb.config.tc_workfd_git_rebase_git_src_path)
tb.write_lx_cmd_check(tb.workfd, 'git checkout ' + tb.config.tc_workfd_git_rebase_git_base_branch)
tb.write_lx_cmd_check(tb.workfd, 'git fetch')
tb.write_lx_cmd_check(tb.workfd, 'git pull')
tb.write_lx_cmd_check(tb.workfd, 'git checkout ' + tb.config.tc_workfd_git_rebase_git_work_branch)
tb.write_lx_cmd_check(tb.workfd, 'git rebase ' + tb.config.tc_workfd_git_rebase_git_base_branch)
tb.event.create_event('main', 'tc_workfd_git_rebase.py', 'SET_DOC_FILENAME_NOIRQ_END', 'git_rebase_' + base)

# go back to old path ?
tb.end_tc(True)