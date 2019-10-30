
# -*- coding: utf-8 -*-

"""
datatrusts.principles
~~~~~~~~~~~~~~
This module provides the ability to create ethical principles for a data trust, along with default principles.

Available principles:
``Fairness``:
    The ability for an individual to determine whether or not their data will be used


These defaults come from a community-led effort managed by Data for Democracy called the Global Data Ethics Project.
Detailed documentation about these principles can be found here:

https://www.datafordemocracy.org/documents/GDEP-Ethics-Framework-Principles-one-sheet.pdf

"""

COMMITMENTS = [
            "FAIRNESS: All trust members and approved data users will make a dedicated effort to understand, mitigate and communicate the presence of bias in both data practice and consumption ",
            "OPENNESS: All trust members and approved data users will practice humility and openness. Transparent practices, community engagement, and responsible communications are an integral part of my data ethics practice.",
            "RELIABILITY: All trust members and approved data users will ensure that every effort is made to glean a complete understanding of what is contained within data, where it came from, and how it was created. They will also extend this effort for future users of all data and derivative data.",
            "TRUST: All trust members and approved data users will work to build public confidence in data practitioners. They will make every effort to use data and algorithm in ways that maximize the informed participation of people in in communities being served and impacted by the data.",
            "SOCIAL BENEFIT: All trust members and approved data users will place people before data and am responsible for maximizing social benefit and minimizing harm. They will consider the impact of their work on communities of people, other living beings, ecosystems and the world-at-large."
            ]

CPEDS_PRINCIPLES = {
            "Principle 1":"Consider (if not collect) informed and purposeful consent of data subjects for all projects, and discard resulting data when that consent expires.",
            "Principle 2":"Make best effort to guarantee the security of data, subjects, and algorithm to prevent unauthorized access, policy violations, tampering, or other harm or actions outside the data subjects’ consent.",
            "Principle 3":"Make best effort to protect anonymous data subjects, and any associated data, against any attempts to reverse-engineer, de-anonymize, or otherwise expose confidential information.",
            "Principle 4":"Practice responsible transparency as the default where possible, throughout the entire data lifecycle.",
            "Principle 5":"Foster diversity by making efforts to ensure inclusion of participants, representation of viewpoints and communities, and openness. The data community should be open to, welcoming of, and inclusive of people from diverse backgrounds.",
            "Principle 6":"Acknowledge and mitigate unfair bias throughout all aspects of data work.",
            "Principle 7":"Hold up datasets with clearly established provenance as the expected norm, rather than the exception.",
            "Principle 8":"Respect relevant tensions of all stakeholders as it relates to privacy and data ownership.",
            "Principle 9":"Take great care to communicate responsibly and accessibly.",
            "Principle 10":"Ensure that all data practitioners take responsibility for exercising ethical imagination in their work, including considering the implication of what came before and what may come after, and actively working to increase benefit and prevent harm to others."
            }

def default_principles():
    return {principle:text for (principle, text) in CPEDS_PRINCIPLES.items()}
