from ..PackageTypes import ExecutablePackage

class Openssl(ExecutablePackage):
    version_args = ['version']
    version_regex = '[0-9]+\.[0-9]+(\.[0-9]+[a-z]?)?'
