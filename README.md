
# Kedro TF MultiModal ML :hammer: [Template]

[![kedro-MultiModal-ML](https://github.com/tensilick/kedro-MultiModal-ML/blob/develop/notes/multimodal.drawio.svg)](https://github.com/tensilick/kedro-MultiModal-ML/blob/develop/notes/multimodal.drawio.svg)

This is a *template* for **multi-modal machine learning in healthcare** using the [Kedro](https://kedro.org/) framework. You can fuse reports, tabular data, and images using various fusion methods (Early & Late fusion. Other fusion methods and graph data are a work in progress). This project is compatible with [Kubeflow](https://www.kubeflow.org) and [Vertex AI](https://cloud.google.com/vertex-ai).

## Usage
* For understanding the [Kedro](https://kedro.org/) platform, please start with the [overview](#overview) :point_down:
* This is a template repository. Generate a new repository with the same directory structure by selecting the **Use this template** button :point_up: and use it as a [Kedro project.](https://kedro.readthedocs.io/en/stable/get_started/new_project.html)
* Install dependencies `pip install -r src/requirements.lock`
* Refer to the [default pipeline](src/kedro_MultiModal_ML/pipelines/train/pipeline.py) for usage examples.
* Refer to [sample data](/data/01_raw/) for data format. Prefix model datasets with appropriate model type from image_ , text_ , tabular_ , and bert_. (text_ is for CNN text models)
* Refer to [catalogue](conf/base/catalog.yml) for inputs and outputs
* See [parameters](conf/base/parameters/train.yml) that can be tweaked.

The essential pipelines are in [requirements.txt](src/requirements.txt). More details on the components are in their respective repositories :point_down: (PR welcome. Read CONTRIBUTING.md in the repositories)

* [kedro-tf-image](https://github.com/tensilick/kedro-tf-image)
* [kedro-tf-text](https://github.com/tensilick/kedro-tf-text)
* [kedro-tf-utils](https://github.com/tensilick/kedro-tf-utils)
* [kedro-dicom](https://github.com/tensilick/kedro-dicom) (*optional*) for processing DICOM images
* [kedro-graph](https://github.com/tensilick/kedro-graph) (*optional*) for creating [DGL](https://www.dgl.ai/) graph from multimodal data.
* [fhiry](https://github.com/tensilick/fhiry) (*optional*) for flattening [FHIR resources](https://www.hl7.org/fhir/overview.html).

Familiar guide, troubleshooting help, rules and guidelines, project dependencies, and packaging your Kedro project details stay the same. Make sure to acknowledge the new URLs and project paths.