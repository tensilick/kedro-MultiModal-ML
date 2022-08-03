
from setuptools import find_packages, setup

entry_point = (
    "kedro-tf-multimodal = kedro_tf_multimodal.__main__:main"
)


# get the dependencies and installs
with open("requirements.txt", encoding="utf-8") as f:
    # Make sure we strip all comments and options (e.g "--extra-index-url")
    # that arise from a modified pip.conf file that configure global options
    # when running kedro build-reqs
    requires = []
    for line in f:
        req = line.split("#", 1)[0].strip()