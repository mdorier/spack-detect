from ..PackageTypes import ExecutablePackage


class Flex(ExecutablePackage):
    
    executable = 'flex'
    version_args = ['--version']
    version_regex = '[0-9]+\.[0-9]+(\.[0-9]+)?'
