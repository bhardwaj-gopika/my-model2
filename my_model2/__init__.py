from my_model2.files import VARIABLE_FILE
from lume_model.utils import variables_from_yaml

INPUT_VARIABLES, OUTPUT_VARIABLES = variables_from_yaml(VARIABLE_FILE)

from . import _version
__version__ = _version.get_versions()['version']
