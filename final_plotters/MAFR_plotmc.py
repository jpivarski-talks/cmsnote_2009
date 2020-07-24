import ROOT
from math import *
execfile("/home/jpivarski/bin/tdrstyle.py")
c1 = ROOT.TCanvas()
execfile("geometryXMLparser.py")

########################################################

tdrStyle.SetOptStat("emrou")
tdrStyle.SetStatW(0.38)
tdrStyle.SetStatH(0.06)
tdrStyle.SetStatFontSize(0.035)
initialMC = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/standardmisalign2.xml")
finalnoneMC = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/SCENARIOSAFE_cosmics_then_collisions/SCENARIOSAFENOEM13_NONE_4.xml")
finalMC = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/SCENARIOSAFE_cosmics_then_collisions/SCENARIOSAFENOEM13_STARTUP_4.xml")
# finalMC = MuonGeometry("/home/jpivarski/work/cmssw_test/new_startup_scenario2009/CMSSW_2_1_7/src/MuonAlignmentRcd_cosmics-50pb-1-noME13_v1_CHECKME.xml")
execfile("/home/jpivarski/work/results/CRAFTchambers2/SCENARIOSAFE_cosmics_then_collisions/SCENARIOSAFENOEM13_STARTUP_4_report.py")

histograms = {}
for param in "x", "y", "z", "phix", "phiy", "phiz":
    for region in "initial", "none", "final":
        histograms[param + region] = ROOT.TH1F("h" + param + region, "", 50, -10., 10.)

for r in reports:
    if r.status == "PASS":
        if r.postal_address[0] == "DT":
            initialposition = initialMC.dt[r.postal_address[1:]]
            noneposition = finalnoneMC.dt[r.postal_address[1:]]
            position = finalMC.dt[r.postal_address[1:]]
            wheel, station, sector = r.postal_address[1:]
            if wheel in (-1, 0, 1) and station != 4: region = "cosmic"
            elif station == 4: region = "station4"
            else: region = "sides"
            
        if r.postal_address[0] == "CSC":
            initialposition = initialMC.csc[r.postal_address[1:]]
            noneposition = finalnoneMC.csc[r.postal_address[1:]]
            position = finalMC.csc[r.postal_address[1:]]
            region = "endcaps"

        if abs(position.x*10.) > 10: print "bad convergence", r.postal_address, position.x*10.

        if True: # and region == "cosmic":
            histograms["xinitial"].Fill(initialposition.x*10.)
            histograms["xnone"].Fill(noneposition.x*10.)
            histograms["xfinal"].Fill(position.x*10.)
            if region == "cosmic":
                histograms["yinitial"].Fill(initialposition.y*10.)
                histograms["ynone"].Fill(noneposition.y*10.)
                histograms["yfinal"].Fill(position.y*10.)
                histograms["zinitial"].Fill(initialposition.z*10.)
                histograms["znone"].Fill(noneposition.z*10.)
                histograms["zfinal"].Fill(position.z*10.)
            if region == "cosmic" or region == "sides":
                histograms["phixinitial"].Fill(initialposition.phix*1000.)
                histograms["phixnone"].Fill(noneposition.phix*1000.)
                histograms["phixfinal"].Fill(position.phix*1000.)
            histograms["phiyinitial"].Fill(initialposition.phiy*1000.)
            histograms["phiynone"].Fill(noneposition.phiy*1000.)
            histograms["phiyfinal"].Fill(position.phiy*1000.)
            histograms["phizinitial"].Fill(initialposition.phiz*1000.)
            histograms["phiznone"].Fill(noneposition.phiz*1000.)
            histograms["phizfinal"].Fill(position.phiz*1000.)

#         if region == "cosmic" or region == "sides":
#             histograms["xinitial"].Fill(initialposition.x*10.)
#             histograms["xnone"].Fill(noneposition.x*10.)
#             histograms["xfinal"].Fill(position.x*10.)
#             histograms["yinitial"].Fill(initialposition.y*10.)
#             histograms["ynone"].Fill(noneposition.y*10.)
#             histograms["yfinal"].Fill(position.y*10.)
#             histograms["zinitial"].Fill(initialposition.z*10.)
#             histograms["znone"].Fill(noneposition.z*10.)
#             histograms["zfinal"].Fill(position.z*10.)
#             histograms["phixinitial"].Fill(initialposition.phix*1000.)
#             histograms["phixnone"].Fill(noneposition.phix*1000.)
#             histograms["phixfinal"].Fill(position.phix*1000.)
#             histograms["phiyinitial"].Fill(initialposition.phiy*1000.)
#             histograms["phiynone"].Fill(noneposition.phiy*1000.)
#             histograms["phiyfinal"].Fill(position.phiy*1000.)
#             histograms["phizinitial"].Fill(initialposition.phiz*1000.)
#             histograms["phiznone"].Fill(noneposition.phiz*1000.)
#             histograms["phizfinal"].Fill(position.phiz*1000.)

    else:
        print "fit failure", r.postal_address

# def draw(param, title):
#     histograms[param + "initial"].SetFillColor(ROOT.kMagenta+2)
#     histograms[param + "everywhere"].SetFillColor(ROOT.kYellow)

#     histograms[param + "everywhere"].SetXTitle(title)
#     histograms[param + "everywhere"].GetXaxis().CenterTitle()

#     histograms[param + "everywhere"].Draw()
#     histograms[param + "initial"].Draw("same")
#     histograms[param + "everywhere"].Draw("same")

def draw(param, title):
    histograms[param + "final"].SetFillColor(ROOT.kYellow)
    histograms[param + "initial"].SetFillColor(ROOT.kMagenta-2)
    histograms[param + "none"].SetLineStyle(2)

    histograms[param + "final"].SetXTitle(title)
    histograms[param + "final"].GetXaxis().CenterTitle()
    histograms[param + "final"].SetAxisRange(0, histograms[param + "none"].GetMaximum()*1.2, "Y")

    histograms[param + "final"].Draw()
    histograms[param + "initial"].Draw("same")
    histograms[param + "final"].Draw("same")
    histograms[param + "none"].Draw("same")

c1.Clear()
c1.Divide(3, 2)
c1.GetPad(1).cd(); draw("x", "Local x accuracy (mm)")
tlegend = ROOT.TLegend(0.13, 0.74, 0.51, 0.99)
tlegend.SetFillColor(ROOT.kWhite)
tlegend.SetBorderSize(1)
tlegend.AddEntry(histograms["xinitial"], " before", "f")
tlegend.AddEntry(histograms["xfinal"], " after (statbox)", "f")
tlegend.AddEntry(histograms["xnone"], " ideal tracker", "f")
tlegend.SetTextSize(0.05)
tlegend.Draw()
c1.GetPad(2).cd(); draw("y", "Local y accuracy (mm)")
c1.GetPad(3).cd(); draw("z", "Local z accuracy (mm)")
c1.GetPad(4).cd(); draw("phix", "Local #phi_{x} accuracy (mrad)")
c1.GetPad(5).cd(); draw("phiy", "Local #phi_{y} accuracy (mrad)")
c1.GetPad(6).cd(); draw("phiz", "Local #phi_{z} accuracy (mrad)")
# c1.SaveAs("scenario_cosmics.pdf")

c1.Clear()
c1.Divide(3, 1)
c1.GetPad(1).cd(); draw("x", "Local x accuracy (mm)")
tlegend = ROOT.TLegend(0.13, 0.74, 0.51, 0.99)
tlegend.SetFillColor(ROOT.kWhite)
tlegend.SetBorderSize(1)
tlegend.AddEntry(histograms["xinitial"], " before", "f")
tlegend.AddEntry(histograms["xfinal"], " after (statbox)", "f")
tlegend.AddEntry(histograms["xnone"], " ideal tracker", "f")
tlegend.SetTextSize(0.05)
tlegend.Draw()
c1.GetPad(2).cd(); draw("phiy", "Local #phi_{y} accuracy (mrad)")
c1.GetPad(3).cd(); draw("phiz", "Local #phi_{z} accuracy (mrad)")
# c1.SaveAs("scenario_cosmics.pdf")














# tdrStyle.SetOptStat("emrou")
# tdrStyle.SetStatW(0.38)
# tdrStyle.SetStatH(0.06)
# tdrStyle.SetStatFontSize(0.035)
# initialMC = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/startup_v11.xml")
# finalMC = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/startup_v12.xml")
# finalMC = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/startup_31X.xml")
# interloper = MuonGeometry("/home/jpivarski/work/cmssw_test/new_startup_scenario2009/CMSSW_2_1_7/src/scenario_versions/generated_V02-09-05_CHECKME.xml")
# execfile("/home/jpivarski/work/results/CRAFTchambers2/SCENARIOSAFE_cosmics_then_collisions/SCENARIOSAFE_NONE_4_report.py")

# histograms = {}
# for param in "x", "y", "z", "phix", "phiy", "phiz":
#     for region in "initial", "inter", "final":
#         histograms[param + region] = ROOT.TH1F("h" + param + region, "", 50, -20., 20.)

# for r in reports:
#     if True:
#         if r.postal_address[0] == "DT":
#             initialposition = initialMC.dt[r.postal_address[1:]]
#             position = finalMC.dt[r.postal_address[1:]]
#             interpos = interloper.dt[r.postal_address[1:]]
#             wheel, station, sector = r.postal_address[1:]
#             continue

#         if r.postal_address[0] == "CSC":
#             initialposition = initialMC.csc[r.postal_address[1:]]
#             position = finalMC.csc[r.postal_address[1:]]
#             interpos = interloper.csc[r.postal_address[1:]]
#             endcap, station, ring, chamber = r.postal_address[1:]

#         if True:
#             histograms["xinitial"].Fill(initialposition.x*10.)
#             histograms["xfinal"].Fill(position.x*10.)
#             histograms["xinter"].Fill(interpos.x*10.)
#             histograms["yinitial"].Fill(initialposition.y*10.)
#             histograms["yfinal"].Fill(position.y*10.)
#             histograms["yinter"].Fill(interpos.y*10.)
#             histograms["zinitial"].Fill(initialposition.z*10.)
#             histograms["zfinal"].Fill(position.z*10.)
#             histograms["zinter"].Fill(interpos.z*10.)
#             histograms["phixinitial"].Fill(initialposition.phix*1000.)
#             histograms["phixfinal"].Fill(position.phix*1000.)
#             histograms["phixinter"].Fill(interpos.phix*1000.)
#             histograms["phiyinitial"].Fill(initialposition.phiy*1000.)
#             histograms["phiyfinal"].Fill(position.phiy*1000.)
#             histograms["phiyinter"].Fill(interpos.phiy*1000.)
#             histograms["phizinitial"].Fill(initialposition.phiz*1000.)
#             histograms["phizfinal"].Fill(position.phiz*1000.)
#             histograms["phizinter"].Fill(interpos.phiz*1000.)

# def draw(param, title):
#     histograms[param + "final"].SetLineColor(ROOT.kBlue)
#     histograms[param + "initial"].SetLineColor(ROOT.kBlack)
#     histograms[param + "inter"].SetLineColor(ROOT.kRed)
#     histograms[param + "inter"].SetLineStyle(2)

#     histograms[param + "final"].SetXTitle(title)
#     histograms[param + "final"].GetXaxis().CenterTitle()
#     histograms[param + "final"].SetAxisRange(0, max(histograms[param + "initial"].GetMaximum(), histograms[param + "inter"].GetMaximum(), histograms[param + "final"].GetMaximum())*1.2, "Y")

#     histograms[param + "final"].Draw()
#     histograms[param + "initial"].Draw("same")
#     histograms[param + "final"].Draw("same")
#     histograms[param + "inter"].Draw("same")

# c1.Clear()
# c1.Divide(3, 2)
# c1.GetPad(1).cd(); draw("x", "Local x accuracy (mm)")
# tlegend = ROOT.TLegend(0.13, 0.74, 0.51, 0.99)
# tlegend.SetFillColor(ROOT.kWhite)
# tlegend.SetBorderSize(1)
# tlegend.AddEntry(histograms["xinitial"], " STARTUP_V11", "l")
# tlegend.AddEntry(histograms["xfinal"], " STARTUP_V12", "l")
# tlegend.AddEntry(histograms["xinter"], " V02-09-04", "l")
# tlegend.SetTextSize(0.05)
# tlegend.Draw()
# c1.GetPad(2).cd(); draw("y", "Local y accuracy (mm)")
# c1.GetPad(3).cd(); draw("z", "Local z accuracy (mm)")
# c1.GetPad(4).cd(); draw("phix", "Local #phi_{x} accuracy (mrad)")
# c1.GetPad(5).cd(); draw("phiy", "Local #phi_{y} accuracy (mrad)")
# c1.GetPad(6).cd(); draw("phiz", "Local #phi_{z} accuracy (mrad)")

