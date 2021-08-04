# vznncv-pyocd-builder

Helper project to build standalone pyOCD executable with PyInstaller

## Usage

1. Install requirements:

   - python 3.8 or higher
   - tox

2. Build pyocd executable with tox command `PYOCD_VERSION=<pyocd_version> tox -e pyinstaller`. For example:
   
   ```
   PYOCD_VERSION=0.31.0 tox -e pyinstaller
   ```

   After build a `pyocd` will be located in *dist* folder.

## TODO:

- add CI/CD for automatic builds and releases
- add simple tests to check result file
