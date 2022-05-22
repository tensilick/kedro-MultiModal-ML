"""Project pipelines."""
from typing import Dict

from kedro.pipeline import Pipeline
from kedro_tf_multimodal.pipelines.train.pipeline import create_pipeline, create_train_pipeline

# TODO: https://github.com/tensorflow/hub/issues/705
import tensorflow_text as text

def register_pipelines() -> D