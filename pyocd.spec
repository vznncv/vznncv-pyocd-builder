# -*- mode: python ; coding: utf-8 -*-


block_cipher = None

def collect_runtime_hooks():
    import os.path
    result = []
    for dir_entry in os.scandir(os.path.abspath('runtime_hooks')):
        if dir_entry.is_dir() or not dir_entry.name.endswith('.py'):
            continue
        result.append(dir_entry.path)
    return result


def collect_package_data(pkg_info: dict, pkg_name: str, metadata: bool = False):
    import PyInstaller.utils.hooks

    binaries = pkg_info.setdefault('binaries', [])
    datas = pkg_info.setdefault('datas', [])
    hiddenimports = pkg_info.setdefault('hiddenimports', [])

    # collect data
    if metadata:
        datas += PyInstaller.utils.hooks.copy_metadata(pkg_name)
    datas += PyInstaller.utils.hooks.collect_data_files(pkg_name, include_py_files=False)
    # collect binaries
    binaries += PyInstaller.utils.hooks.collect_data_files(
        pkg_name,
        include_py_files=True,
        includes=['**/*.dll', '**/*.dylib', '**/*.so', ]
    )
    # collect package modules
    hiddenimports += PyInstaller.utils.hooks.collect_submodules(pkg_name)

    return pkg_info


pkg_info = {}
collect_package_data(pkg_info, 'pyocd', metadata=True)
collect_package_data(pkg_info, 'cmsis_pack_manager')

a = Analysis(['entry_point/pyocdw.py'],
             pathex=[],
             binaries=pkg_info['binaries'],
             datas=pkg_info['datas'],
             hiddenimports=pkg_info['hiddenimports'],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=collect_runtime_hooks(),
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,  
          [],
          name='pyocd',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
