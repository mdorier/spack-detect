import re

def package_name_from_class(pkg):
    s = str(pkg).split('.')[-1]
    words = re.findall('[A-Z][^A-Z]*', s)
    return '-'.join([ w.lower() for w in words])
