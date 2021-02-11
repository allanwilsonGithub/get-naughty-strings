Get Naughty Strings
================

Installation
###############

You can install by python3-pip:

    $ pip3 install .

Usage
#####

    $ python3
    >>> from get_naughty_strings import get_naughty_strings
    >>> print(get_naughty_strings.__doc__)
    >>> print(get_naughty_strings.UrlDownloader.__doc__)
    >>> help(get_naughty_strings)
    >>> quit()

    >>> from get_naughty_strings import get_naughty_strings
    >>> get_naughty_strings.UrlDownloader.return_naughty_strings_as_json()
    >>> quit()


Change Log
##########

See `CHANGELOG.md` for details.

Building the pip installable package
####################################

    >>> python3 -m pip install --upgrade build
    >>> python3 -m build