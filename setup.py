
from setuptools import setup, find_packages
from pwmanager.core.version import get_version

VERSION = get_version()

f = open('README.md', 'r')
LONG_DESCRIPTION = f.read()
f.close()

setup(
    name='pwmanager',
    version=VERSION,
    description='Another password manager...',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author='Mauro Filipe Maia',
    author_email='dev@maurofilipemaia.dev',
    url='https://pwmanager.maurofilipemaia.dev/',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'tests*']),
    package_data={'pwmanager': ['templates/*']},
    include_package_data=True,
    entry_points="""
        [console_scripts]
        pwmanager = pwmanager.main:main
    """,
)
