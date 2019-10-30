
# -*- coding: utf-8 -*-

# Copyright 2019 BrightHive Inc. All Rights Reserved.
# <see AUTHORS file>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

"""
    datatrusts.cli
    ~~~~~~~~~
    A simple command line application to create data trusts.
    :copyright: © 2019 by the BrightHive team.
    :license: Apache 2.0, see LICENSE for more details.
"""


from __future__ import print_function


from .init import (
    script_relative_path,
    scaffold_directories_and_notebooks,
    greeting_1
    msg_prompt_lets_begin
)

import ast
import inspect
import os
import platform
import re
import ssl
import sys
import traceback
from functools import update_wrapper
from operator import attrgetter
from threading import Lock, Thread

import six
import re
import os
import json
import logging
import sys
import warnings

import click

from datatrusts import __version__
import datatrusts
from datatrusts.trust_context import TrustContext, DataTrust



warnings.filterwarnings('ignore')

try:
    from termcolor import colored
except ImportError:
    colored = None

# Take over the entire datatrusts module logging namespace when running CLI
logger = logging.getLogger("datatrusts")


def cli_message(string):
    mod_string = re.sub(
        "<blue>(.*?)</blue>",
        colored("\g<1>", "blue"),
        string
    )
    mod_string = re.sub(
        "<green>(.*?)</green>",
        colored("\g<1>", "green"),
        mod_string
    )
    mod_string = re.sub(
        "<yellow>(.*?)</yellow>",
        colored("\g<1>", "yellow"),
        mod_string
    )

    six.print_(colored(mod_string))


@click.group()
@click.version_option(version=__version__)
@click.option('--verbose', '-v', is_flag=True, default=False,
              help='Set datatrusts to use verbose output.')
def cli(verbose):
    """datatrusts command-line interface"""
    if verbose:
        logger.setLevel(logging.DEBUG)

@cli.command('init', short_help='Create a new data trust project')
@click.argument('trust_name')
@click.option('--trustfile', '-f', default=None)
@click.option('--directory', '-d', default='./')
def init(trust_name):
    """Initialize a new data trust project.

    This guided input walks the user through setting up a trust instance.

    It scaffolds directories, sets up the resource registry, creates a trustfile, and
    appends to a `.gitignore` file.
    """
    six.print_(colored(
        figlet_format("Data Trusts", font="big"),
        color="cyan"
    ))

    cli_message(greeting_1)

    if not click.confirm(msg_prompt_lets_begin, default=True):
        cli_message(
            "OK - run datatrusts init again when ready. Exiting..."
        )
        exit(0)


    try:
        context = TrustContext.create(target_directory)
    except DataContextError as err:
        logger.critical(err.message)
        sys.exit(-1)

    base_dir = context.root_directory
    scaffold_directories_and_notebooks(base_dir)
    cli_message(
        "\nDone.",
    )



@cli.command('create', short_help='Create a new data trust.')
@click.option('--title', '-i', default='New Data Trust',
              help='The title of the trust')
@click.option('--goal', '-g', default='Combine data for shared value',
              help='The initial primary goal of the data trust')
@click.option('--trustee', '-t', default='Combine data for shared value',
              help='The initial trustee of the trust')
@click.option('--member', '-m', default='Member 1',
              help='The initial members of the trust')
@pass_script_info
def write_trustfile(title, goal, trustee, member):
    """Create a new data trust with a minimum viable coalition.

    """
    datatrust = datatrusts.DataTrust(title=title, goals=goal, trustee=trustee, members=member)


def main(as_module=False):
    args = sys.argv[1:]

    if as_module:
        this_module = 'datatrusts'

        if sys.version_info < (2, 7):
            this_module += '.cli'

        name = 'python -m ' + this_module

        # Python rewrites "python -m datatrusts" to the path to the file in argv.
        # Restore the original command so that the reloader works.
        sys.argv = ['-m', this_module] + args
    else:
        name = None

    cli.main(args=args, prog_name=name)


if __name__ == '__main__':
    main(as_module=True)