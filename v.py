#import plop

def deuce():
    print("dropping deuce")

## Find the library in LD_LIBRARY_PATH and load it

import ctypes
#import os


# Add the directory containing your library to LD_LIBRARY_PATH
#ld_library_path = os.environ.get("LD_LIBRARY_PATH", "")
#library_paths = ld_library_path.split(":")

#library=None

#for path in library_paths:
#    try:
#        print("trying " + path)
#        library = ctypes.CDLL(os.path.join(path, "libplop.so"))

library = ctypes.CDLL("libv.so")


#        break  # Found the library
#    except OSError:
#        pass  # Library not found in this directory

# my_library=ctypes.cdll.LoadLibrary("src/plop.so")

#plop1=library.plop1
#plop2=library.plop2

v1=library.v1
v2=library.v2

