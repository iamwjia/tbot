# SPDX-License-Identifier: GPL-2.0
#
# Description:
#
# start an scp transfer
# tb.config.tc_workfd_scp_opt: scp options
# tb.config.tc_workfd_scp_from: from where
# tb.config.tc_workfd_scp_to: to where
#
# If the scp command asks for  "password" the testcase extracts
# the user and ip from scp output "user@ip's password:"
# and writes the password it find in password.py with
#
# tb.write_stream_passwd(tb.workfd, user, ip)
#
# to the scp command ... if no user and or ip
# is found ... scp command fails and so the testcase.
#
# An errorneous scp command exits with an error code.
# check this error code when scp command finished,
# and return True, if no error, else False.
#
#
# used variables
#
# - tb.config.tc_workfd_scp_opt
#| if != 'none' contains scp option string
#| default: 'none'
#
# - tb.config.tc_workfd_scp_from
#| string from where scp copy
#| default: ''
#
# - tb.config.tc_workfd_scp_to
#| string to where scp copy
#| default: ''
#
# End:

from tbotlib import tbot

tb.define_variable('tc_workfd_scp_opt', '')
tb.define_variable('tc_workfd_scp_from', '')
tb.define_variable('tc_workfd_scp_to', '')

c = tb.workfd

if tb.config.tc_workfd_scp_opt == 'none':
    opt = ''
else:
    opt = tb.config.tc_workfd_scp_opt

cmd = 'scp ' + opt + ' ' + tb.config.tc_workfd_scp_from + ' ' + tb.config.tc_workfd_scp_to
tb.eof_write(c, cmd, split=c.line_length / 2)
loop = True
s = ['Are you sure', 'Do you want to', 'password', 'ETA', '\n']
while loop:
    tmp = tb.tbot_rup_and_check_strings(c, s)
    if tmp == '0':
        tb.eof_write(c, 'yes', start=False)
    if tmp == '1':
        tb.eof_write(c, 'y', start=False)
    elif tmp == '2':
        # get the user name (before @) from scp output
        tmp = tb.buf.split('@')
        try:
            tmp[1]
            # OK, there is a @
            user = tmp[0].replace('\r', '')
            user = user.replace('\n', '')
        except:
            # Hmm.. no user name found ... what to do?
            # currently tbot searches now for user ''
            # which it not found -> wrng password send,
            # which leads in failure of the scp cmd ...
            user = ''

        if user != '':
            tmp = tmp[1].split("'s ")
            try:
                tmp[1]
                # Ok "'s " found
                ip = tmp[0]
            except:
                # no ip, same as no user ...
                ip = ''
        tb.write_stream_passwd(tb.workfd, user, ip)
    elif tmp == '3':
        tb.tbot_trigger_wdt()
    elif tmp == '4':
        tb.tbot_trigger_wdt()
    elif tmp == 'prompt':
        loop = False

ret = self.call_tc("tc_workfd_check_cmd_success.py")
tb.end_tc(ret)
