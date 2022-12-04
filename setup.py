from setuptools import find_packages
from setuptools import setup


setup(
    name='pre_commit_sync',
    description='Keeping files sync between web and git.',
    url='https://github.com/dvolgyes/pre-commit-sync',
    version='0.3.0',
    author='David Volgyes',
    author_email='david.volgyes@ieee.org',

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],

    packages=find_packages(exclude=('tests*', 'testing*')),
    install_requires=[
        'gitpython',
    ],
    entry_points={
        'console_scripts': [
            'pre-commit-sync = pre_commit_sync.pre_commit_sync:main',
        ],
    },
)
