"""
Simple library to make naughty strings available to Robot Framework tests
"""


import requests

class UrlDownloader:
    """
    Allows Robot Framework tests to retrieve Naughty Strings as an array for use in manual or autotesting
    of input fields or other forms.
    """

    @staticmethod
    def return_naughty_strings_as_json():
        """
        Gets the strings in json format from publicly available URL
        Returns these strings as an array to be used in Robot Framwork scripts for manual or autotests
        """

        url = "https://raw.githubusercontent.com/minimaxir/big-list-of-naughty-strings/master/blns.json"

        try:
            r = requests.get(url)
            assert r.status_code < 400
            return r.json()
        except (ValueError, ConnectionError, AssertionError):
            return ''
