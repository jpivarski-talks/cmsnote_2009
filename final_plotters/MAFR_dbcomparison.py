import ROOT
from math import *
execfile("/home/jpivarski/bin/tdrstyle.py")
c1 = ROOT.TCanvas()
execfile("geometryXMLparser.py")

initialData = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/internalDTalignment_correct.xml")
finalData = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_sync1/DTCRAFTiter01.xml")

initialData = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_sync1/DTCRAFTiter01.xml")
finalData = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_sync1/DTCRAFTiter02.xml")

initialData = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_sync1/DTCRAFTiter02.xml")
finalData = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_sync1/DTCRAFTiter03.xml")

# initialData = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_sync1/DTCRAFTiter03.xml")
# finalData = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_sync1/DTCRAFTiter04.xml")

# initialData = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_sync1/DTCRAFTiter04.xml")
# finalData = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_sync1/DTCRAFTiter05.xml")

initialData = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/internalDTalignment_correct.xml")
finalData = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_sync1/DTCRAFTiter03.xml")

initialData = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_sync1/DTCRAFTiter03.xml")
finalData = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_sync1/MillePede.xml")
execfile("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_sync1/DTCRAFTiter03_report.py")



initialData = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_sync1_realtracker/DTCRAFTiter03.xml")
finalData = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_sync1/DTCRAFTiter03.xml")
finalData = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/V4alignment.xml")
finalData = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/V11alignment.xml")
finalData = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_sync1_realtracker_ignoreSL2/STATSiter13.xml")
execfile("/home/jpivarski/work/results/final_stats_check/STATSiter13_report.py")

execfile("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_sync1_realtracker/DTCRAFTiter03_report.py")
execfile("previously_aligned.py")

for r in reports:
    if r.status == "FAIL":
        print r.postal_address




# initialData = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/internalDTalignment_correct.xml")
# finalData = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_sync1_w2bin/DTCRAFTiter01.xml")

# initialData = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_sync1_w2bin/DTCRAFTiter01.xml")
# finalData = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_sync1_w2bin/DTCRAFTiter02.xml")

# initialData = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_sync1_w2bin/DTCRAFTiter02.xml")
# finalData = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_sync1_w2bin/DTCRAFTiter03.xml")

# initialData = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_sync1/DTCRAFTiter03.xml")
# finalData = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_sync1_w2bin/DTCRAFTiter03.xml")

# execfile("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_sync1_w2bin/DTCRAFTiter03_report.py")

initialData = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_sync1_realtracker/DTCRAFTiter03.xml")
finalData = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_sync1_realtracker-1/DTCRAFTiter03.xml")
finalData = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_sync1/DTCRAFTiter03.xml")
execfile("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_sync1_realtracker/DTCRAFTiter03_report.py")


initialData = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_sync1_realtracker/DTCRAFTiter03.xml")
initialData = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_sync1/DTCRAFTiter03.xml")
finalData = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_sync1_realtrackerAPE/DTCRAFTiter03.xml")
execfile("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_sync1_realtracker/DTCRAFTiter03_report.py")

tdrStyle.SetOptStat("mrou")
tdrStyle.SetStatW(0.40)
tdrStyle.SetStatFontSize(0.05)

histograms = {}
for param in "x", "y", "z", "phix", "phiy", "phiz":
    for region in 1, 2, 3, 4, 5:
        histograms[param + str(region)] = ROOT.TH1F("h" + param + str(region), "", 50, -15, 15.)

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
    if r.status == "PASS":
        if r.postal_address[0] == "DT":  # and r.postal_address[2] != 4:
            initial = initialData.dt[r.postal_address[1:]]
            final = finalData.dt[r.postal_address[1:]]
        else: continue

#         if r.postal_address in previously_aligned:
#             if r.deltax is not None and r.deltax.error != 0.: fill("x", r, (final.x - initial.x)*10.)
#             if r.deltaphiz is not None and r.deltaphiz.error != 0.: fill("phiz", r, (final.phiz - initial.phiz)*1000.)

#         if r.postal_address in previously_aligned_iny:
#             if r.deltay is not None and r.deltay.error != 0.: fill("y", r, (final.y - initial.y)*10.)

#         if False:
#             if r.deltaz is not None and r.deltaz.error != 0.: fill("z", r, (final.z - initial.z)*10.)
#             if r.deltaphix is not None and r.deltaphix.error != 0.: fill("phix", r, (final.phix - initial.phix)*1000.)
#             if r.deltaphiy is not None and r.deltaphiy.error != 0.: fill("phiy", r, (final.phiy - initial.phiy)*1000.)

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
c1.GetPad(1).cd(); draw("x", "Local x alignment difference (mm)")
tlegend = ROOT.TLegend(0.17, 0.55+0.15, 0.45, 0.98)
tlegend.SetFillColor(ROOT.kWhite)
tlegend.SetBorderSize(1)
# tlegend.AddEntry(histograms["x5"], " wheel +2", "f")
tlegend.AddEntry(histograms["x4"], " wheel +1", "f")
tlegend.AddEntry(histograms["x3"], " wheel 0", "f")
tlegend.AddEntry(histograms["x2"], " wheel -1", "f")
# tlegend.AddEntry(histograms["x1"], " wheel -2", "f")
tlegend.SetTextSize(0.05)
tlegend.Draw()
c1.GetPad(2).cd(); draw("y", "Local y alignment difference (mm)")
c1.GetPad(3).cd(); draw("z", "Local z alignment difference (mm)")
c1.GetPad(4).cd(); draw("phix", "Local #phi_{x} alignment difference (mrad)")
c1.GetPad(5).cd(); draw("phiy", "Local #phi_{y} alignment difference (mrad)")
c1.GetPad(6).cd(); draw("phiz", "Local #phi_{z} alignment difference (mrad)")

c1.SaveAs("hip_finaltrackerAPEdiff.pdf")

c1.SaveAs("hip_tracker_difference.pdf")
c1.SaveAs("hip_millepede_difference.pdf")
# c1.SaveAs("hip_2bin_difference.pdf")
# c1.SaveAs("hip_difference_v11all.pdf")
c1.SaveAs("hip_difference_v11all.pdf")
# c1.SaveAs("hip_difference_v4.pdf")

execfile("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_sync1_realtracker/DTCRAFTiter03_report.py")
realtracker_reports = reports
execfile("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_sync1/DTCRAFTiter03_report.py")

h = ROOT.TH1F("h", "", 100, 0, 2)
for realr, r in zip(realtracker_reports, reports):
    if realr.postal_address != r.postal_address: raise Exception
    if realr.status == "PASS":
        h.Fill(float(realr.posNum) / float(r.posNum))
h.SetXTitle("N(tracks with new tracker)/N(tracks with V11 tracker)")
h.GetXaxis().CenterTitle()
h.SetFillColor(ROOT.kBlue-10)
h.Draw()

############################

tdrStyle.SetOptStat("mrou")
tdrStyle.SetStatW(0.40)
tdrStyle.SetStatFontSize(0.05)

histograms = {}
for param in "x", "y", "z", "phix", "phiy", "phiz":
    for region in 1, 2, 3, 4:
        histograms[param + str(region)] = ROOT.TH1F("h" + param + str(region), "", 50, -15, 15.)

def fill(param, r, value):
    if r.postal_address[0] == "DT":
        if r.postal_address[2] == 1: region = 1
        elif r.postal_address[2] == 2: region = 2
        elif r.postal_address[2] == 3: region = 3
        elif r.postal_address[2] == 4: region = 4

        for reg in range(region, 5):
            histograms[param + str(reg)].Fill(value)

for r in reports:
    if r.status == "PASS":
        if r.postal_address[0] == "DT":  #  and r.postal_address[2] != 4:
            initial = initialData.dt[r.postal_address[1:]]
            final = finalData.dt[r.postal_address[1:]]
        else: continue

#         if r.postal_address in previously_aligned:
#             if r.deltax is not None and r.deltax.error != 0.: fill("x", r, (final.x - initial.x)*10.)
#             if r.deltaphiz is not None and r.deltaphiz.error != 0.: fill("phiz", r, (final.phiz - initial.phiz)*1000.)

#         if r.postal_address in previously_aligned_iny:
#             if r.deltay is not None and r.deltay.error != 0.: fill("y", r, (final.y - initial.y)*10.)

#         if False:
#             if r.deltaz is not None and r.deltaz.error != 0.: fill("z", r, (final.z - initial.z)*10.)
#             if r.deltaphix is not None and r.deltaphix.error != 0.: fill("phix", r, (final.phix - initial.phix)*1000.)
#             if r.deltaphiy is not None and r.deltaphiy.error != 0.: fill("phiy", r, (final.phiy - initial.phiy)*1000.)

        if r.deltax is not None and r.deltax.error != 0.: fill("x", r, (final.x - initial.x)*10.)
        if r.deltay is not None and r.deltay.error != 0.: fill("y", r, (final.y - initial.y)*10.)
        if r.deltaz is not None and r.deltaz.error != 0.: fill("z", r, (final.z - initial.z)*10.)
        if r.deltaphix is not None and r.deltaphix.error != 0.: fill("phix", r, (final.phix - initial.phix)*1000.)
        if r.deltaphiy is not None and r.deltaphiy.error != 0.: fill("phiy", r, (final.phiy - initial.phiy)*1000.)
        if r.deltaphiz is not None and r.deltaphiz.error != 0.: fill("phiz", r, (final.phiz - initial.phiz)*1000.)

def draw(param, title):
    histograms[param + str(4)].SetFillColor(ROOT.kGray+3)
    histograms[param + str(3)].SetFillColor(ROOT.kGray+2)
    histograms[param + str(2)].SetFillColor(ROOT.kGray+1)
    histograms[param + str(1)].SetFillColor(ROOT.kGray)

    histograms[param + str(4)].SetXTitle(title)
    histograms[param + str(4)].GetXaxis().CenterTitle()

    histograms[param + str(4)].Draw()
    histograms[param + str(3)].Draw("same")
    histograms[param + str(2)].Draw("same")
    histograms[param + str(1)].Draw("same")

c1.Clear()
c1.Divide(3, 2)
c1.GetPad(1).cd(); draw("x", "Local x alignment difference (mm)")
tlegend = ROOT.TLegend(0.17, 0.55+0.05, 0.45, 0.98)
tlegend.SetFillColor(ROOT.kWhite)
tlegend.SetBorderSize(1)
tlegend.AddEntry(histograms["x4"], " station 4", "f")
tlegend.AddEntry(histograms["x3"], " station 3", "f")
tlegend.AddEntry(histograms["x2"], " station 2", "f")
tlegend.AddEntry(histograms["x1"], " station 1", "f")
tlegend.SetTextSize(0.05)
tlegend.Draw()
c1.GetPad(2).cd(); draw("y", "Local y alignment difference (mm)")
c1.GetPad(3).cd(); draw("z", "Local z alignment difference (mm)")
c1.GetPad(4).cd(); draw("phix", "Local #phi_{x} alignment difference (mrad)")
c1.GetPad(5).cd(); draw("phiy", "Local #phi_{y} alignment difference (mrad)")
c1.GetPad(6).cd(); draw("phiz", "Local #phi_{z} alignment difference (mrad)")

c1.SaveAs("hip_tracker_difference2.pdf")
c1.SaveAs("hip_millepede_difference2.pdf")
c1.SaveAs("hip_difference2_v11all.pdf")
# c1.SaveAs("hip_difference2_v11.pdf")
# c1.SaveAs("hip_difference2_v4.pdf")

############################

tdrStyle.SetOptStat("")
tdrStyle.SetStatW(0.40)
tdrStyle.SetStatFontSize(0.05)
# mc0 = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/testpattern.xml")
# mc1 = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/DTMC1_sync1/DTMCiter01.xml")
# mc2 = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/DTMC1_sync1/DTMCiter02.xml")
# mc3 = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/DTMC1_sync1/DTMCiter03.xml")
# execfile("/home/jpivarski/work/results/CRAFTchambers2/DTMC1_sync1/DTMCiter03_report.py")
mc0 = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/randominitial.xml")
mc1 = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/DTMC1_sync1_fullyrandom/DTMCiter01.xml")
mc2 = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/DTMC1_sync1_fullyrandom/DTMCiter02.xml")
mc3 = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/DTMC1_sync1_fullyrandom/DTMCiter03.xml")
execfile("/home/jpivarski/work/results/CRAFTchambers2/DTMC1_sync1_fullyrandom/DTMCiter03_report.py")

# a really hacky way to add the Millepede results
# mc2 = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/Alignments6DegNueva.xml") # not the right ones
# mc2 = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/IDEAL_V12_IdealTK-B_RandomScenario_3it.xml")
# mc2 = MuonGeometry("/tmp/tmp.xml")
mc2 = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/MP_MonteCarlo_2p0.xml")

histograms = {}
for param in "x", "y", "z":
    for iteration in range(5):
        histograms[param + str(iteration)] = ROOT.TH1F("h" + param + str(iteration), "", 50, -10, 10.)
for param in "phix", "phiy", "phiz":
    for iteration in range(5):
        histograms[param + str(iteration)] = ROOT.TH1F("h" + param + str(iteration), "", 50, -5, 5.)

for r in reports:
    if r.status == "PASS":
        position = {}
        if r.postal_address[0] == "DT":
            position[0] = mc0.dt[r.postal_address[1:]]
            position[1] = mc1.dt[r.postal_address[1:]]
            position[2] = mc2.dt[r.postal_address[1:]]
            position[3] = mc3.dt[r.postal_address[1:]]
        elif r.postal_address[0] == "CSC":
            position[0] = mc0.csc[r.postal_address[1:]]
            position[1] = mc1.csc[r.postal_address[1:]]
            position[2] = mc2.csc[r.postal_address[1:]]
            position[3] = mc3.csc[r.postal_address[1:]]
        for param in "x", "y", "z":
            for iteration in range(4):
                if r.__dict__["delta" + param] is not None and r.__dict__["delta" + param].error != 0.:
                    histograms[param + str(iteration)].Fill(position[iteration].__dict__[param]*10.)
        for param in "phix", "phiy", "phiz":
            for iteration in range(4):
                if r.__dict__["delta" + param] is not None and r.__dict__["delta" + param].error != 0.:
                    histograms[param + str(iteration)].Fill(position[iteration].__dict__[param]*1000.)

def draw(param, title):
    histograms[param + str(0)].SetFillColor(ROOT.kMagenta+2)
    histograms[param + str(1)].SetFillColor(ROOT.kYellow-4)
    histograms[param + str(2)].SetFillColor(ROOT.kGreen-3)
    histograms[param + str(3)].SetFillColor(ROOT.kCyan+2)
#     histograms[param + str(4)].SetFillColor(ROOT.kBlue-8)

    histograms[param + str(3)].SetXTitle(title)
    histograms[param + str(3)].GetXaxis().CenterTitle()

    histograms[param + str(3)].Draw()
    histograms[param + str(0)].Draw("same")
    histograms[param + str(1)].Draw("same")
    histograms[param + str(2)].Draw("same")
    histograms[param + str(3)].Draw("same")
#     histograms[param + str(4)].Draw("same")

c1.Clear()
c1.Divide(3, 2)
c1.GetPad(1).cd(); draw("x", "Local x accuracy (mm)")
tlegend = ROOT.TLegend(0.17, 0.55, 0.45, 0.98)
tlegend.SetFillColor(ROOT.kWhite)
tlegend.SetBorderSize(1)
tlegend.AddEntry(histograms["x0"], " initial", "f")
tlegend.AddEntry(histograms["x1"], " iter 1", "f")
tlegend.AddEntry(histograms["x2"], " iter 2", "f")
tlegend.AddEntry(histograms["x3"], " iter 3", "f")
tlegend.Draw()
c1.GetPad(2).cd(); draw("y", "Local y accuracy (mm)")
c1.GetPad(3).cd(); draw("z", "Local z accuracy (mm)")
c1.GetPad(4).cd(); draw("phix", "Local #phi_{x} accuracy (mrad)")
c1.GetPad(5).cd(); draw("phiy", "Local #phi_{y} accuracy (mrad)")
c1.GetPad(6).cd(); draw("phiz", "Local #phi_{z} accuracy (mrad)")

c1.SaveAs("hip_MC.pdf")

histcopies = []
def draw(param, title, title2):
    histcopies.append(histograms[param + str(2)].Clone())
    histcopies[-1].SetLineStyle(2)

    histograms[param + str(0)].SetFillColor(ROOT.kMagenta-2)
    histograms[param + str(3)].SetFillColor(ROOT.kYellow)
    histograms[param + str(2)].SetFillColor(ROOT.kRed-7)

    histograms[param + str(3)].SetXTitle(title)
    histograms[param + str(3)].GetXaxis().CenterTitle()

    histograms[param + str(3)].SetYTitle(title2)
    histograms[param + str(3)].GetYaxis().CenterTitle()

    histograms[param + str(3)].Draw()
    histograms[param + str(0)].Draw("same")
    histograms[param + str(2)].Draw("same")
    histograms[param + str(3)].Draw("same")
    histcopies[-1].Draw("same")

def draw(param, title, title2):
    histcopies.append(histograms[param + str(0)].Clone())
    histcopies[-1].SetLineStyle(2)

    histograms[param + str(0)].SetFillColor(ROOT.kMagenta-2)
    histograms[param + str(3)].SetFillColor(ROOT.kYellow)
    histograms[param + str(2)].SetFillColor(ROOT.kRed-7)

    histograms[param + str(3)].SetXTitle(title)
    histograms[param + str(3)].GetXaxis().CenterTitle()

    histograms[param + str(3)].SetYTitle(title2)
    histograms[param + str(3)].GetYaxis().CenterTitle()

    histograms[param + str(3)].Draw()
    histograms[param + str(0)].Draw("same")
    histograms[param + str(3)].Draw("same")
    histcopies[-1].Draw("same")

histograms["x3"].SetAxisRange(0, 70, "Y")
histograms["y3"].SetAxisRange(0, 23, "Y")
histograms["z3"].SetAxisRange(0, 28, "Y")
histograms["phix3"].SetAxisRange(0, 22, "Y")
histograms["phiy3"].SetAxisRange(0, 65, "Y")
histograms["phiz3"].SetAxisRange(0, 45, "Y")

c1.Clear()
c1.Divide(3, 2)
c1.GetPad(1).cd(); draw("x", "x^{aligned} - x^{true} (mm)", "Chambers/0.4 mm")
c1.GetPad(2).cd(); draw("y", "y^{aligned} - y^{true} (mm)", "Chambers/0.4 mm")
c1.GetPad(3).cd(); draw("z", "z^{aligned} - z^{true} (mm)", "Chambers/0.4 mm")
tlegend = ROOT.TLegend(0.55, 0.55+0.2, 0.98, 0.98)
tlegend.SetFillColor(ROOT.kWhite)
tlegend.SetBorderSize(1)
# tlegend.AddEntry(histograms["z3"], " Reference-Target", "f")
# tlegend.AddEntry(histograms["z2"], " Millepede", "f")
# tlegend.AddEntry(histograms["z0"], " unaligned", "f")
tlegend.AddEntry(histograms["z3"], " aligned MC", "f")
tlegend.AddEntry(histograms["z0"], " unaligned MC", "f")
tlegend.Draw()
c1.GetPad(4).cd(); draw("phix", "#phi_{x}^{aligned} - #phi_{x}^{true} (mrad)", "Chambers/0.2 mrad")
c1.GetPad(5).cd(); draw("phiy", "#phi_{y}^{aligned} - #phi_{y}^{true} (mrad)", "Chambers/0.2 mrad")
c1.GetPad(6).cd(); draw("phiz", "#phi_{z}^{aligned} - #phi_{z}^{true} (mrad)", "Chambers/0.2 mrad")

c1.SaveAs("hip_MC_simple2.pdf")
c1.SaveAs("MCcomparison_hip_Millepede.pdf")

print "$x$ &", histograms["x3"].GetMean()*1000., "&", histograms["x3"].GetRMS(), "&", histograms["x2"].GetMean()*1000., "&", histograms["x2"].GetRMS()
print "$y$ &", histograms["y3"].GetMean()*1000., "&", histograms["y3"].GetRMS(), "&", histograms["y2"].GetMean()*1000., "&", histograms["y2"].GetRMS()
print "$z$ &", histograms["z3"].GetMean()*1000., "&", histograms["z3"].GetRMS(), "&", histograms["z2"].GetMean()*1000., "&", histograms["z2"].GetRMS()
print "$\\phi_x$", histograms["phix3"].GetMean()*1000., "&", histograms["phix3"].GetRMS(), "&", histograms["phix2"].GetMean()*1000., "&", histograms["phix2"].GetRMS()
print "$\\phi_y$", histograms["phiy3"].GetMean()*1000., "&", histograms["phiy3"].GetRMS(), "&", histograms["phiy2"].GetMean()*1000., "&", histograms["phiy2"].GetRMS()
print "$\\phi_z$", histograms["phiz3"].GetMean()*1000., "&", histograms["phiz3"].GetRMS(), "&", histograms["phiz2"].GetMean()*1000., "&", histograms["phiz2"].GetRMS()

# x 0.19227642693 0.531488741209
# y 0.840959320335 1.09140023684
# z 0.629510331093 2.86186997265
# phix 0.416977942171 1.23114390145
# phiy 0.0948276256709 1.00824368096
# phiz 0.287431085615 1.20139131613

# x 0.00306399444444 0.19227642693 -0.00467578412698 0.531488741209
# y 0.0354857633333 0.840959320335 0.0528892033333 1.09140023684
# z 0.0510387077778 0.629510331093 -0.181841272222 2.86186997265
# phix 0.0396768888889 0.416977942171 0.00197818181818 1.23114390145
# phiy 0.00135968253968 0.0948276256709 -0.00576182539683 1.00824368096
# phiz 0.014495952381 0.287431085615 6.16e-05 1.20139131613

print "\\textcolor{blue}{\\bf %.3f} & \\textcolor{blue}{\\bf %.3f} & \\textcolor{blue}{\\bf %.3f} & \\textcolor{blue}{\\bf %.3f} & \\textcolor{blue}{\\bf %.3f} & \\textcolor{blue}{\\bf %.3f} \\\\" % (histograms["x2"].GetRMS(), histograms["y2"].GetRMS(), histograms["z2"].GetRMS(), histograms["phix2"].GetRMS(), histograms["phiy2"].GetRMS(), histograms["phiz2"].GetRMS())


############################

tdrStyle.SetOptStat("mr")
mc0 = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/testpattern.xml")
mc1 = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/DTMC1_sync1/DTMCiter01.xml")
mc2 = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/DTMC1_sync1/DTMCiter02.xml")
mc3 = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/DTMC1_sync1/DTMCiter03.xml")
execfile("/home/jpivarski/work/results/CRAFTchambers2/DTMC1_sync1/DTMCiter03_report.py")

histograms = {}
for param in "x", "y", "z", "phix", "phiy", "phiz":
    for iteration in range(5):
        histograms[param + str(iteration)] = ROOT.TH1F("h" + param + str(iteration), "", 50, -10, 10.)

for r in reports:
    if r.status == "PASS":
        position = {}
        if r.postal_address[0] == "DT":
            position[0] = mc0.dt[r.postal_address[1:]]
            position[1] = mc1.dt[r.postal_address[1:]]
            position[2] = mc2.dt[r.postal_address[1:]]
            position[3] = mc3.dt[r.postal_address[1:]]
        elif r.postal_address[0] == "CSC":
            position[0] = mc0.csc[r.postal_address[1:]]
            position[1] = mc1.csc[r.postal_address[1:]]
            position[2] = mc2.csc[r.postal_address[1:]]
            position[3] = mc3.csc[r.postal_address[1:]]
        for param in "x", "y", "z":
            for iteration in range(4):
                if r.__dict__["delta" + param] is not None and r.__dict__["delta" + param].error != 0.:
                    histograms[param + str(iteration)].Fill(position[iteration].__dict__[param] / r.__dict__["delta" + param].error)
        for param in "phix", "phiy", "phiz":
            for iteration in range(4):
                if r.__dict__["delta" + param] is not None and r.__dict__["delta" + param].error != 0.:
                    histograms[param + str(iteration)].Fill(position[iteration].__dict__[param] / r.__dict__["delta" + param].error)

def draw(param, title):
    histograms[param + str(0)].SetFillColor(ROOT.kMagenta+2)
    histograms[param + str(1)].SetFillColor(ROOT.kYellow-4)
    histograms[param + str(2)].SetFillColor(ROOT.kGreen-3)
    histograms[param + str(3)].SetFillColor(ROOT.kCyan+2)
#     histograms[param + str(4)].SetFillColor(ROOT.kBlue-8)

    histograms[param + str(3)].SetXTitle(title)
    histograms[param + str(3)].GetXaxis().CenterTitle()

    histograms[param + str(3)].Draw()
    histograms[param + str(0)].Draw("same")
    histograms[param + str(1)].Draw("same")
    histograms[param + str(2)].Draw("same")
    histograms[param + str(3)].Draw("same")
#     histograms[param + str(4)].Draw("same")

c1.Clear()
c1.Divide(3, 2)
c1.GetPad(1).cd(); draw("x", "Normalized local x (sigmas)")
tlegend = ROOT.TLegend(0.17, 0.55, 0.45, 0.98)
tlegend.SetFillColor(ROOT.kWhite)
tlegend.SetBorderSize(1)
tlegend.AddEntry(histograms["x0"], " initial", "f")
tlegend.AddEntry(histograms["x1"], " iter 1", "f")
tlegend.AddEntry(histograms["x2"], " iter 2", "f")
tlegend.AddEntry(histograms["x3"], " iter 3", "f")
tlegend.Draw()
c1.GetPad(2).cd(); draw("y", "Normalized local y (sigmas)")
c1.GetPad(3).cd(); draw("z", "Normalized local z (sigmas)")
c1.GetPad(4).cd(); draw("phix", "Normalized local #phi_{x} (sigmas)")
c1.GetPad(5).cd(); draw("phiy", "Normalized local #phi_{y} (sigmas)")
c1.GetPad(6).cd(); draw("phiz", "Normalized local #phi_{z} (sigmas)")

c1.SaveAs("hip_MCnorm.pdf")

##################################

tdrStyle.SetOptStat("mro")
tdrStyle.SetStatW(0.40)
tdrStyle.SetStatFontSize(0.05)

execfile("/home/jpivarski/work/results/CRAFTchambers2/DTMC1_sync1/DTMCiter03_report.py")

hx = ROOT.TH1F("hx", "", 20, 0., 3.)
hy = ROOT.TH1F("hy", "", 20, 0., 6.)
hz = ROOT.TH1F("hz", "", 20, 0., 6.)
hphix = ROOT.TH1F("hphix", "", 20, 0., 3.)
hphiy = ROOT.TH1F("hphiy", "", 20, 0., 3.)
hphiz = ROOT.TH1F("hphiz", "", 20, 0., 3.)

for r in reports:
    if r.status == "PASS":
        if r.deltax is not None and r.deltax.error != 0.: hx.Fill(r.deltax.error*10.)
        if r.deltay is not None and r.deltay.error != 0.: hy.Fill(r.deltay.error*10.)
        if r.deltaz is not None and r.deltaz.error != 0.: hz.Fill(r.deltaz.error*10.)
        if r.deltaphix is not None and r.deltaphix.error != 0.: hphix.Fill(r.deltaphix.error*1000.)
        if r.deltaphiy is not None and r.deltaphiy.error != 0.: hphiy.Fill(r.deltaphiy.error*1000.)
        if r.deltaphiz is not None and r.deltaphiz.error != 0.: hphiz.Fill(r.deltaphiz.error*1000.)

hx.SetXTitle("Local x uncertainty (mm)")
hy.SetXTitle("Local y uncertainty (mm)")
hz.SetXTitle("Local z uncertainty (mm)")
hphix.SetXTitle("Local #phi_{x} uncertainty (mrad)")
hphiy.SetXTitle("Local #phi_{y} uncertainty (mrad)")
hphiz.SetXTitle("Local #phi_{z} uncertainty (mrad)")
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

##################################

tdrStyle.SetOptStat("mro")
tdrStyle.SetStatW(0.40)
tdrStyle.SetStatFontSize(0.05)

mc3 = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/DTMC1_sync1/DTMCiter03.xml")
execfile("/home/jpivarski/work/results/CRAFTchambers2/DTMC1_sync1/DTMCiter03_report.py")

Hx = ROOT.TH1F("Hx", "", 20, 0., 3.)
Hy = ROOT.TH1F("Hy", "", 20, 0., 6.)
Hz = ROOT.TH1F("Hz", "", 20, 0., 6.)
Hphix = ROOT.TH1F("Hphix", "", 20, 0., 3.)
Hphiy = ROOT.TH1F("Hphiy", "", 20, 0., 3.)
Hphiz = ROOT.TH1F("Hphiz", "", 20, 0., 3.)

for r in reports:
    if r.status == "PASS":
        position = mc3.dt[r.postal_address[1:]]

        if r.deltax is not None and r.deltax.error != 0.:
            if r.deltax.error < abs(position.x): Hx.Fill(sqrt(position.x**2 - r.deltax.error**2)*10.)
            else: hx.Fill(0.)
        if r.deltay is not None and r.deltay.error != 0.:
            if r.deltay.error < abs(position.y): Hy.Fill(sqrt(position.y**2 - r.deltay.error**2)*10.)
            else: hy.Fill(0.)
        if r.deltaz is not None and r.deltaz.error != 0.:
            if r.deltaz.error < abs(position.z): Hz.Fill(sqrt(position.z**2 - r.deltaz.error**2)*10.)
            else: hz.Fill(0.)
        if r.deltaphix is not None and r.deltaphix.error != 0.:
            if r.deltaphix.error < abs(position.phix): Hphix.Fill(sqrt(position.phix**2 - r.deltaphix.error**2)*1000.)
            else: hphix.Fill(0.)
        if r.deltaphiy is not None and r.deltaphiy.error != 0.:
            if r.deltaphiy.error < abs(position.phiy): Hphiy.Fill(sqrt(position.phiy**2 - r.deltaphiy.error**2)*1000.)
            else: hphiy.Fill(0.)
        if r.deltaphiz is not None and r.deltaphiz.error != 0.:
            if r.deltaphiz.error < abs(position.phiz): Hphiz.Fill(sqrt(position.phiz**2 - r.deltaphiz.error**2)*1000.)
            else: hphiz.Fill(0.)

Hx.SetXTitle("Local x systematic uncertainty (mm)")
Hy.SetXTitle("Local y systematic uncertainty (mm)")
Hz.SetXTitle("Local z systematic uncertainty (mm)")
Hphix.SetXTitle("Local #phi_{x} systematic uncertainty (mrad)")
Hphiy.SetXTitle("Local #phi_{y} systematic uncertainty (mrad)")
Hphiz.SetXTitle("Local #phi_{z} systematic uncertainty (mrad)")
Hx.GetXaxis().CenterTitle()
Hy.GetXaxis().CenterTitle()
Hz.GetXaxis().CenterTitle()
Hphix.GetXaxis().CenterTitle()
Hphiy.GetXaxis().CenterTitle()
Hphiz.GetXaxis().CenterTitle()
Hx.SetFillColor(ROOT.kYellow)
Hy.SetFillColor(ROOT.kYellow)
Hz.SetFillColor(ROOT.kYellow)
Hphix.SetFillColor(ROOT.kYellow)
Hphiy.SetFillColor(ROOT.kYellow)
Hphiz.SetFillColor(ROOT.kYellow)

h2x = hx.Clone()
h2y = hy.Clone()
h2z = hz.Clone()
h2phix = hphix.Clone()
h2phiy = hphiy.Clone()
h2phiz = hphiz.Clone()
h2x.SetFillColor(0)
h2y.SetFillColor(0)
h2z.SetFillColor(0)
h2phix.SetFillColor(0)
h2phiy.SetFillColor(0)
h2phiz.SetFillColor(0)
h2x.SetLineStyle(2)
h2y.SetLineStyle(2)
h2z.SetLineStyle(2)
h2phix.SetLineStyle(2)
h2phiy.SetLineStyle(2)
h2phiz.SetLineStyle(2)

c1.Clear()
c1.Divide(3, 2)
c1.GetPad(1).cd(); Hx.Draw()
c1.GetPad(2).cd(); Hy.Draw()
c1.GetPad(3).cd(); Hz.Draw()
c1.GetPad(4).cd(); Hphix.Draw()
c1.GetPad(5).cd(); Hphiy.Draw()
c1.GetPad(6).cd(); Hphiz.Draw()

c1.Clear()
c1.Divide(3, 2)
c1.GetPad(1).cd(); hx.Draw(); Hx.Draw("same"); h2x.Draw("same")
tlegend = ROOT.TLegend(0.6, 0.53, 0.98, 0.72)
tlegend.SetFillColor(ROOT.kWhite)
tlegend.SetBorderSize(1)
tlegend.AddEntry(hx, " statistical", "f")
tlegend.AddEntry(Hx, " systematic", "f")
tlegend.Draw()
c1.GetPad(2).cd(); hy.Draw(); Hy.Draw("same"); h2y.Draw("same")
c1.GetPad(3).cd(); hz.Draw(); Hz.Draw("same"); h2z.Draw("same")
c1.GetPad(4).cd(); hphix.Draw(); Hphix.Draw("same"); h2phix.Draw("same")
c1.GetPad(5).cd(); hphiy.Draw(); Hphiy.Draw("same"); h2phiy.Draw("same")
c1.GetPad(6).cd(); hphiz.Draw(); Hphiz.Draw("same"); h2phiz.Draw("same")
c1.SaveAs("hip_MCuncertainties.pdf")

##################################

tdrStyle.SetOptStat("mro")
tdrStyle.SetStatW(0.40)
tdrStyle.SetStatFontSize(0.05)

execfile("/home/jpivarski/work/results/CRAFTchambers2/DTMC1_sync1/DTMCiter03_report.py")
mcreports = reports
execfile("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_sync1/DTCRAFTiter03_report.py")
datareports = reports

hx = ROOT.TH1F("hx", "", 20, 0., 3.)
hy = ROOT.TH1F("hy", "", 20, 0., 6.)
hz = ROOT.TH1F("hz", "", 20, 0., 6.)
hphix = ROOT.TH1F("hphix", "", 20, 0., 3.)
hphiy = ROOT.TH1F("hphiy", "", 20, 0., 3.)
hphiz = ROOT.TH1F("hphiz", "", 20, 0., 3.)

for r in datareports:
    for r2 in mcreports:
        if r2.postal_address == r.postal_address: break

    if r2.postal_address == r.postal_address and r.status == "PASS" and r2.status == "PASS":
        if r.deltax is not None and r.deltax.error != 0.: hx.Fill(r.deltax.error / r2.deltax.error)
        if r.deltay is not None and r.deltay.error != 0.: hy.Fill(r.deltay.error / r2.deltay.error)
        if r.deltaz is not None and r.deltaz.error != 0.: hz.Fill(r.deltaz.error / r2.deltaz.error)
        if r.deltaphix is not None and r.deltaphix.error != 0.: hphix.Fill(r.deltaphix.error / r2.deltaphix.error)
        if r.deltaphiy is not None and r.deltaphiy.error != 0.: hphiy.Fill(r.deltaphiy.error / r2.deltaphiy.error)
        if r.deltaphiz is not None and r.deltaphiz.error != 0.: hphiz.Fill(r.deltaphiz.error / r2.deltaphiz.error)

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

##############################################

good_alignment = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_sync1_realtracker/DTCRAFTiter03.xml")
v4_alignment = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/V4alignment.xml")
v11_alignment = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/V11alignment.xml")

execfile("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_sync1_realtracker/DTCRAFTiter03_report.py")
execfile("previously_aligned.py")

def sorter(a, b):
    out = cmp(a.postal_address[1], b.postal_address[1])
    if out == 0:
        out = cmp(a.postal_address[2], b.postal_address[2])
    if out == 0:
        out = cmp(a.postal_address[3], b.postal_address[3])
    return out

reports.sort(sorter)

for r in reports:
    if r.postal_address[0] == "DT":
        good = good_alignment.dt[r.postal_address[1:]]
        v4 = v4_alignment.dt[r.postal_address[1:]]
        v11 = v11_alignment.dt[r.postal_address[1:]]

        print "%d, %d, %d & " % r.postal_address[1:],

        print "%03.2f,"%(v4.x*10.), " ", "%03.2f,"%(v4.y*10.), " ", "%03.2f,"%(v4.z*10.), " ", "%03.2f,"%(v4.phix*1000.), " ", "%03.2f,"%(v4.phiy*1000.), " ", "%03.2f,"%(v4.phiz*1000.), " & ",

        if r.postal_address in previously_aligned and r.postal_address in previously_aligned_iny:
            print "%03.2f,"%(v11.x*10.), " ", "%03.2f,"%(v11.y*10.), " ", "%03.2f,"%(v11.phiz*1000.), " & ", 
        elif r.postal_address in previously_aligned and r.postal_address not in previously_aligned_iny:
            print "%03.2f,"%(v11.x*10.), " ", "{\it (%03.2f),}"%(v11.y*10.), " ", "%03.2f,"%(v11.phiz*1000.), " & ", 
        elif r.postal_address not in previously_aligned and r.postal_address in previously_aligned_iny:
            print "{\it (%03.2f),}"%(v11.x*10.), " ", "%03.2f,"%(v11.y*10.), " ", "{\it (%03.2f),}"%(v11.phiz*1000.), " & ", 
        else:
            print "{\it (%03.2f),}"%(v11.x*10.), " ", "{\it (%03.2f),}"%(v11.y*10.), " ", "{\it (%03.2f),}"%(v11.phiz*1000.), " & ", 

        if r.status == "PASS":
            print "%03.2f,"%(good.x*10.), " ", "%03.2f,"%(good.y*10.), " ", "%03.2f,"%(good.z*10.), " ", "%03.2f,"%(good.phix*1000.), " ", "%03.2f,"%(good.phiy*1000.), " ", "%03.2f,"%(good.phiz*1000.), " \\\\"
        else:
            print "{\it (%03.2f,}"%(good.x*10.), " ", "{\it %03.2f,}"%(good.y*10.), " ", "{\it %03.2f,}"%(good.z*10.), " ", "{\it %03.2f,}"%(good.phix*1000.), " ", "{\it %03.2f,}"%(good.phiy*1000.), " ", "{\it %03.2f),}"%(good.phiz*1000.), " \\\\"

##############################################

mcscenario = MuonGeometry("/home/jpivarski/work/cmssw_test/new_startup_scenario2009/CMSSW_2_1_7/src/MCScenario_CRAFT1_22X_CHECKME.xml")

tdrStyle.SetOptStat("mrou")
tdrStyle.SetStatW(0.40)
tdrStyle.SetStatFontSize(0.05)

histograms = {}
for param in "x", "y", "z", "phix", "phiy", "phiz":
    for region in 1, 2, 3:
        histograms[param + str(region)] = ROOT.TH1F("h" + param + str(region), "", 50, -15, 15.)

def fill(param, region, value):
    for reg in range(region, 3+1):
        histograms[param + str(reg)].Fill(value)

for wheel in -2, -1, 0, 1, 2:
    for station in 1, 2, 3, 4:
        if station == 4: nsectors = 14
        else: nsectors = 12
        for sector in range(1, nsectors+1):
            if wheel in (-1, 0, 1) and sector not in (1, 7): region = 1
            else: region = 2

            fill("x", region, mcscenario.dt[wheel, station, sector].x*10.)
            fill("y", region, mcscenario.dt[wheel, station, sector].y*10.)
            fill("z", region, mcscenario.dt[wheel, station, sector].z*10.)
            fill("phix", region, mcscenario.dt[wheel, station, sector].phix*1000.)
            fill("phiy", region, mcscenario.dt[wheel, station, sector].phiy*1000.)
            fill("phiz", region, mcscenario.dt[wheel, station, sector].phiz*1000.)

for endcap in 1, 2:
    for (station, ring) in ((1, 1), (1, 2), (1, 3), (1, 4), (2, 1), (2, 2), (3, 1), (3, 2), (4, 1)):
        if (station, ring) in ((2, 1), (3, 1), (4, 1)): nchambers = 18
        else: nchambers = 36
        for chamber in range(1, nchambers+1):
            fill("x", 3, mcscenario.csc[endcap, station, ring, chamber].x*10.)
            fill("y", 3, mcscenario.csc[endcap, station, ring, chamber].y*10.)
            fill("z", 3, mcscenario.csc[endcap, station, ring, chamber].z*10.)
            fill("phix", 3, mcscenario.csc[endcap, station, ring, chamber].phix*1000.)
            fill("phiy", 3, mcscenario.csc[endcap, station, ring, chamber].phiy*1000.)
            fill("phiz", 3, mcscenario.csc[endcap, station, ring, chamber].phiz*1000.)

def draw(param, title):
    histograms[param + str(3)].SetFillColor(ROOT.kGreen+1)
    histograms[param + str(2)].SetFillColor(ROOT.kCyan+2)
    histograms[param + str(1)].SetFillColor(ROOT.kBlue-8)

    histograms[param + str(3)].SetXTitle(title)
    histograms[param + str(3)].GetXaxis().CenterTitle()

    histograms[param + str(3)].Draw()
    histograms[param + str(2)].Draw("same")
    histograms[param + str(1)].Draw("same")

c1.Clear()
c1.Divide(3, 2)
c1.GetPad(1).cd(); draw("x", "Local x misalignment (mm)")
tlegend = ROOT.TLegend(0.17-0.15, 0.55+0.15, 0.45, 0.98)
tlegend.SetFillColor(ROOT.kWhite)
tlegend.SetBorderSize(1)
tlegend.AddEntry(histograms["x3"], " CSCs", "f")
tlegend.AddEntry(histograms["x2"], " unaligned DTs", "f")
tlegend.AddEntry(histograms["x1"], " aligned DTs", "f")
tlegend.SetTextSize(0.05)
tlegend.Draw()
c1.GetPad(2).cd(); draw("y", "Local y misalignment (mm)")
c1.GetPad(3).cd(); draw("z", "Local z misalignment (mm)")
c1.GetPad(4).cd(); draw("phix", "Local #phi_{x} misalignment (mrad)")
c1.GetPad(5).cd(); draw("phiy", "Local #phi_{y} misalignment (mrad)")
c1.GetPad(6).cd(); draw("phiz", "Local #phi_{z} misalignment (mrad)")
c1.SaveAs("mcscenario.png")
