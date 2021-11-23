# python build_kubeflow_pipeline.py <project_image>

import re
from pathlib import Path
from typing import Dict, Set

import click

from kfp import aws, dsl
from kfp.compiler.compiler import Compiler

from kedro.framework.project import pipelines
from kedro.framework.startup import bootstrap_project
from kedro.pipeline.node import Node

_PIPELINE = None
_IMAGE = None


@click.command()
@click.argument("image", required=True)
@click.option("-p", "--pipeline", "pipeline_name", def