from ..PackageTypes import ExecutablePackage


class PkgConfig(ExecutablePackage):
    
    executable = 'pkg-config'
    version_args = ['--version']
    version_regex = '[0-9]+\.[0-9]+(\.[0-9]+)?'
