# setup.py
from distutils.core import setup
import py2exe

setup(windows=[ {
                "script" : "main.py",
                "icon_resources": [(1, "icon.ico")]
                 }
                ],
      data_files=[("",["forumbanner.gif","test.jpg","archive.html","images.json","icon.ico"])],
      zipfile=None)
