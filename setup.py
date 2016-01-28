import os
from setuptools import setup, find_packages
from wagtailmodeladmin import __version__

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name="wagtailmenus",
    version=__version__,
    author="Andy Babic",
    author_email="ababic@rkh.co.uk",
    description=(
        "Gives you better control over the behaviour of your main menu, and "
        "allows you to define flat menus for output in templates."),
    long_description=README,
    packages=find_packages(),
    license="MIT",
    keywords="wagtail cms model utility",
    download_url="https://github.com/rkhleics/wagailmenus/tarball/0.1",
    url="https://github.com/rkhleics/wagailmenus",
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        'Topic :: Internet :: WWW/HTTP',
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    install_requires=[
        "wagtail>=1.3.1",
        "wagtailmodeladmin>=1.2.5"
    ],
)
