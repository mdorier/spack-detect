from ..PackageTypes import HeaderPackage


class Zlib(HeaderPackage):
    header_file = 'zlib.h'
    version_macro = 'ZLIB_VERSION'
