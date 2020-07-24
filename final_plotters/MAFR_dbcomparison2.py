import ROOT
from math import *
execfile("/home/jpivarski/bin/tdrstyle.py")
c1 = ROOT.TCanvas()
execfile("geometryXMLparser.py")

########################################################

tdrStyle.SetOptStat("mrou")
tdrStyle.SetStatW(0.38)
tdrStyle.SetStatH(0.05)
tdrStyle.SetStatFontSize(0.035)
initialMC = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/RANDOMMC_20_twoBin_100011/randominitialCSC.xml")
finalMC = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/RANDOMMC_20_twoBin_100011/PATTERNiter03.xml")
execfile("/home/jpivarski/work/results/CRAFTchambers2/RANDOMMC_20_twoBin_100011/PATTERNiter03_report.py")

histograms = {}
for param in "x", "phiy", "phiz":
    for region in "me13", "outer", "inner", "me11", "me12", "dt", "initial":
        if param == "x":
            histograms[param + region] = ROOT.TH1F("h" + param + region, "", 40, -2., 2.)
        else:
            histograms[param + region] = ROOT.TH1F("h" + param + region, "", 70, -3.5, 3.5)

def fill(param, r, value):
    if r.postal_address[0] == "DT": region = "dt"
    elif r.postal_address[0] == "CSC" and r.postal_address[2:4] in ((1, 1), (1, 4)): region = "me11"
    elif r.postal_address[0] == "CSC" and r.postal_address[2:4] == (1, 2): region = "me12"
    elif r.postal_address[0] == "CSC" and r.postal_address[2:4] == (1, 3): region = "me13"
    elif r.postal_address[0] == "CSC" and r.postal_address[3] == 1: region = "inner"
    elif r.postal_address[0] == "CSC" and r.postal_address[3] == 2: region = "outer"
    else: raise Exception
    alist = ["me13", "outer", "inner", "me11", "me12", "dt"]
    for reg in alist[alist.index(region):]:
        histograms[param + reg].Fill(value)

for r in reports:
    if r.status == "PASS":
        if r.postal_address[0] == "DT":
            initialposition = initialMC.dt[r.postal_address[1:]]
            position = finalMC.dt[r.postal_address[1:]]
        if r.postal_address[0] == "CSC":
            initialposition = initialMC.csc[r.postal_address[1:]]
            position = finalMC.csc[r.postal_address[1:]]

        if r.deltax is not None and r.deltax.error != 0.:
            histograms["xinitial"].Fill(initialposition.x*10.)
            fill("x", r, position.x*10.)
        if r.deltaphiy is not None and r.deltaphiy.error != 0.:
            histograms["phiyinitial"].Fill(initialposition.phiy*1000.)
            fill("phiy", r, position.phiy*1000.)
        if r.deltaphiz is not None and r.deltaphiz.error != 0.:
            histograms["phizinitial"].Fill(initialposition.phiz*1000.)
            fill("phiz", r, position.phiz*1000.)

def draw(param, title):
    histograms[param + "initial"].SetLineColor(ROOT.kRed)

    histograms[param + "dt"].SetFillColor(ROOT.kGray)
    histograms[param + "me12"].SetFillColor(ROOT.kRed-9)
    histograms[param + "me11"].SetFillColor(ROOT.kYellow)
    histograms[param + "inner"].SetFillColor(ROOT.kMagenta-6)
    histograms[param + "outer"].SetFillColor(ROOT.kCyan)
    histograms[param + "me13"].SetFillColor(ROOT.kGreen)

    histograms[param + "dt"].SetXTitle(title)
    histograms[param + "dt"].GetXaxis().CenterTitle()

    histograms[param + "dt"].Draw()
    histograms[param + "me12"].Draw("same")
    histograms[param + "me11"].Draw("same")
    histograms[param + "inner"].Draw("same")
    histograms[param + "outer"].Draw("same")
    histograms[param + "me13"].Draw("same")

    histograms[param + "initial"].Draw("same")

c1.Clear()
c1.Divide(3, 1)
c1.GetPad(1).cd(); draw("x", "Local x accuracy (mm)")
c1.GetPad(2).cd(); draw("phiy", "Local #phi_{y} accuracy (mrad)")
c1.GetPad(3).cd(); draw("phiz", "Local #phi_{z} accuracy (mrad)")
tlegend = ROOT.TLegend(0.6, 0.39, 0.98, 0.77)
tlegend.SetFillColor(ROOT.kWhite)
tlegend.SetBorderSize(1)
tlegend.AddEntry(histograms["phizinitial"], " before align", "l")
tlegend.AddEntry(histograms["phizdt"], " DT", "f")
tlegend.AddEntry(histograms["phizme12"], " ME1/2", "f")
tlegend.AddEntry(histograms["phizme11"], " ME1/1", "f")
tlegend.AddEntry(histograms["phizinner"], " ME2,3,4/1", "f")
tlegend.AddEntry(histograms["phizouter"], " ME2,3/2", "f")
tlegend.AddEntry(histograms["phizme13"], " ME1/3", "f")
tlegend.SetTextSize(0.05)
tlegend.Draw()
c1.SaveAs("mc_cscresolution.pdf")

