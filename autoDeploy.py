#!/usr/bin/env python3

import os

thisFolder = os.path.dirname(os.path.realpath(__file__))
strExeuteReg = 'regedit.exe /s ' + thisFolder + '\\wt.reg'

# 导入注册表
os.system(strExeuteReg)

# 复制图标
strIconPath = thisFolder + '\\ico'
strIconInstallPath = r'C:\Users\Administrator\AppData\Local\wxc\ico'
os.makedirs(strIconInstallPath)
