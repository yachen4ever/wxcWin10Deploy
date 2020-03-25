#!/usr/bin/env python3

import os,shutil

thisFolder = os.path.dirname(os.path.realpath(__file__))
strExeuteReg = 'regedit.exe /s ' + thisFolder + '\\wt.reg'

# 导入注册表
os.system(strExeuteReg)

# 复制Windows Terminal图标
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

shutil.copyfile(strWgetFilePath, strWgetInstallFilePath)

# 复制git bash的git-prompt.sh
strGitPromptFilePath=thisFolder + '\\git-prompt.sh'
strGitPromptInstallFilePath=r'C:\Program Files\Git\etc\profile.d\git-prompt.sh'

shutil.copyfile(strGitPromptFilePath, strGitPromptInstallFilePath)

# 添加OpenSSH Client
strExecutePS='powershell "Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0"'
os.system(strExecutePS)

# 添加OpenSSH Server
strExecutePS='powershell "Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0"'
os.system(strExecutePS)

strSshdConfigPath = thisFolder + '\\sshd_config'
strSshdConfigInstallPath=r'C:\ProgramData\ssh\sshd_config'
shutil.copyfile(strSshdConfigPath, strSshdConfigInstallPath)

# 开启OpenSSH Server
os.system('net start sshd')

# 复制ssh config文件
strSSHConfigFilePath = thisFolder + '\\config'
strSSHConfigInstallPath = r'C:\Users\Administrator\.ssh\'
if not os.path.exists(strSSHConfigInstallPath):
	os.makedirs(strSSHConfigInstallPath)
shutil.copyfile(strSSHConfigFilePath, strSSHConfigInstallPath+'\\'+config)

# 设置Oracle的环境变量
strSetOracleLangPath = 'setx "NLS_LANG" "SIMPLIFIED CHINESE_CHINA.ZHS16GBK" /m'

# # 安装字体
# strFontsPath = thisFolder + '\\font'
# strFontsInstallPath = r'C:\Windows\Fonts'
# fonts = os.listdir(strFontsPath)
# for font in fonts:
# 	shutil.copyfile(strFontsPath + '\\'+font,strFontsInstallPath+'\\'+font)

# 创建Consolas的FontLink
strRegConsolasFontLink=r'reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\FontLink\SystemLink" /v "Consolas" /t REG_MULTI_SZ /d "MSYH.TTC,Microsoft YaHei UI,128,96\0MSYH.TTC,Microsoft YaHei UI" /f'
strRegFiraCodeFontLink=r'reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\FontLink\SystemLink" /v "Fira Code" /t REG_MULTI_SZ /d "MSYH.TTC,Microsoft YaHei UI,128,96\0MSYH.TTC,Microsoft YaHei UI" /f'

os.system(strRegConsolasFontLink)
os.system(strRegFiraCodeFontLink)