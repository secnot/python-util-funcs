from collections import OrderedDict

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
    Returns list containing elements that don't repeat
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

