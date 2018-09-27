"""Various general definitions.

"""


import re
from . import utils


TEMPLATE_PATH = 'sagas-mp3/{saga_name}/Textes/'
REFWORDS = 'REF', 'LOL', 'TRI', 'JDM'
REG_CHAPTER = re.compile(r"^Chapitre ([0-9]+) - (.+)$")
REG_CHARACTER = re.compile(r"^([A-Z0-9ÉÈÊÀÄÂÔÛÏ.,!?' -]+) : ?")
REG_LINE = re.compile(r"^([A-Z0-9ÉÈÊÀÄÂÔÛÏ.,!?' -]+) : (.+)")
UNPARSABLES = {
    TEMPLATE_PATH.format(saga_name='Reflets') + 'Fleau.html',
}


assert REG_CHAPTER.fullmatch('Chapitre 1 - Introduction à la quête')


SAGA_NAME = {
    'Reflets': "Reflets d'Acide",
    'Xantah': "La Légende de Xantah",
    'Adoprixtoxis': "Adoprixtoxis",
}


SAGA_ALIASES = utils.reverse_multivalues_dict({
    'Reflets': ('rda', 'reflets', 'reflet', 'reflets d\'acide', 'reflet d\'acide'),
    'Xantah': ('xantah', 'xantha', 'xant'),
    'Adoprixtoxis': ('adoprixtoxis', 'adop'),
}, unique_value=True)


