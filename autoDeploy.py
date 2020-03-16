#!/usr/bin/env python3

import os,shutil

thisFolder = os.path.dirname(os.path.realpath(__file__))
strExeuteReg = 'regedit.exe /s ' + thisFolder + '\\wt.reg'

# 导入注册表
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
