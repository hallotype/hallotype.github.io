for gn in CurrentFont().selection:
    g = CurrentFont()[gn]
    if gn.lower() in CurrentFont():continue
    if len(g.name) ==1:
        print(g.name, hex(ord(g.name.lower())))
        u = list(g.unicodes)
        u.append(ord(g.name.lower()))
        g.unicodes = u
    