from ..PackageTypes import ExecutablePackage


class Libtool(ExecutablePackage):
    
    executable = 'libtoolize'
    version_args = ['--version']
    version_regex = '[0-9]+\.[0-9]+(\.[0-9]+)?'
