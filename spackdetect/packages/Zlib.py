from ..PackageTypes import ExecutablePackage


class Zlib(ExecutablePackage):
    
    executable = 'zip'
    version_args = ['--version']
    version_regex = '[0-9]+\.[0-9]+(\.[0-9]+)?'
