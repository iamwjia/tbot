# SPDX-License-Identifier: GPL-2.0
#
# Description:
# connect with kermit to serials board console
# - if tb.config.tc_workfd_connect_with_kermit_ssh != 'none'
#   connect first with ssh to another PC (where kermit is started)
# - start kermit
# - if tb.config.tc_workfd_connect_with_kermit_rlogin == 'none'
#     set line tb.config.kermit_line and speed tb.config.kermit_speed and
#     kermit parameter list tb.config.tc_workfd_connect_with_kermit_settings
#     than connect to serial line.
#   else
#     connect with command in tb.config.tc_workfd_connect_with_kermit_rlogin
# - if you need sudo rights set tb.config.tc_workfd_connect_with_kermit_sudo = 'yes'
#   and a sudo is preceded to kermit.
#   the sudo password is searched with
#   user:  tb.config.user + '_kermit'
#   board: tb.config.boardname
#
#
# used variables
#
# - tb.config.kermit_line
#| used serial linux device
#| default: '/dev/ttyUSB0'
#
# - tb.config.kermit_speed
#| serial line speed
#| default: '115200'
#
# - tb.config.tc_workfd_connect_with_kermit_ssh
#| call tc_workfd_ssh.py with
#| tb.config.workfd_ssh_cmd = tb.config.tc_workfd_connect_with_kermit_ssh
#| default: 'none'
#
# - tb.config.tc_workfd_connect_with_kermit_sudo
#| use sudo for kermit
#| default: 'none'
#
# - tb.config.tc_workfd_connect_with_kermit_rlogin
#| rlogin string for kermit. If != 'none'
#| do not 'set line', 'set speed' and 'connect'
#| default: 'none'
#
# - tb.config.tc_workfd_connect_with_kermit_settings
#| list of additionally kermit parameter, which get
#| set after 'set line' and 'set speed'
#| default: '["set carrier-watch off",
#|        "set handshake none",
#|        "set flow-control none",
#|        "robust",
#|        "set file type bin",
#|        "set file name lit",
#|        "set rec pack 1000",
#|        "set send pack 1000",
#|        "set window 5",
#|    ]'
#
# End:

from tbotlib import tbot

tb.define_variable('tc_workfd_connect_with_kermit_ssh', 'none')
tb.define_variable('tc_workfd_connect_with_kermit_sudo', 'none')
tb.define_variable('tc_workfd_connect_with_kermit_rlogin', 'none')
tb.define_variable('kermit_line', '/dev/ttyUSB0')
tb.define_variable('kermit_speed', '115200')
tb.define_variable('tc_workfd_connect_with_kermit_settings', '[ "set carrier-watch off", \
 "set handshake none", \
 "set flow-control none", \
 "robust", \
 "set file type bin", \
 "set file name lit", \
 "set rec pack 1000", \
  "set send pack 1000", \
  "set window 5", \
]')

if tb.config.tc_workfd_connect_with_kermit_ssh != 'none':
    tb.config.workfd_ssh_cmd = tb.config.tc_workfd_connect_with_kermit_ssh
    tb.config.workfd_ssh_cmd_prompt = '$'
    tb.eof_call_tc("tc_workfd_ssh.py")

if tb.config.tc_workfd_connect_with_kermit_sudo != 'none':
    pre = 'sudo '
else:
    pre = ''

tb.eof_write(tb.workfd, pre + 'kermit', start=False)
oldprompt = tb.workfd.get_prompt()
tb.workfd.set_prompt('C-Kermit>', 'linux')

searchlist = ["assword", "Locked"]
tmp = True
retu = False
while tmp == True:
    ret = tb.tbot_rup_and_check_strings(tb.workfd, searchlist)
    if ret == '0':
       tb.write_stream_passwd(tb.workfd, tb.config.user + '_kermit', tb.config.boardname)
    if ret == '1':
       retu = True
    elif ret == 'prompt':
       tmp = False

    if retu == True:
        tb.workfd.set_prompt(oldprompt, 'linux')
        tb.eof_write(tb.workfd, 'exit', start=False)
        tb.end_tc(False)

if tb.config.tc_workfd_connect_with_kermit_rlogin == 'none':
    # check for "no effect", "Sorry, write access"
    tb.eof_write(tb.workfd, "set line " + tb.config.kermit_line, start=False)
    searchlist = ["no effect", "Sorry, write access", "Sorry, device is in use", "Device or resource busy"]
    tmp = True
    retu = False
    while tmp == True:
        ret = tb.tbot_rup_and_check_strings(tb.workfd, searchlist)
        if ret == '0':
            retu = True
        if ret == '1':
            retu = True
        if ret == '2':
            retu = True
        if ret == '3':
            retu = True
        elif ret == 'prompt':
            tmp = False

    if retu == True:
        tb.workfd.set_prompt(oldprompt, 'linux')
        tb.gotprompt = True
        tb.end_tc(False)

    tb.eof_write_cmd(tb.workfd, "set speed " + tb.config.kermit_speed, start=False)
    for cmd in tb.config.tc_workfd_connect_with_kermit_settings:
        tb.eof_write_cmd(tb.workfd, cmd, start=False)

    tb.eof_write(tb.workfd, "connect")
    searchlist = ["Connecting"]
    tmp = True
    ret = tb.tbot_rup_and_check_strings(tb.workfd, searchlist)
    if ret != '0':
        tb.gotprompt = True
        tb.end_tc(False)
else:
    tb.eof_write(tb.workfd, tb.config.tc_workfd_connect_with_kermit_rlogin, start=False)

searchlist = ['----------------------------------------------------']
ret = tb.tbot_rup_and_check_strings(tb.workfd, searchlist)
if ret != '0':
    tb.gotprompt = True
    tb.end_tc(False)

if tb.config.tc_workfd_connect_with_kermit_rlogin != 'none':
    searchlist = ['----------------------------------------------------', '\n']
    oldt = tb.workfd.get_timeout()
    tb.workfd.set_timeout(5)
    tmp = True
    cnt = 0
    while tmp == True:
        ret = tb.tbot_rup_and_check_strings(tb.workfd, searchlist)
        if ret == '0':
            # some Error with connect, leave kermit
            tb.workfd.set_timeout(oldt)
            tb.workfd.set_prompt(oldprompt, 'linux')
            tb.eof_write_cmd(tb.workfd, 'exit', start=False)
            tb.gotprompt = True
            tb.end_tc(False)
        if ret == '1':
            if cnt > -1:
                cnt += 1
                if cnt > 100:
                    logging.warn("Seems board emits endless chars, try to poweroff")
                    tb.eof_call_tc("tc_lab_poweroff.py")
                    cnt = -1
        else:
            tmp = False
    tb.workfd.set_timeout(oldt)

tb.gotprompt = True
# set now U-Boot prompt ?
tb.workfd.set_prompt(tb.config.uboot_prompt, 'u-boot')
tb.in_state_linux = False
tb.workfd.termlength_set = False
tb.end_tc(True)
