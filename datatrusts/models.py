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
datatrusts.models
~~~~~~~~~~~~~~~
This module contains the primary objects for datatrusts.
"""

"""
TODO: Consider consolidating member resource and trust resource into simply resource, where a property is resource owner.
TODO: Consider chancing dicts to lists for members, 
"""

from datatrusts.templates.principles import default_principles


class DataTrust(object):
    """A user-created :class:`DataTrust (Datatrust>` object

    The DataTrust object implements a data structure for storing data trust info and acts as the central
    object.  It is passed the name of the Trust.  Once it is created it will act as a central registry for
    the create, add, destroy, and view functions, the data trust rules, templates configuration and much more.

    :param title: the title of the trust.
    :param goals: One or more shared purposes of trust members in combining their data.
    :param trustee: dictionary of headers to send.
    :param members: dictionary of {filename: fileobject} files to multipart upload.
    :param resources: the body to attach to the request. If a dictionary or
        list of tuples ``[(key, value)]`` is provided, form-encoding will
        take place.
    :param uses: json for the body to attach to the request (if files or data is not specified).
    :param functions: algorithm and mathematical functions that can be called in one or more dag in the generation and use of trust resource. This is to enforce algorithmic trasparency.
    :param dags: dictionary of functions that are approved for operation on resource.
    :param users: dictionary of users of resource.
    :param principles: dictionary of ethical principles that all trust members and trustee agree to.

    Usage::

      >>> import datatrusts
      >>> dt = datatrusts.Datatrust('Goodwill', ['Measuring the impact of job training programs in the goodwill network.'])
      >>> dt.show()
        title:
    """

    def __init__(self,
                 title=None, goals=None, trustee=None, members=None, resources=None,
                 uses=None, functions=None, dags=None, users=None, principles=None):

        # Default empty dicts for dict params.
        title = "" if title is None else title
        goals = [] if goals is None else goals #a list of strings, each articulating a goal
        trustee = [] if trustee is None else trustee
        members = [] if members is None else members #a dict of dicts
        resources = [] if resources is None else resources
        uses = [] if uses is None else uses
        functions = [] if functions is None else functions
        dags = [] if dags is None else dags
        users = [] if users is None else users
        principles = [] if principles is None else principles

        self.principles = default_principles()

        self.title = title
        self.goals = goals
        self.trustee = trustee
        self.members = members
        self.resouces = resources
        self.uses = uses
        self.functions = functions
        self.dags = dags
        self.users = users
        self.principles = principles

    def add_member(self, name=None, data_steward_name=None, data_steward_email=None, status=None, membership_date=None):
        """
        Adds new member to the list of members in the trust
        :param name: legal name of the member organization
        :param data_steward_name: name of the data steward for the member organization
        :param data_steward_email: contact email for the data steward for the member organization
        :return:
        """
        self.members = self.members.append({"name":name,"data_steward_name":data_steward_name,"data_steward_emailt":data_steward_email, "status":status, "membership_date":membership_date})

    def add_resource(self, name=None, type=None, owner=None, description=None, datapackage=None):
        """
        Adds new data resource to the list of resource in the trust
        :param name:
        :param owner:
        :param description:
        :param datapackage:
        :return:
        """
        self.resources = self.resources.append({"name":name, "type":type, "owner":owner, "desciption":description, "datapackage":datapackage})



    def summary(self):
        """
        Reports a summary of the trust in standard out
        :return:
        """
        print("Summary of ", self.title)
        print("List of Goals: ", self.goals)
        print("Trustee Name: ", self.trustee["name"])
        print("Number of Members", len(self.members))
        print("Number of Resources: ", len(self.resources))