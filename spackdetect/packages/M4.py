from ..PackageTypes import ExecutablePackage


class M4(ExecutablePackage):
    
    executable = 'm4'
    version_args = ['--version']
    version_regex = '[0-9]+\.[0-9]+(\.[0-9]+)?'
