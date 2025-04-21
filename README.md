# My Model2

This repository packages the `MyModel2` in `my_model2/model.py ` for execution with [Prefect](https://docs.prefect.io/) using the flow described in `my_model2/flow/flow.py` using the variables:

<!--- The input and output variable tables are replaced when generating the project in template/hooks/post_gen_project.py-->
# input_variables
|variable name| type |default|
|-------------|------|------:|
|input1       |scalar|      1|
|input2       |scalar|      2|


# output_variables
|variable_name| type |
|-------------|------|
|output1      |scalar|
|output2      |scalar|
|output3      |scalar|



## Installation

This package may be installed using pip:
```
pip install git+https://github.com/bhardwaj-gopika/my-model2
```


## Dev

Install dev environment:
```
conda env create -f dev-environment.yml
```

Activate your environment:
```
conda activate my-model2-dev
```

Install package:
```
pip install -e .
```

Tests can be executed from the root directory using:
```
pytest .
```

### Note
This README was automatically generated using the template defined in https://github.com/slaclab/lume-services-model-template with the following configuration:

```json
{
    "author": "Gopika Bhardwaj",
    "email": "gopikab@stanford.edu",
    "github_username": "bhardwaj-gopika",
    "github_url": "https://github.com/bhardwaj-gopika/my-model2",
    "project_name": "My Model2", 
    "repo_name": "my-model2", 
    "package": "my_model2",
    "model_class": "MyModel2"
}
```
