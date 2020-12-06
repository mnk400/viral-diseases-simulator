# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=['C:\\Users\\Manik\\Drive\\Projects\\virussim'],
             binaries=[],
             datas=[('C:\\Users\\Manik\\Drive\\Projects\\virussim\\assets\\icon-512.png','assets'),
                    ('C:\\Users\\Manik\\Drive\\Projects\\virussim\\config\\config.ini','config'),
                    ('C:\\Users\\Manik\\Drive\\Projects\\virussim\\config\\test_config.ini','config')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=True)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [('v', None, 'OPTION')],
          exclude_binaries=True,
          name='main',
          debug=True,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='main')
