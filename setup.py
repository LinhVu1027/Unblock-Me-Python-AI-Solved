import sys
from cx_Freeze import setup, Executable

executables = [
    Executable("graphics.py",
               appendScriptToExe=True,
               appendScriptToLibrary=False,
               )
]

buildOptions = dict(create_shared_zip=False)

setup(name="unblockme",
      version="0.1",
      description="unblock me game",
      options=dict(build_exe=buildOptions),
      executables=executables,
      )
