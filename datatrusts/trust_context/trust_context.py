# -*- coding: utf-8 -*-

import gremlin_python
import toml
import networkx as nx

from datatrust.party import Party

#TODO: Add graph context using gremlin

class TrustContext(object):
    """A TrustContext represents a Data Trust repository. It organizes the key components and relationships between the properties of a trust
    (name, goals, domain, etc.) the parties to the trust (members, trustee, users, governance body, etc.) the resource, the relationships, and entities of a trust (
    members, resource, dag, algorithm, and uses.

    The TrustContext is stored and configured via a json file called a trustfile stored in a directory call trustfile.
    Trustfiles

    One of the goals of the TrustContext is to increase the discoverability onf novel connection across data resource.

    """

    @classmethod
    def create(cls, trust_root_dir=None):
        """Build a new data trust context.

        :param trust_root_dir:
        :return:
        """

        if not os.path.isdir(project_root_dir):
            raise DataContextError("project_root_dir must be a directory in which to initialize a new TrustContext")
        else:
            try:
                os.mkdir(os.path.join(project_root_dir, "data_trust"))
            except (FileExistsError, OSError):
                raise DataContextError(
                    "Cannot create a TrustContext object when a great_expectations directory "
                    "already exists at the provided root directory.")

            with open(os.path.join(project_root_dir, "data_trust/trustfile.toml"), "w") as template:
                template.write(PROJECT_TEMPLATE)

        return cls(os.path.join(project_root_dir, "data_trust"))




    def __init__(self,context_root_dir=None, trustfile=None):
        """TrustContext constructore

        :param context_root_dir:
        :param trustfile:
        """
        # determine the "context root directory" - this is the parent of "trustfiles" dir
        if context_root_dir is None:
            if os.path.isdir("../trustfiles") and os.path.isfile("../Mytrust.yml"):
                context_root_dir = "../"
            elif os.path.isdir("./great_expectations") and \
                    os.path.isfile("./great_expectations/great_expectations.yml"):
                context_root_dir = "./great_expectations"
            elif os.path.isdir("./") and os.path.isfile("./great_expectations.yml"):
                context_root_dir = "./"
            else:
                raise(
                    "Unable to locate context root directory. Please provide a directory name."
                )

        #TODO: set up trust config as TOML file. later convert to JSON


    def graph(self, resources=None):
        """
        Create a graph to represent the resource metadata and governance for sharing
        :param resources:
        :return:
        """

        TrustGraph = nx.MultiDiGraph()
        TrustGraph.add_node()

    def get_trust_config(self, trustfile):
        """

        :param trustfile:
        :return:
        """

        return trustfile


#TODO  add methods: add_goal, add_trustee, add_member,

class DataTrust(TrustContext):
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

    def __init__(self,context_root_dir=None, trustfile=None):
        # Default empty dicts for dict params.
        id = ""
        title = "" if title is None else title
        goals = [] if goals is None else goals  # a list of strings, each articulating a goal
        trustee = [] if trustee is None else trustee
        members = [] if members is None else members  # a dict of dicts
        resources = [] if resources is None else resources
        uses = [] if uses is None else uses
        algorithms = [] if algorithms is None else algorithms
        dags = [] if dags is None else dags
        users = [] if users is None else users
        principles = [] if principles is None else principles


        self.id = id
        self.title = title
        self.goals = goals
        self.trustee = trustee
        self.members = members
        self.resouces = resources
        self.uses = uses
        self.algorithms = algorithms
        self.dags = dags
        self.users = users
        self.principles = principles
        #self.principles = templates.default_principles()

    def create_from_template(self,template_name):

        dt = self

        return dt


    def add_member(self, name=None, data_steward_name=None, data_steward_email=None, status=None, membership_date=None):
        """
        Adds new member to the list of members in the trust
        :param name: legal name of the member organization
        :param data_steward_name: name of the data steward for the member organization
        :param data_steward_email: contact email for the data steward for the member organization
        :return:
        """
        self.members = self.members.append(
            {"name": name, "data_steward_name": data_steward_name, "data_steward_emailt": data_steward_email,
             "status": status, "membership_date": membership_date})

    def add_resource(self, name=None, type=None, owner=None, description=None, datapackage=None):
        """
        Adds new data resource to the list of resource in the trust
        :param name:
        :param owner:
        :param description:
        :param datapackage:
        :return:
        """
        self.resources = self.resources.append(
            {"name": name, "type": type, "owner": owner, "desciption": description, "datapackage": datapackage})

    def summary(self):
        """
        Reports a summary of the trust in standard out
        :return:
        """
        print("Summary of ", self.title)
        print("List of Goals: ", self.goals)
        print("Trustee Name: ", self.trustee["name"])
        print("Number of Members", len(self.members))

    def get_datatrust_config(self):
        """

        :return:
        """
        config = dict(self._datatrust)
        


    def save_trustfile(self, filepath=None):
        """
        Saves toml-formatted trustfile to main director base on current trust values.
        :param filepath:
        :return:
        """

        datatrust_config = self.get_datatrust_config()

        if filepath is None and self._trust_context is not None:
            self._trust_context.save_datatrust_config(datatrust_config)
        elif filepath is not None:
            datatrust_config_str = json.dumps(datatrust_config, indent=2)
            open(filepath, 'w').write(datatrust_config_str)
        else:
            raise ValueError("Unable to save trustfile: filepath or trust_context must be available.")
