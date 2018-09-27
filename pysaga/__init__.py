

from . import utils
from . import commons
from .saga import Saga
from .parse_line import parse_line


__version__ = '0.0.1'


def get(saga_name:str):
    try:
        saga_name = commons.SAGA_ALIASES[saga_name.lower()]
    except KeyError:
        raise KeyError(f"Saga name '{saga_name}' is unknown")
    return Saga(saga_name)


rda = get('Reflets')
