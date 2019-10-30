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
DataTrust Python Library

datatrusts is a multi-party data management library, written in python, that helps organizations set up data trusts.



"""

from __future__ import absolute_import

#module API
from .party import Party
from .trust_context import TrustContext, DataTrust


# Also importable from root
#from .connection import postgresql

__version__ = '0.0.1'


# module level doc-string
__doc__ = """
datatrusts - a Python library that can help you build and manage Data Trusts
=====================================================================
**datatrusts** is a Python package providing data
structures designed to help establish multi-party data trusts.
It aims to be the fundamental high-level building block for
creating and managing multi-party data sharing. Additionally, it has
the broader goal of becoming **the most powerful and flexible open source data
sharing tool available in any language**. Help us move toward this goal
by contributing.

Main Features
-------------
Here are just a few of the things that datatrusts will help you do:
  - set up the parties of a data trust
  - set up and manage the data resource involved in a data trust
"""
