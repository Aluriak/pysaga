"""Definition of the function able to parse lines of raw data

"""


from operator import itemgetter
from collections import defaultdict
from .commons import REG_LINE, REFWORDS


def parse_line(line:str) -> (str, str, dict):
    "Parse a single line, return (character, line, references)"
    match = REG_LINE.fullmatch(line)
    # print(f"PARSING LINE: '{line}'")
    # if match:
        # print('GROUPS:', match.groups())
    if not match: return None
    char, content = match.groups(0)
    refs = defaultdict(list)  # take care of refs
    while True:
        # handle even the worst cases, where multiple REF and LOL are mixed.
        indexes = {}  # refword: righest index showing 'REFWORD:'
        for refword in REFWORDS:
            index = content.rfind(f'{refword}:')
            if index >= 0:
                indexes[refword] = index
        if indexes:
            refword, index = max(indexes.items(), key=itemgetter(1))
            content, ref = content[:index], content[index:]
            refs[refword].append(ref[len(refword)+1:])
        else:
            break
    return char, content, {w: tuple(reversed(rs)) if len(rs) > 1 else rs[0]
                           for w, rs in refs.items()}
