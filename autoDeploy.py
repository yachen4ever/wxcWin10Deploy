#!/usr/bin/env python3

import os, shutil, getpass

# 获取当前用户的userprofile
strOSUserName = getpass.getuser()
strOSPassword = 'MAPLE4ever'
strUserProfile = os.path.expanduser('~')

# 获取脚本所在目录
thisFolder = os.path.dirname(os.path.realpath(__file__))

# 导入Windows Terminal右键菜单注册表设置  |  尚未适配用户名
strExeuteReg = 'regedit.exe /s ' + thisFolder + '\\wt.reg'
os.system(strExeuteReg)

# 复制Windows Terminal图标
strIconPath = thisFolder + '\\ico'
strIconInstallPath = strUserProfile + '\\AppData\\Local\\wxc\\ico'
print(strIconInstallPath)
if not os.path.exists(strIconInstallPath):
	os.makedirs(strIconInstallPath)

icons = os.listdir(strIconPath)
for icon in icons:
	shutil.copyfile(strIconPath + '\\'+icon,strIconInstallPath+'\\'+icon)

# 复制Windows Terminal的配置文件
strWtConfigFilePath = thisFolder + '\\wtprofiles.json'
strWtConfigInstallFilePath = strUserProfile + '\\AppData\\Local\\Packages\\Microsoft.WindowsTerminal_8wekyb3d8bbwe\\LocalState\\profiles.json'

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
os.system('sc config sshd start=auto')

# 复制ssh config文件
strSSHConfigFilePath = thisFolder + '\\config'
strSSHConfigInstallPath = strUserProfile + '\\.ssh'
if not os.path.exists(strSSHConfigInstallPath):
	os.makedirs(strSSHConfigInstallPath)
shutil.copyfile(strSSHConfigFilePath, strSSHConfigInstallPath+'\\'+'config')

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

# 设置Windows自动登录
strRegAutoLoginUserName=r'reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon" /v "DefaultUserName" /d "' + strOSUserName + '" /f'
strRegAutoLoginPwd=r'reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon" /v "DefaultPassword" /d "' + strOSPassword + '" /f'
strRegAutoAdminLogin=r'reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon" /v "AutoAdminLogon" /d "1" /f'
os.system(strRegAutoLoginUserName)
os.system(strRegAutoLoginPwd)
os.system(strRegAutoAdminLogin)
