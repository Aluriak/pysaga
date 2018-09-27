
import pysaga
from pysaga import parse_line
from functools import partial


EXPECTED_MATCHES = {  # line to parse: expected result given by parse_line
    "GLOUM : je m'appelle GLOUM": ('GLOUM', "je m'appelle GLOUM", {}),
    "GROUPE : moi moi moi moi ?! Hep ! Choisis-moi ! Hep ! Choisis-moi ! SBAFFREF:Référence au premier Shrek, où l'âne insiste de la même manière pour que Shrek l'emmène avec lui.": (
        'GROUPE',
        'moi moi moi moi ?! Hep ! Choisis-moi ! Hep ! Choisis-moi ! SBAFF',
        {'REF': "Référence au premier Shrek, où l'âne insiste de la même manière pour que Shrek l'emmène avec lui."}
    ),
    "PHONY : TEXTÏ^!REF:ref1LOL:lol1REF:ref2REF:ref3^LOL:lol2": (
        'PHONY', "TEXTÏ^!",
        {'REF': ('ref1', 'ref2', 'ref3^'), 'LOL': ('lol1', 'lol2')}
    ),
}



def template_test(text, expected):
    "A template for test functions, each of them testing a specific text"
    found = parse_line(text)
    assert found == expected


# populate globals with test functions
for idx, data in enumerate(EXPECTED_MATCHES.items(), start=1):
    globals()['test_case_' + str(idx)] = partial(template_test, *data)
