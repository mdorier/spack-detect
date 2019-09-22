from ..PackageTypes import ExecutablePackage


class Bzip2(ExecutablePackage):
    
    executable = 'bzip2'
    version_args = ['--version']
    version_regex = '[0-9]+\.[0-9]+(\.[0-9]+)?'
