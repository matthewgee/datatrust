# -*- coding: utf-8 -*-

import os
import glob
import shutil

from datatrusts.utils import safe_mmkdir
from datatrusts import __version__ as __version__


def script_relative_path(file_path):
    '''
    Useful for testing with local files. Use a path relative to where the
    test resides and this function will return the absolute path
    of that file. Otherwise it will be relative to script that
    ran the test

    Note this is expensive performance wise so if you are calling this many
    times you may want to call it once and cache the base dir.
    '''
    # from http://bit.ly/2snyC6s

    import inspect
    scriptdir = inspect.stack()[1][1]
    return os.path.join(os.path.dirname(os.path.abspath(scriptdir)), file_path)


def scaffold_directories_and_notebooks(base_dir):
    """Add basic directories for an initial, opinionated data trust."""

    safe_mmkdir(base_dir, exist_ok=True)
    notebook_dir_name = "notebooks"

    open(os.path.join(base_dir, ".gitignore"), 'w').write("misc/")

    for directory in [notebook_dir_name, "expectation", "resource", "misc", "dag", "algorithm"]:
        safe_mmkdir(os.path.join(base_dir, directory), exist_ok=True)

    for misc in ["validations", "credentials", "documentation", "samples"]:
        safe_mmkdir(os.path.join(base_dir, "misc",
                                 misc), exist_ok=True)

    for notebook in glob.glob(script_relative_path("../notebooks/init_notebooks/*.ipynb")):
        notebook_name = os.path.basename(notebook)
        shutil.copyfile(notebook, os.path.join(
            base_dir, notebook_dir_name, notebook_name))


# !!! This injects a version tag into the docs. We should test that those versioned docs exist in RTD.
greeting_1 = """
Responsibly discover more together with a Data Trust.

If you're new to BrightHive Data Trusts, this tutorial is a good place to start:

    <blue>https://docs.brighthive.io</blue>
""".format(__version__.replace(".", "_"))

msg_prompt_lets_begin = """
Let's get started with a new data trust by scaffolding a new datatrust directory:

    datatrust_name
        ├── datatrust.yml
        ├── trustfile
        ├── resource
        │   ├── datapackages
        │   ├── raw
        │   ├── resource.yml
        ├── expectation
        ├── dag
        ├── algorithm
        ├── notebooks
        ├── misc
        │   ├── credentials
        │   ├── documentation
        │   └── examples
        └── .gitignore

OK to proceed?
"""