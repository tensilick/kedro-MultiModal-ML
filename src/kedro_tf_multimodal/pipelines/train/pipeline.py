"""
This is a boilerplate pipeline 'train'
generated using Kedro 0.18.1
"""

from kedro.pipeline import Pipeline, node, pipeline

from kedro_tf_utils.pipelines.train.pipeline import create_train_pipeline
from kedro_tf_utils.pipelines.fusion.pipeline import create_fusion_pipeline
from kedro.pipeline.modular_pipeline import pipeline as modular_pipeline
from kedro_tf_text.pipelines.bert.pipeline import download_bert

from kedro_tf_text.pipelines.tabular.pipeline import tabular_model_pipeline
from kedro_tf_image.pipelines.preprocess.pipeline import create_classification_layer

from kedro_tf_text.pipelines.preprocess.pipeline import process_text_pipeline, glove_embedding
from kedro_tf_text.pipelines.cnn.pipeline import cn