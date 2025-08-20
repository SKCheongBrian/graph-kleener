def _space_separated_string(s):
    res = ['"']
    res.append(str(s))
    res.append('" ')
    return "".join(res)

def _weight_to_DistNat(weight):
    res = ['(DistNat ']
    res.append(str(int(weight)))
    res.append(')')
    return "".join(res)


def igraph_to_kleen_graph(graph):
    res = []
    for e in graph.es:
        current = ['EdgeFact (Edge ']
        src, dst = e.tuple
        current.append(_space_separated_string(src))
        current.append(_space_separated_string(dst))
        current.append(_weight_to_DistNat(e["weight"]))
        current.append(')')
        res.append("".join(current))
    return "".join(['[', ", ".join(res), ', StartFact (Start "0")]'])


