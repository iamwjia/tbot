# SPDX-License-Identifier: GPL-2.0
#
# Description:
# test U-Boots help cmd
# may we add a list as parameter, so we can adapt it board
# specific.
# End:

from tbotlib import tbot

searchlist = ["?       - alias for 'help'", "bdinfo  - print Board Info structure"]
logging.info("args: %s", searchlist)

# set board state for which the tc is valid
tb.set_board_state("u-boot")

tmp = "help"
tb.eof_write(tb.c_con, tmp)

tb.tbot_rup_check_all_strings(tb.c_con, searchlist, endtc=True)
