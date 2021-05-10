IMPORTANT: as of May 2021, this project will no longer be maintained.
To make spack detect existing external packages, please use
[spack external find](https://spack.readthedocs.io/en/latest/build_settings.html?automatically-find-external-packages).

# spack-detect

This project provides utilities to detect system-provided packages
and generate the YAML configurations for Spack.

### Installing

```
git clone https://github.com/mdorier/spack-detect.git
cd spack-detect
python setup.py install
```

### Using

To generate `packages.yaml` in the current directory, use the following command.

```
spack-detect -o packages.yaml -v
```

### Contributing

If you want to contribute a package, you can create a package file in
`spackdetect/packages`. The python file should have the package name following
spack's naming conventions. For instance, for the `zlib` package, we want to
have a `Zlib.py` file (first letter capitalized). For the `pkg-config` package,
we want the name to be `PkgConfig.py` (first letter of each word capitalized).

If your package can be detected by searching for a header file in a standard
location, make your package class inherite from `HeaderPackage` and define
the `header_file` and `version_macro` variables. For example here is the Zlib
package:

```python
from ..PackageTypes import HeaderPackage


class Zlib(HeaderPackage):
    header_file = 'zlib.h'
    version_macro = 'ZLIB_VERSION'
```

Note that if you don't provide these variables, they will default to `x.h`
and `X_VERSION`, where `x` is your package name (e.g. `zlib` for the `Zlib` package)
and `X` is the capitalized name.

If your package can be detected by executing a command with some arguments
and parsing the output (e.g. `bison --version`), you can make it inherite from
`ExecutablePackage` and define the `executable`, `version_args`, and `version_regex`
variables. `executable` is the name of the executable to call, `version_args` is
the array of argument to pass to get the version, and `version_regex` is the regular
expression to run on the output to figure out the version. Here is an example
witgh the Bison package.

```python
from ..PackageTypes import ExecutablePackage


class Bison(ExecutablePackage):
    executable = 'bison'
    version_args = ['--version']
    version_regex = '[0-9]+\.[0-9]+(\.[0-9]+)?'
```

Note that if you don't provide these variables, they will default to `'x'`
(where `x` is the name of the package, e.g., `bison` for the Bison package),
`['--version']`, and `'[0-9]+\.[0-9]+(\.[0-9]+)?'`, respectively.
