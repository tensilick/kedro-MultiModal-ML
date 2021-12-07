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
@click.option("-p", "--pipeline", "pipeline_name", default=None)
@click.option("--env", "-e", type=str, default=None)
def generate_kfp(image: str, pipeline_name: str, env: str) -> None:
    """Generates a workflow spec yaml file from a Kedro pipeline.

    Args:
        image: container image name.
        pipeline_name: pipeline name to build a workflow spec.
        env: Kedro configuration environment name.

    """
    global _PIPELINE
    global _IMAGE
    _IMAGE = image

    project_path = Path.cwd()
    metadata = bootstrap_project(project_path)
    package_name = metadata.package_name

    pipeline_name = pipeline_name or "__default__"
    _PIPELINE = pipelines.get(pipeline_name)

    Compiler().compile(convert_kedro_pipeline_to_kfp, package_name + ".yaml")


@dsl.pipeline(name="Kedro pipeline", description="Kubeflow pipeline for Kedro project")
def convert_kedro_pipeline_to_kfp() -> None:
    """Convert from a Kedro pipeline into a kfp container graph."""
    node_dependencies = _PIPELINE.node_dependencies
    kfp_ops = _build_kfp_ops(node_dependencies)
    for node, dependencies in node_dependencies.items():
        for dependency in depende