# This file contains a helper function to get the absolute path
# of the built "template" go library.
# The reason we need this is because setuptools builds shared libraries
# with a filename encoding the platform (for example, "template.cpython-38-x86_64-linux-gnu.so")

import sysconfig
from pathlib import Path
from kapitan_helm import helm_binding # We use this to determine the path

def get_dl_path():
    target_folder = Path(helm_binding.__file__)
    target_folder = target_folder.parent
    target_folder = target_folder.parent
    target_lib = target_folder / "template{}".format(sysconfig.get_config_var("EXT_SUFFIX"))

    return str(target_lib)



if __name__ == "__main__":
    print(get_dl_path())