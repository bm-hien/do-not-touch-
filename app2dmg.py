
import sys
from setuptools import setup

APP = ['bmhien.py']  # Replace 'your_script.py' with the name of your Python script
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'iconfile': 'icon.icns',  # Replace 'icon.icns' with the path to your icon file
    'plist': {
        'CFBundleName': 'bmhien',  # Replace 'Your App Name' with your app's name
        'CFBundleShortVersionString': '1.0',
        'CFBundleGetInfoString': 'just a tester',  # Replace 'Your App Description' with your app's description
        'CFBundleExecutable': 'bmhien',  # Replace 'Your App Executable' with your app's executable name
    },
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
