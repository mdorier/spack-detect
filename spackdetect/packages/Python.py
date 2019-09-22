from ..PackageTypes import ExecutablePackage


class Python(ExecutablePackage):
    
    executable = 'python'
    version_args = ['--version']
    version_regex = '[0-9]+\.[0-9]+(\.[0-9]+)?'
