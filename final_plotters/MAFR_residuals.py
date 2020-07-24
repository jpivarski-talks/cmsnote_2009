import os
import ROOT
execfile("/home/jpivarski/bin/tdrstyle.py")
c1 = ROOT.TCanvas()

directory_before = "/home/jpivarski/work/results/CRAFTchambers2/RESIDUALS_before/"
directory_6dof = "/home/jpivarski/work/results/CRAFTchambers2/RESIDUALS_6dof/"
directory_optimal = "/home/jpivarski/work/results/CRAFTchambers2/RESIDUALS_optimal/"
plotDirectory = "AlignmentMonitorMuonResidualsSummary/iter1/"

tfiles_before = [ROOT.TFile(directory_before + f) for f in os.listdir(directory_before) if f[-5:] == ".root"]
tfiles_6dof = [ROOT.TFile(directory_6dof + f) for f in os.listdir(directory_6dof) if f[-5:] == ".root"]
tfiles_optimal = [ROOT.TFile(directory_optimal + f) for f in os.listdir(directory_optimal) if f[-5:] == ".root"]

def getall(name, which):
    if which == "before": tfiles = tfiles_before
    elif which == "6dof": tfiles = tfiles_6dof
    elif which == "optimal": tfiles = tfiles_optimal

    output = tfiles[0].Get(plotDirectory + name).Clone()
    for h in tfiles[1:]:
        output.Add(h.Get(plotDirectory + name))
    return output

barrel_rawx_optimal = getall("barrel_rawx", "optimal")
barrel_cut1x_optimal = getall("barrel_cut1x", "optimal")

station1_rawx_before = getall("station1_rawx", "before")
station1_rawx_6dof = getall("station1_rawx", "6dof")
station1_rawx_optimal = getall("station1_rawx", "optimal")
station1_cut1x_before = getall("station1_cut1x", "before")
station1_cut1x_6dof = getall("station1_cut1x", "6dof")
station1_cut1x_optimal = getall("station1_cut1x", "optimal")
station2_cut1x_before = getall("station2_cut1x", "before")
station2_cut1x_6dof = getall("station2_cut1x", "6dof")
station2_cut1x_optimal = getall("station2_cut1x", "optimal")
station3_cut1x_before = getall("station3_cut1x", "before")
station3_cut1x_6dof = getall("station3_cut1x", "6dof")
station3_cut1x_optimal = getall("station3_cut1x", "optimal")
station4_cut1x_before = getall("station4_cut1x", "before")
station4_cut1x_6dof = getall("station4_cut1x", "6dof")
station4_cut1x_optimal = getall("station4_cut1x", "optimal")
station12_xdifffid1cut_before = getall("station12_xdifffid1cut", "before")
station12_xdifffid1cut_6dof = getall("station12_xdifffid1cut", "6dof")
station12_xdifffid1cut_optimal = getall("station12_xdifffid1cut", "optimal")
station23_xdifffid1cut_before = getall("station23_xdifffid1cut", "before")
station23_xdifffid1cut_6dof = getall("station23_xdifffid1cut", "6dof")
station23_xdifffid1cut_optimal = getall("station23_xdifffid1cut", "optimal")
station34_xdifffid1cut_before = getall("station34_xdifffid1cut", "before")
station34_xdifffid1cut_6dof = getall("station34_xdifffid1cut", "6dof")
station34_xdifffid1cut_optimal = getall("station34_xdifffid1cut", "optimal")
station1_rawy_before = getall("station1_rawy", "before")
station1_rawy_6dof = getall("station1_rawy", "6dof")
station1_rawy_optimal = getall("station1_rawy", "optimal")
station1_cut1y_before = getall("station1_cut1y", "before")
station1_cut1y_6dof = getall("station1_cut1y", "6dof")
station1_cut1y_optimal = getall("station1_cut1y", "optimal")
station2_cut1y_before = getall("station2_cut1y", "before")
station2_cut1y_6dof = getall("station2_cut1y", "6dof")
station2_cut1y_optimal = getall("station2_cut1y", "optimal")
station3_cut1y_before = getall("station3_cut1y", "before")
station3_cut1y_6dof = getall("station3_cut1y", "6dof")
station3_cut1y_optimal = getall("station3_cut1y", "optimal")
station12_ydifffid1cut_before = getall("station12_ydifffid1cut", "before")
station12_ydifffid1cut_6dof = getall("station12_ydifffid1cut", "6dof")
station12_ydifffid1cut_optimal = getall("station12_ydifffid1cut", "optimal")
station23_ydifffid1cut_before = getall("station23_ydifffid1cut", "before")
station23_ydifffid1cut_6dof = getall("station23_ydifffid1cut", "6dof")
station23_ydifffid1cut_optimal = getall("station23_ydifffid1cut", "optimal")

station1_rawx_before = getall("station1_rawx", "before")
station1_rawx_6dof = getall("station1_rawx", "6dof")
station1_rawx_optimal = getall("station1_rawx", "optimal")
station1_rawy_before = getall("station1_rawy", "before")
station1_rawy_6dof = getall("station1_rawy", "6dof")
station1_rawy_optimal = getall("station1_rawy", "optimal")
station1_rawdxdz_before = getall("station1_rawdxdz", "before")
station1_rawdxdz_6dof = getall("station1_rawdxdz", "6dof")
station1_rawdxdz_optimal = getall("station1_rawdxdz", "optimal")
station1_rawdydz_before = getall("station1_rawdydz", "before")
station1_rawdydz_6dof = getall("station1_rawdydz", "6dof")
station1_rawdydz_optimal = getall("station1_rawdydz", "optimal")
station2_rawx_before = getall("station2_rawx", "before")
station2_rawx_6dof = getall("station2_rawx", "6dof")
station2_rawx_optimal = getall("station2_rawx", "optimal")
station2_rawy_before = getall("station2_rawy", "before")
station2_rawy_6dof = getall("station2_rawy", "6dof")
station2_rawy_optimal = getall("station2_rawy", "optimal")
station2_rawdxdz_before = getall("station2_rawdxdz", "before")
station2_rawdxdz_6dof = getall("station2_rawdxdz", "6dof")
station2_rawdxdz_optimal = getall("station2_rawdxdz", "optimal")
station2_rawdydz_before = getall("station2_rawdydz", "before")
station2_rawdydz_6dof = getall("station2_rawdydz", "6dof")
station2_rawdydz_optimal = getall("station2_rawdydz", "optimal")
station3_rawx_before = getall("station3_rawx", "before")
station3_rawx_6dof = getall("station3_rawx", "6dof")
station3_rawx_optimal = getall("station3_rawx", "optimal")
station3_rawy_before = getall("station3_rawy", "before")
station3_rawy_6dof = getall("station3_rawy", "6dof")
station3_rawy_optimal = getall("station3_rawy", "optimal")
station3_rawdxdz_before = getall("station3_rawdxdz", "before")
station3_rawdxdz_6dof = getall("station3_rawdxdz", "6dof")
station3_rawdxdz_optimal = getall("station3_rawdxdz", "optimal")
station3_rawdydz_before = getall("station3_rawdydz", "before")
station3_rawdydz_6dof = getall("station3_rawdydz", "6dof")
station3_rawdydz_optimal = getall("station3_rawdydz", "optimal")
station4_rawx_before = getall("station4_rawx", "before")
station4_rawx_6dof = getall("station4_rawx", "6dof")
station4_rawx_optimal = getall("station4_rawx", "optimal")
station4_rawy_before = getall("station4_rawy", "before")
station4_rawy_6dof = getall("station4_rawy", "6dof")
station4_rawy_optimal = getall("station4_rawy", "optimal")
station4_rawdxdz_before = getall("station4_rawdxdz", "before")
station4_rawdxdz_6dof = getall("station4_rawdxdz", "6dof")
station4_rawdxdz_optimal = getall("station4_rawdxdz", "optimal")
station4_rawdydz_before = getall("station4_rawdydz", "before")
station4_rawdydz_6dof = getall("station4_rawdydz", "6dof")
station4_rawdydz_optimal = getall("station4_rawdydz", "optimal")

wheelA_rawx_before = getall("wheelA_rawx", "before")
wheelA_rawx_6dof = getall("wheelA_rawx", "6dof")
wheelA_rawx_optimal = getall("wheelA_rawx", "optimal")
wheelA_rawy_before = getall("wheelA_rawy", "before")
wheelA_rawy_6dof = getall("wheelA_rawy", "6dof")
wheelA_rawy_optimal = getall("wheelA_rawy", "optimal")
wheelA_rawdxdz_before = getall("wheelA_rawdxdz", "before")
wheelA_rawdxdz_6dof = getall("wheelA_rawdxdz", "6dof")
wheelA_rawdxdz_optimal = getall("wheelA_rawdxdz", "optimal")
wheelA_rawdydz_before = getall("wheelA_rawdydz", "before")
wheelA_rawdydz_6dof = getall("wheelA_rawdydz", "6dof")
wheelA_rawdydz_optimal = getall("wheelA_rawdydz", "optimal")
wheelB_rawx_before = getall("wheelB_rawx", "before")
wheelB_rawx_6dof = getall("wheelB_rawx", "6dof")
wheelB_rawx_optimal = getall("wheelB_rawx", "optimal")
wheelB_rawy_before = getall("wheelB_rawy", "before")
wheelB_rawy_6dof = getall("wheelB_rawy", "6dof")
wheelB_rawy_optimal = getall("wheelB_rawy", "optimal")
wheelB_rawdxdz_before = getall("wheelB_rawdxdz", "before")
wheelB_rawdxdz_6dof = getall("wheelB_rawdxdz", "6dof")
wheelB_rawdxdz_optimal = getall("wheelB_rawdxdz", "optimal")
wheelB_rawdydz_before = getall("wheelB_rawdydz", "before")
wheelB_rawdydz_6dof = getall("wheelB_rawdydz", "6dof")
wheelB_rawdydz_optimal = getall("wheelB_rawdydz", "optimal")
wheelC_rawx_before = getall("wheelC_rawx", "before")
wheelC_rawx_6dof = getall("wheelC_rawx", "6dof")
wheelC_rawx_optimal = getall("wheelC_rawx", "optimal")
wheelC_rawy_before = getall("wheelC_rawy", "before")
wheelC_rawy_6dof = getall("wheelC_rawy", "6dof")
wheelC_rawy_optimal = getall("wheelC_rawy", "optimal")
wheelC_rawdxdz_before = getall("wheelC_rawdxdz", "before")
wheelC_rawdxdz_6dof = getall("wheelC_rawdxdz", "6dof")
wheelC_rawdxdz_optimal = getall("wheelC_rawdxdz", "optimal")
wheelC_rawdydz_before = getall("wheelC_rawdydz", "before")
wheelC_rawdydz_6dof = getall("wheelC_rawdydz", "6dof")
wheelC_rawdydz_optimal = getall("wheelC_rawdydz", "optimal")
wheelD_rawx_before = getall("wheelD_rawx", "before")
wheelD_rawx_6dof = getall("wheelD_rawx", "6dof")
wheelD_rawx_optimal = getall("wheelD_rawx", "optimal")
wheelD_rawy_before = getall("wheelD_rawy", "before")
wheelD_rawy_6dof = getall("wheelD_rawy", "6dof")
wheelD_rawy_optimal = getall("wheelD_rawy", "optimal")
wheelD_rawdxdz_before = getall("wheelD_rawdxdz", "before")
wheelD_rawdxdz_6dof = getall("wheelD_rawdxdz", "6dof")
wheelD_rawdxdz_optimal = getall("wheelD_rawdxdz", "optimal")
wheelD_rawdydz_before = getall("wheelD_rawdydz", "before")
wheelD_rawdydz_6dof = getall("wheelD_rawdydz", "6dof")
wheelD_rawdydz_optimal = getall("wheelD_rawdydz", "optimal")
wheelE_rawx_before = getall("wheelE_rawx", "before")
wheelE_rawx_6dof = getall("wheelE_rawx", "6dof")
wheelE_rawx_optimal = getall("wheelE_rawx", "optimal")
wheelE_rawy_before = getall("wheelE_rawy", "before")
wheelE_rawy_6dof = getall("wheelE_rawy", "6dof")
wheelE_rawy_optimal = getall("wheelE_rawy", "optimal")
wheelE_rawdxdz_before = getall("wheelE_rawdxdz", "before")
wheelE_rawdxdz_6dof = getall("wheelE_rawdxdz", "6dof")
wheelE_rawdxdz_optimal = getall("wheelE_rawdxdz", "optimal")
wheelE_rawdydz_before = getall("wheelE_rawdydz", "before")
wheelE_rawdydz_6dof = getall("wheelE_rawdydz", "6dof")
wheelE_rawdydz_optimal = getall("wheelE_rawdydz", "optimal")

wheelA_cut1x_before = getall("wheelA_cut1x", "before")
wheelA_cut1x_6dof = getall("wheelA_cut1x", "6dof")
wheelA_cut1x_optimal = getall("wheelA_cut1x", "optimal")
wheelA_cut1y_before = getall("wheelA_cut1y", "before")
wheelA_cut1y_6dof = getall("wheelA_cut1y", "6dof")
wheelA_cut1y_optimal = getall("wheelA_cut1y", "optimal")
wheelB_cut1x_before = getall("wheelB_cut1x", "before")
wheelB_cut1x_6dof = getall("wheelB_cut1x", "6dof")
wheelB_cut1x_optimal = getall("wheelB_cut1x", "optimal")
wheelB_cut1y_before = getall("wheelB_cut1y", "before")
wheelB_cut1y_6dof = getall("wheelB_cut1y", "6dof")
wheelB_cut1y_optimal = getall("wheelB_cut1y", "optimal")
wheelC_cut1x_before = getall("wheelC_cut1x", "before")
wheelC_cut1x_6dof = getall("wheelC_cut1x", "6dof")
wheelC_cut1x_optimal = getall("wheelC_cut1x", "optimal")
wheelC_cut1y_before = getall("wheelC_cut1y", "before")
wheelC_cut1y_6dof = getall("wheelC_cut1y", "6dof")
wheelC_cut1y_optimal = getall("wheelC_cut1y", "optimal")
wheelD_cut1x_before = getall("wheelD_cut1x", "before")
wheelD_cut1x_6dof = getall("wheelD_cut1x", "6dof")
wheelD_cut1x_optimal = getall("wheelD_cut1x", "optimal")
wheelD_cut1y_before = getall("wheelD_cut1y", "before")
wheelD_cut1y_6dof = getall("wheelD_cut1y", "6dof")
wheelD_cut1y_optimal = getall("wheelD_cut1y", "optimal")
wheelE_cut1x_before = getall("wheelE_cut1x", "before")
wheelE_cut1x_6dof = getall("wheelE_cut1x", "6dof")
wheelE_cut1x_optimal = getall("wheelE_cut1x", "optimal")
wheelE_cut1y_before = getall("wheelE_cut1y", "before")
wheelE_cut1y_6dof = getall("wheelE_cut1y", "6dof")
wheelE_cut1y_optimal = getall("wheelE_cut1y", "optimal")


c1.Clear()

barrel_rawx_optimal.SetFillColor(ROOT.kGreen-3)
barrel_cut1x_optimal.SetFillColor(ROOT.kGreen-9)
barrel_rawx_optimal.SetXTitle("All x residuals in the barrel (mm)")
barrel_rawx_optimal.GetXaxis().CenterTitle()

barrel_rawx_optimal.Draw()
barrel_cut1x_optimal.Draw("same")
ROOT.gPad.SetLogy(1)

tlegend = ROOT.TLegend(0.6, 0.8, 0.98, 0.98)
tlegend.SetFillColor(ROOT.kWhite)
tlegend.SetBorderSize(1)
tlegend.SetTextSize(0.03)
tlegend.AddEntry(barrel_rawx_optimal, "Raw residuals", "f")
tlegend.AddEntry(barrel_rawx_optimal, "RMS is " + str(round(barrel_rawx_optimal.GetRMS(), 1)) + " mm", "")
tlegend.AddEntry(barrel_cut1x_optimal, "|#Deltadx/dz| < 1 mrad", "f")
tlegend.AddEntry(barrel_cut1x_optimal, "RMS is " + str(round(barrel_cut1x_optimal.GetRMS(), 1)) + " mm", "")
tlegend.Draw()
c1.SaveAs("residuals_explanation.pdf")

ROOT.gPad.SetLogy(0)




c1.Clear()
c1.Divide(2, 2)

for h in station1_rawx_before, station1_rawdxdz_before, station1_rawy_before, station1_rawdydz_before:
    h.GetXaxis().SetLabelSize(0.07)
    h.GetXaxis().SetTitleSize(0.07)
    h.GetXaxis().SetTitleOffset(0.8)
    h.GetXaxis().CenterTitle()
    h.GetYaxis().SetLabelSize(0.07)

c1.GetPad(1).cd()
station1_rawx_before.SetAxisRange(-50., 50., "X")
station1_rawx_before.SetAxisRange(0, 30000, "Y")
station1_rawx_before.SetXTitle("Station 1 x residuals (mm)")
station1_rawx_6dof.SetLineColor(ROOT.kRed)
station1_rawx_optimal.SetLineColor(ROOT.kGreen+3)
station1_rawx_before.Draw()
station1_rawx_6dof.Draw("same")
station1_rawx_optimal.Draw("same")

c1.GetPad(2).cd()
station1_rawdxdz_before.SetAxisRange(-50., 50., "X")
station1_rawdxdz_before.SetAxisRange(0, 40000, "Y")
station1_rawdxdz_before.SetXTitle("Station 1 dx/dz residuals (mrad)")
station1_rawdxdz_6dof.SetLineColor(ROOT.kRed)
station1_rawdxdz_optimal.SetLineColor(ROOT.kGreen+3)
station1_rawdxdz_before.Draw()
station1_rawdxdz_6dof.Draw("same")
station1_rawdxdz_optimal.Draw("same")

tlegend = ROOT.TLegend(0.58, 0.7, 0.99, 0.98)
tlegend.SetFillColor(ROOT.kWhite)
tlegend.SetBorderSize(1)
tlegend.SetTextSize(0.06)
tlegend.AddEntry(station1_rawdxdz_before, "Before alignment", "l")
tlegend.AddEntry(station1_rawdxdz_6dof, "6-DOF alignment", "l")
tlegend.AddEntry(station1_rawdxdz_optimal, "Production alignment", "l")
tlegend.Draw()

c1.GetPad(3).cd()
station1_rawy_before.SetAxisRange(-50., 50., "X")
station1_rawy_before.SetAxisRange(0, 15000, "Y")
station1_rawy_before.SetXTitle("Station 1 y residuals (mm)")
station1_rawy_6dof.SetLineColor(ROOT.kRed)
station1_rawy_optimal.SetLineColor(ROOT.kGreen+3)
station1_rawy_before.Draw()
station1_rawy_6dof.Draw("same")
station1_rawy_optimal.Draw("same")

c1.GetPad(4).cd()
station1_rawdydz_before.SetAxisRange(-50., 50., "X")
station1_rawdydz_before.SetAxisRange(0, 8000, "Y")
station1_rawdydz_before.SetXTitle("Station 1 dy/dz residuals (mrad)")
station1_rawdydz_6dof.SetLineColor(ROOT.kRed)
station1_rawdydz_optimal.SetLineColor(ROOT.kGreen+3)
station1_rawdydz_before.Draw()
station1_rawdydz_6dof.Draw("same")
station1_rawdydz_optimal.Draw("same")

c1.SaveAs("residuals_rawstation1.pdf")




c1.Clear()
c1.Divide(2, 2)

for h in station1_cut1x_before, station2_cut1x_before, station3_cut1x_before, station4_cut1x_before:
    h.GetXaxis().SetLabelSize(0.07)
    h.GetXaxis().SetTitleSize(0.07)
    h.GetXaxis().SetTitleOffset(0.8)
    h.GetXaxis().CenterTitle()
    h.GetYaxis().SetLabelSize(0.07)

c1.GetPad(1).cd()
station1_cut1x_before.SetAxisRange(-50., 50., "X")
station1_cut1x_before.SetAxisRange(0, 10000, "Y")
station1_cut1x_before.SetXTitle("Station 1 x residuals (mm)")
station1_cut1x_6dof.SetLineColor(ROOT.kRed)
station1_cut1x_optimal.SetLineColor(ROOT.kGreen+3)
station1_cut1x_before.Draw()
station1_cut1x_6dof.Draw("same")
station1_cut1x_optimal.Draw("same")

c1.GetPad(2).cd()
station2_cut1x_before.SetAxisRange(-50., 50., "X")
station2_cut1x_before.SetAxisRange(0, 8000, "Y")
station2_cut1x_before.SetXTitle("Station 2 x residuals (mm)")
station2_cut1x_6dof.SetLineColor(ROOT.kRed)
station2_cut1x_optimal.SetLineColor(ROOT.kGreen+3)
station2_cut1x_before.Draw()
station2_cut1x_6dof.Draw("same")
station2_cut1x_optimal.Draw("same")

tlegend = ROOT.TLegend(0.58, 0.7, 0.99, 0.98)
tlegend.SetFillColor(ROOT.kWhite)
tlegend.SetBorderSize(1)
tlegend.SetTextSize(0.06)
tlegend.AddEntry(station2_cut1x_before, "Before alignment", "l")
tlegend.AddEntry(station2_cut1x_6dof, "6-DOF alignment", "l")
tlegend.AddEntry(station2_cut1x_optimal, "Production alignment", "l")
tlegend.Draw()

c1.GetPad(3).cd()
station3_cut1x_before.SetAxisRange(-50., 50., "X")
station3_cut1x_before.SetAxisRange(0, 5000, "Y")
station3_cut1x_before.SetXTitle("Station 3 x residuals (mm)")
station3_cut1x_6dof.SetLineColor(ROOT.kRed)
station3_cut1x_optimal.SetLineColor(ROOT.kGreen+3)
station3_cut1x_before.Draw()
station3_cut1x_6dof.Draw("same")
station3_cut1x_optimal.Draw("same")

c1.GetPad(4).cd()
station4_cut1x_before.SetAxisRange(-50., 50., "X")
station4_cut1x_before.SetAxisRange(0, 3000, "Y")
station4_cut1x_before.SetXTitle("Station 4 x residuals (mm)")
station4_cut1x_6dof.SetLineColor(ROOT.kRed)
station4_cut1x_optimal.SetLineColor(ROOT.kGreen+3)
station4_cut1x_before.Draw()
station4_cut1x_6dof.Draw("same")
station4_cut1x_optimal.Draw("same")

c1.SaveAs("residuals_cut1x.pdf")






c1.Clear()

for h in station12_xdifffid1cut_before, station23_xdifffid1cut_before, station34_xdifffid1cut_before:
    h.GetXaxis().SetLabelSize(0.05)
    h.GetXaxis().SetTitleSize(0.05)
    h.GetXaxis().SetTitleOffset(1)
    h.GetXaxis().CenterTitle()
    h.GetYaxis().SetLabelSize(0.05)

station12_xdifffid1cut_before.SetAxisRange(-10., 10., "X")
station12_xdifffid1cut_before.SetAxisRange(0, 1000, "Y")
station12_xdifffid1cut_before.SetXTitle("Station 2 x minus station 1 x (mm)")
station12_xdifffid1cut_6dof.SetLineColor(ROOT.kRed)
station12_xdifffid1cut_optimal.SetLineColor(ROOT.kGreen+3)
station12_xdifffid1cut_before.Draw()
station12_xdifffid1cut_6dof.Draw("same")
station12_xdifffid1cut_optimal.Draw("same")

tlegend = ROOT.TLegend(0.17, 0.85, 0.99, 0.98)
tlegend.SetFillColor(ROOT.kWhite)
tlegend.SetBorderSize(1)
tlegend.SetTextSize(0.04)
tlegend.AddEntry(station12_xdifffid1cut_before, "Before alignment, RMS = %3.2g mm" % station12_xdifffid1cut_before.GetRMS(), "l")
tlegend.AddEntry(station12_xdifffid1cut_6dof, "6-DOF alignment, %3.2g mm" % station12_xdifffid1cut_6dof.GetRMS(), "l")
tlegend.AddEntry(station12_xdifffid1cut_optimal, "Production alignment, %3.2g mm" % station12_xdifffid1cut_optimal.GetRMS(), "l")
tlegend.Draw()
c1.SaveAs("residuals_xdifffid1cut_12.pdf")

station23_xdifffid1cut_before.SetAxisRange(-10., 10., "X")
station23_xdifffid1cut_before.SetAxisRange(0, 700, "Y")
station23_xdifffid1cut_before.SetXTitle("Station 3 x minus station 2 x (mm)")
station23_xdifffid1cut_6dof.SetLineColor(ROOT.kRed)
station23_xdifffid1cut_optimal.SetLineColor(ROOT.kGreen+3)
station23_xdifffid1cut_before.Draw()
station23_xdifffid1cut_6dof.Draw("same")
station23_xdifffid1cut_optimal.Draw("same")

tlegend = ROOT.TLegend(0.17, 0.85, 0.99, 0.98)
tlegend.SetFillColor(ROOT.kWhite)
tlegend.SetBorderSize(1)
tlegend.SetTextSize(0.04)
tlegend.AddEntry(station23_xdifffid1cut_before, "Before alignment, RMS = %3.2g mm" % station23_xdifffid1cut_before.GetRMS(), "l")
tlegend.AddEntry(station23_xdifffid1cut_6dof, "6-DOF alignment, %3.2g mm" % station23_xdifffid1cut_6dof.GetRMS(), "l")
tlegend.AddEntry(station23_xdifffid1cut_optimal, "Production alignment, %3.2g mm" % station23_xdifffid1cut_optimal.GetRMS(), "l")
tlegend.Draw()
c1.SaveAs("residuals_xdifffid1cut_23.pdf")

station34_xdifffid1cut_before.SetAxisRange(-10., 10., "X")
station34_xdifffid1cut_before.SetAxisRange(0, 360, "Y")
station34_xdifffid1cut_before.SetXTitle("Station 4 x minus station 3 x (mm)")
station34_xdifffid1cut_6dof.SetLineColor(ROOT.kRed)
station34_xdifffid1cut_optimal.SetLineColor(ROOT.kGreen+3)
station34_xdifffid1cut_before.Draw()
station34_xdifffid1cut_6dof.Draw("same")
station34_xdifffid1cut_optimal.Draw("same")

tlegend = ROOT.TLegend(0.17, 0.85, 0.99, 0.98)
tlegend.SetFillColor(ROOT.kWhite)
tlegend.SetBorderSize(1)
tlegend.SetTextSize(0.04)
tlegend.AddEntry(station34_xdifffid1cut_before, "Before alignment, RMS = %3.2g mm" % station34_xdifffid1cut_before.GetRMS(), "l")
tlegend.AddEntry(station34_xdifffid1cut_6dof, "6-DOF alignment, %3.2g mm" % station34_xdifffid1cut_6dof.GetRMS(), "l")
tlegend.AddEntry(station34_xdifffid1cut_optimal, "Production alignment, %3.2g mm" % station34_xdifffid1cut_optimal.GetRMS(), "l")
tlegend.Draw()
c1.SaveAs("residuals_xdifffid1cut_34.pdf")

