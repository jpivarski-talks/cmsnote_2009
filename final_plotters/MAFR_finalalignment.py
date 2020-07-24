execfile("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_wAPE_optimal/DTCRAFTiter04_report.py")

def converged(r):
    convx = 0.
    convy = 0.
    convz = 0.
    convphix = 0.
    convphiy = 0.
    convphiz = 0.
    
    if r.deltax is not None: convx = abs(r.deltax.value)*10.
    if r.deltay is not None: convy = abs(r.deltay.value)*10.
    if r.deltaz is not None: convz = abs(r.deltaz.value)*10.
    if r.deltaphix is not None: convphix = abs(r.deltaphix.value)*1000.
    if r.deltaphiy is not None: convphiy = abs(r.deltaphiy.value)*1000.
    if r.deltaphiz is not None: convphiz = abs(r.deltaphiz.value)*1000.
    
    return convx < 0.1 and convy < 0.1 and convz < 0.1 and convphix < 0.1 and convphiy < 0.1 and convphiz < 0.1

bad_addresses = []
for r in reports:
    if r.postal_address[0] == "DT":
        if r.status != "PASS": bad_addresses.append(r.postal_address); continue
        if not converged(r): bad_addresses.append(r.postal_address); continue

        if r.deltax is not None and r.deltax.error*10. > 1.: bad_addresses.append(r.postal_address); continue
        if r.deltay is not None and r.deltay.error*10. > 1.: bad_addresses.append(r.postal_address); continue
        if r.deltaz is not None and r.deltaz.error*10. > 1.: bad_addresses.append(r.postal_address); continue
        if r.deltaphix is not None and r.deltaphix.error*1000. > 1.: bad_addresses.append(r.postal_address); continue
        if r.deltaphiy is not None and r.deltaphiy.error*1000. > 1.: bad_addresses.append(r.postal_address); continue
        if r.deltaphiz is not None and r.deltaphiz.error*1000. > 1.: bad_addresses.append(r.postal_address); continue

        print r.postal_address[1], r.postal_address[2], r.postal_address[3], r.deltax.error*10., r.deltaphiy.error*1000.

bad_addresses.sort()
print "\n".join(map(str, bad_addresses))

execfile("geometryXMLparser.py")
unaligned = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/internalDTalignment.xml")
aligned = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_wAPE_optimal/DTCRAFTiter04.xml")

for address in bad_addresses:
    aligned.dt[address[1:]] = unaligned.dt[address[1:]]
    aligned.dt[address[1:]].xx = 1000000.
    aligned.dt[address[1:]].xy = 0.
    aligned.dt[address[1:]].xz = 0.
    aligned.dt[address[1:]].yy = 1000000.
    aligned.dt[address[1:]].yz = 0.
    aligned.dt[address[1:]].zz = 1000000.

aligned.xml(file("final_production_alignment.xml", "w"))

######

bad_addresses2 = []
for r in reports:
    if r.postal_address[0] == "DT":
        if r.status != "PASS": continue
        if not converged(r): bad_addresses2.append(r.postal_address); continue

        if r.deltax is not None and r.deltax.error*10. > 1.: bad_addresses2.append(r.postal_address); continue
        if r.deltay is not None and r.deltay.error*10. > 1.: bad_addresses2.append(r.postal_address); continue
        if r.deltaz is not None and r.deltaz.error*10. > 1.: bad_addresses2.append(r.postal_address); continue
        if r.deltaphix is not None and r.deltaphix.error*1000. > 1.: bad_addresses2.append(r.postal_address); continue
        if r.deltaphiy is not None and r.deltaphiy.error*1000. > 1.: bad_addresses2.append(r.postal_address); continue
        if r.deltaphiz is not None and r.deltaphiz.error*1000. > 1.: bad_addresses2.append(r.postal_address); continue

bad_addresses2.sort()
print "\n".join(map(str, bad_addresses2))


#################################################################

execfile("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_wAPE_100GeV/DTCRAFTiter03_report.py")

def converged(r):
    convx = 0.
    convy = 0.
    convz = 0.
    convphix = 0.
    convphiy = 0.
    convphiz = 0.
    
    if r.deltax is not None: convx = abs(r.deltax.value)*10.
    if r.deltay is not None: convy = abs(r.deltay.value)*10.
    if r.deltaz is not None: convz = abs(r.deltaz.value)*10.
    if r.deltaphix is not None: convphix = abs(r.deltaphix.value)*1000.
    if r.deltaphiy is not None: convphiy = abs(r.deltaphiy.value)*1000.
    if r.deltaphiz is not None: convphiz = abs(r.deltaphiz.value)*1000.
    
    return convx < 0.1 and convy < 0.1 and convz < 0.1 and convphix < 0.1 and convphiy < 0.1 and convphiz < 0.1

bad_addresses = []
for r in reports:
    if r.postal_address[0] == "DT":
        if r.status != "PASS": bad_addresses.append(r.postal_address); continue
        if not converged(r): bad_addresses.append(r.postal_address); continue

        if r.deltax is not None and r.deltax.error*10. > 1.: bad_addresses.append(r.postal_address); continue
        if r.deltay is not None and r.deltay.error*10. > 1.: bad_addresses.append(r.postal_address); continue
        if r.deltaz is not None and r.deltaz.error*10. > 1.: bad_addresses.append(r.postal_address); continue
        if r.deltaphix is not None and r.deltaphix.error*1000. > 1.: bad_addresses.append(r.postal_address); continue
        if r.deltaphiy is not None and r.deltaphiy.error*1000. > 1.: bad_addresses.append(r.postal_address); continue
        if r.deltaphiz is not None and r.deltaphiz.error*1000. > 1.: bad_addresses.append(r.postal_address); continue

        # print r.postal_address[1], r.postal_address[2], r.postal_address[3], r.deltax.error*10., r.deltaphiy.error*1000.



bad_addresses.sort()
print "\n".join(map(str, bad_addresses))

execfile("geometryXMLparser.py")
unaligned = MuonGeometry("final_production_alignment_CHECK.xml")
aligned = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_wAPE_100GeV/DTCRAFTiter03.xml")

for address in bad_addresses:
    aligned.dt[address[1:]] = unaligned.dt[address[1:]]
    aligned.dt[address[1:]].xx = 1000000.
    aligned.dt[address[1:]].xy = 0.
    aligned.dt[address[1:]].xz = 0.
    aligned.dt[address[1:]].yy = 1000000.
    aligned.dt[address[1:]].yz = 0.
    aligned.dt[address[1:]].zz = 1000000.

aligned.xml(file("alignment_with_100GeVcut.xml", "w"))

