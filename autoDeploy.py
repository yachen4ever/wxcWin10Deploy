#!/usr/bin/env python3

import os,shutil

thisFolder = os.path.dirname(os.path.realpath(__file__))

# 导入注册表
strExeuteReg = 'regedit.exe /s ' + thisFolder + '\\wt.reg'
os.system(strExeuteReg)

# 复制图标
strIconPath = thisFolder + '\\ico'
strIconInstallPath = r'C:\Users\Administrator\AppData\Local\wxc\ico'
if not os.path.exists(strIconInstallPath):
	os.makedirs(strIconInstallPath)

icons = os.listdir(strIconPath)
for icon in icons:
	shutil.copyfile(strIconPath + '\\'+icon,strIconInstallPath+'\\'+icon)

# 复制Windows Terminal的配置文件
strWtConfigFilePath = thisFolder + '\\wtprofiles.json'
strWtConfigInstallFilePath = r'C:\Users\Administrator\AppData\Local\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState\profiles.json'

shutil.copyfile(strWtConfigFilePath,strWtConfigInstallFilePath)

# 复制wget到git bash的/usr/bin
strWgetFilePath=thisFolder + '\\wget.exe'
strWgetInstallFilePath=r'C:\Program Files\Git\usr\bin\wget.exe'

shutil.copyfile(strWgetFilePath,strWgetInstallFilePath)

# 添加OpenSSH Server
strExecutePS='powershell "Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0"'
os.system(strExecutePS)

strSshdConfigPath = thisFolder + '\\sshd_config'
strSshdConfigInstallPath=r'C:\ProgramData\ssh\sshd_config'
shutil.copyfile(strSshdConfigPath, strSshdConfigInstallPath)

# 开启OpenSSH Server
os.system('net start sshd')

# 设置Oracle的环境变量
strSetOracleLangPath = 'setx "NLS_LANG" "SIMPLIFIED CHINESE_CHINA.ZHS16GBK" /m'