import subprocess
import re

class BasePackage():
    """
    Base class for all packages. Classes that do not derive (directly or indirectly)
    from this class will not be considered by the detection program.
    """
    pass

class ExecutablePackage(BasePackage):
    """
    Packages deriving from ExecutablePackage have an executable that can be called
    with an argument such as --version to get the version of the package. It is
    assumed that the path to the system-provided package is in PATH.

    Packages deriving from this class must have the 'executable', 'version_args'
    and 'version_regex' class variables.
    """

    @staticmethod
    def version(pkg):
        command = [ pkg.executable ]
        command.extend(pkg.version_args)
        proc = subprocess.Popen(command,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT)
        stdout_value, stderr_value = proc.communicate()
        v = re.search(pkg.version_regex, stdout_value)
        return v.group()

    @staticmethod
    def path(pkg):
        command = [ 'which', pkg.executable ]
        proc = subprocess.Popen(command,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT)
        stdout_value, stderr_value = proc.communicate()
        p = stdout_value.rstrip()
        p = p.split('/bin/')
        del p[-1]
        return '/bin/'.join(p)
