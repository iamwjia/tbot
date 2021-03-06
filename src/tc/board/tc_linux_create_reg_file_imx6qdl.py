# SPDX-License-Identifier: GPL-2.0
#
# Description:
# create a regfile for imx6qdl SoC registers
# End:

from tbotlib import tbot
import time

tb.workfd = tb.c_ctrl

# IOMUX
tb.config.tc_lx_create_reg_file_name = 'imx6qdl_iomux_module.reg'
tb.config.tc_lx_create_reg_file_start = '0x20e0000'
tb.config.tc_lx_create_reg_file_stop = '0x20e0950'
tb.config.tc_lx_readreg_mask = 0xffffffff
tb.config.tc_lx_readreg_type = 'w'
tb.eof_call_tc("tc_lx_create_reg_file.py")

# CCM
tb.config.tc_lx_create_reg_file_name = 'imx6qdl_ccm_module.reg'
tb.config.tc_lx_create_reg_file_start = '0x020c4000'
tb.config.tc_lx_create_reg_file_stop = '0x020c408c'
tb.config.tc_lx_readreg_mask = 0xffffffff
tb.config.tc_lx_readreg_type = 'w'
tb.eof_call_tc("tc_lx_create_reg_file.py")


tb.end_tc(True)
