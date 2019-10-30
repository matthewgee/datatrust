


class Party(object):

    def __init__(self, type=None, name=None):
        """
        Define a party to a data trust. This is the superclass inherited by all Party type classes, including Trustee, Member, User, and Owner.
        """
        self.name = "" if name is None else name
        self.type = "" if type is None else type

    @property
    def name(self):

        return self.name

    @property
    def type(self):

        return self.type

    def summary(self):
        print("Name: " + self.name)
        print("Type: " + self.type)


class Trustee(Party):

    def __init__(self,name=None):
        """
        Defines a Trustee as a type of party in a datatrust, along with the metadata model
        """
        self.type = "trustee"



class Member(Party):

    def __init__(self):
        """

        """
        self.type = "member"

class User(Party):

    def __init__(self):
        """

        """
        self.type = "user"


class Owner(Party):

    def __init__(self):
        """

        """
        self.type = "owner"