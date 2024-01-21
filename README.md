### cygwin-ldd

Tool to list dependencies of a dll using python.

Kudos to yan12125 for the original script:
https://gist.github.com/yan12125/63c7241596e628553d21

## Requirements

- Python
- `pefile` package from pypi

## Usage

    $ ln -s cygwin-ldd.sh x86_64-pc-cygwin-ldd
    $ ./x86_64-pc-cygwin-ldd /usr/x86_64-pc-cygwin/bin/cygc++-1.dll
            cygwin1.dll => /usr/x86_64-pc-cygwin/bin/cygwin1.dll
            KERNEL32.dll => not found
            ntdll.dll => not found
            cygc++abi-1.dll => /usr/x86_64-pc-cygwin/bin/cygc++abi-1.dll
            cygunwind-1.dll => /usr/x86_64-pc-cygwin/bin/cygunwind-1.dll

## See also

You can also checkout another similar tool:
https://github.com/LRN/ntldd
