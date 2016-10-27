from setuptools import setup, find_packages

setup(
    name='helloworld',
    version='0.1',
    description="test",
    long_description='test',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    entry_points="""\
        [console_scripts]
        helloworld = helloworld:main
    """,
)
