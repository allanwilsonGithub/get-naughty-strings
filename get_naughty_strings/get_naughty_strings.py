"""
Simple library to make naughty strings available to Robot Framework tests

Note:
Some of these strings, eg emojis, are unsupported by Chrome Web-driver so you can use "Run Keyword and Ignore Error"
WebDriverException: Message: unknown error: ChromeDriver only supports characters in the BMP
"""

import requests


def get_naughty_strings():
    """
    Allows Robot Framework tests to retrieve Naughty Strings as an array for use in manual or auto-testing
    of input fields or other forms.

    Gets the strings in json format from publicly available URL
    Returns these strings as an array to be used in Robot Framework scripts for manual or autotests
    """

    url = "https://raw.githubusercontent.com/minimaxir/big-list-of-naughty-strings/master/blns.json"

    try:
        r = requests.get(url)
        assert r.status_code < 400
        return r.json()
    except (ValueError, ConnectionError, AssertionError):
        return ''
