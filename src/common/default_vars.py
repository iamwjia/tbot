# This file contains default values for all
# variables testcases use ...

debug = False
debugstatus = False
uboot_autoboot_key = ''
state_uboot_timeout = 1
tb_power_state = 'undef'
term_line_length = '200'
wdt_timeout = '120' # wdt timeout after 2 minutes
state_linux_timeout = 4
labsshprompt = '$ '
tc_return = True
tc_workfd_check_if_cmd_exist_cmdname = 'none'
ub_boot_linux_cmd = 'run tbot_boot_linux'
do_connect_to_board = True
tftpboardname = 'config.boardname'
boardlabname = 'config.boardname'
boardlabpowername = 'config.boardname'
tftpboardrootdir = ''
tc_lab_toolchain_rev = "5.4"
tc_lab_toolchain_name = "armv5te"
tc_lx_gpio_val = '1'
tc_workfd_check_if_file_exists_name = "bonnie++-1.03e.tgz"
tc_workfd_check_if_dir_exists_name = "mtd-utils"
tc_workfd_apply_patchwork_patches_list = []
tc_workfd_apply_patchwork_patches_list_hand = []
tc_workfd_apply_patchwork_patches_blacklist = []
tc_workfd_apply_patchwork_patches_checkpatch_cmd = 'none'
tc_workfd_apply_patchwork_patches_eof = 'yes'
tc_workfd_get_patchwork_number_list_order = '-delegate'
tc_workfd_rm_file_name = 'none'
tc_workfd_cd_name = 'none'
tc_lab_get_linux_source_git_repo = "/home/git/linux.git"
tc_lab_get_linux_source_git_repo_user = 'anonymous'
tc_lab_get_linux_source_git_branch = "master"
tc_lab_get_linux_source_git_reference = 'none'
tc_workfd_apply_local_patches_dir = 'none'
tc_workfd_apply_local_patches_checkpatch_cmd = 'none'
tc_workfd_apply_local_patches_checkpatch_cmd_strict = "no"
tc_workfd_get_list_of_files_mask = '*'
tc_workfd_compile_linux_boardname = 'config.boardname'
tc_workfd_compile_linux_clean = 'yes'
tc_workfd_compile_linux_modules = 'none'
tc_workfd_compile_linux_modules_path = 'none'
tc_workfd_compile_linux_dt_name = 'none'
tc_workfd_compile_linux_append_dt = 'no'
tc_workfd_compile_linux_load_addr = 'no'
tc_workfd_compile_linux_make_target = 'uImage'
tc_workfd_compile_linux_fit_its_file = 'no'
tc_workfd_compile_linux_fit_file = 'no'
tc_workfd_compile_linux_mkimage = '/home/hs/i2c/u-boot/tools/mkimage'
tc_workfd_compile_linux_makeoptions = ''
workfd_get_patchwork_number_user = 'hs'
workfd_get_patchwork_number_list_order = '-delegate'
tc_workfd_connect_with_kermit_ssh = "none"
tc_workfd_connect_with_kermit_sudo = "none"
tc_workfd_connect_with_kermit_rlogin = "none"
kermit_line = '/dev/ttyUSB0'
kermit_speed = '115200'
tc_lab_denx_power_tc = 'tc_lab_denx_power.py'
tc_lab_denx_get_power_state_tc = 'tc_lab_denx_get_power_state.py'
tc_lab_denx_connect_to_board_tc = 'tc_lab_denx_connect_to_board.py'
tc_lab_denx_disconnect_from_board_tc = 'tc_lab_denx_disconnect_from_board.py'
tc_lx_trigger_wdt_cmd = '/home/hs/wdt &'
tc_workfd_create_ubi_rootfs_path = '/opt/eldk-5.4/armv7a-hf/rootfs-minimal-mtdutils'
tc_workfd_create_ubi_rootfs_target = '/tftpboot/dxr2/tbot/rootfs-minimal.ubifs'
workfd_ssh_cmd_prompt = '$'
workfd_ssh_cmd_opt = ''
linux_prompt_default = 'root@generic-armv7a-hf:~# '
labprompt = 'config.linux_prompt'
linux_user = 'root'
create_dot = 'no'
create_statistic = 'no'
create_dashboard = 'no'
create_webpatch = 'no'
create_html_log = 'no'
create_documentation = 'no'
event_documentation_strip_list = []
switch_su_board = 'lab'
tc_workfd_can_ssh = 'no'
tc_workfd_can_ssh_prompt = '$'
tc_workfd_can_su = 'no'
tc_workfd_can_dev = 'can0'
tc_workfd_can_bitrate = '500000'
tc_workfd_can_iproute_dir = '/home/hs/iproute2'
tc_workfd_can_util_dir = '/home/hs/can-utils'
tc_workfd_hdparm_path = '/home/hs/shc/hdparm-9.50/'
tc_workfd_hdparm_dev = '/dev/mmcblk1'
tc_workfd_hdparm_min = '12.0'
tb_set_after_linux = ''
