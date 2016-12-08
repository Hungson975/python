# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.5.0-beta.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class V1alpha1Role(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, metadata=None, rules=None):
        """
        V1alpha1Role - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'metadata': 'V1ObjectMeta',
            'rules': 'list[V1alpha1PolicyRule]'
        }

        self.attribute_map = {
            'metadata': 'metadata',
            'rules': 'rules'
        }

        self._metadata = metadata
        self._rules = rules


    @property
    def metadata(self):
        """
        Gets the metadata of this V1alpha1Role.
        Standard object's metadata.

        :return: The metadata of this V1alpha1Role.
        :rtype: V1ObjectMeta
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this V1alpha1Role.
        Standard object's metadata.

        :param metadata: The metadata of this V1alpha1Role.
        :type: V1ObjectMeta
        """

        self._metadata = metadata

    @property
    def rules(self):
        """
        Gets the rules of this V1alpha1Role.
        Rules holds all the PolicyRules for this Role

        :return: The rules of this V1alpha1Role.
        :rtype: list[V1alpha1PolicyRule]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """
        Sets the rules of this V1alpha1Role.
        Rules holds all the PolicyRules for this Role

        :param rules: The rules of this V1alpha1Role.
        :type: list[V1alpha1PolicyRule]
        """
        if rules is None:
            raise ValueError("Invalid value for `rules`, must not be `None`")

        self._rules = rules

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
