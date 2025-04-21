from typing import Dict

from prefect import flow, get_run_logger, task
from lume_services.results import Result
from lume_model.variables import InputVariable, OutputVariable
from my_model2.model import MyModel2
from my_model2 import INPUT_VARIABLES

@task()
def format_file(output_variables):
    text = str(output_variables["output2"].value + output_variables["output3"].value)
    return text

@task()
def format_result(
    input_variables: Dict[str, InputVariable],
    output_variables: Dict[str, OutputVariable],
):
    inputs = {var_name: var.value for var_name, var in input_variables.items()}
    outputs = {var_name: var.value for var_name, var in output_variables.items()}

    return Result(inputs=inputs, outputs=outputs)


@task()
def load_input(var_name, parameter):
    # Confirm Inputs are Correctly Loaded!
    logger = get_run_logger()
    if parameter.value is None:
        parameter.value = parameter.default
    logger.info(f'Loaded {var_name} with value {parameter}')
    return parameter


@task()
def evaluate(formatted_input_vars, settings=None):

    if settings is None:
        settings = {}

    model = MyModel2(**settings)

    return model.evaluate(formatted_input_vars)


# DEFINE TASK FOR SAVING DB RESULT
# See docs: https://slaclab.github.io/lume-services/api/tasks/#lume_services.tasks.db.SaveDBResult
#save_db_result_task = SaveDBResult(timeout=30)

# DEFINE TASK FOR SAVING FILE
# See docs: https://slaclab.github.io/lume-services/api/tasks/#lume_services.tasks.file.SaveFile
#save_file_task = SaveFile(timeout=30)

# If your model requires loading a file object, you use the task pre-packaged
# with LUME-services:
# load_file_task = LoadFile(timeout=30)

# If your model requires loading a results database entry, you can use the LoadDBResult
# task packaged with LUME-services:
# load_db_result_task = LoadDBResult(timeout=10)

@flow(name="my_model2_flow")
def my_model2_flow(filename: str = None, filesystem_identifier:str = None):
    logger = get_run_logger()
    logger.info(f'Starting flow run...')
    logger.info(f"Filename: {filename}, Filesystem ID: {filesystem_identifier}")
    # CONFIGURE LUME-SERVICES
    # see https://slaclab.github.io/lume-services/workflows/#configuring-flows-for-use-with-lume-services
    #configure = configure_lume_services()

    # CHECK WHETHER THE FLOW IS RUNNING LOCALLY
    # If the flow runs using a local backend, the results service will not be available
    #running_local = check_local_execution()
    #running_local.set_upstream(configure)

    # SET UP INPUT VARIABLE PARAMETERS.
    # These are parameters that can be supplied to the workflow at runtime
    input_variable_parameter_dict = {}
    for var in INPUT_VARIABLES:
        if var.value is None:
            var.value = var.default

    formatted_input_variables = {var.name: var for var in INPUT_VARIABLES}

    # If additional preprocessing is necessary, the user can implement a preprocessing task
    # formatted_input_vars = preprocessing_task(formatted_input_vars)

    # RUN EVALUATION
    output_variables = evaluate.submit(formatted_input_variables).result()
    print("Output variables:", output_variables)
    return output_variables
