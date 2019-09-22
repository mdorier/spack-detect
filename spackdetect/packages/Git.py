from ..PackageTypes import ExecutablePackage


class Git(ExecutablePackage):
    
    executable = 'git'
    version_args = ['--version']
    version_regex = '[0-9]+\.[0-9]+(\.[0-9]+)?'
