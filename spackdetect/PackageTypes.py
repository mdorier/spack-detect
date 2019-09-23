import subprocess
import re
from os import path
from .util import package_name_from_class

class BasePackage(object):
    """
    Base class for all packages. Classes that do not derive (directly or indirectly)
    from this class will not be considered by the detection program.
    """
    pass

class ExecutablePackageMeta(type):
    """
    Metaclass for ExecutablePackage. When creating a child class of ExecutablePackage,
    this metaclass will set the default package_name, executable, version_args, and
    version_regex fields.
    """
    def __new__(metaname, classname, baseclasses, attrs):
        if not 'package_name' in attrs:
            attrs['package_name'] = package_name_from_class(classname)
        if not 'executable' in attrs:
            attrs['executable'] = package_name_from_class(classname)
        if not 'version_args' in attrs:
            attrs['version_args'] = ['--version']
        if not 'version_regex' in attrs:
            attrs['version_regex'] = '[0-9]+\.[0-9]+(\.[0-9]+)?'
        cls = type.__new__(metaname, classname, baseclasses, attrs)
        return cls

class ExecutablePackage(BasePackage):
    """
    Packages deriving from ExecutablePackage have an executable that can be called
    with an argument such as --version to get the version of the package. It is
    assumed that the path to the system-provided package is in PATH.

    Packages deriving from this class can override the 'executable', 'version_args'
    and 'version_regex' fields.
    """

    __metaclass__ = ExecutablePackageMeta

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


class HeaderPackageMeta(type):
    """
    Metaclass for HeaderPackage. When creating a child class of HeaderPackage,
    this metaclass will set the default package_name, header_file, version_macro fields.
    """
    def __new__(metaname, classname, baseclasses, attrs):
        if not 'package_name' in attrs:
            attrs['package_name'] = package_name_from_class(classname)
        if not 'header_file' in attrs:
            attrs['header_file'] = package_name_from_class(classname)+'.h'
        if not 'version_macro' in attrs:
            attrs['version_macro'] = classname.upper()+'_VERSION'
        cls = type.__new__(metaname, classname, baseclasses, attrs)
        return cls


class HeaderPackage(BasePackage):
    """
    Packages deriving from HeaderPackage have a header file that can be
    parsed to find out the version using preprocessor macros. It is assumed
    that the path to such a header file can be found in gcc's default include
    locations.
    """
    __metaclass__ = HeaderPackageMeta
    header_locations = {'/usr/include' : '/usr'}

    @staticmethod
    def __search_header_location(filename):
        for loc in HeaderPackage.header_locations:
            if path.exists(loc + '/' + filename):
                return loc
        return None

    @staticmethod
    def __search_macro_value(filename, macroname):
        with open(filename) as f:
            for line in f:
                if not '#define' in line:
                    continue
                definition = line.split(' ')
                if definition[1] == macroname:
                    v = definition[2].replace('"','').replace('\n','')
                    return v
        return None

    @staticmethod
    def version(pkg):
        location = HeaderPackage.__search_header_location(pkg.header_file)
        fullpath = location + '/' + pkg.header_file
        v = HeaderPackage.__search_macro_value(fullpath, pkg.version_macro)
        return v

    @staticmethod
    def path(pkg):
        loc = HeaderPackage.__search_header_location(pkg.header_file)
        return HeaderPackage.header_locations[loc]
