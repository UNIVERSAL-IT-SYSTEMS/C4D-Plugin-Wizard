# encoding: utf-8
"""
This is a setup.py script generated by py2applet
and modified by AUTHOR.

Usage:
    python setup.py py2app -OR-
    python setup.py py2app -A (for alias mode)
"""
from setuptools import setup

import re
import sys
import time

def get_version(filelist):
    '''
    Whacky hack for getting the version info from the main.py or 
    another application/cli script file, since you can trigger an 
    endless import loop when you try to import from your APP files 
    in setup.py
    '''
    default = (0, 0, 0)
    for name in filelist:
        try:
            with open(name) as script:
                for line in script:
                    match = re.match(r'__version__\s*=\s*(.+)', line)
                    if match:
                        code = compile('version_tuple = %s' % match.group(1), '<string>', 'single')
                        ns = {}
                        exec(code, ns) # IGNORE:W0122
                        return ns['version_tuple']
        except Exception:  # IGNORE:W0703
            pass  # fall thru to end
    return default


encoding = sys.getdefaultencoding()

app = ['gui.py']
app_name = "C4D Plugin Wizard"
author = u'André Berg'.encode(encoding)
bundle_identifier = 'com.seramediavfx.' + app_name.replace(' ', '')
copyrite = unichr(169).encode(encoding)  # copyright symbol
version = get_version(app)
version_string = '.'.join(str(x) for x in version)
year = time.strftime("%y")

plist = {'CFBundleIdentifier': bundle_identifier,
         'CFBundleShortVersionString': version_string,
         'CFBundleGetInfoString': '%s v%s, Copyright %s %s. All rights reserved.' % (app_name, version_string, author, year),
         'NSHumanReadableCopyright': '%s %s, %s' % (copyrite, author, year)
}

data_files = ['c4dplugwiz.py']
resources = ['images', 'c4dplugwiz_data'] 

# options = {
#     'argv_emulation': True,
#     'iconfile': 'res/c4dapp.icns',
#     'plist': plist,  
#     'includes': ['sip', 'PyQt4', 'PyQt4.QtCore', 'PyQt4.QtGui'],
#     'excludes': ['Tkinter', 'wx', 'libavg', 'lxml', 'PIL', 'pandas', 'zope', 'markupsafe', 
#                  'coverage', 'Cython', 'Crypto', 'OpenSSL', 'PySide', 'sklearn', 'simplejson'
#                  'OpenGL', 'scipy', 'numpy', 'matplotlib', 'PyQt4.QtDesigner', 'PyQt4.QtNetwork', 
#                  'PyQt4.QtOpenGL', 'PyQt4.QtScript', 'PyQt4.QtSql', 'PyQt4.QtTest', 'PyQt4.QtWebKit', 
#                  'PyQt4.QtXml', 'PyQt4.phonon']
# }

options = {
    'argv_emulation': True, 
    'plist': plist,
    'iconfile': 'res/c4dapp.icns',
    'includes': ['sip'],
    'excludes': ['Tkinter', 'wx', 'libavg', 'lxml', 'PIL', 'pandas', 'zope', 'markupsafe', 
                 'coverage', 'Cython', 'Crypto', 'OpenSSL', 'PySide', 'sklearn', 'simplejson'
                 'OpenGL', 'scipy', 'numpy', 'matplotlib', 'PyQt4.QtDBus', 'PyQt4.QtDeclarative', 
                 'PyQt4.QtHelp', 'PyQt4.QtMultimedia', 'PyQt4.QtNetwork', 'PyQt4.QtScript', 
                 'PyQt4.QtScriptTools', 'PyQt4.QtSql', 'PyQt4.QtSvg', 'PyQt4.QtXml', 'PyQt4.QtXmlPatterns', 
                 'PyQt4.phonon'],
    #'packages': ['PyQt4']
    # Uncomment the following 2 lines if you want more control over which 
    # Qt modules get byte-compiled into the final app. Comment out the previous 
    # 2 lines in that case. If your app ends up being huge regardless you may
    # need to use a fresh environment using virtualenv.
    #'includes': ['sip', 'PyQt4', 'PyQt4.QtCore', 'PyQt4.QtGui'],
    #'excludes': ['PyQt4.QtDBus', 'PyQt4.QtDeclarative', 'PyQt4.QtHelp', 'PyQt4.QtMultimedia', 
    #             'PyQt4.QtNetwork', 'PyQt4.QtScript', 'PyQt4.QtScriptTools', 'PyQt4.QtSql', 
    #             'PyQt4.QtSvg', 'PyQt4.QtXml', 'PyQt4.QtXmlPatterns', 'PyQt4.phonon']
}

setup(
    app=app,
    name=app_name,
    data_files=(data_files + resources),
    options={'py2app': options},
    setup_requires=['py2app']
)