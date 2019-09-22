from ..PackageTypes import ExecutablePackage


class Coreutils(ExecutablePackage):
    
    executable = 'ls'
    version_args = ['--version']
    version_regex = '[0-9]+\.[0-9]+(\.[0-9]+)?'
