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
from kedro_tf_text.pipelines.cnn.pipeline import cnn_text_pipeline

# Download BERT model and save it in the TF Hub format in bert_model_saved catalog
bert_model = modular_pipeline(pipe=download_bert, parameters={
                              "params:bert_model": "params:multimodal"})
# creates a tabular model from the tabular data and saves it in the tabular_model_saved catalog.
# The tabular data in csv has ID, column1, column2, columnx, label format: Refer to https://github.com/dermatologist/kedro-tf-text
tabular_model = modular_pipeline(pipe=tabular_model_pipeline, outputs={"tabular_model": "tabular_model_saved"}, parameters={
    "params:tabular": "params:multimodal"})

""" For CNN TEXT MODEL"""
preprocess_text_pipeline 