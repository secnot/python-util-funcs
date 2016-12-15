from collections import OrderedDict, Iterable

def unique(seq, idfun=None): 
    """
    Returns a list containing only the first aparence of each item
    (stable - preserves relative order)

    Arguments:
        seq: List/ Sequence to process
        idfun (callable): function that returns a identification for
         each item of seq, 
    """
    if idfun is None:
        def idfun(x): return x

    seen = {}
    result = []
    for item in seq:
        marker = idfun(item)
        # in old Python versions:
        # if seen.has_key(marker)
        # but in new ones:
        if marker in seen: continue
        seen[marker] = 1
        result.append(item)
    return result


def non_repeat(seq, idfun=None):
    """
    Returns list containing elements that only appear once.
    (stable - preserves relative order)

    Arguments:
        seq: List/ Sequence to process
        idfun (callable): function that returns a identification for
         each item of seq, 
    """
    if idfun is None:
        def idfun(x): return x

    seen = OrderedDict()
    for item in seq:
        marker = idfun(item)
        if marker in seen:
            seen[marker] = None
        else:
            seen[marker] = (1, item) # tuple to Distingish None items

    return [value[1] for key, value in seen.items() if value]



def _flatten(lst, depth, ftypes=(list, tuple)):
    for e in lst:
        if not depth:
            yield e
        elif not isinstance(e, ftypes):
            yield e
        else:
            for b in _flatten(e, depth-1, ftypes):
                yield b

def flatten(lst, depth=1, ftypes=(list, tuple)):
    """
    Flatten nested list to the required depth.
    """
    assert depth>=0
    return [e for e in _flatten(lst, depth, ftypes)]



def flatten_all(lst):
    return None
