import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='ftw',
    description='Framework for Testing WAFs',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Chaim Sanders, Zack Allen',
    author_email='zma4580@gmail.com, chaim.sanders@gmail.com',
    url='https://github.com/coreruleset/ftw',
    include_package_data=True,
    package_data={
          'ftw': ['util/public_suffix_list.dat']
    },
    entry_points={
        'pytest11': [
            'ftw = ftw.pytest_plugin'
        ]
    },
    keywords=['waf'],
    project_urls={
        "Bug Tracker": 'https://github.com/coreruleset/ftw/issues',
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Framework :: Pytest",
    ],
    packages=["ftw"],
    python_requires=">=3.6",
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    install_requires=[
        'Brotli==1.0.9',
        'IPy==1.01',
        'PyYAML==6.0',
        'pytest==6.2.5',
        'python-dateutil==2.8.2'
    ],
)
