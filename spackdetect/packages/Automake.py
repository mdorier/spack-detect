from ..PackageTypes import ExecutablePackage


class Automake(ExecutablePackage):
    
    executable = 'automake'
    version_args = ['--version']
    version_regex = '[0-9]+\.[0-9]+(\.[0-9]+)'
