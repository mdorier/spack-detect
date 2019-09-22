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
