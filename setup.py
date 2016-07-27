from distutils.core import setup, Extension

try:
    import stat_tools
except:
    raise ImportError("Cannot import stat_tools please download from `http://code.icecube.wisc.edu/svn/sandbox/schoenen/stat_tools`")

module = Extension('kde', sources = ['kde.c'])
setup(name = 'kde', version = '0.1',ext_modules = [module])
