# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.22.6
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from kubernetes_asyncio.client.configuration import Configuration


class V1ServiceAccountTokenProjection(object):
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
        'audience': 'str',
        'expiration_seconds': 'int',
        'path': 'str'
    }

    attribute_map = {
        'audience': 'audience',
        'expiration_seconds': 'expirationSeconds',
        'path': 'path'
    }

    def __init__(self, audience=None, expiration_seconds=None, path=None, local_vars_configuration=None):  # noqa: E501
        """V1ServiceAccountTokenProjection - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._audience = None
        self._expiration_seconds = None
        self._path = None
        self.discriminator = None

        if audience is not None:
            self.audience = audience
        if expiration_seconds is not None:
            self.expiration_seconds = expiration_seconds
        self.path = path

    @property
    def audience(self):
        """Gets the audience of this V1ServiceAccountTokenProjection.  # noqa: E501

        Audience is the intended audience of the token. A recipient of a token must identify itself with an identifier specified in the audience of the token, and otherwise should reject the token. The audience defaults to the identifier of the apiserver.  # noqa: E501

        :return: The audience of this V1ServiceAccountTokenProjection.  # noqa: E501
        :rtype: str
        """
        return self._audience

    @audience.setter
    def audience(self, audience):
        """Sets the audience of this V1ServiceAccountTokenProjection.

        Audience is the intended audience of the token. A recipient of a token must identify itself with an identifier specified in the audience of the token, and otherwise should reject the token. The audience defaults to the identifier of the apiserver.  # noqa: E501

        :param audience: The audience of this V1ServiceAccountTokenProjection.  # noqa: E501
        :type audience: str
        """

        self._audience = audience

    @property
    def expiration_seconds(self):
        """Gets the expiration_seconds of this V1ServiceAccountTokenProjection.  # noqa: E501

        ExpirationSeconds is the requested duration of validity of the service account token. As the token approaches expiration, the kubelet volume plugin will proactively rotate the service account token. The kubelet will start trying to rotate the token if the token is older than 80 percent of its time to live or if the token is older than 24 hours.Defaults to 1 hour and must be at least 10 minutes.  # noqa: E501

        :return: The expiration_seconds of this V1ServiceAccountTokenProjection.  # noqa: E501
        :rtype: int
        """
        return self._expiration_seconds

    @expiration_seconds.setter
    def expiration_seconds(self, expiration_seconds):
        """Sets the expiration_seconds of this V1ServiceAccountTokenProjection.

        ExpirationSeconds is the requested duration of validity of the service account token. As the token approaches expiration, the kubelet volume plugin will proactively rotate the service account token. The kubelet will start trying to rotate the token if the token is older than 80 percent of its time to live or if the token is older than 24 hours.Defaults to 1 hour and must be at least 10 minutes.  # noqa: E501

        :param expiration_seconds: The expiration_seconds of this V1ServiceAccountTokenProjection.  # noqa: E501
        :type expiration_seconds: int
        """

        self._expiration_seconds = expiration_seconds

    @property
    def path(self):
        """Gets the path of this V1ServiceAccountTokenProjection.  # noqa: E501

        Path is the path relative to the mount point of the file to project the token into.  # noqa: E501

        :return: The path of this V1ServiceAccountTokenProjection.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this V1ServiceAccountTokenProjection.

        Path is the path relative to the mount point of the file to project the token into.  # noqa: E501

        :param path: The path of this V1ServiceAccountTokenProjection.  # noqa: E501
        :type path: str
        """
        if self.local_vars_configuration.client_side_validation and path is None:  # noqa: E501
            raise ValueError("Invalid value for `path`, must not be `None`")  # noqa: E501

        self._path = path

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1ServiceAccountTokenProjection):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1ServiceAccountTokenProjection):
            return True

        return self.to_dict() != other.to_dict()
