from setuptools import setup, find_packages

setup(
    name='netbox-circuit-id',
    version='0.1',
    description='NetBox plugin to manage circuit IDs for cables',
    install_requires=[],
    packages=find_packages(include=["circuit_id*"]),
    include_package_data=True,
    zip_safe=False,
)