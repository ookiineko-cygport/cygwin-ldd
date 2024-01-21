#!/usr/bin/env python
# WTFPL - Do What the Fuck You Want to Public License
from __future__ import print_function
import pefile
import os
import os.path
import sys
import re


def get_dependency(filename):
    deps = []
    pe = pefile.PE(filename)
    for imp in pe.DIRECTORY_ENTRY_IMPORT:
        deps.append(imp.dll.decode())
    return deps


def dep_tree(target, root, prefix=None):
    if not prefix:
        #print('Target =', target)
        prefix = '/usr/'+target+'/bin'
        #print('Using default prefix', prefix)
    dep_dlls = dict()

    def dep_tree_impl(root, prefix):
        for dll in get_dependency(root):
            if dll in dep_dlls:
                continue
            full_path = os.path.join(prefix, dll)
            if os.path.exists(full_path):
                dep_dlls[dll] = full_path
                dep_tree_impl(full_path, prefix=prefix)
            else:
                dep_dlls[dll] = 'not found'

    dep_tree_impl(root, prefix)
    return (dep_dlls)


if __name__ == '__main__':
    if not (m := re.match('^(.*)-ldd$', os.path.basename(sys.argv[0]))):
        raise ValueError('executable must be named ${TARGET}-ldd')
    arch = m.groups()[0]
    filename = sys.argv[1]
    for dll, full_path in dep_tree(arch, filename).items():
        print(' ' * 7, dll, '=>', full_path)

