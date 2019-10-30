# -*- coding: utf-8 -*-

import .utils

class Resource(object):
    """Resources are the primary object managed by a trust. They are described datasets that have flexible, associated metdata.



    """

    def __init__(self, name, type, trust_context=None):
        """Create a new resource


        :param name:
        :param type:
        :param trust_context:
        """

        self._trust_context=trust_context
        self._name = name

        @property
        def name(self):
            """
            Property for the resource name
            :param self:
            :return:
            """
            return self._name

        @property
        def trust_context(self):
            """
            Property for attached TrustContext
            :param self:
            :return:
            """
            return self._trust_context


#TODO: add data package as definition
#TODO: add relations: mayUse, mayCreate
