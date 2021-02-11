import setuptools
import get_naughty_strings

setuptools.setup(
    name="get_naughty_strings",
    version=get_naughty_strings.__version__,
    author=get_naughty_strings.__author__,
    author_email="allan.wilson@vaisala.com",
    description="Get naughty strings",
    long_description=open('README.md').read(),
    long_description_content_type="text/x-rst",
    url="https://TODO/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    project_urls={
        "Source":"https://TODO",
    },
)