from distutils.core import setup
import py2exe,os

setup(	options = {'py2exe': {'bundle_files': 1}},
		windows=[{"script":"C:\NatLink\NatLink\MacroSystem\exe\homebrew\\element\\element.py", 'icon_resources':[(1,'icon.ico')]}]
	)