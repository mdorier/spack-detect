from ..PackageTypes import ExecutablePackage


class Gettext(ExecutablePackage):
    
    executable = 'gettext'
    version_args = ['--version']
    version_regex = '[0-9]+\.[0-9]+(\.[0-9]+)*'
