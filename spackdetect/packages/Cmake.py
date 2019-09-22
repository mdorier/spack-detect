from ..PackageTypes import ExecutablePackage


class Cmake(ExecutablePackage):
    
    executable = 'cmake'
    version_args = ['--version']
    version_regex = '[0-9]+\.[0-9]+(\.[0-9]+)?'
