from setuptools import setup, find_packages
from os import path
import versioneer

cur_dir = path.abspath(path.dirname(__file__))

# parse requirements
with open(path.join(cur_dir, "requirements.txt"), "r") as f:
    requirements = f.read().split()

setup(
    name="my_model2",
    author="Gopika Bhardwaj",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    packages=find_packages(),
    #  license="...",
    install_requires=requirements,
    url="https://github.com/bhardwaj-gopika/my-model2",
    include_package_data=True,
    python_requires=">=3.8",
    entry_points={
        "orchestration": [
            "my_model2.model=\
                my_model2.model:MyModel2",
            "my_model2.flow=\
                my_model2.flow:flow",
        ]
    },
)
