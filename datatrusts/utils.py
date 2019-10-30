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

#TODO: from_trustfile

from .trust_context import TrustContext, DataTrust
import json
import pandas as pd
import pypandoc

def from_trustfile(trustfile):
    """
    Creates ad instance of the :class:`Datatrust <DataTrust>` object from a json trustfile

    :param trustfile:
    :return datatrust:
    """
    with open(trustfile) as handle:
        trustdict = json.loads(handle.read())
    dt = DataTrust()

    for key, value in trustdict.items():
        setattr(dt,key,value)

    return dt

def to_trustfile(datatrust,filename):
    """
    Creates json trustfile from a :class:`DataTrust <DataTrust>` object.

    :param trustfile:
    :return:
    """
    with open(filename, 'w') as fp:
        json.dump(datatrust,fp)

    return print('trustfile writen to %s' % filename)

def to_dataframe_from_list(listdicts):
    """
    Creates a Pandas :class:`DataFrame <DataFrame>` object from lists within a :class:`DataTrust <DataTrust>` instance.

    :param listdicts:
    :return DataFrame:
    """

    return df = pd.DataFrame(listdicts)



def write_data_trust_agreement(datatrust, filename="data_trust_member_agreement", format='readme'):
    """

    :param datatrust: pass the datatrust object
    :param format: defines the format for the contract output. Valid values include
    :param filename: allows user to pass filename for output contract
    :return: document formatted in
    """
    #create readme as base format
    if format=='readme':



    return 0

def safe_mmkdir(directory, exist_ok=True):
    """Simple wrapper since exist_ok is not available in python 2"""
    if not exist_ok:
        raise ValueError(
            "This wrapper should only be used for exist_ok=True; it is designed to make porting easier later")
    try:
        os.makedirs(directory)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise