import ROOT
from math import *
execfile("/home/jpivarski/bin/tdrstyle.py")
# tdrStyle.SetOptTitle(1)
# tdrStyle.SetTitleBorderSize(1)
# tdrStyle.SetFillColor(ROOT.kWhite)
# tdrStyle.SetTitleFontSize(0.1)
c1 = ROOT.TCanvas()

############################

execfile("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_wAPE/DTCRAFTiter04_report.py")
execfile("geometryXMLparser.py")
finalData = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_wAPE/DTCRAFTiter04.xml")

for r in reports:
    if r.postal_address[0] == "DT": chamber = finalData.dt[r.postal_address[1:]]
    elif r.postal_address[0] == "CSC": chamber = finalData.csc[r.postal_address[1:]]

    failed = (r.status != "PASS")
    bigerr = (chamber.xx > 0.)

    if failed != bigerr:
        print r.status, chamber.xx, chamber.yy, chamber.zz

############################

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

############################

tdrStyle.SetOptStat("")

# execfile("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_wAPE/DTCRAFTiter04_report.py")
# execfile("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_wAPE_optimal/DTCRAFTiter04_report.py")
# # execfile("/home/jpivarski/work/results/CRAFTchambers2/ALLATONCE_PATTERN5/PATTERNiter04_report.py")

execfile("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_wAPE_100GeV/DTCRAFTiter04_report.py")

hx = ROOT.TH2F("hx", "", 100, -20., 20., 100, 0., 3.)
hy = ROOT.TH2F("hy", "", 100, -20., 20., 100, 0., 3.)
hz = ROOT.TH2F("hz", "", 100, -20., 20., 100, 0., 3.)
hphix = ROOT.TH2F("hphix", "", 100, -10., 10., 100, 0., 3.)
hphiy = ROOT.TH2F("hphiy", "", 100, -3., 3., 100, 0., 3.)
hphiz = ROOT.TH2F("hphiz", "", 100, -3., 3., 100, 0., 3.)

for r in reports:
    if r.status == "PASS":
        if r.deltax is not None and r.deltax.value > 0.: hx.Fill(r.deltax.value*10., r.deltax.error*10.)
        if r.deltay is not None and r.deltay.value > 0.: hy.Fill(r.deltay.value*10., r.deltay.error*10.)
        if r.deltaz is not None and r.deltaz.value > 0.: hz.Fill(r.deltaz.value*10., r.deltaz.error*10.)
        if r.deltaphix is not None and r.deltaphix.value > 0.: hphix.Fill(r.deltaphix.value*1000., r.deltaphix.error*1000.)
        if r.deltaphiy is not None and r.deltaphiy.value > 0.: hphiy.Fill(r.deltaphiy.value*1000., r.deltaphiy.error*1000.)
        if r.deltaphiz is not None and r.deltaphiz.value > 0.: hphiz.Fill(r.deltaphiz.value*1000., r.deltaphiz.error*1000.)

        if r.deltax is not None and r.deltax.value > 0. and abs(r.deltax.value*10.) > 20.: raise Exception, str(r.deltax.value*10.)
        if r.deltay is not None and r.deltay.value > 0. and abs(r.deltay.value*10.) > 20.: raise Exception, str(r.deltay.value*10.)
        if r.deltaz is not None and r.deltaz.value > 0. and abs(r.deltaz.value*10.) > 20.: raise Exception, str(r.deltaz.value*10.)
        if r.deltaphix is not None and r.deltaphix.value > 0. and abs(r.deltaphix.value*1000.) > 10.: raise Exception, str(r.deltaphix.value*1000.)
        if r.deltaphiy is not None and r.deltaphiy.value > 0. and abs(r.deltaphiy.value*1000.) > 3.: raise Exception, str(r.deltaphiy.value*1000.)
        if r.deltaphiz is not None and r.deltaphiz.value > 0. and abs(r.deltaphiz.value*1000.) > 3.: raise Exception, str(r.deltaphiz.value*1000.)

hx.SetXTitle("Local x 4^{th} iteration correction (mm)")
hy.SetXTitle("Local y 4^{th} iteration correction (mm)")
hz.SetXTitle("Local z 4^{th} iteration correction (mm)")
hphix.SetXTitle("Local #phi_{x} 4^{th} iteration correction (mrad)")
hphiy.SetXTitle("Local #phi_{y} 4^{th} iteration correction (mrad)")
hphiz.SetXTitle("Local #phi_{z} 4^{th} iteration correction (mrad)")

hx.SetYTitle("Local x quoted uncertainty (mm)")
hy.SetYTitle("Local y quoted uncertainty (mm)")
hz.SetYTitle("Local z quoted uncertainty (mm)")
hphix.SetYTitle("Local #phi_{x} quoted uncertainty (mrad)")
hphiy.SetYTitle("Local #phi_{y} quoted uncertainty (mrad)")
hphiz.SetYTitle("Local #phi_{z} quoted uncertainty (mrad)")

hx.GetXaxis().CenterTitle()
hy.GetXaxis().CenterTitle()
hz.GetXaxis().CenterTitle()
hphix.GetXaxis().CenterTitle()
hphiy.GetXaxis().CenterTitle()
hphiz.GetXaxis().CenterTitle()

hx.GetYaxis().CenterTitle()
hy.GetYaxis().CenterTitle()
hz.GetYaxis().CenterTitle()
hphix.GetYaxis().CenterTitle()
hphiy.GetYaxis().CenterTitle()
hphiz.GetYaxis().CenterTitle()

all_tlines = []
def tlines(top):
    tline1 = ROOT.TLine(-0.1, 0, -0.1, top)
    tline2 = ROOT.TLine(0.1, 0, 0.1, top)
    tline1.SetLineStyle(2)
    tline2.SetLineStyle(2)
    tline1.Draw("same")
    tline2.Draw("same")
    all_tlines.append(tline1)
    all_tlines.append(tline2)

c1.Clear()
c1.Divide(3, 2)

c1.GetPad(1).cd(); hx.Draw(); tlines(3.)
c1.GetPad(2).cd(); hy.Draw(); tlines(3.)
c1.GetPad(3).cd(); hz.Draw(); tlines(3.)
c1.GetPad(4).cd(); hphix.Draw(); tlines(3.)
c1.GetPad(5).cd(); hphiy.Draw(); tlines(3.)
c1.GetPad(6).cd(); hphiz.Draw(); tlines(3.)
# ROOT.gPad.SaveAs("data_convergence_plots_optimal.pdf")

############################

tdrStyle.SetOptStat("")
execfile("geometryXMLparser.py")
mc0 = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/testpattern.xml")
mc1 = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/ALLATONCE_PATTERN5/PATTERNiter01.xml")
mc2 = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/ALLATONCE_PATTERN5/PATTERNiter02.xml")
mc3 = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/ALLATONCE_PATTERN5/PATTERNiter03.xml")
mc4 = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/ALLATONCE_PATTERN5/PATTERNiter04.xml")
execfile("/home/jpivarski/work/results/CRAFTchambers2/ALLATONCE_PATTERN5/PATTERNiter04_report.py")

histograms = {}
for param in "x", "y", "z", "phix", "phiy", "phiz":
    for iteration in range(5):
        histograms[param + str(iteration)] = ROOT.TH1F("h" + param + str(iteration), "", 50, -10, 10.)

for r in reports:
    if r.status == "PASS" and converged(r):
        position = {}
        if r.postal_address[0] == "DT":
            continue
            position[0] = mc0.dt[r.postal_address[1:]]
            position[1] = mc1.dt[r.postal_address[1:]]
            position[2] = mc2.dt[r.postal_address[1:]]
            position[3] = mc3.dt[r.postal_address[1:]]
            position[4] = mc4.dt[r.postal_address[1:]]
        elif r.postal_address[0] == "CSC":
            position[0] = mc0.csc[r.postal_address[1:]]
            position[1] = mc1.csc[r.postal_address[1:]]
            position[2] = mc2.csc[r.postal_address[1:]]
            position[3] = mc3.csc[r.postal_address[1:]]
            position[4] = mc4.csc[r.postal_address[1:]]
        for param in "x", "y", "z":
            for iteration in range(5):
                if r.__dict__["delta" + param] is not None and r.__dict__["delta" + param].error != 0.:
                    histograms[param + str(iteration)].Fill(position[iteration].__dict__[param]*10.)
        for param in "phix", "phiy", "phiz":
            for iteration in range(5):
                if r.__dict__["delta" + param] is not None and r.__dict__["delta" + param].error != 0.:
                    histograms[param + str(iteration)].Fill(position[iteration].__dict__[param]*1000.)

def draw(param, title):
    histograms[param + str(0)].SetFillColor(ROOT.kMagenta+2)
    histograms[param + str(1)].SetFillColor(ROOT.kYellow-4)
    histograms[param + str(2)].SetFillColor(ROOT.kGreen-3)
#     histograms[param + str(3)].SetFillColor(ROOT.kCyan+2)
#     histograms[param + str(4)].SetFillColor(ROOT.kBlue-8)

    histograms[param + str(0)].SetXTitle(title)
    histograms[param + str(0)].GetXaxis().CenterTitle()

    histograms[param + str(2)].Draw()
    histograms[param + str(0)].Draw("same")
    histograms[param + str(1)].Draw("same")
    histograms[param + str(2)].Draw("same")
#     histograms[param + str(3)].Draw("same")
#     histograms[param + str(4)].Draw("same")

c1.Clear()
c1.Divide(3, 2)
c1.GetPad(1).cd(); draw("x", "Local x accuracy (mm)")
c1.GetPad(2).cd(); draw("y", "Local y accuracy (mm)")
c1.GetPad(3).cd(); draw("z", "Local z accuracy (mm)")
tlegend = ROOT.TLegend(0.3, 0.65, 0.95, 0.95)
tlegend.SetFillColor(ROOT.kWhite)
tlegend.SetBorderSize(1)
tlegend.AddEntry(histograms["z0"], "before alignment", "f")
tlegend.AddEntry(histograms["z1"], "iteration 1", "f")
tlegend.AddEntry(histograms["z2"], "iteration 2", "f")
tlegend.Draw()
c1.GetPad(4).cd(); draw("phix", "Local #phi_{x} accuracy (mrad)")
c1.GetPad(5).cd(); draw("phiy", "Local #phi_{y} accuracy (mrad)")
c1.GetPad(6).cd(); draw("phiz", "Local #phi_{z} accuracy (mrad)")
ROOT.gPad.SaveAs("mc_convergence.pdf")

############################

import re
execfile("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_wAPE/DTCRAFTiter04_report.py")
execfile("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_wAPE_optimal/DTCRAFTiter04_report.py")

def drawbarrel(fileName, reports, whattodo, template="template_barrel.svg"):
    template = file(template)
    output = file(fileName, "w")
    for line in template.readlines():
        outline = line
        match = re.search("id=\"([A-Za-z0-9]+)\".*fill=\"[A-Za-z0-9]+\"", line)
        if match is not None:
            name = match.groups()[0]
            for r in reports:
                if r.name == name:
                    outline = re.sub("fill=\"[A-Za-z0-9]+\"", "fill=\"%s\"" % whattodo(r), line)
                    break
        output.write(outline)
    output.close()

def rgb(r, g, b, maximum=1.):
  return "#%02x%02x%02x" % (max(0, min(r*255./maximum, 255)), max(0, min(g*255./maximum, 255)), max(0, min(b*255./maximum, 255)))

def fitokay(r):
    if r.status == "FAIL":
        return "none"
    
    if not converged(r): return "yellow"

    err = 0.
    if r.deltax is not None: err += (r.deltax.error*10.)**2
    if r.deltay is not None: err += (r.deltay.error*10.)**2
    if r.deltaz is not None: err += (r.deltaz.error*10.)**2
    if r.deltaphix is not None: err += (r.deltaphix.error*1000.)**2
    if r.deltaphiy is not None: err += (r.deltaphiy.error*1000.)**2
    if r.deltaphiz is not None: err += (r.deltaphiz.error*1000.)**2
    err = sqrt(err)

    return rgb(1 - err/5., 0., 0.)

drawbarrel("data_convergence_optimal.svg", reports, fitokay)

#####################

execfile("geometryXMLparser.py")

# initialData = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/internalDTalignment.xml")
# finalData = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_wAPE/DTCRAFTiter04.xml")
# execfile("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_wAPE/DTCRAFTiter04_report.py")

# initialData = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/internalDTalignment.xml")
# finalData = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_wAPE_optimal/DTCRAFTiter04.xml")
# execfile("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_wAPE_optimal/DTCRAFTiter04_report.py")
# execfile("previously_aligned.py")

# initialMC = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/testpattern.xml")
# finalMC = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/ALLATONCE_PATTERN5/PATTERNiter04.xml")
# execfile("/home/jpivarski/work/results/CRAFTchambers2/ALLATONCE_PATTERN5/PATTERNiter04_report.py")

# initialData = MuonGeometry("final_production_alignment_CHECKwithlayers.xml")
# finalData = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_wAPE_100GeV/DTCRAFTiter04.xml")
# execfile("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_wAPE_100GeV/DTCRAFTiter04_report.py")

initialData = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/internalDTalignment_correct.xml")
finalData = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT_wAPE_100GeV_newinternal/DTCRAFTiter01.xml")

initialData = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT_wAPE_100GeV_newinternal/DTCRAFTiter01.xml")
finalData = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT_wAPE_100GeV_newinternal/DTCRAFTiter02.xml")

initialData = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT_wAPE_100GeV_newinternal/DTCRAFTiter02.xml")
finalData = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT_wAPE_100GeV_newinternal/DTCRAFTiter03.xml")

initialData = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT_wAPE_100GeV_newinternal/DTCRAFTiter03.xml")
finalData = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT_wAPE_100GeV_newinternal/DTCRAFTiter04.xml")

initialData = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT_wAPE_100GeV_newinternal/DTCRAFTiter04.xml")
finalData = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT_wAPE_100GeV_newinternal/DTCRAFTiter05.xml")

initialData = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/internalDTalignment_correct.xml")
finalData = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT_wAPE_100GeV_newinternal/DTCRAFTiter05.xml")

execfile("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT_wAPE_100GeV_newinternal/DTCRAFTiter05_report.py")

tdrStyle.SetOptStat("mrou")
tdrStyle.SetStatW(0.40)
tdrStyle.SetStatFontSize(0.05)

histograms = {}
for param in "x", "y", "z", "phix", "phiy", "phiz":
    for region in 1, 2, 3, 4, 5:
        histograms[param + str(region)] = ROOT.TH1F("h" + param + str(region), "", 50, -15, 15.)
# for param in "phix", "phiy", "phiz":
#     for region in 1, 2, 3, 4, 5:
#         histograms[param + str(region)] = ROOT.TH1F("h" + param + str(region), "", 50, -10, 10.)
# for param in "y", "z":
#     for region in 1, 2, 3, 4, 5:
#         histograms[param + str(region)] = ROOT.TH1F("h" + param + str(region), "", 50, -30, 30.)

def fill(param, r, value):
    if r.postal_address[0] == "DT":
        if r.postal_address[1] == -2: region = 1
        elif r.postal_address[1] == -1: region = 2
        elif r.postal_address[1] == 0: region = 3
        elif r.postal_address[1] == 1: region = 4
        elif r.postal_address[1] == 2: region = 5

        for reg in range(region, 6):
            histograms[param + str(reg)].Fill(value)

for r in reports:
    if r.status == "PASS": #  and converged(r):
        if r.postal_address[0] == "DT":
            initial = initialData.dt[r.postal_address[1:]]
            final = finalData.dt[r.postal_address[1:]]
        else: continue

#         if r.postal_address not in previously_aligned: continue
#         if r.postal_address not in previously_aligned_iny: continue

        if r.deltax is not None and r.deltax.error != 0.: fill("x", r, (final.x - initial.x)*10.)
        if r.deltay is not None and r.deltay.error != 0.: fill("y", r, (final.y - initial.y)*10.)
        if r.deltaz is not None and r.deltaz.error != 0.: fill("z", r, (final.z - initial.z)*10.)
        if r.deltaphix is not None and r.deltaphix.error != 0.: fill("phix", r, (final.phix - initial.phix)*1000.)
        if r.deltaphiy is not None and r.deltaphiy.error != 0.: fill("phiy", r, (final.phiy - initial.phiy)*1000.)
        if r.deltaphiz is not None and r.deltaphiz.error != 0.: fill("phiz", r, (final.phiz - initial.phiz)*1000.)

def draw(param, title):
    histograms[param + str(5)].SetFillColor(ROOT.kRed-4)
    histograms[param + str(4)].SetFillColor(ROOT.kYellow)
    histograms[param + str(3)].SetFillColor(ROOT.kGreen+1)
    histograms[param + str(2)].SetFillColor(ROOT.kCyan+2)
    histograms[param + str(1)].SetFillColor(ROOT.kBlue-8)

    histograms[param + str(5)].SetXTitle(title)
    histograms[param + str(5)].GetXaxis().CenterTitle()

    histograms[param + str(5)].Draw()
    histograms[param + str(4)].Draw("same")
    histograms[param + str(3)].Draw("same")
    histograms[param + str(2)].Draw("same")
    histograms[param + str(1)].Draw("same")

c1.Clear()
c1.Divide(3, 2)
c1.GetPad(1).cd(); draw("x", "Local x alignment correction (mm)")
tlegend = ROOT.TLegend(0.17, 0.55, 0.45, 0.98)
tlegend.SetFillColor(ROOT.kWhite)
tlegend.SetBorderSize(1)
tlegend.AddEntry(histograms["x5"], " wheel +2", "f")
tlegend.AddEntry(histograms["x4"], " wheel +1", "f")
tlegend.AddEntry(histograms["x3"], " wheel 0", "f")
tlegend.AddEntry(histograms["x2"], " wheel -1", "f")
tlegend.AddEntry(histograms["x1"], " wheel -2", "f")
tlegend.SetTextSize(0.05)
tlegend.Draw()
c1.GetPad(2).cd(); draw("y", "Local y alignment correction (mm)")
histograms["z5"].SetAxisRange(0, 17, "Y")
c1.GetPad(3).cd(); draw("z", "Local z alignment correction (mm)")
c1.GetPad(4).cd(); draw("phix", "Local #phi_{x} alignment correction (mrad)")
c1.GetPad(5).cd(); draw("phiy", "Local #phi_{y} alignment correction (mrad)")
c1.GetPad(6).cd(); draw("phiz", "Local #phi_{z} alignment correction (mrad)")
c1.SaveAs("data_100GeV_newinternal_iterall.pdf")

#####################

# execfile("geometryXMLparser.py")
# oneDataset = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_wAPE_optimal/DTCRAFTiter04.xml")
# anotherDataset = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_wAPE/DTCRAFTiter04.xml")
# execfile("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_wAPE_optimal/DTCRAFTiter04_report.py")

# execfile("geometryXMLparser.py")
# oneDataset = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_wAPE_TIDTECallowed/DTCRAFTiter04.xml")
# anotherDataset = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_wAPE/DTCRAFTiter04.xml")
# execfile("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_wAPE/DTCRAFTiter04_report.py")

execfile("geometryXMLparser.py")
# oneDataset = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_wAPE_optimal/DTCRAFTiter04.xml")
# anotherDataset = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_wAPE_optimal/DTCRAFTiter03.xml")
anotherDataset = MuonGeometry("final_production_alignment.xml")
oneDataset = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_wAPE_afterFinal2/DTCRAFTiter01.xml")
execfile("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_wAPE_optimal/DTCRAFTiter04_report.py")

tdrStyle.SetOptStat("mrou")
tdrStyle.SetStatW(0.40)
tdrStyle.SetStatFontSize(0.05)

histograms = {}
normhistograms = {}
for param in "x", "y", "z", "phix", "phiy", "phiz":
    for region in 1, 2, 3, 4, 5:
        histograms[param + str(region)] = ROOT.TH1F("h" + param + str(region), "", 50, -10., 10.)
        normhistograms[param + str(region)] = ROOT.TH1F("normh" + param + str(region), "", 50, -15., 15.)

def fill(param, r, value, normvalue):
    if r.postal_address[0] == "DT":
        if r.postal_address[1] == -2: region = 1
        elif r.postal_address[1] == -1: region = 2
        elif r.postal_address[1] == 0: region = 3
        elif r.postal_address[1] == 1: region = 4
        elif r.postal_address[1] == 2: region = 5

        for reg in range(region, 6):
            histograms[param + str(reg)].Fill(value)
            normhistograms[param + str(reg)].Fill(normvalue)

for r in reports:
    if r.status == "PASS" and converged(r):
        if r.postal_address[0] == "DT":
            one = oneDataset.dt[r.postal_address[1:]]
            another = anotherDataset.dt[r.postal_address[1:]]
        else: continue

        if r.deltax is not None and r.deltax.error*10. > 1.: continue
        if r.deltay is not None and r.deltay.error*10. > 1.: continue
        if r.deltaz is not None and r.deltaz.error*10. > 1.: continue
        if r.deltaphix is not None and r.deltaphix.error*1000. > 1.: continue
        if r.deltaphiy is not None and r.deltaphiy.error*1000. > 1.: continue
        if r.deltaphiz is not None and r.deltaphiz.error*1000. > 1.: continue

        if r.deltax is not None and 0. < r.deltax.error*10.: fill("x", r, (another.x - one.x)*10., (another.x - one.x)/r.deltax.error)
        if r.deltay is not None and 0. < r.deltay.error*10.: fill("y", r, (another.y - one.y)*10., (another.y - one.y)/r.deltay.error)
        if r.deltaz is not None and 0. < r.deltaz.error*10.: fill("z", r, (another.z - one.z)*10., (another.z - one.z)/r.deltaz.error)
        if r.deltaphix is not None and 0. < r.deltaphix.error*1000.: fill("phix", r, (another.phix - one.phix)*1000., (another.phix - one.phix)/r.deltaphix.error)
        if r.deltaphiy is not None and 0. < r.deltaphiy.error*1000.: fill("phiy", r, (another.phiy - one.phiy)*1000., (another.phiy - one.phiy)/r.deltaphiy.error)
        if r.deltaphiz is not None and 0. < r.deltaphiz.error*1000.: fill("phiz", r, (another.phiz - one.phiz)*1000., (another.phiz - one.phiz)/r.deltaphiz.error)

def draw(param, title):
    histograms[param + str(5)].SetFillColor(ROOT.kRed-4)
    histograms[param + str(4)].SetFillColor(ROOT.kYellow)
    histograms[param + str(3)].SetFillColor(ROOT.kGreen+1)
    histograms[param + str(2)].SetFillColor(ROOT.kCyan+2)
    histograms[param + str(1)].SetFillColor(ROOT.kBlue-8)

    histograms[param + str(5)].SetXTitle(title)
    histograms[param + str(5)].GetXaxis().CenterTitle()

    histograms[param + str(5)].Draw()
    histograms[param + str(4)].Draw("same")
    histograms[param + str(3)].Draw("same")
    histograms[param + str(2)].Draw("same")
    histograms[param + str(1)].Draw("same")

def drawnorm(param, title):
    normhistograms[param + str(5)].SetFillColor(ROOT.kRed-4)
    normhistograms[param + str(4)].SetFillColor(ROOT.kYellow)
    normhistograms[param + str(3)].SetFillColor(ROOT.kGreen+1)
    normhistograms[param + str(2)].SetFillColor(ROOT.kCyan+2)
    normhistograms[param + str(1)].SetFillColor(ROOT.kBlue-8)

    normhistograms[param + str(5)].SetXTitle(title)
    normhistograms[param + str(5)].GetXaxis().CenterTitle()

    normhistograms[param + str(5)].Draw()
    normhistograms[param + str(4)].Draw("same")
    normhistograms[param + str(3)].Draw("same")
    normhistograms[param + str(2)].Draw("same")
    normhistograms[param + str(1)].Draw("same")

# c1.Clear()
# c1.Divide(3, 2)
# c1.GetPad(1).cd(); draw("x", "Local x difference of fixing DOF (mm)")
# tlegend = ROOT.TLegend(0.17, 0.55, 0.45, 0.98)
# tlegend.SetFillColor(ROOT.kWhite)
# tlegend.SetBorderSize(1)
# tlegend.AddEntry(histograms["x5"], " wheel +2", "f")
# tlegend.AddEntry(histograms["x4"], " wheel +1", "f")
# tlegend.AddEntry(histograms["x3"], " wheel 0", "f")
# tlegend.AddEntry(histograms["x2"], " wheel -1", "f")
# tlegend.AddEntry(histograms["x1"], " wheel -2", "f")
# tlegend.SetTextSize(0.05)
# tlegend.Draw()
# c1.GetPad(2).cd(); draw("y", "Local y difference of fixing DOF (mm)")
# c1.GetPad(3).cd(); draw("z", "Local z difference of fixing DOF (mm)")
# c1.GetPad(4).cd(); draw("phix", "Local #phi_{x} difference of fixing DOF (mrad)")
# c1.GetPad(5).cd(); draw("phiy", "Local #phi_{y} difference of fixing DOF (mrad)")
# c1.GetPad(6).cd(); draw("phiz", "Local #phi_{z} difference of fixing DOF (mrad)")
# ROOT.gPad.SaveAs("data_effect_of_fixingdof.pdf")

# c1.Clear()
# c1.Divide(3, 2)
# c1.GetPad(1).cd(); drawnorm("x", "Local x DOF difference / quoted error")
# tlegend = ROOT.TLegend(0.17, 0.55, 0.45, 0.98)
# tlegend.SetFillColor(ROOT.kWhite)
# tlegend.SetBorderSize(1)
# tlegend.AddEntry(normhistograms["x5"], " wheel +2", "f")
# tlegend.AddEntry(normhistograms["x4"], " wheel +1", "f")
# tlegend.AddEntry(normhistograms["x3"], " wheel 0", "f")
# tlegend.AddEntry(normhistograms["x2"], " wheel -1", "f")
# tlegend.AddEntry(normhistograms["x1"], " wheel -2", "f")
# tlegend.SetTextSize(0.05)
# tlegend.Draw()
# c1.GetPad(2).cd(); drawnorm("y", "Local y DOF difference / quoted error")
# c1.GetPad(3).cd(); drawnorm("z", "Local z DOF difference / quoted error")
# c1.GetPad(4).cd(); drawnorm("phix", "Local #phi_{x} DOF difference / quoted error")
# c1.GetPad(5).cd(); drawnorm("phiy", "Local #phi_{y} DOF difference / quoted error")
# c1.GetPad(6).cd(); drawnorm("phiz", "Local #phi_{z} DOF difference / quoted error")
# ROOT.gPad.SaveAs("data_effect_of_fixingdof_norm.pdf")

# c1.Clear()
# c1.Divide(3, 2)
# c1.GetPad(1).cd(); draw("x", "Local x difference from TID/TEC (mm)")
# tlegend = ROOT.TLegend(0.17, 0.55, 0.45, 0.98)
# tlegend.SetFillColor(ROOT.kWhite)
# tlegend.SetBorderSize(1)
# tlegend.AddEntry(histograms["x5"], " wheel +2", "f")
# tlegend.AddEntry(histograms["x4"], " wheel +1", "f")
# tlegend.AddEntry(histograms["x3"], " wheel 0", "f")
# tlegend.AddEntry(histograms["x2"], " wheel -1", "f")
# tlegend.AddEntry(histograms["x1"], " wheel -2", "f")
# tlegend.SetTextSize(0.05)
# tlegend.Draw()
# c1.GetPad(2).cd(); draw("y", "Local y difference from TID/TEC (mm)")
# c1.GetPad(3).cd(); draw("z", "Local z difference from TID/TEC (mm)")
# c1.GetPad(4).cd(); draw("phix", "Local #phi_{x} difference from TID/TEC (mrad)")
# c1.GetPad(5).cd(); draw("phiy", "Local #phi_{y} difference from TID/TEC (mrad)")
# c1.GetPad(6).cd(); draw("phiz", "Local #phi_{z} difference from TID/TEC (mrad)")
# ROOT.gPad.SaveAs("data_effect_of_TIDTEC_all.pdf")

# c1.Clear()
# c1.Divide(3, 2)
# c1.GetPad(1).cd(); drawnorm("x", "Local x TID/TEC difference / quoted error")
# tlegend = ROOT.TLegend(0.17, 0.55, 0.45, 0.98)
# tlegend.SetFillColor(ROOT.kWhite)
# tlegend.SetBorderSize(1)
# tlegend.AddEntry(normhistograms["x5"], " wheel +2", "f")
# tlegend.AddEntry(normhistograms["x4"], " wheel +1", "f")
# tlegend.AddEntry(normhistograms["x3"], " wheel 0", "f")
# tlegend.AddEntry(normhistograms["x2"], " wheel -1", "f")
# tlegend.AddEntry(normhistograms["x1"], " wheel -2", "f")
# tlegend.SetTextSize(0.05)
# tlegend.Draw()
# c1.GetPad(2).cd(); drawnorm("y", "Local y TID/TEC difference / quoted error")
# c1.GetPad(3).cd(); drawnorm("z", "Local z TID/TEC difference / quoted error")
# c1.GetPad(4).cd(); drawnorm("phix", "Local #phi_{x} TID/TEC difference / quoted error")
# c1.GetPad(5).cd(); drawnorm("phiy", "Local #phi_{y} TID/TEC difference / quoted error")
# c1.GetPad(6).cd(); drawnorm("phiz", "Local #phi_{z} TID/TEC difference / quoted error")
# ROOT.gPad.SaveAs("data_effect_of_TIDTEC_norm.pdf")

c1.Clear()
c1.Divide(3, 2)
c1.GetPad(1).cd(); draw("x", "Local x another iteration as confirmation (mm)")
tlegend = ROOT.TLegend(0.17, 0.55, 0.45, 0.98)
tlegend.SetFillColor(ROOT.kWhite)
tlegend.SetBorderSize(1)
tlegend.AddEntry(histograms["x5"], " wheel +2", "f")
tlegend.AddEntry(histograms["x4"], " wheel +1", "f")
tlegend.AddEntry(histograms["x3"], " wheel 0", "f")
tlegend.AddEntry(histograms["x2"], " wheel -1", "f")
tlegend.AddEntry(histograms["x1"], " wheel -2", "f")
tlegend.SetTextSize(0.05)
tlegend.Draw()
c1.GetPad(2).cd(); draw("y", "Local y another iteration as confirmation (mm)")
c1.GetPad(3).cd(); draw("z", "Local z another iteration as confirmation (mm)")
c1.GetPad(4).cd(); draw("phix", "Local #phi_{x} another iteration as confirmation (mrad)")
c1.GetPad(5).cd(); draw("phiy", "Local #phi_{y} another iteration as confirmation (mrad)")
c1.GetPad(6).cd(); draw("phiz", "Local #phi_{z} another iteration as confirmation (mrad)")
c1.SaveAs("data_iteration_confirmation.pdf")

#####################

# execfile("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_wAPE/DTCRAFTiter04_report.py")
execfile("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_wAPE_100GeV/DTCRAFTiter04_report.py")
execfile("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_wAPE_100GeV_afterFixErrors/DTCRAFTiter01_report.py")
execfile("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT_wAPE_100GeV_newinternal/DTCRAFTiter05_report.py")

tdrStyle.SetOptStat("mro")
tdrStyle.SetStatW(0.40)
tdrStyle.SetStatFontSize(0.05)

hx = ROOT.TH1F("hx", "", 20, 0., 3.)
hy = ROOT.TH1F("hy", "", 20, 0., 6.)
hz = ROOT.TH1F("hz", "", 20, 0., 6.)
hphix = ROOT.TH1F("hphix", "", 20, 0., 3.)
hphiy = ROOT.TH1F("hphiy", "", 20, 0., 3.)
hphiz = ROOT.TH1F("hphiz", "", 20, 0., 3.)

for r in reports:
    if r.status == "PASS":  # and converged(r):
        if r.deltax is not None and r.deltax.error != 0.: hx.Fill(r.deltax.error*10.)
        if r.deltay is not None and r.deltay.error != 0.: hy.Fill(r.deltay.error*10.)
        if r.deltaz is not None and r.deltaz.error != 0.: hz.Fill(r.deltaz.error*10.)
        if r.deltaphix is not None and r.deltaphix.error != 0.: hphix.Fill(r.deltaphix.error*1000.)
        if r.deltaphiy is not None and r.deltaphiy.error != 0.: hphiy.Fill(r.deltaphiy.error*1000.)
        if r.deltaphiz is not None and r.deltaphiz.error != 0.: hphiz.Fill(r.deltaphiz.error*1000.)

hx.SetXTitle("Local x statistical uncertainty (mm)")
hy.SetXTitle("Local y statistical uncertainty (mm)")
hz.SetXTitle("Local z statistical uncertainty (mm)")
hphix.SetXTitle("Local #phi_{x} statistical uncertainty (mrad)")
hphiy.SetXTitle("Local #phi_{y} statistical uncertainty (mrad)")
hphiz.SetXTitle("Local #phi_{z} statistical uncertainty (mrad)")
hx.GetXaxis().CenterTitle()
hy.GetXaxis().CenterTitle()
hz.GetXaxis().CenterTitle()
hphix.GetXaxis().CenterTitle()
hphiy.GetXaxis().CenterTitle()
hphiz.GetXaxis().CenterTitle()
hx.SetFillColor(ROOT.kBlue-10)
hy.SetFillColor(ROOT.kBlue-10)
hz.SetFillColor(ROOT.kBlue-10)
hphix.SetFillColor(ROOT.kBlue-10)
hphiy.SetFillColor(ROOT.kBlue-10)
hphiz.SetFillColor(ROOT.kBlue-10)

c1.Clear()
c1.Divide(3, 2)
c1.GetPad(1).cd(); hx.Draw()
c1.GetPad(2).cd(); hy.Draw()
c1.GetPad(3).cd(); hz.Draw()
c1.GetPad(4).cd(); hphix.Draw()
c1.GetPad(5).cd(); hphiy.Draw()
c1.GetPad(6).cd(); hphiz.Draw()
c1.SaveAs("data_100GeV_newinternal_quoted_uncertainty.pdf")

###############

##### HERE!!!
execfile("geometryXMLparser.py")
finalMC = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/ALLATONCE_PATTERN7/PATTERNiter01.xml")
execfile("/home/jpivarski/work/results/CRAFTchambers2/ALLATONCE_PATTERN7/PATTERNiter01_report.py")
tdrStyle.SetOptStat("mr")
tdrStyle.SetStatW(0.30)
tdrStyle.SetStatFontSize(0.05)


######## high pT MC 350k events
execfile("geometryXMLparser.py")
finalMC = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/DTMC1_sync1_fullyrandom/DTMCiter03.xml")
execfile("/home/jpivarski/work/results/CRAFTchambers2/DTMC1_sync1_fullyrandom/DTMCiter03_report.py")
fullstats_reports = reports
tdrStyle.SetOptStat("mr")
tdrStyle.SetStatW(0.30)
tdrStyle.SetStatFontSize(0.05)
########

######## high pT MC 100k events
execfile("geometryXMLparser.py")
finalMC = MuonGeometry("/home/jpivarski/work/results/final_stats_check/LOTSOFSTUFF/STATSiter22.xml")
execfile("/home/jpivarski/work/results/final_stats_check/LOTSOFSTUFF/STATSiter22_report.py")
smallstats_reports = reports
tdrStyle.SetOptStat("mr")
tdrStyle.SetStatW(0.30)
tdrStyle.SetStatFontSize(0.05)
########

# the data
execfile("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_sync1_realtracker/DTCRAFTiter03_report.py")

def mean(xlist):
    return sum(xlist) / float(len(xlist))
from math import *

allx = []
ally = []
allz = []
allphix = []
allphiy = []
allphiz = []
for r in reports:
    if r.status == "PASS":
        if r.deltax is not None and r.deltax.error != 0.: allx.append((r.deltax.error*10.)**2)
        if r.deltay is not None and r.deltay.error != 0.: ally.append((r.deltay.error*10.)**2)
        if r.deltaz is not None and r.deltaz.error != 0.: allz.append((r.deltaz.error*10.)**2)
        if r.deltaphix is not None and r.deltaphix.error != 0.: allphix.append((r.deltaphix.error*1000.)**2)
        if r.deltaphiy is not None and r.deltaphiy.error != 0.: allphiy.append((r.deltaphiy.error*1000.)**2)
        if r.deltaphiz is not None and r.deltaphiz.error != 0.: allphiz.append((r.deltaphiz.error*1000.)**2)
print sqrt(mean(allx)), sqrt(mean(ally)), sqrt(mean(allz))
print sqrt(mean(allphix)), sqrt(mean(allphiy)), sqrt(mean(allphiz))

h = ROOT.TH1F("h", "", 100, 0, 0.5)
for r in reports:
    if r.status == "PASS":
        if r.deltax is not None and r.deltax.error != 0.: h.Fill(r.deltax.error*10.)
h.Draw()




c1.Clear()
h = ROOT.TH1F("h", "", 100, 0, 5)
for rfull, rsmall in zip(fullstats_reports, smallstats_reports):
    if rfull.status == rsmall.status == "PASS":
        if rfull.deltax is not None and rsmall.deltax is not None and rfull.deltax.error != 0: h.Fill((rsmall.deltax.error / rfull.deltax.error)**2)
#         if rfull.deltay is not None and rsmall.deltay is not None and rfull.deltay.error != 0: h.Fill((rsmall.deltay.error / rfull.deltay.error)**2)
#         if rfull.deltaz is not None and rsmall.deltaz is not None and rfull.deltaz.error != 0: h.Fill((rsmall.deltaz.error / rfull.deltaz.error)**2)
#         if rfull.deltaphix is not None and rsmall.deltaphix is not None and rfull.deltaphix.error != 0: h.Fill((rsmall.deltaphix.error / rfull.deltaphix.error)**2)
#         if rfull.deltaphiy is not None and rsmall.deltaphiy is not None and rfull.deltaphiy.error != 0: h.Fill((rsmall.deltaphiy.error / rfull.deltaphiy.error)**2)
#         if rfull.deltaphiz is not None and rsmall.deltaphiz is not None and rfull.deltaphiz.error != 0: h.Fill((rsmall.deltaphiz.error / rfull.deltaphiz.error)**2)
h.Draw()



# histograms = {}
# normhistograms = {}
# for param in "x", "y", "z", "phix", "phiy", "phiz":
#     for region in 1, 2, 3, 4, 5, 6:
#         histograms[param + str(region)] = ROOT.TH1F("h" + param + str(region), "", 50, -5., 5.)
#         normhistograms[param + str(region)] = ROOT.TH1F("nh" + param + str(region), "", 50, -10., 10.)

histograms = {}
normhistograms = {}
for param in "x", "y", "z", "phix", "phiy", "phiz":
    for region in 1, 2, 3, 4:
        histograms[param + str(region)] = ROOT.TH1F("h" + param + str(region), "", 50, -5., 5.)
        normhistograms[param + str(region)] = ROOT.TH1F("nh" + param + str(region), "", 50, -10., 10.)

def fill(param, r, value, normvalue):
#     if r.postal_address[0] == "DT":
#         if abs(r.postal_address[1]) == 0: region = 1
#         elif abs(r.postal_address[1]) == 1: region = 2
#         else: region = 3
#     elif r.postal_address[0] == "CSC":
#         if r.postal_address[2:4] == (1, 3): region = 4
#         elif r.postal_address[3] == 2: region = 5
#         else: region = 6

#     for reg in range(region, 7):
#         histograms[param + str(reg)].Fill(value)
#         normhistograms[param + str(reg)].Fill(normvalue)
    if r.postal_address[0] == "DT":
        region = r.postal_address[2]
    elif r.postal_address[0] == "CSC":
        return

    for reg in range(region, 5):
        histograms[param + str(reg)].Fill(value)
        normhistograms[param + str(reg)].Fill(normvalue)

for r in reports:
    if r.status == "PASS":    # converged(r)
        if r.postal_address[0] == "DT": position = finalMC.dt[r.postal_address[1:]]
        if r.postal_address[0] == "CSC": position = finalMC.csc[r.postal_address[1:]]

        if r.deltax is not None and r.deltax.error != 0.: fill("x", r, position.x*10., position.x / r.deltax.error)
        if r.deltay is not None and r.deltay.error != 0.: fill("y", r, position.y*10., position.y / r.deltay.error)
        if r.deltaz is not None and r.deltaz.error != 0.: fill("z", r, position.z*10., position.z / r.deltaz.error)
        if r.deltaphix is not None and r.deltaphix.error != 0.: fill("phix", r, position.phix*1000., position.phix / r.deltaphix.error)
        if r.deltaphiy is not None and r.deltaphiy.error != 0.: fill("phiy", r, position.phiy*1000., position.phiy / r.deltaphiy.error)
        if r.deltaphiz is not None and r.deltaphiz.error != 0.: fill("phiz", r, position.phiz*1000., position.phiz / r.deltaphiz.error)

def draw(param, title, norm=False):
    if norm: h = normhistograms
    else: h = histograms

#     h[param + str(6)].SetFillColor(ROOT.kMagenta+2)
#     h[param + str(5)].SetFillColor(ROOT.kRed-4)
#     h[param + str(4)].SetFillColor(ROOT.kYellow)
#     h[param + str(3)].SetFillColor(ROOT.kGreen+1)
#     h[param + str(2)].SetFillColor(ROOT.kCyan+2)
#     h[param + str(1)].SetFillColor(ROOT.kBlue-8)

#     h[param + str(6)].SetXTitle(title)
#     h[param + str(6)].GetXaxis().CenterTitle()

#     h[param + str(6)].Draw()
#     h[param + str(5)].Draw("same")
#     h[param + str(4)].Draw("same")
#     h[param + str(3)].Draw("same")
#     h[param + str(2)].Draw("same")
#     h[param + str(1)].Draw("same")

    h[param + str(4)].SetFillColor(ROOT.kYellow)
    h[param + str(3)].SetFillColor(ROOT.kGreen+1)
    h[param + str(2)].SetFillColor(ROOT.kCyan+2)
    h[param + str(1)].SetFillColor(ROOT.kBlue-8)

    h[param + str(4)].SetXTitle(title)
    h[param + str(4)].GetXaxis().CenterTitle()

    h[param + str(4)].Draw()
    h[param + str(3)].Draw("same")
    h[param + str(2)].Draw("same")
    h[param + str(1)].Draw("same")

# c1.Clear()
# c1.Divide(3, 2)
# c1.GetPad(1).cd(); draw("x", "Local x accuracy (mm)")
# c1.GetPad(2).cd(); draw("y", "Local y accuracy (mm)")
# c1.GetPad(3).cd(); draw("z", "Local z accuracy (mm)")
# tlegend = ROOT.TLegend(0.65, 0.2, 0.99, 0.78)
# tlegend.SetFillColor(ROOT.kWhite)
# tlegend.SetBorderSize(1)
# tlegend.AddEntry(histograms["z6"], "MEn/1", "f")
# tlegend.AddEntry(histograms["z5"], "MEn/2", "f")
# tlegend.AddEntry(histograms["z4"], "ME1/3", "f")
# tlegend.AddEntry(histograms["z3"], "DT wheel #pm 2", "f")
# tlegend.AddEntry(histograms["z2"], "DT wheel #pm 1", "f")
# tlegend.AddEntry(histograms["z1"], "DT wheel 0", "f")
# tlegend.SetTextSize(0.05)
# tlegend.Draw()
# c1.GetPad(4).cd(); draw("phix", "Local #phi_{x} accuracy (mrad)")
# c1.GetPad(5).cd(); draw("phiy", "Local #phi_{y} accuracy (mrad)")
# c1.GetPad(6).cd(); draw("phiz", "Local #phi_{z} accuracy (mrad)")
# ROOT.gPad.SaveAs("mc_accuracy.pdf")

# c1.Clear()
# c1.Divide(3, 2)
# c1.GetPad(1).cd(); draw("x", "Local x error / quoted uncertainty", True)
# c1.GetPad(2).cd(); draw("y", "Local y error / quoted uncertainty", True)
# c1.GetPad(3).cd(); draw("z", "Local z error / quoted uncertainty", True)
# tlegend = ROOT.TLegend(0.65, 0.2, 0.99, 0.78)
# tlegend.SetFillColor(ROOT.kWhite)
# tlegend.SetBorderSize(1)
# tlegend.AddEntry(normhistograms["z6"], "MEn/1", "f")
# tlegend.AddEntry(normhistograms["z5"], "MEn/2", "f")
# tlegend.AddEntry(normhistograms["z4"], "ME1/3", "f")
# tlegend.AddEntry(normhistograms["z3"], "DT wheel #pm 2", "f")
# tlegend.AddEntry(normhistograms["z2"], "DT wheel #pm 1", "f")
# tlegend.AddEntry(normhistograms["z1"], "DT wheel 0", "f")
# tlegend.SetTextSize(0.05)
# tlegend.Draw()
# c1.GetPad(4).cd(); draw("phix", "Local #phi_{x} error / quoted uncertainty", True)
# c1.GetPad(5).cd(); draw("phiy", "Local #phi_{y} error / quoted uncertainty", True)
# c1.GetPad(6).cd(); draw("phiz", "Local #phi_{z} error / quoted uncertainty", True)
# ROOT.gPad.SaveAs("mc_accuracy_of_uncertainties.pdf")

c1.Clear()
c1.Divide(3, 2)
c1.GetPad(1).cd(); draw("x", "Local x accuracy (mm)")
c1.GetPad(2).cd(); draw("y", "Local y accuracy (mm)")
c1.GetPad(3).cd(); draw("z", "Local z accuracy (mm)")
tlegend = ROOT.TLegend(0.65, 0.3, 0.99, 0.78)
tlegend.SetFillColor(ROOT.kWhite)
tlegend.SetBorderSize(1)
tlegend.AddEntry(histograms["z4"], "station 4", "f")
tlegend.AddEntry(histograms["z3"], "station 3", "f")
tlegend.AddEntry(histograms["z2"], "station 2", "f")
tlegend.AddEntry(histograms["z1"], "station 1", "f")
tlegend.SetTextSize(0.05)
tlegend.Draw()
c1.GetPad(4).cd(); draw("phix", "Local #phi_{x} accuracy (mrad)")
c1.GetPad(5).cd(); draw("phiy", "Local #phi_{y} accuracy (mrad)")
c1.GetPad(6).cd(); draw("phiz", "Local #phi_{z} accuracy (mrad)")
ROOT.gPad.SaveAs("mc_accuracy_bystation.pdf")

c1.Clear()
c1.Divide(3, 2)
c1.GetPad(1).cd(); draw("x", "Local x error / quoted uncertainty", True)
c1.GetPad(2).cd(); draw("y", "Local y error / quoted uncertainty", True)
c1.GetPad(3).cd(); draw("z", "Local z error / quoted uncertainty", True)
tlegend = ROOT.TLegend(0.65, 0.3, 0.99, 0.78)
tlegend.SetFillColor(ROOT.kWhite)
tlegend.SetBorderSize(1)
tlegend.AddEntry(histograms["z4"], "station 4", "f")
tlegend.AddEntry(histograms["z3"], "station 3", "f")
tlegend.AddEntry(histograms["z2"], "station 2", "f")
tlegend.AddEntry(histograms["z1"], "station 1", "f")
tlegend.SetTextSize(0.05)
tlegend.Draw()
c1.GetPad(4).cd(); draw("phix", "Local #phi_{x} error / quoted uncertainty", True)
c1.GetPad(5).cd(); draw("phiy", "Local #phi_{y} error / quoted uncertainty", True)
c1.GetPad(6).cd(); draw("phiz", "Local #phi_{z} error / quoted uncertainty", True)
ROOT.gPad.SaveAs("mc_accuracy_of_uncertainties_bystation.pdf")

##############

# execfile("/home/jpivarski/work/results/CRAFTchambers2/ALLATONCE_PATTERN5/PATTERNiter04_report.py")
# tdrStyle.SetOptStat("mro")
# tdrStyle.SetStatW(0.40)
# tdrStyle.SetStatFontSize(0.05)

# c1.Clear()
# h = ROOT.TH1F("h", "", 100, 0., 30.)
# for r in reports:
#     if r.status == "PASS" and converged(r):
#         h.Fill(r.redchi2)
# h.Draw()

#################

import re
execfile("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_wAPE_optimal/DTCRAFTiter04_report.py")

def drawbarrel(fileName, reports, whattodo, template="template_barrel.svg"):
    template = file(template)
    output = file(fileName, "w")
    for line in template.readlines():
        outline = line
        match = re.search("id=\"([A-Za-z0-9]+)\".*fill=\"[A-Za-z0-9]+\"", line)
        if match is not None:
            name = match.groups()[0]
            for r in reports:
                if r.name == name:
                    outline = re.sub("fill=\"[A-Za-z0-9]+\"", "fill=\"%s\"" % whattodo(r), line)
                    break
        output.write(outline)
    output.close()

def rgb(r, g, b, maximum=1.):
  return "#%02x%02x%02x" % (max(0, min(r*255./maximum, 255)), max(0, min(g*255./maximum, 255)), max(0, min(b*255./maximum, 255)))

def select_for_final(r):
    if r.status == "FAIL":
        return "none"
    
    if not converged(r): return "none"

    if r.deltax is not None and r.deltax.error*10. > 1.: return "none"
    if r.deltay is not None and r.deltay.error*10. > 1.: return "none"
    if r.deltaz is not None and r.deltaz.error*10. > 1.: return "none"
    if r.deltaphix is not None and r.deltaphix.error*1000. > 1.: return "none"
    if r.deltaphiy is not None and r.deltaphiy.error*1000. > 1.: return "none"
    if r.deltaphiz is not None and r.deltaphiz.error*1000. > 1.: return "none"

    return "red"

drawbarrel("data_final_map.svg", reports, select_for_final)




execfile("geometryXMLparser.py")

initialData = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/internalDTalignment.xml")
finalData = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_wAPE_optimal/DTCRAFTiter04.xml")
execfile("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_wAPE_optimal/DTCRAFTiter04_report.py")

tdrStyle.SetOptStat("mrou")
tdrStyle.SetStatW(0.40)
tdrStyle.SetStatFontSize(0.05)

histograms = {}
for param in "x", "y", "z":
    for region in 1, 2, 3, 4, 5:
        histograms[param + str(region)] = ROOT.TH1F("h" + param + str(region), "", 50, -12, 12.)
for param in "phix", "phiy", "phiz":
    for region in 1, 2, 3, 4, 5:
        histograms[param + str(region)] = ROOT.TH1F("h" + param + str(region), "", 50, -10, 10.)
# for param in "y", "z":
#     for region in 1, 2, 3, 4, 5:
#         histograms[param + str(region)] = ROOT.TH1F("h" + param + str(region), "", 50, -30, 30.)

def fill(param, r, value):
    if r.postal_address[0] == "DT":
        if r.postal_address[1] == -2: region = 1
        elif r.postal_address[1] == -1: region = 2
        elif r.postal_address[1] == 0: region = 3
        elif r.postal_address[1] == 1: region = 4
        elif r.postal_address[1] == 2: region = 5

        for reg in range(region, 6):
            histograms[param + str(reg)].Fill(value)

for r in reports:
    if r.status == "PASS" and converged(r):
        if r.postal_address[0] == "DT":
            initial = initialData.dt[r.postal_address[1:]]
            final = finalData.dt[r.postal_address[1:]]
        else: continue

        if r.deltax is not None and r.deltax.error*10. > 1.: continue
        if r.deltay is not None and r.deltay.error*10. > 1.: continue
        if r.deltaz is not None and r.deltaz.error*10. > 1.: continue
        if r.deltaphix is not None and r.deltaphix.error*1000. > 1.: continue
        if r.deltaphiy is not None and r.deltaphiy.error*1000. > 1.: continue
        if r.deltaphiz is not None and r.deltaphiz.error*1000. > 1.: continue

        if r.deltax is not None and r.deltax.error != 0.: fill("x", r, (final.x - initial.x)*10.)
        if r.deltay is not None and r.deltay.error != 0.: fill("y", r, (final.y - initial.y)*10.)
        if r.deltaz is not None and r.deltaz.error != 0.: fill("z", r, (final.z - initial.z)*10.)
        if r.deltaphix is not None and r.deltaphix.error != 0.: fill("phix", r, (final.phix - initial.phix)*1000.)
        if r.deltaphiy is not None and r.deltaphiy.error != 0.: fill("phiy", r, (final.phiy - initial.phiy)*1000.)
        if r.deltaphiz is not None and r.deltaphiz.error != 0.: fill("phiz", r, (final.phiz - initial.phiz)*1000.)

def draw(param, title):
    histograms[param + str(5)].SetFillColor(ROOT.kRed-4)
    histograms[param + str(4)].SetFillColor(ROOT.kYellow)
    histograms[param + str(3)].SetFillColor(ROOT.kGreen+1)
    histograms[param + str(2)].SetFillColor(ROOT.kCyan+2)
    histograms[param + str(1)].SetFillColor(ROOT.kBlue-8)

    histograms[param + str(5)].SetXTitle(title)
    histograms[param + str(5)].GetXaxis().CenterTitle()

    histograms[param + str(5)].Draw()
    histograms[param + str(4)].Draw("same")
    histograms[param + str(3)].Draw("same")
    histograms[param + str(2)].Draw("same")
    histograms[param + str(1)].Draw("same")

c1.Clear()
c1.Divide(3, 2)
c1.GetPad(1).cd(); draw("x", "Local x alignment correction (mm)")
tlegend = ROOT.TLegend(0.17, 0.55, 0.45, 0.98)
tlegend.SetFillColor(ROOT.kWhite)
tlegend.SetBorderSize(1)
tlegend.AddEntry(histograms["x5"], " wheel +2", "f")
tlegend.AddEntry(histograms["x4"], " wheel +1", "f")
tlegend.AddEntry(histograms["x3"], " wheel 0", "f")
tlegend.AddEntry(histograms["x2"], " wheel -1", "f")
tlegend.AddEntry(histograms["x1"], " wheel -2", "f")
tlegend.SetTextSize(0.05)
tlegend.Draw()
c1.GetPad(2).cd(); draw("y", "Local y alignment correction (mm)")
histograms["z5"].SetAxisRange(0, 17, "Y")
c1.GetPad(3).cd(); draw("z", "Local z alignment correction (mm)")
c1.GetPad(4).cd(); draw("phix", "Local #phi_{x} alignment correction (mrad)")
c1.GetPad(5).cd(); draw("phiy", "Local #phi_{y} alignment correction (mrad)")
c1.GetPad(6).cd(); draw("phiz", "Local #phi_{z} alignment correction (mrad)")
c1.SaveAs("data_final_corrections.pdf")


#############

execfile("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_wAPE_afterFinal/DTCRAFTiter01_report.py")
afterFinal = reports

initialData = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_wAPE_optimal/DTCRAFTiter04.xml")
finalData = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_wAPE_afterFinal/DTCRAFTiter01.xml")
execfile("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_wAPE_optimal/DTCRAFTiter04_report.py")

bad_addresses = []
output_for_marcus = {}
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
        
        for r2 in afterFinal:
            if r2.postal_address == r.postal_address and r2.status == "PASS":

                initial = initialData.dt[r.postal_address[1:]]
                final = finalData.dt[r.postal_address[1:]]

                if r.deltax is not None and r.deltax.error != 0.: fill("x", r, (final.x - initial.x)*10.)
                if r.deltay is not None and r.deltay.error != 0.: fill("y", r, (final.y - initial.y)*10.)
                if r.deltaz is not None and r.deltaz.error != 0.: fill("z", r, (final.z - initial.z)*10.)
                if r.deltaphix is not None and r.deltaphix.error != 0.: fill("phix", r, (final.phix - initial.phix)*1000.)
                if r.deltaphiy is not None and r.deltaphiy.error != 0.: fill("phiy", r, (final.phiy - initial.phiy)*1000.)
                if r.deltaphiz is not None and r.deltaphiz.error != 0.: fill("phiz", r, (final.phiz - initial.phiz)*1000.)

                if r2.deltay is None:
                    print r2.postal_address, r2.deltax.value*10., r2.deltaz.value*10., r2.deltaphix.value*1000., r2.deltaphiy.value*1000., r2.deltaphiz.value*1000.
                else:
                    print r2.postal_address, r2.deltax.value*10., r2.deltay.value*10., r2.deltaz.value*10., r2.deltaphix.value*1000., r2.deltaphiy.value*1000., r2.deltaphiz.value*1000.

        final = finalData.dt[r.postal_address[1:]]
        output_for_marcus[r.postal_address] = "Wheel %d station %d sector %d x %g y %g z %g phix %g phiy %g phiz %g" % (r.postal_address[1], r.postal_address[2], r.postal_address[3], final.x*10., final.y*10., final.z*10., final.phix*1000., final.phiy*1000., final.phiz*1000.)

bad_addresses.sort()
print "\n".join(map(str, bad_addresses))

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


keys = output_for_marcus.keys()
keys.sort()
for key in keys:
    print output_for_marcus[key]


#############################

execfile("geometryXMLparser.py")

initialData = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/internalDTalignment.xml")
finalData = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_wAPE_optimal/DTCRAFTiter04.xml")
execfile("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_wAPE_optimal/DTCRAFTiter04_report.py")
execfile("previously_aligned.py")

tdrStyle.SetOptStat("")

histograms = {}
for param in "x", "y", "phix", "phiy", "phiz":
    for wheel in "A", "B", "C", "D", "E":
        for station in "1", "2", "3", "4":
            if station == "4": nsectors = 14
            else: nsectors = 12
            histograms["h" + param + wheel + station] = ROOT.TH1F("h" + param + wheel + station, "", nsectors, 0.5, nsectors + 0.5)
            histograms["hh" + param + wheel + station] = ROOT.TH1F("hh" + param + wheel + station, "", nsectors, 0.5, nsectors + 0.5)

            if wheel == "A": realwheel = "-2"
            elif wheel == "B": realwheel = "-1"
            elif wheel == "C": realwheel = "0"
            elif wheel == "D": realwheel = "+1"
            elif wheel == "E": realwheel = "+2"

            histograms["h" + param + wheel + station].SetXTitle("Wheel %s station %s sector number" % (realwheel, station))
            if param == "x": histograms["h" + param + wheel + station].SetYTitle("x correction w.r.t. V11 (mm)")
            if param == "y": histograms["h" + param + wheel + station].SetYTitle("y correction w.r.t. V11 (mm)")
            if param == "phix": histograms["h" + param + wheel + station].SetYTitle("#phi_{x} correction w.r.t. V11 (mrad)")
            if param == "phiy": histograms["h" + param + wheel + station].SetYTitle("#phi_{y} correction w.r.t. V11 (mrad)")
            if param == "phiz": histograms["h" + param + wheel + station].SetYTitle("#phi_{z} correction w.r.t. V11 (mrad)")

for r in reports:
    if r.status == "PASS" and converged(r):
        if r.postal_address[0] == "DT":
            initial = initialData.dt[r.postal_address[1:]]
            final = finalData.dt[r.postal_address[1:]]
        else: continue

        if r.postal_address[1] == -2: wheel = "A"
        elif r.postal_address[1] == -1: wheel = "B"
        elif r.postal_address[1] == 0: wheel = "C"
        elif r.postal_address[1] == 1: wheel = "D"
        elif r.postal_address[1] == 2: wheel = "E"

        if r.postal_address[2] == 1: station = "1"
        if r.postal_address[2] == 2: station = "2"
        if r.postal_address[2] == 3: station = "3"
        if r.postal_address[2] == 4: station = "4"

        sector = r.postal_address[3]

        histograms["hhx" + wheel + station].SetBinContent(sector, 2000.)
        histograms["hhx" + wheel + station].SetBinError(sector, 1000.)
        histograms["hhy" + wheel + station].SetBinContent(sector, 2000.)
        histograms["hhy" + wheel + station].SetBinError(sector, 1000.)
        histograms["hhphix" + wheel + station].SetBinContent(sector, 2000.)
        histograms["hhphix" + wheel + station].SetBinError(sector, 1000.)
        histograms["hhphiy" + wheel + station].SetBinContent(sector, 2000.)
        histograms["hhphiy" + wheel + station].SetBinError(sector, 1000.)
        histograms["hhphiz" + wheel + station].SetBinContent(sector, 2000.)
        histograms["hhphiz" + wheel + station].SetBinError(sector, 1000.)

        if r.deltax is not None and r.deltax.error != 0.:
            histograms["hx" + wheel + station].SetBinContent(sector, (final.x - initial.x)*10.)
            histograms["hx" + wheel + station].SetBinError(sector, r.deltax.error*10.)

            if r.postal_address in previously_aligned:
                histograms["hhx" + wheel + station].SetBinContent(sector, (final.x - initial.x)*10.)
                histograms["hhx" + wheel + station].SetBinError(sector, r.deltax.error*10.)

        else:
            histograms["hx" + wheel + station].SetBinContent(sector, 2000.)
            histograms["hx" + wheel + station].SetBinError(sector, 1000.)

        if r.deltay is not None and r.deltay.error != 0.:
            histograms["hy" + wheel + station].SetBinContent(sector, (final.y - initial.y)*10.)
            histograms["hy" + wheel + station].SetBinError(sector, r.deltay.error*10.)

            if r.postal_address in previously_aligned_iny:
                histograms["hhy" + wheel + station].SetBinContent(sector, (final.y - initial.y)*10.)
                histograms["hhy" + wheel + station].SetBinError(sector, r.deltay.error*10.)
                
        else:
            histograms["hy" + wheel + station].SetBinContent(sector, 2000.)
            histograms["hy" + wheel + station].SetBinError(sector, 1000.)

#         if r.deltaz is not None and r.deltaz.error != 0.:
#             histograms["hz" + wheel + station].SetBinContent(sector, (final.z - initial.z)*10.)
#             histograms["hz" + wheel + station].SetBinError(sector, r.deltaz.error*10.)
#         else:
#             histograms["hz" + wheel + station].SetBinContent(sector, 2000.)
#             histograms["hz" + wheel + station].SetBinError(sector, 1000.)

        if r.deltaphix is not None and r.deltaphix.error != 0.:
            histograms["hphix" + wheel + station].SetBinContent(sector, (final.phix - initial.phix)*1000.)
            histograms["hphix" + wheel + station].SetBinError(sector, r.deltaphix.error*1000.)
        else:
            histograms["hphix" + wheel + station].SetBinContent(sector, 2000.)
            histograms["hphix" + wheel + station].SetBinError(sector, 1000.)

        if r.deltaphiy is not None and r.deltaphiy.error != 0.:
            histograms["hphiy" + wheel + station].SetBinContent(sector, (final.phiy - initial.phiy)*1000.)
            histograms["hphiy" + wheel + station].SetBinError(sector, r.deltaphiy.error*1000.)
        else:
            histograms["hphiy" + wheel + station].SetBinContent(sector, 2000.)
            histograms["hphiy" + wheel + station].SetBinError(sector, 1000.)

        if r.deltaphiz is not None and r.deltaphiz.error != 0.:
            histograms["hphiz" + wheel + station].SetBinContent(sector, (final.phiz - initial.phiz)*1000.)
            histograms["hphiz" + wheel + station].SetBinError(sector, r.deltaphiz.error*1000.)

            if r.postal_address in previously_aligned:
                histograms["hhphiz" + wheel + station].SetBinContent(sector, (final.phiz - initial.phiz)*1000.)
                histograms["hhphiz" + wheel + station].SetBinError(sector, r.deltaphiz.error*1000.)

        else:
            histograms["hphiz" + wheel + station].SetBinContent(sector, 2000.)
            histograms["hphiz" + wheel + station].SetBinError(sector, 1000.)

for param in "x", "y", "phix", "phiy", "phiz":
    for wheel in "A", "B", "C", "D", "E":
        for station in "1", "2", "3", "4":
            histograms["h" + param + wheel + station].SetAxisRange(-12, 12, "Y")
            histograms["h" + param + wheel + station].GetXaxis().CenterTitle()
            histograms["h" + param + wheel + station].GetYaxis().CenterTitle()

            histograms["hh" + param + wheel + station].SetMarkerColor(ROOT.kRed)
            histograms["hh" + param + wheel + station].SetLineColor(ROOT.kRed)

# for param in "x", "y", "phix", "phiy", "phiz":
#     for wheel in "A", "B", "C", "D", "E":
#         for station in "1", "2", "3", "4":
#             print "histograms[\"h" + param + wheel + station + "\"].Draw(\"e1\"); histograms[\"hh" + param + wheel + station + "\"].Draw(\"samee1\"); ROOT.gPad.SaveAs(\"data_all_" + param + wheel + station + ".pdf\")"

histograms["hxA1"].Draw("e1"); histograms["hhxA1"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_xA1.pdf")
histograms["hxA2"].Draw("e1"); histograms["hhxA2"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_xA2.pdf")
histograms["hxA3"].Draw("e1"); histograms["hhxA3"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_xA3.pdf")
histograms["hxA4"].Draw("e1"); histograms["hhxA4"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_xA4.pdf")
histograms["hxB1"].Draw("e1"); histograms["hhxB1"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_xB1.pdf")
histograms["hxB2"].Draw("e1"); histograms["hhxB2"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_xB2.pdf")
histograms["hxB3"].Draw("e1"); histograms["hhxB3"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_xB3.pdf")
histograms["hxB4"].Draw("e1"); histograms["hhxB4"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_xB4.pdf")
histograms["hxC1"].Draw("e1"); histograms["hhxC1"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_xC1.pdf")
histograms["hxC2"].Draw("e1"); histograms["hhxC2"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_xC2.pdf")
histograms["hxC3"].Draw("e1"); histograms["hhxC3"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_xC3.pdf")
histograms["hxC4"].Draw("e1"); histograms["hhxC4"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_xC4.pdf")
histograms["hxD1"].Draw("e1"); histograms["hhxD1"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_xD1.pdf")
histograms["hxD2"].Draw("e1"); histograms["hhxD2"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_xD2.pdf")
histograms["hxD3"].Draw("e1"); histograms["hhxD3"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_xD3.pdf")
histograms["hxD4"].Draw("e1"); histograms["hhxD4"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_xD4.pdf")
histograms["hxE1"].Draw("e1"); histograms["hhxE1"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_xE1.pdf")
histograms["hxE2"].Draw("e1"); histograms["hhxE2"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_xE2.pdf")
histograms["hxE3"].Draw("e1"); histograms["hhxE3"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_xE3.pdf")
histograms["hxE4"].Draw("e1"); histograms["hhxE4"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_xE4.pdf")
histograms["hyA1"].Draw("e1"); histograms["hhyA1"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_yA1.pdf")
histograms["hyA2"].Draw("e1"); histograms["hhyA2"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_yA2.pdf")
histograms["hyA3"].Draw("e1"); histograms["hhyA3"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_yA3.pdf")
histograms["hyA4"].Draw("e1"); histograms["hhyA4"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_yA4.pdf")
histograms["hyB1"].Draw("e1"); histograms["hhyB1"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_yB1.pdf")
histograms["hyB2"].Draw("e1"); histograms["hhyB2"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_yB2.pdf")
histograms["hyB3"].Draw("e1"); histograms["hhyB3"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_yB3.pdf")
histograms["hyB4"].Draw("e1"); histograms["hhyB4"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_yB4.pdf")
histograms["hyC1"].Draw("e1"); histograms["hhyC1"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_yC1.pdf")
histograms["hyC2"].Draw("e1"); histograms["hhyC2"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_yC2.pdf")
histograms["hyC3"].Draw("e1"); histograms["hhyC3"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_yC3.pdf")
histograms["hyC4"].Draw("e1"); histograms["hhyC4"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_yC4.pdf")
histograms["hyD1"].Draw("e1"); histograms["hhyD1"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_yD1.pdf")
histograms["hyD2"].Draw("e1"); histograms["hhyD2"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_yD2.pdf")
histograms["hyD3"].Draw("e1"); histograms["hhyD3"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_yD3.pdf")
histograms["hyD4"].Draw("e1"); histograms["hhyD4"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_yD4.pdf")
histograms["hyE1"].Draw("e1"); histograms["hhyE1"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_yE1.pdf")
histograms["hyE2"].Draw("e1"); histograms["hhyE2"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_yE2.pdf")
histograms["hyE3"].Draw("e1"); histograms["hhyE3"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_yE3.pdf")
histograms["hyE4"].Draw("e1"); histograms["hhyE4"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_yE4.pdf")
histograms["hphixA1"].Draw("e1"); histograms["hhphixA1"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_phixA1.pdf")
histograms["hphixA2"].Draw("e1"); histograms["hhphixA2"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_phixA2.pdf")
histograms["hphixA3"].Draw("e1"); histograms["hhphixA3"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_phixA3.pdf")
histograms["hphixA4"].Draw("e1"); histograms["hhphixA4"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_phixA4.pdf")
histograms["hphixB1"].Draw("e1"); histograms["hhphixB1"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_phixB1.pdf")
histograms["hphixB2"].Draw("e1"); histograms["hhphixB2"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_phixB2.pdf")
histograms["hphixB3"].Draw("e1"); histograms["hhphixB3"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_phixB3.pdf")
histograms["hphixB4"].Draw("e1"); histograms["hhphixB4"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_phixB4.pdf")
histograms["hphixC1"].Draw("e1"); histograms["hhphixC1"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_phixC1.pdf")
histograms["hphixC2"].Draw("e1"); histograms["hhphixC2"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_phixC2.pdf")
histograms["hphixC3"].Draw("e1"); histograms["hhphixC3"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_phixC3.pdf")
histograms["hphixC4"].Draw("e1"); histograms["hhphixC4"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_phixC4.pdf")
histograms["hphixD1"].Draw("e1"); histograms["hhphixD1"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_phixD1.pdf")
histograms["hphixD2"].Draw("e1"); histograms["hhphixD2"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_phixD2.pdf")
histograms["hphixD3"].Draw("e1"); histograms["hhphixD3"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_phixD3.pdf")
histograms["hphixD4"].Draw("e1"); histograms["hhphixD4"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_phixD4.pdf")
histograms["hphixE1"].Draw("e1"); histograms["hhphixE1"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_phixE1.pdf")
histograms["hphixE2"].Draw("e1"); histograms["hhphixE2"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_phixE2.pdf")
histograms["hphixE3"].Draw("e1"); histograms["hhphixE3"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_phixE3.pdf")
histograms["hphixE4"].Draw("e1"); histograms["hhphixE4"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_phixE4.pdf")
histograms["hphiyA1"].Draw("e1"); histograms["hhphiyA1"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_phiyA1.pdf")
histograms["hphiyA2"].Draw("e1"); histograms["hhphiyA2"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_phiyA2.pdf")
histograms["hphiyA3"].Draw("e1"); histograms["hhphiyA3"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_phiyA3.pdf")
histograms["hphiyA4"].Draw("e1"); histograms["hhphiyA4"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_phiyA4.pdf")
histograms["hphiyB1"].Draw("e1"); histograms["hhphiyB1"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_phiyB1.pdf")
histograms["hphiyB2"].Draw("e1"); histograms["hhphiyB2"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_phiyB2.pdf")
histograms["hphiyB3"].Draw("e1"); histograms["hhphiyB3"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_phiyB3.pdf")
histograms["hphiyB4"].Draw("e1"); histograms["hhphiyB4"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_phiyB4.pdf")
histograms["hphiyC1"].Draw("e1"); histograms["hhphiyC1"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_phiyC1.pdf")
histograms["hphiyC2"].Draw("e1"); histograms["hhphiyC2"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_phiyC2.pdf")
histograms["hphiyC3"].Draw("e1"); histograms["hhphiyC3"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_phiyC3.pdf")
histograms["hphiyC4"].Draw("e1"); histograms["hhphiyC4"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_phiyC4.pdf")
histograms["hphiyD1"].Draw("e1"); histograms["hhphiyD1"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_phiyD1.pdf")
histograms["hphiyD2"].Draw("e1"); histograms["hhphiyD2"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_phiyD2.pdf")
histograms["hphiyD3"].Draw("e1"); histograms["hhphiyD3"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_phiyD3.pdf")
histograms["hphiyD4"].Draw("e1"); histograms["hhphiyD4"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_phiyD4.pdf")
histograms["hphiyE1"].Draw("e1"); histograms["hhphiyE1"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_phiyE1.pdf")
histograms["hphiyE2"].Draw("e1"); histograms["hhphiyE2"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_phiyE2.pdf")
histograms["hphiyE3"].Draw("e1"); histograms["hhphiyE3"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_phiyE3.pdf")
histograms["hphiyE4"].Draw("e1"); histograms["hhphiyE4"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_phiyE4.pdf")
histograms["hphizA1"].Draw("e1"); histograms["hhphizA1"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_phizA1.pdf")
histograms["hphizA2"].Draw("e1"); histograms["hhphizA2"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_phizA2.pdf")
histograms["hphizA3"].Draw("e1"); histograms["hhphizA3"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_phizA3.pdf")
histograms["hphizA4"].Draw("e1"); histograms["hhphizA4"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_phizA4.pdf")
histograms["hphizB1"].Draw("e1"); histograms["hhphizB1"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_phizB1.pdf")
histograms["hphizB2"].Draw("e1"); histograms["hhphizB2"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_phizB2.pdf")
histograms["hphizB3"].Draw("e1"); histograms["hhphizB3"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_phizB3.pdf")
histograms["hphizB4"].Draw("e1"); histograms["hhphizB4"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_phizB4.pdf")
histograms["hphizC1"].Draw("e1"); histograms["hhphizC1"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_phizC1.pdf")
histograms["hphizC2"].Draw("e1"); histograms["hhphizC2"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_phizC2.pdf")
histograms["hphizC3"].Draw("e1"); histograms["hhphizC3"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_phizC3.pdf")
histograms["hphizC4"].Draw("e1"); histograms["hhphizC4"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_phizC4.pdf")
histograms["hphizD1"].Draw("e1"); histograms["hhphizD1"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_phizD1.pdf")
histograms["hphizD2"].Draw("e1"); histograms["hhphizD2"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_phizD2.pdf")
histograms["hphizD3"].Draw("e1"); histograms["hhphizD3"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_phizD3.pdf")
histograms["hphizD4"].Draw("e1"); histograms["hhphizD4"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_phizD4.pdf")
histograms["hphizE1"].Draw("e1"); histograms["hhphizE1"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_phizE1.pdf")
histograms["hphizE2"].Draw("e1"); histograms["hhphizE2"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_phizE2.pdf")
histograms["hphizE3"].Draw("e1"); histograms["hhphizE3"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_phizE3.pdf")
histograms["hphizE4"].Draw("e1"); histograms["hhphizE4"].Draw("samee1"); ROOT.gPad.SaveAs("data_all_phizE4.pdf")

for param in "x", "y", "phix", "phiy", "phiz":
    for wheel in "A", "B", "C", "D", "E":
        for station in "1", "2", "3", "4":
            print r"""\begin{frame}
\frametitle{Chamber-by-chamber differences}
\framesubtitle{previously-aligned chambers are in \textcolor{red}{red}}
\includegraphics[height=\linewidth, angle=90]{data_all_%s%s%s.pdf}
\end{frame}
""" % (param, wheel, station)

################################

execfile("geometryXMLparser.py")

# initialData = MuonGeometry("final_production_alignment_CHECK.xml")
# finalData = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_wAPE_100GeV/DTCRAFTiter01.xml")
# execfile("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_wAPE_100GeV/DTCRAFTiter01_report.py")

# initialData = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_wAPE_100GeV/DTCRAFTiter01.xml")
# finalData = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_wAPE_100GeV/DTCRAFTiter02.xml")
# execfile("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_wAPE_100GeV/DTCRAFTiter02_report.py")

# initialData = MuonGeometry("final_production_alignment_CHECK.xml")
# finalData = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_wAPE_100GeV/DTCRAFTiter02.xml")
# execfile("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_wAPE_100GeV/DTCRAFTiter02_report.py")

# initialData = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_wAPE_100GeV/DTCRAFTiter02.xml")
# finalData = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_wAPE_100GeV/DTCRAFTiter03.xml")
# execfile("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_wAPE_100GeV/DTCRAFTiter03_report.py")

initialData = MuonGeometry("final_production_alignment_CHECK.xml")
finalData = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_wAPE_100GeV/DTCRAFTiter03.xml")
execfile("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_wAPE_100GeV/DTCRAFTiter03_report.py")

# initialData = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_wAPE_100GeV/DTCRAFTiter03.xml")
# finalData = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_wAPE_100GeV_afterTest/DTCRAFTiter01.xml")
# execfile("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_wAPE_100GeV/DTCRAFTiter03_report.py")

tdrStyle.SetOptStat("mrou")
tdrStyle.SetStatW(0.40)
tdrStyle.SetStatFontSize(0.05)

histograms = {}
histograms2 = {}
for param in "x", "y", "z":
    for region in 1, 2, 3, 4, 5:
        histograms[param + str(region)] = ROOT.TH1F("h" + param + str(region), "", 25, -15., 15.)
    for station in 1, 2, 3, 4:
        histograms2[param + str(station)] = ROOT.TH1F("h2" + param + str(station), "", 25, -15., 15.)

for param in "phix", "phiy", "phiz":
    for region in 1, 2, 3, 4, 5:
        histograms[param + str(region)] = ROOT.TH1F("h" + param + str(region), "", 25, -10, 10.)
    for station in 1, 2, 3, 4:
        histograms2[param + str(station)] = ROOT.TH1F("h2" + param + str(station), "", 25, -10, 10.)

def fill(param, r, value):
    if r.postal_address[0] == "DT":
        if r.postal_address[1] == -2: region = 1
        elif r.postal_address[1] == -1: region = 2
        elif r.postal_address[1] == 0: region = 3
        elif r.postal_address[1] == 1: region = 4
        elif r.postal_address[1] == 2: region = 5

        for reg in range(region, 6):
            histograms[param + str(reg)].Fill(value)

        station = r.postal_address[2]
        for sta in range(station, 5):
            histograms2[param + str(sta)].Fill(value)

for r in reports:
    if r.status == "PASS" and converged(r):
        if r.postal_address[0] == "DT":
            initial = initialData.dt[r.postal_address[1:]]
            final = finalData.dt[r.postal_address[1:]]
        else: continue

        if r.deltax.error*10. > 1.: continue

#         if r.deltax is not None and r.deltax.error*10. > 1.: continue
#         if r.deltay is not None and r.deltay.error*10. > 1.: continue
#         if r.deltaz is not None and r.deltaz.error*10. > 1.: continue
#         if r.deltaphix is not None and r.deltaphix.error*1000. > 1.: continue
#         if r.deltaphiy is not None and r.deltaphiy.error*1000. > 1.: continue
#         if r.deltaphiz is not None and r.deltaphiz.error*1000. > 1.: continue

        if r.deltax is not None and 0. < r.deltax.error*10.: fill("x", r, (final.x - initial.x)*10.)
        if r.deltay is not None and 0. < r.deltay.error*10.: fill("y", r, (final.y - initial.y)*10.)
        if r.deltaz is not None and 0. < r.deltaz.error*10.: fill("z", r, (final.z - initial.z)*10.)
        if r.deltaphix is not None and 0. < r.deltaphix.error*1000.: fill("phix", r, (final.phix - initial.phix)*1000.)
        if r.deltaphiy is not None and 0. < r.deltaphiy.error*1000.: fill("phiy", r, (final.phiy - initial.phiy)*1000.)
        if r.deltaphiz is not None and 0. < r.deltaphiz.error*1000.: fill("phiz", r, (final.phiz - initial.phiz)*1000.)

def draw(param, title):
    histograms[param + str(5)].SetFillColor(ROOT.kRed-4)
    histograms[param + str(4)].SetFillColor(ROOT.kYellow)
    histograms[param + str(3)].SetFillColor(ROOT.kGreen+1)
    histograms[param + str(2)].SetFillColor(ROOT.kCyan+2)
    histograms[param + str(1)].SetFillColor(ROOT.kBlue-8)

    histograms[param + str(5)].SetXTitle(title)
    histograms[param + str(5)].GetXaxis().CenterTitle()

    histograms[param + str(5)].Draw()
    histograms[param + str(4)].Draw("same")
    histograms[param + str(3)].Draw("same")
    histograms[param + str(2)].Draw("same")
    histograms[param + str(1)].Draw("same")

def draw2(param, title):
    histograms2[param + str(4)].SetFillColor(ROOT.kGray+3)
    histograms2[param + str(3)].SetFillColor(ROOT.kGray+2)
    histograms2[param + str(2)].SetFillColor(ROOT.kGray+1)
    histograms2[param + str(1)].SetFillColor(ROOT.kGray)

    histograms2[param + str(4)].SetXTitle(title)
    histograms2[param + str(4)].GetXaxis().CenterTitle()

    histograms2[param + str(4)].Draw()
    histograms2[param + str(3)].Draw("same")
    histograms2[param + str(2)].Draw("same")
    histograms2[param + str(1)].Draw("same")

c1.Clear()
c1.Divide(3, 2)
c1.GetPad(1).cd(); draw("x", "Local x effect of p_{T} > 100 GeV cut (mm)")
tlegend = ROOT.TLegend(0.17, 0.55, 0.45, 0.98)
tlegend.SetFillColor(ROOT.kWhite)
tlegend.SetBorderSize(1)
tlegend.AddEntry(histograms["x5"], " wheel +2", "f")
tlegend.AddEntry(histograms["x4"], " wheel +1", "f")
tlegend.AddEntry(histograms["x3"], " wheel 0", "f")
tlegend.AddEntry(histograms["x2"], " wheel -1", "f")
tlegend.AddEntry(histograms["x1"], " wheel -2", "f")
tlegend.SetTextSize(0.05)
tlegend.Draw()
c1.GetPad(2).cd(); draw("y", "Local y effect of p_{T} > 100 GeV cut (mm)")
c1.GetPad(3).cd(); draw("z", "Local z effect of p_{T} > 100 GeV cut (mm)")
c1.GetPad(4).cd(); draw("phix", "Local #phi_{x} effect of p_{T} > 100 GeV cut (mrad)")
c1.GetPad(5).cd(); draw("phiy", "Local #phi_{y} effect of p_{T} > 100 GeV cut (mrad)")
c1.GetPad(6).cd(); draw("phiz", "Local #phi_{z} effect of p_{T} > 100 GeV cut (mrad)")
c1.SaveAs("data_effect_of_100GeVcut.pdf")

c1.Clear()
c1.Divide(3, 2)
c1.GetPad(1).cd(); draw2("x", "Local x effect of p_{T} > 100 GeV cut (mm)")
tlegend = ROOT.TLegend(0.17, 0.55, 0.45, 0.98)
tlegend.SetFillColor(ROOT.kWhite)
tlegend.SetBorderSize(1)
tlegend.AddEntry(histograms2["x4"], " station 4", "f")
tlegend.AddEntry(histograms2["x3"], " station 3", "f")
tlegend.AddEntry(histograms2["x2"], " station 2", "f")
tlegend.AddEntry(histograms2["x1"], " station 1", "f")
tlegend.SetTextSize(0.05)
tlegend.Draw()
c1.GetPad(2).cd(); draw2("y", "Local y effect of p_{T} > 100 GeV cut (mm)")
c1.GetPad(3).cd(); draw2("z", "Local z effect of p_{T} > 100 GeV cut (mm)")
c1.GetPad(4).cd(); draw2("phix", "Local #phi_{x} effect of p_{T} > 100 GeV cut (mrad)")
c1.GetPad(5).cd(); draw2("phiy", "Local #phi_{y} effect of p_{T} > 100 GeV cut (mrad)")
c1.GetPad(6).cd(); draw2("phiz", "Local #phi_{z} effect of p_{T} > 100 GeV cut (mrad)")
c1.SaveAs("data_effect_of_100GeVcut2.pdf")

################################

# execfile("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_wAPE_100GeV/DTCRAFTiter01_report.py")
# execfile("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_wAPE_optimal/DTCRAFTiter01_report.py")

# h = ROOT.TH1F("h", "", 100, -2., 2.)

# for r in reports:
#     if r.status == "PASS":
#         if r.deltax.error*10. < 1.:
#             h.Fill(r.deltax.antisym*10.)

# c1.Clear()
# h.Draw()

################################

# initialData = MuonGeometry("final_production_alignment_global.xml")
# finalData = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_wAPE_100GeV/DTCRAFTiter01_global.xml")
# execfile("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_wAPE_100GeV/DTCRAFTiter01_report.py")

# initialData = MuonGeometry("final_production_alignment_global.xml")
# finalData = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_wAPE_100GeV/DTCRAFTiter02_global.xml")
# execfile("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_wAPE_100GeV/DTCRAFTiter02_report.py")

initialData = MuonGeometry("final_production_alignment_global.xml")
finalData = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_wAPE_100GeV/DTCRAFTiter03_global.xml")
execfile("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_wAPE_100GeV/DTCRAFTiter03_report.py")

# initialData = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/V4alignment_global.xml")
# initialData = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/V11alignment_global.xml")

tdrStyle.SetOptStat("mrou")
tdrStyle.SetStatW(0.35)
tdrStyle.SetStatFontSize(0.05)

histograms = {}
histograms2 = {}
for param in "deltaphi", "rphi":
    for region in 1, 2, 3, 4, 5, 10, 20, 30, 40, 50:
        if param == "rphi":
            histograms[param + str(region)] = ROOT.TH1F("h" + param + str(region), "", 25, -15., 15.)
        elif param == "deltaphi":
            histograms[param + str(region)] = ROOT.TH1F("h" + param + str(region), "", 25, -2., 2.)
    for sta in 1, 2, 3, 4:
        if param == "rphi":
            histograms2[param + str(sta)] = ROOT.TH1F("h2" + param + str(sta), "", 25, -15., 15.)
        elif param == "deltaphi":
            histograms2[param + str(sta)] = ROOT.TH1F("h2" + param + str(sta), "", 25, -2., 2.)

def fill(param, r, value):
    if r.postal_address[0] == "DT":
        if r.postal_address[1] == -2: region = 1
        elif r.postal_address[1] == -1: region = 2
        elif r.postal_address[1] == 0: region = 3
        elif r.postal_address[1] == 1: region = 4
        elif r.postal_address[1] == 2: region = 5

        for reg in range(region, 6):
            histograms[param + str(reg)].Fill(value)

        if r.postal_address[1] == 2: region = 1
        elif r.postal_address[1] == 1: region = 2
        elif r.postal_address[1] == 0: region = 3
        elif r.postal_address[1] == -1: region = 4
        elif r.postal_address[1] == -2: region = 5

        for reg in range(region, 6):
            histograms[param + str(reg*10)].Fill(value)

        station = r.postal_address[2]
        for sta in range(station, 5):
            histograms2[param + str(sta)].Fill(value)

for r in reports:
    if r.status == "PASS" and converged(r):
        if r.postal_address[0] == "DT":
            initial = initialData.dt[r.postal_address[1:]]
            final = finalData.dt[r.postal_address[1:]]
        else: continue

        if r.deltax.error*10. > 1.: continue

        if r.deltax is not None and 0. < r.deltax.error*10.:
            radius1 = sqrt(final.x**2 + final.y**2)
            radius2 = sqrt(initial.x**2 + initial.y**2)
            radius = (radius1 + radius2) / 2.

            phi1 = atan2(final.y, final.x)
            phi2 = atan2(initial.y, initial.x)
            deltaphi = phi1 - phi2
            while deltaphi < -pi: deltaphi += 2.*pi
            while deltaphi > pi: deltaphi -= 2.*pi

            fill("deltaphi", r, deltaphi*1000.)
            fill("rphi", r, radius*deltaphi*10.)

def draw1(param, title):
    histograms[param + str(5)].SetFillColor(ROOT.kRed-4)
    histograms[param + str(4)].SetFillColor(ROOT.kYellow)
    histograms[param + str(3)].SetFillColor(ROOT.kGreen+1)
    histograms[param + str(2)].SetFillColor(ROOT.kCyan+2)
    histograms[param + str(1)].SetFillColor(ROOT.kBlue-8)

    histograms[param + str(5)].SetXTitle(title)
    histograms[param + str(5)].GetXaxis().CenterTitle()

    histograms[param + str(5)].Draw()
    histograms[param + str(4)].Draw("same")
    histograms[param + str(3)].Draw("same")
    histograms[param + str(2)].Draw("same")
    histograms[param + str(1)].Draw("same")

def draw2(param, title):
    histograms[param + str(50)].SetFillColor(ROOT.kBlue-8)
    histograms[param + str(40)].SetFillColor(ROOT.kCyan+2)
    histograms[param + str(30)].SetFillColor(ROOT.kGreen+1)
    histograms[param + str(20)].SetFillColor(ROOT.kYellow)
    histograms[param + str(10)].SetFillColor(ROOT.kRed-4)

    histograms[param + str(50)].SetXTitle(title)
    histograms[param + str(50)].GetXaxis().CenterTitle()

    histograms[param + str(50)].Draw()
    histograms[param + str(40)].Draw("same")
    histograms[param + str(30)].Draw("same")
    histograms[param + str(20)].Draw("same")
    histograms[param + str(10)].Draw("same")

def draw3(param, title):
    histograms2[param + str(4)].SetFillColor(ROOT.kGray+3)
    histograms2[param + str(3)].SetFillColor(ROOT.kGray+2)
    histograms2[param + str(2)].SetFillColor(ROOT.kGray+1)
    histograms2[param + str(1)].SetFillColor(ROOT.kGray)

    histograms2[param + str(4)].SetXTitle(title)
    histograms2[param + str(4)].GetXaxis().CenterTitle()

    histograms2[param + str(4)].Draw()
    histograms2[param + str(3)].Draw("same")
    histograms2[param + str(2)].Draw("same")
    histograms2[param + str(1)].Draw("same")

c1.Clear()
c1.Divide(3, 2)
c1.GetPad(1).cd(); draw1("deltaphi", "Global #Delta#phi effect of p_{T} > 100 GeV cut (mrad)")
tlegend = ROOT.TLegend(0.17, 0.55, 0.45, 0.98)
tlegend.SetFillColor(ROOT.kWhite)
tlegend.SetBorderSize(1)
tlegend.AddEntry(histograms["deltaphi5"], " wheel +2", "f")
tlegend.AddEntry(histograms["deltaphi4"], " wheel +1", "f")
tlegend.AddEntry(histograms["deltaphi3"], " wheel 0", "f")
tlegend.AddEntry(histograms["deltaphi2"], " wheel -1", "f")
tlegend.AddEntry(histograms["deltaphi1"], " wheel -2", "f")
tlegend.SetTextSize(0.05)
tlegend.Draw()
c1.GetPad(4).cd(); draw1("rphi", "Global r#phi effect of p_{T} > 100 GeV cut (mm)")
tlegend.Draw()
c1.GetPad(2).cd(); draw2("deltaphi", "Global #Delta#phi effect of p_{T} > 100 GeV cut (mrad)")
tlegend2 = ROOT.TLegend(0.17, 0.55, 0.45, 0.98)
tlegend2.SetFillColor(ROOT.kWhite)
tlegend2.SetBorderSize(1)
tlegend2.AddEntry(histograms["deltaphi50"], " wheel -2", "f")
tlegend2.AddEntry(histograms["deltaphi40"], " wheel -1", "f")
tlegend2.AddEntry(histograms["deltaphi30"], " wheel 0", "f")
tlegend2.AddEntry(histograms["deltaphi20"], " wheel +1", "f")
tlegend2.AddEntry(histograms["deltaphi10"], " wheel +2", "f")
tlegend2.SetTextSize(0.05)
tlegend2.Draw()
c1.GetPad(5).cd(); draw2("rphi", "Global r#phi effect of p_{T} > 100 GeV cut (mm)")
tlegend2.Draw()
c1.GetPad(3).cd(); draw3("deltaphi", "Global #Delta#phi effect of p_{T} > 100 GeV cut (mrad)")
tlegend3 = ROOT.TLegend(0.17, 0.55, 0.45, 0.98)
tlegend3.SetFillColor(ROOT.kWhite)
tlegend3.SetBorderSize(1)
tlegend3.AddEntry(histograms2["deltaphi4"], " station 4", "f")
tlegend3.AddEntry(histograms2["deltaphi3"], " station 3", "f")
tlegend3.AddEntry(histograms2["deltaphi2"], " station 2", "f")
tlegend3.AddEntry(histograms2["deltaphi1"], " station 1", "f")
tlegend3.SetTextSize(0.05)
tlegend3.Draw()
c1.GetPad(6).cd(); draw3("rphi", "Global r#phi effect of p_{T} > 100 GeV cut (mm)")
tlegend3.Draw()
c1.SaveAs("data_effect_of_100GeVcut3.pdf")

