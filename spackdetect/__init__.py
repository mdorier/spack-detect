import importlib
import inspect
import os
import glob
import argparse
import yaml
from .PackageTypes import BasePackage
from .util import package_name_from_class

def list_packages(
        plugins_package_directory_path,
        plugins_package_name=None,
        base_class=None):

    if(plugins_package_name is None):
        plugins_package_name = os.path.basename(plugins_package_directory_path)

    # -----------------------------
    # Iterate all python files within that directory
    plugin_file_paths = glob.glob(os.path.join(plugins_package_directory_path, "*.py"))
    for plugin_file_path in plugin_file_paths:
        plugin_file_name = os.path.basename(plugin_file_path)

        module_name = os.path.splitext(plugin_file_name)[0]

        if module_name.startswith("__"):
            continue

        # -----------------------------
        # Import python file
    
        module = importlib.import_module("." + module_name, package=plugins_package_name)
        # -----------------------------
        # Iterate items inside imported python file

        for item in dir(module):
            value = getattr(module, item)
            if not value:
                continue

            if not inspect.isclass(value):
                continue

            if base_class is not None:
                if not issubclass(value, base_class):
                    continue

            if value == base_class:
                continue

            if not '.packages.' in value.__module__:
                continue

            # -----------------------------
            # Instantiate / return type (depends on create_instance)

            yield value

def detect_version(package):
    for base in package.__bases__:
        try:
            v = base.version(package)
            return v
        except Exception as e:
            pass
    return None

def detect_path(package):
    for base in package.__bases__:
        try:
            v = base.path(package)
            return v
        except Exception as e:
            pass
    return None

def print_red(msg):
    print(u'\u001b[31m'+str(msg)+u'\u001b[0m')

def print_yellow(msg):
    print(u'\u001b[33m'+str(msg)+u'\u001b[0m')

def print_green(msg):
    print(u'\u001b[32m'+str(msg)+u'\u001b[0m')

def main():
    parser = argparse.ArgumentParser(description='Autodetection of system-provided Spack packages.')
    parser.add_argument('-o', action='store', help='Output YAML file', required=True)
    parser.add_argument('-v', action='store_true', help='Verbose standard output', default=False)
    args = parser.parse_args()

    verbose = args.v
    output = args.o

    packages = [ pkg for pkg in list_packages(os.path.dirname(__file__)+'/packages',
                                    'spackdetect.packages',
                                    base_class=BasePackage) ]
    yaml_data = dict()
    yaml_data['packages'] = dict()

    for pkg in packages:
        pkg_name = pkg.package_name
        pkg_version = detect_version(pkg)
        if(pkg_version is None):
            if(verbose):
                print_yellow('Package '+pkg_name+' not found on this system')
            continue
        pkg_path = detect_path(pkg)
        p = { 'paths' : {
                pkg_name+'@'+pkg_version : pkg_path
                },
              'buildable' : False
            }
        yaml_data['packages'][pkg_name] = p
        if(verbose):
            print_green('Package '+pkg_name+' found, version '+pkg_version+' in '+pkg_path)

    if(verbose):
        print('Generating configuration in '+output)
    with open(output,'w+') as f:
        f.write(yaml.dump(yaml_data))
