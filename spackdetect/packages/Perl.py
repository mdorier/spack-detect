from ..PackageTypes import ExecutablePackage


class Perl(ExecutablePackage):
    
    executable = 'perl'
    version_args = ['--version']
    version_regex = '[0-9]+\.[0-9]+\.[0-9]+'
