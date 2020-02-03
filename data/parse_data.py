import rdflib
import json
from tqdm import tqdm

g = rdflib.Graph()
data = g.parse(location="data/musicknowledge.ttl", format="turtle")

res = {}
for d in data:
    s = str(d[0]).split('#')[1]
    p = str(d[1]).split('#')[1]
    o = str(d[2])
    if '#' in o:
        o = o.split('#')[1]

    if s not in res:
        res[s] = {}
    res[s][p] = o

json.dump(res, open('data/data.json', 'w'))
