"""
AWS Lambda handler entry point
"""
from ._s3 import list_packages


def read_package_list():
    pass


class IndexBuilder(object):
    """
    This class builds PyPi repository index files for the provided
    package list.
    """

    def __init__(self, packages):
        """
        :param packages: the package list
        :type packages: list
        """
        self._packages = packages

    @property
    def simple_index(self):
        """
        :return: the simple index file contents
        :rtype: str
        """
        return ''

    @property
    def pypi_index(self):
        """
        :return: the full index file contents
        :rtype: str
        """
        return ''


def write_index(object_key, content):
    pass


def lambda_handler(event, context):
    """
    Entry point for a Lambda function, triggered by an S3 PutObject.

    :param event: the PutObject Event
    :type event: dict
    :param context: the Lambda function context
    """
    packages = list_packages()



# Load package list
# Clear index directories?
# Regenerate index files
