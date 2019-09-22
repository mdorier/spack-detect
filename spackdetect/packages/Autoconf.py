from ..PackageTypes import ExecutablePackage


class Autoconf(ExecutablePackage):
    
    executable = 'autoconf'
    version_args = ['--version']
    version_regex = '[0-9]+\.[0-9]+(\.[0-9]+)?'
