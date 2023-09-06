#!/usr/bin/env python
from setuptools import find_namespace_packages, setup

package_name = "dbt-piperider"
# make sure this always matches dbt/adapters/{adapter}/__version__.py
package_version = "1.5.0"
description = """The PipeRiderAdapter adapter plugin for dbt"""

setup(
    name=package_name,
    version=package_version,
    description=description,
    long_description=description,
    author="InfuseAI Dev Team",
    author_email="dev@infuseai.io",
    url="https://github.com/InfuseAI/dbt-piperider",
    packages=find_namespace_packages(include=["dbt", "dbt.*"]),
    include_package_data=True,
    install_requires=[
        "dbt-core~=1.5.0",
    ],
)
