
```
saved_model_cli show --all --dir data/07_model_output/train/
saved_model_cli show --all --dir data/08_reporting/
```


MetaGraphDef with tag-set: 'serve' contains the following SignatureDefs:

signature_def['__saved_model_init_op']:
  The given SavedModel SignatureDef contains the following input(s):
  The given SavedModel SignatureDef contains the following output(s):
    outputs['__saved_model_init_op'] tensor_info:
        dtype: DT_INVALID
        shape: unknown_rank
        name: NoOp
  Method name is:

signature_def['serving_default']:
  The given SavedModel SignatureDef contains the following input(s):
    inputs['age'] tensor_info:
        dtype: DT_FLOAT
        shape: (-1, 1)
        name: serving