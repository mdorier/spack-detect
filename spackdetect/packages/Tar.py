from ..PackageTypes import ExecutablePackage


class Tar(ExecutablePackage):
    
    executable = 'tar'
    version_args = ['--version']
    version_regex = '[0-9]+\.[0-9]+(\.[0-9]+)?'
