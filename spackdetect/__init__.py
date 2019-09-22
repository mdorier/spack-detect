import importlib
import inspect
import os
import glob
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

def main():
    for pkg in list_packages(os.path.dirname(__file__)+'/packages',
            'spackdetect.packages',
            base_class=BasePackage):
        pkg_name = package_name_from_class(pkg)
        print('Package '+pkg_name+' version: '+str(detect_version(pkg)))
