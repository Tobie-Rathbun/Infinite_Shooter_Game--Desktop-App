# -*- mode: python ; coding: utf-8 -*-

added_files = [

("resources/sprites/npc/soldier", "resources/sprites/npc/soldier"),
("resources/sprites/npc/soldier/attack", "resources/sprites/npc/soldier/attack"),
("resources/sprites/npc/soldier/death", "resources/sprites/npc/soldier/death"),
("resources/sprites/npc/soldier/idle", "resources/sprites/npc/soldier/idle"),
("resources/sprites/npc/soldier/pain", "resources/sprites/npc/soldier/pain"),
("resources/sprites/npc/soldier/walk", "resources/sprites/npc/soldier/walk"),
("resources/sprites/npc/caco_demon", "resources/sprites/npc/caco_demon"),
("resources/sprites/npc/caco_demon/attack", "resources/sprites/npc/caco_demon/attack"),
("resources/sprites/npc/caco_demon/death", "resources/sprites/npc/caco_demon/death"),
("resources/sprites/npc/caco_demon/idle", "resources/sprites/npc/caco_demon/idle"),
("resources/sprites/npc/caco_demon/pain", "resources/sprites/npc/caco_demon/pain"),
("resources/sprites/npc/caco_demon/walk", "resources/sprites/npc/caco_demon/walk"),
("resources/sprites/npc/cyber_demon", "resources/sprites/npc/cyber_demon"),
("resources/sprites/npc/cyber_demon/attack", "resources/sprites/npc/cyber_demon/attack"),
("resources/sprites/npc/cyber_demon/death", "resources/sprites/npc/cyber_demon/death"),
("resources/sprites/npc/cyber_demon/idle", "resources/sprites/npc/cyber_demon/idle"),
("resources/sprites/npc/cyber_demon/pain", "resources/sprites/npc/cyber_demon/pain"),
("resources/sprites/npc/cyber_demon/walk", "resources/sprites/npc/cyber_demon/walk"),
("resources/sprites/animated_sprites", "resources/sprites/animated_sprites"),
("resources/sprites/static_sprites", "resources/sprites/static_sprites"),
("resources/sound", "resources/sound")

]


block_cipher = None


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=added_files,
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
