
from collections import defaultdict


def reverse_multivalues_dict(d:dict, unique_value:bool=False) -> dict:
    """Return a new dict with each item of value as key, and key as value

    >>> sorted(list(reverse_multivalues_dict({'a': 'bc', 'd': 'ef'}).items()))
    [('b', {'a'}), ('c', {'a'}), ('e', {'d'}), ('f', {'d'})]
    >>> sorted(list(reverse_multivalues_dict({'a': 'bc', 'd': 'ef'}, unique_value=True).items()))
    [('b', 'a'), ('c', 'a'), ('e', 'd'), ('f', 'd')]

    """
    ret = {} if unique_value else defaultdict(set)
    for key, values in d.items():
        for value in values:
            if unique_value:
                ret[value] = key
            else:
                ret[value].add(key)
    return ret
