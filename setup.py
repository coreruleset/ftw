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
        'Brotli==1.0.7',
        'IPy==0.83',
        'PyYAML==5.4',
        'pytest==4.6',
        'python-dateutil==2.6.0'
    ],
)
