from setuptools import setup, find_packages

setup(
    name='ns.one',
    version='0.1',
    description="test",
    long_description='test',
    packages=find_packages(),
    namespace_packages=['ns'],
    include_package_data=True,
    zip_safe=False,
)
