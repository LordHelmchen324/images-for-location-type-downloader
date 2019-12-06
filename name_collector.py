import overpy

api = overpy.Overpass()
result = api.query("""
    nwr[building=church](45.2440, 10.1321, 46.0932, 11.9861);
    out center;
    """)

print()

names = [], lats = [], lons = []

for node in result.nodes:
    print(node)
    names.append(node.tags["name"])
    lats.append(node.lat)
    lons.append(node.lon)

for way in result.ways:
    print(way)
    names.append(village + "," + way.tags["name"])
    node = way.get_nodes(resolve_missing=True)[0]
    lats.append(node.lat)
    lons.append(node.lon)

#for relation in result.relations:
#    names.append(village + "," + way.tags['name'])
#    node = way.get_nodes(resolve_missing=True)[0]
#    lats.append(node.lat)
#    lons.append(node.lon)

with open("names.csv", "w") as f:
    for (i, _) in enumerate(names):
        f.write(names[i] + "," + lats[i] + "," + lons[i])