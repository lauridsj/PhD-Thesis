with open("literature.bib") as f:
    lines = f.readlines()

collaborations = ["CMS", "ATLAS", "ALICE", "LHCb", "D0", "CDF"]

outlines = []

current = None
currenttag = None

for l in lines:
    lstrip = l.strip()
    if lstrip.startswith("@"):
        is_coll = False
        for coll in collaborations:
            if ("{" + coll + ":") in lstrip:
                current = coll
                currenttag=lstrip
                is_coll = True
                print(f"{currenttag} is collaboration {coll}")
                break
        if not is_coll:
            current = None
    elif current is not None and lstrip.startswith("author"):
        print(f"Replacing '{lstrip}' in {currenttag}")
        outlines.append('    author = "{' + coll + ' Collaboration}",\n')
        continue
    outlines.append(l)

with open("literature.bib", "w") as f:
    f.writelines(outlines)