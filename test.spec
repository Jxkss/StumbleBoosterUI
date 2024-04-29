# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['test.py'],
    pathex=[],
    binaries=[],
    datas=[('settings.ico', '.'), ('SGbest.png', '.'), ('SGbest2.png', '.'), ('SGbest3.png', '.'), ('stumblebooster.ico', '.'), ('stumblebooster.png', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='test',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    uac_admin=True,
    icon=['C:\\Users\\pierre\\Downloads\\stumblebooster.ico'],
)
