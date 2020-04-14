# coding: utf-8

"""
    NeoLoad API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class ProjectDefinition(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'project_id': 'str',
        'project_name': 'str',
        'project_version': 'str',
        'as_code_files': 'list[AsCodeFile]',
        'scenarios': 'list[ScenarioDefinition]'
    }

    attribute_map = {
        'project_id': 'projectId',
        'project_name': 'projectName',
        'project_version': 'projectVersion',
        'as_code_files': 'asCodeFiles',
        'scenarios': 'scenarios'
    }

    def __init__(self, project_id=None, project_name=None, project_version=None, as_code_files=None, scenarios=None, local_vars_configuration=None):  # noqa: E501
        """ProjectDefinition - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._project_id = None
        self._project_name = None
        self._project_version = None
        self._as_code_files = None
        self._scenarios = None
        self.discriminator = None

        if project_id is not None:
            self.project_id = project_id
        if project_name is not None:
            self.project_name = project_name
        if project_version is not None:
            self.project_version = project_version
        if as_code_files is not None:
            self.as_code_files = as_code_files
        if scenarios is not None:
            self.scenarios = scenarios

    @property
    def project_id(self):
        """Gets the project_id of this ProjectDefinition.  # noqa: E501

        Neoload Project Id.  # noqa: E501

        :return: The project_id of this ProjectDefinition.  # noqa: E501
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ProjectDefinition.

        Neoload Project Id.  # noqa: E501

        :param project_id: The project_id of this ProjectDefinition.  # noqa: E501
        :type: str
        """

        self._project_id = project_id

    @property
    def project_name(self):
        """Gets the project_name of this ProjectDefinition.  # noqa: E501

        Neoload Project name.  # noqa: E501

        :return: The project_name of this ProjectDefinition.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this ProjectDefinition.

        Neoload Project name.  # noqa: E501

        :param project_name: The project_name of this ProjectDefinition.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def project_version(self):
        """Gets the project_version of this ProjectDefinition.  # noqa: E501

        Neoload Project version.  # noqa: E501

        :return: The project_version of this ProjectDefinition.  # noqa: E501
        :rtype: str
        """
        return self._project_version

    @project_version.setter
    def project_version(self, project_version):
        """Sets the project_version of this ProjectDefinition.

        Neoload Project version.  # noqa: E501

        :param project_version: The project_version of this ProjectDefinition.  # noqa: E501
        :type: str
        """

        self._project_version = project_version

    @property
    def as_code_files(self):
        """Gets the as_code_files of this ProjectDefinition.  # noqa: E501


        :return: The as_code_files of this ProjectDefinition.  # noqa: E501
        :rtype: list[AsCodeFile]
        """
        return self._as_code_files

    @as_code_files.setter
    def as_code_files(self, as_code_files):
        """Sets the as_code_files of this ProjectDefinition.


        :param as_code_files: The as_code_files of this ProjectDefinition.  # noqa: E501
        :type: list[AsCodeFile]
        """

        self._as_code_files = as_code_files

    @property
    def scenarios(self):
        """Gets the scenarios of this ProjectDefinition.  # noqa: E501


        :return: The scenarios of this ProjectDefinition.  # noqa: E501
        :rtype: list[ScenarioDefinition]
        """
        return self._scenarios

    @scenarios.setter
    def scenarios(self, scenarios):
        """Sets the scenarios of this ProjectDefinition.


        :param scenarios: The scenarios of this ProjectDefinition.  # noqa: E501
        :type: list[ScenarioDefinition]
        """

        self._scenarios = scenarios

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ProjectDefinition):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProjectDefinition):
            return True

        return self.to_dict() != other.to_dict()