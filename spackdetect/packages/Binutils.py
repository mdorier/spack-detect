from ..PackageTypes import ExecutablePackage


class Binutils(ExecutablePackage):
    
    executable = 'ld'
    version_args = ['-v']
    version_regex = '[0-9]+\.[0-9]+(\.[0-9]+)?'
