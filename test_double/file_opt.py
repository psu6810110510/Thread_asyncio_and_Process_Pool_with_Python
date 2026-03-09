import os
import os.path


def rm_when_lower(filename):
    if filename.isupper():
        return

    if os.path.isfile(filename):
        os.remove(filename)
