from ..PackageTypes import ExecutablePackage


class Bison(ExecutablePackage):
    
    executable = 'bison'
    version_args = ['--version']
    version_regex = '[0-9]+\.[0-9]+(\.[0-9]+)?'
