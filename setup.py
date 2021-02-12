import setuptools
import get_naughty_strings

setuptools.setup(
    name="get_naughty_strings",
    version=get_naughty_strings.__version__,
    author=get_naughty_strings.__author__,
    author_email="allan.wilson@vaisala.com",
    description="Get naughty strings",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://TODO/",
    packages=setuptools.find_packages(),
    install_requires=[
        'requests',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.7',
    project_urls={
        "Source":"https://TODO",
    },
)
