from ..PackageTypes import ExecutablePackage


class Xz(ExecutablePackage):
    
    executable = 'xz'
    version_args = ['--version']
    version_regex = '[0-9]+\.[0-9]+(\.[0-9]+)?'
