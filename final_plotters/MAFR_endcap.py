import ROOT
execfile("/home/jpivarski/bin/tdrstyle.py")
c1 = ROOT.TCanvas()

# iter01: "CSChardwareAndPG.db"
# iter02: "CSCphotogrammetry.db"
# iter03: "V11alignment.db"
# iter04: "idealAlignment.db"

inf = nan = 1000000.

execfile("/home/jpivarski/work/results/CRAFTchambers2/CSCCRAFT1_wAPE_restricted/CSCCRAFTiter01_report.py")
reports_hardware = reports

execfile("/home/jpivarski/work/results/CRAFTchambers2/CSCCRAFT1_wAPE_restricted/CSCCRAFTiter02_report.py")
reports_photogrammetry = reports

execfile("/home/jpivarski/work/results/CRAFTchambers2/CSCCRAFT1_wAPE_restricted/CSCCRAFTiter03_report.py")
reports_oldalignment = reports

execfile("/home/jpivarski/work/results/CRAFTchambers2/CSCCRAFT1_wAPE_restricted/CSCCRAFTiter04_report.py")
reports_ideal = reports




execfile("/home/jpivarski/work/results/CRAFTchambers2/CSCCRAFT1_wAPE_restricted_align/CSCCRAFTiter01_report.py")
reports_hardware = reports



hm12 = ROOT.TH1F("hm12", "", 36, 0.5, 36.5)
hm13 = ROOT.TH1F("hm13", "", 36, 0.5, 36.5)
hm22 = ROOT.TH1F("hm22", "", 36, 0.5, 36.5)
hm32 = ROOT.TH1F("hm32", "", 36, 0.5, 36.5)

hp12 = ROOT.TH1F("hp12", "", 36, 0.5, 36.5)
hp13 = ROOT.TH1F("hp13", "", 36, 0.5, 36.5)
hp22 = ROOT.TH1F("hp22", "", 36, 0.5, 36.5)
hp32 = ROOT.TH1F("hp32", "", 36, 0.5, 36.5)

# for r in reports_hardware:
#     if r.status == "PASS" and r.deltax is not None and 0. < r.deltax.error < inf:
#         if r.postal_address[0] == "CSC" and r.postal_address[1:4] == (1, 1, 2):
#             hp12.SetBinContent(r.postal_address[4], -r.deltax.value*10.)
#             hp12.SetBinError(r.postal_address[4], r.deltax.error*10.)
#         if r.postal_address[0] == "CSC" and r.postal_address[1:4] == (1, 1, 3):
#             hp13.SetBinContent(r.postal_address[4], -r.deltax.value*10.)
#             hp13.SetBinError(r.postal_address[4], r.deltax.error*10.)

#         if r.postal_address[0] == "CSC" and r.postal_address[1:4] == (2, 1, 2):
#             hm12.SetBinContent(r.postal_address[4], r.deltax.value*10.)
#             hm12.SetBinError(r.postal_address[4], r.deltax.error*10.)
#         if r.postal_address[0] == "CSC" and r.postal_address[1:4] == (2, 1, 3):
#             hm13.SetBinContent(r.postal_address[4], r.deltax.value*10.)
#             hm13.SetBinError(r.postal_address[4], r.deltax.error*10.)

#         if r.postal_address[0] == "CSC" and r.postal_address[1:4] == (1, 2, 2):
#             hp22.SetBinContent(r.postal_address[4], -r.deltax.value*10.)
#             hp22.SetBinError(r.postal_address[4], r.deltax.error*10.)
#         if r.postal_address[0] == "CSC" and r.postal_address[1:4] == (1, 3, 2):
#             hp32.SetBinContent(r.postal_address[4], r.deltax.value*10.)
#             hp32.SetBinError(r.postal_address[4], r.deltax.error*10.)

#         if r.postal_address[0] == "CSC" and r.postal_address[1:4] == (2, 2, 2):
#             hm22.SetBinContent(r.postal_address[4], r.deltax.value*10.)
#             hm22.SetBinError(r.postal_address[4], r.deltax.error*10.)
#         if r.postal_address[0] == "CSC" and r.postal_address[1:4] == (2, 3, 2):
#             hm32.SetBinContent(r.postal_address[4], -r.deltax.value*10.)
#             hm32.SetBinError(r.postal_address[4], r.deltax.error*10.)

for r in reports_hardware:
    if r.status == "PASS" and r.deltax is not None and 0. < r.deltax.error < inf:
        if r.postal_address[0] == "CSC" and r.postal_address[1:4] == (1, 1, 2):
            hp12.SetBinContent(r.postal_address[4], r.deltax.value*10.)
            hp12.SetBinError(r.postal_address[4], r.deltax.error*10.)
        if r.postal_address[0] == "CSC" and r.postal_address[1:4] == (1, 1, 3):
            hp13.SetBinContent(r.postal_address[4], r.deltax.value*10.)
            hp13.SetBinError(r.postal_address[4], r.deltax.error*10.)

        if r.postal_address[0] == "CSC" and r.postal_address[1:4] == (2, 1, 2):
            hm12.SetBinContent(r.postal_address[4], r.deltax.value*10.)
            hm12.SetBinError(r.postal_address[4], r.deltax.error*10.)
        if r.postal_address[0] == "CSC" and r.postal_address[1:4] == (2, 1, 3):
            hm13.SetBinContent(r.postal_address[4], r.deltax.value*10.)
            hm13.SetBinError(r.postal_address[4], r.deltax.error*10.)

        if r.postal_address[0] == "CSC" and r.postal_address[1:4] == (1, 2, 2):
            hp22.SetBinContent(r.postal_address[4], r.deltax.value*10.)
            hp22.SetBinError(r.postal_address[4], r.deltax.error*10.)
        if r.postal_address[0] == "CSC" and r.postal_address[1:4] == (1, 3, 2):
            hp32.SetBinContent(r.postal_address[4], r.deltax.value*10.)
            hp32.SetBinError(r.postal_address[4], r.deltax.error*10.)

        if r.postal_address[0] == "CSC" and r.postal_address[1:4] == (2, 2, 2):
            hm22.SetBinContent(r.postal_address[4], r.deltax.value*10.)
            hm22.SetBinError(r.postal_address[4], r.deltax.error*10.)
        if r.postal_address[0] == "CSC" and r.postal_address[1:4] == (2, 3, 2):
            hm32.SetBinContent(r.postal_address[4], r.deltax.value*10.)
            hm32.SetBinError(r.postal_address[4], r.deltax.error*10.)

tdrStyle.SetOptFit(0)
f = ROOT.TF1("f", "[0] + [1]*sin(x*2.*3.1415926/36.) + [2]*cos(x*2.*3.1415926/36.)", 0.5, 36.5)
# hm32.Fit("f")
# hm22.Fit("f")
# hm22.GetFunction("f").SetLineColor(ROOT.kBlack)

hm12.SetXTitle("Chamber number")
hp12.SetXTitle("Chamber number")
hm22.SetXTitle("Chamber number")
hp22.SetXTitle("Chamber number")
hm12.SetYTitle("Local #delta_{x} (mm)")
hp12.SetYTitle("Local #delta_{x} (mm)")
hm22.SetYTitle("Local #delta_{x} (mm)")
hp22.SetYTitle("Local #delta_{x} (mm)")

hm12.GetXaxis().CenterTitle()
hp12.GetXaxis().CenterTitle()
hm22.GetXaxis().CenterTitle()
hp22.GetXaxis().CenterTitle()
hm32.GetXaxis().CenterTitle()
hp32.GetXaxis().CenterTitle()
hm12.GetYaxis().CenterTitle()
hp12.GetYaxis().CenterTitle()
hm22.GetYaxis().CenterTitle()
hp22.GetYaxis().CenterTitle()
hm32.GetYaxis().CenterTitle()
hp32.GetYaxis().CenterTitle()

c1.Clear()
c1.Divide(2, 2)

c1.GetPad(1).cd()
hm12.SetAxisRange(-25., 25., "Y")
hm13.SetMarkerColor(ROOT.kRed)
hm13.SetLineColor(ROOT.kRed)
hm12.Draw("e1")
hm13.Draw("samee1")
tline1 = ROOT.TLine(0.5, 0, 36.5, 0); tline1.SetLineStyle(2); tline1.Draw("same")
tlegend1 = ROOT.TLegend(0.75, 0.8, 0.95, 0.95)
tlegend1.SetFillColor(ROOT.kWhite)
tlegend1.SetBorderSize(1)
tlegend1.AddEntry(hm12, "ME-1/2", "pl")
tlegend1.AddEntry(hm13, "ME-1/3", "pl")
tlegend1.Draw()

c1.GetPad(2).cd()
hp12.SetAxisRange(-25., 25., "Y")
hp13.SetMarkerColor(ROOT.kRed)
hp13.SetLineColor(ROOT.kRed)
hp12.Draw("e1")
hp13.Draw("samee1")
tline2 = ROOT.TLine(0.5, 0, 36.5, 0); tline2.SetLineStyle(2); tline2.Draw("same")
tlegend2 = ROOT.TLegend(0.75, 0.8, 0.95, 0.95)
tlegend2.SetFillColor(ROOT.kWhite)
tlegend2.SetBorderSize(1)
tlegend2.AddEntry(hm12, "ME+1/2", "pl")
tlegend2.AddEntry(hm13, "ME+1/3", "pl")
tlegend2.Draw()

c1.GetPad(3).cd()
hm22.SetAxisRange(-25., 25., "Y")
hm32.SetMarkerColor(ROOT.kRed)
hm32.SetLineColor(ROOT.kRed)
hm22.Draw("e1")
hm32.Draw("samee1")
tline3 = ROOT.TLine(0.5, 0, 36.5, 0); tline3.SetLineStyle(2); tline3.Draw("same")
tlegend3 = ROOT.TLegend(0.75, 0.8, 0.95, 0.95)
tlegend3.SetFillColor(ROOT.kWhite)
tlegend3.SetBorderSize(1)
tlegend3.AddEntry(hm12, "ME-2/2", "pl")
tlegend3.AddEntry(hm13, "ME-3/2", "pl")
tlegend3.Draw()

c1.GetPad(4).cd()
hp22.SetAxisRange(-25., 25., "Y")
hp32.SetMarkerColor(ROOT.kRed)
hp32.SetLineColor(ROOT.kRed)
hp22.Draw("e1")
hp32.Draw("samee1")
tline4 = ROOT.TLine(0.5, 0, 36.5, 0); tline4.SetLineStyle(2); tline4.Draw("same")
tlegend4 = ROOT.TLegend(0.75, 0.8, 0.95, 0.95)
tlegend4.SetFillColor(ROOT.kWhite)
tlegend4.SetBorderSize(1)
tlegend4.AddEntry(hm12, "ME+2/2", "pl")
tlegend4.AddEntry(hm13, "ME+3/2", "pl")
tlegend4.Draw()

# c1.SaveAs("data_endcap_alignments.pdf")

#############################

DXp12 = ROOT.TH1F("DXp12", "", 36, 0.5, 36.5)
DYp12 = ROOT.TH1F("DYp12", "", 36, 0.5, 36.5)
LOCALp12 = ROOT.TH1F("LOCALp12", "", 36, 0.5, 36.5)
DXp22 = ROOT.TH1F("DXp22", "", 36, 0.5, 36.5)
DYp22 = ROOT.TH1F("DYp22", "", 36, 0.5, 36.5)
LOCALp22 = ROOT.TH1F("LOCALp22", "", 36, 0.5, 36.5)
DXp32 = ROOT.TH1F("DXp32", "", 36, 0.5, 36.5)
DYp32 = ROOT.TH1F("DYp32", "", 36, 0.5, 36.5)
LOCALp32 = ROOT.TH1F("LOCALp32", "", 36, 0.5, 36.5)
DXm12 = ROOT.TH1F("DXm12", "", 36, 0.5, 36.5)
DYm12 = ROOT.TH1F("DYm12", "", 36, 0.5, 36.5)
LOCALm12 = ROOT.TH1F("LOCALm12", "", 36, 0.5, 36.5)
DXm22 = ROOT.TH1F("DXm22", "", 36, 0.5, 36.5)
DYm22 = ROOT.TH1F("DYm22", "", 36, 0.5, 36.5)
LOCALm22 = ROOT.TH1F("LOCALm22", "", 36, 0.5, 36.5)
DXm32 = ROOT.TH1F("DXm32", "", 36, 0.5, 36.5)
DYm32 = ROOT.TH1F("DYm32", "", 36, 0.5, 36.5)
LOCALm32 = ROOT.TH1F("LOCALm32", "", 36, 0.5, 36.5)

DXp12.SetBinContent(1, 0.399994*10.)
DYp12.SetBinContent(1, -0.5*10.)
LOCALp12.SetBinContent(1, -0.5*10.)
DXp12.SetBinContent(2, 0.399994*10.)
DYp12.SetBinContent(2, -0.5*10.)
LOCALp12.SetBinContent(2, -0.561862*10.)
DXp12.SetBinContent(3, 0.399994*10.)
DYp12.SetBinContent(3, -0.5*10.)
LOCALp12.SetBinContent(3, -0.606652*10.)
DXp12.SetBinContent(4, 0.399994*10.)
DYp12.SetBinContent(4, -0.5*10.)
LOCALp12.SetBinContent(4, -0.63301*10.)
DXp12.SetBinContent(5, 0.399994*10.)
DYp12.SetBinContent(5, -0.5*10.)
LOCALp12.SetBinContent(5, -0.640133*10.)
DXp12.SetBinContent(6, 0.399994*10.)
DYp12.SetBinContent(6, -0.5*10.)
LOCALp12.SetBinContent(6, -0.627807*10.)
DXp12.SetBinContent(7, 0.399994*10.)
DYp12.SetBinContent(7, -0.5*10.)
LOCALp12.SetBinContent(7, -0.596405*10.)
DXp12.SetBinContent(8, 0.400002*10.)
DYp12.SetBinContent(8, -0.5*10.)
LOCALp12.SetBinContent(8, -0.546889*10.)
DXp12.SetBinContent(9, 0.400002*10.)
DYp12.SetBinContent(9, -0.5*10.)
LOCALp12.SetBinContent(9, -0.480749*10.)
DXp12.SetBinContent(10, 0.4*10.)
DYp12.SetBinContent(10, -0.5*10.)
LOCALp12.SetBinContent(10, -0.4*10.)
DXp12.SetBinContent(11, 0.400002*10.)
DYp12.SetBinContent(11, -0.5*10.)
LOCALp12.SetBinContent(11, -0.307101*10.)
DXp12.SetBinContent(12, 0.400002*10.)
DYp12.SetBinContent(12, -0.5*10.)
LOCALp12.SetBinContent(12, -0.204868*10.)
DXp12.SetBinContent(13, 0.399994*10.)
DYp12.SetBinContent(13, -0.5*10.)
LOCALp12.SetBinContent(13, -0.0964049*10.)
DXp12.SetBinContent(14, 0.399994*10.)
DYp12.SetBinContent(14, -0.5*10.)
LOCALp12.SetBinContent(14, 0.0149807*10.)
DXp12.SetBinContent(15, 0.399994*10.)
DYp12.SetBinContent(15, -0.5*10.)
LOCALp12.SetBinContent(15, 0.125911*10.)
DXp12.SetBinContent(16, 0.399994*10.)
DYp12.SetBinContent(16, -0.5*10.)
LOCALp12.SetBinContent(16, 0.233016*10.)
DXp12.SetBinContent(17, 0.399994*10.)
DYp12.SetBinContent(17, -0.5*10.)
LOCALp12.SetBinContent(17, 0.33304*10.)
DXp12.SetBinContent(18, 0.399994*10.)
DYp12.SetBinContent(18, -0.5*10.)
LOCALp12.SetBinContent(18, 0.422946*10.)
DXp12.SetBinContent(19, 0.399994*10.)
DYp12.SetBinContent(19, -0.5*10.)
LOCALp12.SetBinContent(19, 0.5*10.)
DXp12.SetBinContent(20, 0.399994*10.)
DYp12.SetBinContent(20, -0.5*10.)
LOCALp12.SetBinContent(20, 0.561862*10.)
DXp12.SetBinContent(21, 0.399994*10.)
DYp12.SetBinContent(21, -0.5*10.)
LOCALp12.SetBinContent(21, 0.606652*10.)
DXp12.SetBinContent(22, 0.399994*10.)
DYp12.SetBinContent(22, -0.5*10.)
LOCALp12.SetBinContent(22, 0.63301*10.)
DXp12.SetBinContent(23, 0.399994*10.)
DYp12.SetBinContent(23, -0.5*10.)
LOCALp12.SetBinContent(23, 0.640133*10.)
DXp12.SetBinContent(24, 0.399994*10.)
DYp12.SetBinContent(24, -0.5*10.)
LOCALp12.SetBinContent(24, 0.627807*10.)
DXp12.SetBinContent(25, 0.399994*10.)
DYp12.SetBinContent(25, -0.5*10.)
LOCALp12.SetBinContent(25, 0.596405*10.)
DXp12.SetBinContent(26, 0.400002*10.)
DYp12.SetBinContent(26, -0.5*10.)
LOCALp12.SetBinContent(26, 0.546889*10.)
DXp12.SetBinContent(27, 0.400002*10.)
DYp12.SetBinContent(27, -0.5*10.)
LOCALp12.SetBinContent(27, 0.480749*10.)
DXp12.SetBinContent(28, 0.4*10.)
DYp12.SetBinContent(28, -0.5*10.)
LOCALp12.SetBinContent(28, 0.4*10.)
DXp12.SetBinContent(29, 0.400002*10.)
DYp12.SetBinContent(29, -0.5*10.)
LOCALp12.SetBinContent(29, 0.307101*10.)
DXp12.SetBinContent(30, 0.400002*10.)
DYp12.SetBinContent(30, -0.5*10.)
LOCALp12.SetBinContent(30, 0.204868*10.)
DXp12.SetBinContent(31, 0.399994*10.)
DYp12.SetBinContent(31, -0.5*10.)
LOCALp12.SetBinContent(31, 0.0964049*10.)
DXp12.SetBinContent(32, 0.399994*10.)
DYp12.SetBinContent(32, -0.5*10.)
LOCALp12.SetBinContent(32, -0.0149807*10.)
DXp12.SetBinContent(33, 0.399994*10.)
DYp12.SetBinContent(33, -0.5*10.)
LOCALp12.SetBinContent(33, -0.125911*10.)
DXp12.SetBinContent(34, 0.399994*10.)
DYp12.SetBinContent(34, -0.5*10.)
LOCALp12.SetBinContent(34, -0.233016*10.)
DXp12.SetBinContent(35, 0.399994*10.)
DYp12.SetBinContent(35, -0.5*10.)
LOCALp12.SetBinContent(35, -0.33304*10.)
DXp12.SetBinContent(36, 0.399994*10.)
DYp12.SetBinContent(36, -0.5*10.)
LOCALp12.SetBinContent(36, -0.422946*10.)

DXp22.SetBinContent(1, 0*10.)
DYp22.SetBinContent(1, 0*10.)
LOCALp22.SetBinContent(1, 0*10.)
DXp22.SetBinContent(2, 0*10.)
DYp22.SetBinContent(2, 0*10.)
LOCALp22.SetBinContent(2, 0*10.)
DXp22.SetBinContent(3, 0*10.)
DYp22.SetBinContent(3, 0*10.)
LOCALp22.SetBinContent(3, 0*10.)
DXp22.SetBinContent(4, 0*10.)
DYp22.SetBinContent(4, 0*10.)
LOCALp22.SetBinContent(4, 0*10.)
DXp22.SetBinContent(5, 0*10.)
DYp22.SetBinContent(5, 0*10.)
LOCALp22.SetBinContent(5, 0*10.)
DXp22.SetBinContent(6, 0*10.)
DYp22.SetBinContent(6, 0*10.)
LOCALp22.SetBinContent(6, 0*10.)
DXp22.SetBinContent(7, 0*10.)
DYp22.SetBinContent(7, 0*10.)
LOCALp22.SetBinContent(7, 0*10.)
DXp22.SetBinContent(8, 0*10.)
DYp22.SetBinContent(8, 0*10.)
LOCALp22.SetBinContent(8, 0*10.)
DXp22.SetBinContent(9, 0*10.)
DYp22.SetBinContent(9, 0*10.)
LOCALp22.SetBinContent(9, 0*10.)
DXp22.SetBinContent(10, 0*10.)
DYp22.SetBinContent(10, 0*10.)
LOCALp22.SetBinContent(10, 0*10.)
DXp22.SetBinContent(11, 0*10.)
DYp22.SetBinContent(11, 0*10.)
LOCALp22.SetBinContent(11, 0*10.)
DXp22.SetBinContent(12, 0*10.)
DYp22.SetBinContent(12, 0*10.)
LOCALp22.SetBinContent(12, 0*10.)
DXp22.SetBinContent(13, 0*10.)
DYp22.SetBinContent(13, 0*10.)
LOCALp22.SetBinContent(13, 0*10.)
DXp22.SetBinContent(14, 0*10.)
DYp22.SetBinContent(14, 0*10.)
LOCALp22.SetBinContent(14, 0*10.)
DXp22.SetBinContent(15, 0*10.)
DYp22.SetBinContent(15, 0*10.)
LOCALp22.SetBinContent(15, 0*10.)
DXp22.SetBinContent(16, 0*10.)
DYp22.SetBinContent(16, 0*10.)
LOCALp22.SetBinContent(16, 0*10.)
DXp22.SetBinContent(17, 0*10.)
DYp22.SetBinContent(17, 0*10.)
LOCALp22.SetBinContent(17, 0*10.)
DXp22.SetBinContent(18, 0*10.)
DYp22.SetBinContent(18, 0*10.)
LOCALp22.SetBinContent(18, 0*10.)
DXp22.SetBinContent(19, 0*10.)
DYp22.SetBinContent(19, 0*10.)
LOCALp22.SetBinContent(19, 0*10.)
DXp22.SetBinContent(20, 0*10.)
DYp22.SetBinContent(20, 0*10.)
LOCALp22.SetBinContent(20, 0*10.)
DXp22.SetBinContent(21, 0*10.)
DYp22.SetBinContent(21, 0*10.)
LOCALp22.SetBinContent(21, 0*10.)
DXp22.SetBinContent(22, 0*10.)
DYp22.SetBinContent(22, 0*10.)
LOCALp22.SetBinContent(22, 0*10.)
DXp22.SetBinContent(23, 0*10.)
DYp22.SetBinContent(23, 0*10.)
LOCALp22.SetBinContent(23, 0*10.)
DXp22.SetBinContent(24, 0*10.)
DYp22.SetBinContent(24, 0*10.)
LOCALp22.SetBinContent(24, 0*10.)
DXp22.SetBinContent(25, 0*10.)
DYp22.SetBinContent(25, 0*10.)
LOCALp22.SetBinContent(25, 0*10.)
DXp22.SetBinContent(26, 0*10.)
DYp22.SetBinContent(26, 0*10.)
LOCALp22.SetBinContent(26, 0*10.)
DXp22.SetBinContent(27, 0*10.)
DYp22.SetBinContent(27, 0*10.)
LOCALp22.SetBinContent(27, 0*10.)
DXp22.SetBinContent(28, 0*10.)
DYp22.SetBinContent(28, 0*10.)
LOCALp22.SetBinContent(28, 0*10.)
DXp22.SetBinContent(29, 0*10.)
DYp22.SetBinContent(29, 0*10.)
LOCALp22.SetBinContent(29, 0*10.)
DXp22.SetBinContent(30, 0*10.)
DYp22.SetBinContent(30, 0*10.)
LOCALp22.SetBinContent(30, 0*10.)
DXp22.SetBinContent(31, 0*10.)
DYp22.SetBinContent(31, 0*10.)
LOCALp22.SetBinContent(31, 0*10.)
DXp22.SetBinContent(32, 0*10.)
DYp22.SetBinContent(32, 0*10.)
LOCALp22.SetBinContent(32, 0*10.)
DXp22.SetBinContent(33, 0*10.)
DYp22.SetBinContent(33, 0*10.)
LOCALp22.SetBinContent(33, 0*10.)
DXp22.SetBinContent(34, 0*10.)
DYp22.SetBinContent(34, 0*10.)
LOCALp22.SetBinContent(34, 0*10.)
DXp22.SetBinContent(35, 0*10.)
DYp22.SetBinContent(35, 0*10.)
LOCALp22.SetBinContent(35, 0*10.)
DXp22.SetBinContent(36, 0*10.)
DYp22.SetBinContent(36, 0*10.)
LOCALp22.SetBinContent(36, 0*10.)

DXp32.SetBinContent(1, 0*10.)
DYp32.SetBinContent(1, 0*10.)
LOCALp32.SetBinContent(1, 0*10.)
DXp32.SetBinContent(2, 0*10.)
DYp32.SetBinContent(2, 0*10.)
LOCALp32.SetBinContent(2, 0*10.)
DXp32.SetBinContent(3, 0*10.)
DYp32.SetBinContent(3, 0*10.)
LOCALp32.SetBinContent(3, 0*10.)
DXp32.SetBinContent(4, 0*10.)
DYp32.SetBinContent(4, 0*10.)
LOCALp32.SetBinContent(4, 0*10.)
DXp32.SetBinContent(5, 0*10.)
DYp32.SetBinContent(5, 0*10.)
LOCALp32.SetBinContent(5, 0*10.)
DXp32.SetBinContent(6, 0*10.)
DYp32.SetBinContent(6, 0*10.)
LOCALp32.SetBinContent(6, 0*10.)
DXp32.SetBinContent(7, 0*10.)
DYp32.SetBinContent(7, 0*10.)
LOCALp32.SetBinContent(7, 0*10.)
DXp32.SetBinContent(8, 0*10.)
DYp32.SetBinContent(8, 0*10.)
LOCALp32.SetBinContent(8, 0*10.)
DXp32.SetBinContent(9, 0*10.)
DYp32.SetBinContent(9, 0*10.)
LOCALp32.SetBinContent(9, 0*10.)
DXp32.SetBinContent(10, 0*10.)
DYp32.SetBinContent(10, 0*10.)
LOCALp32.SetBinContent(10, 0*10.)
DXp32.SetBinContent(11, 0*10.)
DYp32.SetBinContent(11, 0*10.)
LOCALp32.SetBinContent(11, 0*10.)
DXp32.SetBinContent(12, 0*10.)
DYp32.SetBinContent(12, 0*10.)
LOCALp32.SetBinContent(12, 0*10.)
DXp32.SetBinContent(13, 0*10.)
DYp32.SetBinContent(13, 0*10.)
LOCALp32.SetBinContent(13, 0*10.)
DXp32.SetBinContent(14, 0*10.)
DYp32.SetBinContent(14, 0*10.)
LOCALp32.SetBinContent(14, 0*10.)
DXp32.SetBinContent(15, 0*10.)
DYp32.SetBinContent(15, 0*10.)
LOCALp32.SetBinContent(15, 0*10.)
DXp32.SetBinContent(16, 0*10.)
DYp32.SetBinContent(16, 0*10.)
LOCALp32.SetBinContent(16, 0*10.)
DXp32.SetBinContent(17, 0*10.)
DYp32.SetBinContent(17, 0*10.)
LOCALp32.SetBinContent(17, 0*10.)
DXp32.SetBinContent(18, 0*10.)
DYp32.SetBinContent(18, 0*10.)
LOCALp32.SetBinContent(18, 0*10.)
DXp32.SetBinContent(19, 0*10.)
DYp32.SetBinContent(19, 0*10.)
LOCALp32.SetBinContent(19, 0*10.)
DXp32.SetBinContent(20, 0*10.)
DYp32.SetBinContent(20, 0*10.)
LOCALp32.SetBinContent(20, 0*10.)
DXp32.SetBinContent(21, 0*10.)
DYp32.SetBinContent(21, 0*10.)
LOCALp32.SetBinContent(21, 0*10.)
DXp32.SetBinContent(22, 0*10.)
DYp32.SetBinContent(22, 0*10.)
LOCALp32.SetBinContent(22, 0*10.)
DXp32.SetBinContent(23, 0*10.)
DYp32.SetBinContent(23, 0*10.)
LOCALp32.SetBinContent(23, 0*10.)
DXp32.SetBinContent(24, 0*10.)
DYp32.SetBinContent(24, 0*10.)
LOCALp32.SetBinContent(24, 0*10.)
DXp32.SetBinContent(25, 0*10.)
DYp32.SetBinContent(25, 0*10.)
LOCALp32.SetBinContent(25, 0*10.)
DXp32.SetBinContent(26, 0*10.)
DYp32.SetBinContent(26, 0*10.)
LOCALp32.SetBinContent(26, 0*10.)
DXp32.SetBinContent(27, 0*10.)
DYp32.SetBinContent(27, 0*10.)
LOCALp32.SetBinContent(27, 0*10.)
DXp32.SetBinContent(28, 0*10.)
DYp32.SetBinContent(28, 0*10.)
LOCALp32.SetBinContent(28, 0*10.)
DXp32.SetBinContent(29, 0*10.)
DYp32.SetBinContent(29, 0*10.)
LOCALp32.SetBinContent(29, 0*10.)
DXp32.SetBinContent(30, 0*10.)
DYp32.SetBinContent(30, 0*10.)
LOCALp32.SetBinContent(30, 0*10.)
DXp32.SetBinContent(31, 0*10.)
DYp32.SetBinContent(31, 0*10.)
LOCALp32.SetBinContent(31, 0*10.)
DXp32.SetBinContent(32, 0*10.)
DYp32.SetBinContent(32, 0*10.)
LOCALp32.SetBinContent(32, 0*10.)
DXp32.SetBinContent(33, 0*10.)
DYp32.SetBinContent(33, 0*10.)
LOCALp32.SetBinContent(33, 0*10.)
DXp32.SetBinContent(34, 0*10.)
DYp32.SetBinContent(34, 0*10.)
LOCALp32.SetBinContent(34, 0*10.)
DXp32.SetBinContent(35, 0*10.)
DYp32.SetBinContent(35, 0*10.)
LOCALp32.SetBinContent(35, 0*10.)
DXp32.SetBinContent(36, 0*10.)
DYp32.SetBinContent(36, 0*10.)
LOCALp32.SetBinContent(36, 0*10.)

DXm12.SetBinContent(1, 0.199249*10.)
DYm12.SetBinContent(1, -0.2606*10.)
LOCALm12.SetBinContent(1, 0.2606*10.)
DXm12.SetBinContent(2, 0.0708618*10.)
DYm12.SetBinContent(2, -0.271961*10.)
LOCALm12.SetBinContent(2, 0.280135*10.)
DXm12.SetBinContent(3, -0.0535889*10.)
DYm12.SetBinContent(3, -0.305443*10.)
LOCALm12.SetBinContent(3, 0.268694*10.)
DXm12.SetBinContent(4, -0.170349*10.)
DYm12.SetBinContent(4, -0.360031*10.)
LOCALm12.SetBinContent(4, 0.226622*10.)
DXm12.SetBinContent(5, -0.275848*10.)
DYm12.SetBinContent(5, -0.434067*10.)
LOCALm12.SetBinContent(5, 0.155203*10.)
DXm12.SetBinContent(6, -0.366882*10.)
DYm12.SetBinContent(6, -0.525299*10.)
LOCALm12.SetBinContent(6, 0.0566076*10.)
DXm12.SetBinContent(7, -0.440704*10.)
DYm12.SetBinContent(7, -0.630951*10.)
LOCALm12.SetBinContent(7, -0.0661857*10.)
DXm12.SetBinContent(8, -0.495064*10.)
DYm12.SetBinContent(8, -0.747803*10.)
LOCALm12.SetBinContent(8, -0.209444*10.)
DXm12.SetBinContent(9, -0.528294*10.)
DYm12.SetBinContent(9, -0.872345*10.)
LOCALm12.SetBinContent(9, -0.368787*10.)
DXm12.SetBinContent(10, -0.5394*10.)
DYm12.SetBinContent(10, -1.00073*10.)
LOCALm12.SetBinContent(10, -0.5394*10.)
DXm12.SetBinContent(11, -0.528038*10.)
DYm12.SetBinContent(11, -1.12912*10.)
LOCALm12.SetBinContent(11, -0.716086*10.)
DXm12.SetBinContent(12, -0.494553*10.)
DYm12.SetBinContent(12, -1.25357*10.)
LOCALm12.SetBinContent(12, -0.893474*10.)
DXm12.SetBinContent(13, -0.439972*10.)
DYm12.SetBinContent(13, -1.37033*10.)
LOCALm12.SetBinContent(13, -1.06619*10.)
DXm12.SetBinContent(14, -0.365936*10.)
DYm12.SetBinContent(14, -1.47583*10.)
LOCALm12.SetBinContent(14, -1.22897*10.)
DXm12.SetBinContent(15, -0.274719*10.)
DYm12.SetBinContent(15, -1.56689*10.)
LOCALm12.SetBinContent(15, -1.3769*10.)
DXm12.SetBinContent(16, -0.169067*10.)
DYm12.SetBinContent(16, -1.6407*10.)
LOCALm12.SetBinContent(16, -1.50542*10.)
DXm12.SetBinContent(17, -0.0521851*10.)
DYm12.SetBinContent(17, -1.69506*10.)
LOCALm12.SetBinContent(17, -1.61068*10.)
DXm12.SetBinContent(18, 0.0723267*10.)
DYm12.SetBinContent(18, -1.72829*10.)
LOCALm12.SetBinContent(18, -1.68948*10.)
DXm12.SetBinContent(19, 0.200745*10.)
DYm12.SetBinContent(19, -1.7394*10.)
LOCALm12.SetBinContent(19, -1.7394*10.)
DXm12.SetBinContent(20, 0.329132*10.)
DYm12.SetBinContent(20, -1.72803*10.)
LOCALm12.SetBinContent(20, -1.75894*10.)
DXm12.SetBinContent(21, 0.453583*10.)
DYm12.SetBinContent(21, -1.69456*10.)
LOCALm12.SetBinContent(21, -1.7475*10.)
DXm12.SetBinContent(22, 0.570343*10.)
DYm12.SetBinContent(22, -1.63997*10.)
LOCALm12.SetBinContent(22, -1.70543*10.)
DXm12.SetBinContent(23, 0.675842*10.)
DYm12.SetBinContent(23, -1.56593*10.)
LOCALm12.SetBinContent(23, -1.634*10.)
DXm12.SetBinContent(24, 0.766891*10.)
DYm12.SetBinContent(24, -1.4747*10.)
LOCALm12.SetBinContent(24, -1.53539*10.)
DXm12.SetBinContent(25, 0.840714*10.)
DYm12.SetBinContent(25, -1.36905*10.)
LOCALm12.SetBinContent(25, -1.4126*10.)
DXm12.SetBinContent(26, 0.895058*10.)
DYm12.SetBinContent(26, -1.2522*10.)
LOCALm12.SetBinContent(26, -1.26936*10.)
DXm12.SetBinContent(27, 0.928295*10.)
DYm12.SetBinContent(27, -1.12766*10.)
LOCALm12.SetBinContent(27, -1.11001*10.)
DXm12.SetBinContent(28, 0.9394*10.)
DYm12.SetBinContent(28, -0.999268*10.)
LOCALm12.SetBinContent(28, -0.9394*10.)
DXm12.SetBinContent(29, 0.92804*10.)
DYm12.SetBinContent(29, -0.87088*10.)
LOCALm12.SetBinContent(29, -0.762714*10.)
DXm12.SetBinContent(30, 0.894554*10.)
DYm12.SetBinContent(30, -0.746429*10.)
LOCALm12.SetBinContent(30, -0.585312*10.)
DXm12.SetBinContent(31, 0.839966*10.)
DYm12.SetBinContent(31, -0.629669*10.)
LOCALm12.SetBinContent(31, -0.412597*10.)
DXm12.SetBinContent(32, 0.76593*10.)
DYm12.SetBinContent(32, -0.52417*10.)
LOCALm12.SetBinContent(32, -0.249807*10.)
DXm12.SetBinContent(33, 0.674713*10.)
DYm12.SetBinContent(33, -0.433105*10.)
LOCALm12.SetBinContent(33, -0.101919*10.)
DXm12.SetBinContent(34, 0.569061*10.)
DYm12.SetBinContent(34, -0.359299*10.)
LOCALm12.SetBinContent(34, 0.0266312*10.)
DXm12.SetBinContent(35, 0.452209*10.)
DYm12.SetBinContent(35, -0.304939*10.)
LOCALm12.SetBinContent(35, 0.131884*10.)
DXm12.SetBinContent(36, 0.327667*10.)
DYm12.SetBinContent(36, -0.271706*10.)
LOCALm12.SetBinContent(36, 0.210679*10.)

DXm22.SetBinContent(1, 0.999878*10.)
DYm22.SetBinContent(1, 0.36855*10.)
LOCALm22.SetBinContent(1, -0.36855*10.)
DXm22.SetBinContent(2, 0.935852*10.)
DYm22.SetBinContent(2, 0.36293*10.)
LOCALm22.SetBinContent(2, -0.194908*10.)
DXm22.SetBinContent(3, 0.87384*10.)
DYm22.SetBinContent(3, 0.346283*10.)
LOCALm22.SetBinContent(3, -0.0265285*10.)
DXm22.SetBinContent(4, 0.815613*10.)
DYm22.SetBinContent(4, 0.319122*10.)
LOCALm22.SetBinContent(4, 0.131438*10.)
DXm22.SetBinContent(5, 0.763*10.)
DYm22.SetBinContent(5, 0.282257*10.)
LOCALm22.SetBinContent(5, 0.274226*10.)
DXm22.SetBinContent(6, 0.71759*10.)
DYm22.SetBinContent(6, 0.236786*10.)
LOCALm22.SetBinContent(6, 0.397503*10.)
DXm22.SetBinContent(7, 0.680756*10.)
DYm22.SetBinContent(7, 0.184174*10.)
LOCALm22.SetBinContent(7, 0.497465*10.)
DXm22.SetBinContent(8, 0.653625*10.)
DYm22.SetBinContent(8, 0.125916*10.)
LOCALm22.SetBinContent(8, 0.571141*10.)
DXm22.SetBinContent(9, 0.637024*10.)
DYm22.SetBinContent(9, 0.0638428*10.)
LOCALm22.SetBinContent(9, 0.61626*10.)
DXm22.SetBinContent(10, 0.63145*10.)
DYm22.SetBinContent(10, -0.00012207*10.)
LOCALm22.SetBinContent(10, 0.63145*10.)
DXm22.SetBinContent(11, 0.63707*10.)
DYm22.SetBinContent(11, -0.0641479*10.)
LOCALm22.SetBinContent(11, 0.616252*10.)
DXm22.SetBinContent(12, 0.653717*10.)
DYm22.SetBinContent(12, -0.12616*10.)
LOCALm22.SetBinContent(12, 0.571144*10.)
DXm22.SetBinContent(13, 0.680878*10.)
DYm22.SetBinContent(13, -0.184387*10.)
LOCALm22.SetBinContent(13, 0.497464*10.)
DXm22.SetBinContent(14, 0.717743*10.)
DYm22.SetBinContent(14, -0.237*10.)
LOCALm22.SetBinContent(14, 0.397483*10.)
DXm22.SetBinContent(15, 0.763214*10.)
DYm22.SetBinContent(15, -0.28241*10.)
LOCALm22.SetBinContent(15, 0.274246*10.)
DXm22.SetBinContent(16, 0.815826*10.)
DYm22.SetBinContent(16, -0.319244*10.)
LOCALm22.SetBinContent(16, 0.131439*10.)
DXm22.SetBinContent(17, 0.874084*10.)
DYm22.SetBinContent(17, -0.346375*10.)
LOCALm22.SetBinContent(17, -0.0265311*10.)
DXm22.SetBinContent(18, 0.936157*10.)
DYm22.SetBinContent(18, -0.362976*10.)
LOCALm22.SetBinContent(18, -0.1949*10.)
DXm22.SetBinContent(19, 1.00012*10.)
DYm22.SetBinContent(19, -0.36855*10.)
LOCALm22.SetBinContent(19, -0.36855*10.)
DXm22.SetBinContent(20, 1.06415*10.)
DYm22.SetBinContent(20, -0.36293*10.)
LOCALm22.SetBinContent(20, -0.542204*10.)
DXm22.SetBinContent(21, 1.12616*10.)
DYm22.SetBinContent(21, -0.346283*10.)
LOCALm22.SetBinContent(21, -0.710569*10.)
DXm22.SetBinContent(22, 1.18439*10.)
DYm22.SetBinContent(22, -0.319122*10.)
LOCALm22.SetBinContent(22, -0.868562*10.)
DXm22.SetBinContent(23, 1.237*10.)
DYm22.SetBinContent(23, -0.282257*10.)
LOCALm22.SetBinContent(23, -1.01135*10.)
DXm22.SetBinContent(24, 1.28241*10.)
DYm22.SetBinContent(24, -0.236786*10.)
LOCALm22.SetBinContent(24, -1.13459*10.)
DXm22.SetBinContent(25, 1.31924*10.)
DYm22.SetBinContent(25, -0.184174*10.)
LOCALm22.SetBinContent(25, -1.23459*10.)
DXm22.SetBinContent(26, 1.34637*10.)
DYm22.SetBinContent(26, -0.125916*10.)
LOCALm22.SetBinContent(26, -1.30824*10.)
DXm22.SetBinContent(27, 1.36298*10.)
DYm22.SetBinContent(27, -0.0638428*10.)
LOCALm22.SetBinContent(27, -1.35336*10.)
DXm22.SetBinContent(28, 1.36855*10.)
DYm22.SetBinContent(28, 0.00012207*10.)
LOCALm22.SetBinContent(28, -1.36855*10.)
DXm22.SetBinContent(29, 1.36293*10.)
DYm22.SetBinContent(29, 0.0641479*10.)
LOCALm22.SetBinContent(29, -1.35336*10.)
DXm22.SetBinContent(30, 1.34628*10.)
DYm22.SetBinContent(30, 0.12616*10.)
LOCALm22.SetBinContent(30, -1.30824*10.)
DXm22.SetBinContent(31, 1.31912*10.)
DYm22.SetBinContent(31, 0.184387*10.)
LOCALm22.SetBinContent(31, -1.23459*10.)
DXm22.SetBinContent(32, 1.28226*10.)
DYm22.SetBinContent(32, 0.237*10.)
LOCALm22.SetBinContent(32, -1.13461*10.)
DXm22.SetBinContent(33, 1.23679*10.)
DYm22.SetBinContent(33, 0.28241*10.)
LOCALm22.SetBinContent(33, -1.01133*10.)
DXm22.SetBinContent(34, 1.18417*10.)
DYm22.SetBinContent(34, 0.319244*10.)
LOCALm22.SetBinContent(34, -0.868561*10.)
DXm22.SetBinContent(35, 1.12592*10.)
DYm22.SetBinContent(35, 0.346375*10.)
LOCALm22.SetBinContent(35, -0.710571*10.)
DXm22.SetBinContent(36, 1.06384*10.)
DYm22.SetBinContent(36, 0.362976*10.)
LOCALm22.SetBinContent(36, -0.542196*10.)

DXm32.SetBinContent(1, 0.999878*10.)
DYm32.SetBinContent(1, 0.36855*10.)
LOCALm32.SetBinContent(1, 0.36855*10.)
DXm32.SetBinContent(2, 0.935852*10.)
DYm32.SetBinContent(2, 0.36293*10.)
LOCALm32.SetBinContent(2, 0.194908*10.)
DXm32.SetBinContent(3, 0.87384*10.)
DYm32.SetBinContent(3, 0.346283*10.)
LOCALm32.SetBinContent(3, 0.0265285*10.)
DXm32.SetBinContent(4, 0.815613*10.)
DYm32.SetBinContent(4, 0.319122*10.)
LOCALm32.SetBinContent(4, -0.131438*10.)
DXm32.SetBinContent(5, 0.763*10.)
DYm32.SetBinContent(5, 0.282257*10.)
LOCALm32.SetBinContent(5, -0.274226*10.)
DXm32.SetBinContent(6, 0.71759*10.)
DYm32.SetBinContent(6, 0.236786*10.)
LOCALm32.SetBinContent(6, -0.397503*10.)
DXm32.SetBinContent(7, 0.680756*10.)
DYm32.SetBinContent(7, 0.184174*10.)
LOCALm32.SetBinContent(7, -0.497465*10.)
DXm32.SetBinContent(8, 0.653625*10.)
DYm32.SetBinContent(8, 0.125916*10.)
LOCALm32.SetBinContent(8, -0.571141*10.)
DXm32.SetBinContent(9, 0.637024*10.)
DYm32.SetBinContent(9, 0.0638428*10.)
LOCALm32.SetBinContent(9, -0.61626*10.)
DXm32.SetBinContent(10, 0.63145*10.)
DYm32.SetBinContent(10, -0.00012207*10.)
LOCALm32.SetBinContent(10, -0.63145*10.)
DXm32.SetBinContent(11, 0.63707*10.)
DYm32.SetBinContent(11, -0.0641479*10.)
LOCALm32.SetBinContent(11, -0.616252*10.)
DXm32.SetBinContent(12, 0.653717*10.)
DYm32.SetBinContent(12, -0.12616*10.)
LOCALm32.SetBinContent(12, -0.571144*10.)
DXm32.SetBinContent(13, 0.680878*10.)
DYm32.SetBinContent(13, -0.184387*10.)
LOCALm32.SetBinContent(13, -0.497464*10.)
DXm32.SetBinContent(14, 0.717743*10.)
DYm32.SetBinContent(14, -0.237*10.)
LOCALm32.SetBinContent(14, -0.397483*10.)
DXm32.SetBinContent(15, 0.763214*10.)
DYm32.SetBinContent(15, -0.28241*10.)
LOCALm32.SetBinContent(15, -0.274246*10.)
DXm32.SetBinContent(16, 0.815826*10.)
DYm32.SetBinContent(16, -0.319244*10.)
LOCALm32.SetBinContent(16, -0.131439*10.)
DXm32.SetBinContent(17, 0.874084*10.)
DYm32.SetBinContent(17, -0.346375*10.)
LOCALm32.SetBinContent(17, 0.0265311*10.)
DXm32.SetBinContent(18, 0.936157*10.)
DYm32.SetBinContent(18, -0.362976*10.)
LOCALm32.SetBinContent(18, 0.1949*10.)
DXm32.SetBinContent(19, 1.00012*10.)
DYm32.SetBinContent(19, -0.36855*10.)
LOCALm32.SetBinContent(19, 0.36855*10.)
DXm32.SetBinContent(20, 1.06415*10.)
DYm32.SetBinContent(20, -0.36293*10.)
LOCALm32.SetBinContent(20, 0.542204*10.)
DXm32.SetBinContent(21, 1.12616*10.)
DYm32.SetBinContent(21, -0.346283*10.)
LOCALm32.SetBinContent(21, 0.710569*10.)
DXm32.SetBinContent(22, 1.18439*10.)
DYm32.SetBinContent(22, -0.319122*10.)
LOCALm32.SetBinContent(22, 0.868562*10.)
DXm32.SetBinContent(23, 1.237*10.)
DYm32.SetBinContent(23, -0.282257*10.)
LOCALm32.SetBinContent(23, 1.01135*10.)
DXm32.SetBinContent(24, 1.28241*10.)
DYm32.SetBinContent(24, -0.236786*10.)
LOCALm32.SetBinContent(24, 1.13459*10.)
DXm32.SetBinContent(25, 1.31924*10.)
DYm32.SetBinContent(25, -0.184174*10.)
LOCALm32.SetBinContent(25, 1.23459*10.)
DXm32.SetBinContent(26, 1.34637*10.)
DYm32.SetBinContent(26, -0.125916*10.)
LOCALm32.SetBinContent(26, 1.30824*10.)
DXm32.SetBinContent(27, 1.36298*10.)
DYm32.SetBinContent(27, -0.0638428*10.)
LOCALm32.SetBinContent(27, 1.35336*10.)
DXm32.SetBinContent(28, 1.36855*10.)
DYm32.SetBinContent(28, 0.00012207*10.)
LOCALm32.SetBinContent(28, 1.36855*10.)
DXm32.SetBinContent(29, 1.36293*10.)
DYm32.SetBinContent(29, 0.0641479*10.)
LOCALm32.SetBinContent(29, 1.35336*10.)
DXm32.SetBinContent(30, 1.34628*10.)
DYm32.SetBinContent(30, 0.12616*10.)
LOCALm32.SetBinContent(30, 1.30824*10.)
DXm32.SetBinContent(31, 1.31912*10.)
DYm32.SetBinContent(31, 0.184387*10.)
LOCALm32.SetBinContent(31, 1.23459*10.)
DXm32.SetBinContent(32, 1.28226*10.)
DYm32.SetBinContent(32, 0.237*10.)
LOCALm32.SetBinContent(32, 1.13461*10.)
DXm32.SetBinContent(33, 1.23679*10.)
DYm32.SetBinContent(33, 0.28241*10.)
LOCALm32.SetBinContent(33, 1.01133*10.)
DXm32.SetBinContent(34, 1.18417*10.)
DYm32.SetBinContent(34, 0.319244*10.)
LOCALm32.SetBinContent(34, 0.868561*10.)
DXm32.SetBinContent(35, 1.12592*10.)
DYm32.SetBinContent(35, 0.346375*10.)
LOCALm32.SetBinContent(35, 0.710571*10.)
DXm32.SetBinContent(36, 1.06384*10.)
DYm32.SetBinContent(36, 0.362976*10.)
LOCALm32.SetBinContent(36, 0.542196*10.)

hm12.SetXTitle("ME-1/2 chamber number")
hp12.SetXTitle("ME+1/2 chamber number")
hm22.SetXTitle("ME-2/2 chamber number")
hp22.SetXTitle("ME+2/2 chamber number")
hm32.SetXTitle("ME-3/2 chamber number")
hp32.SetXTitle("ME+3/2 chamber number")
hm12.SetYTitle("Local #delta_{x} (mm)")
hp12.SetYTitle("Local #delta_{x} (mm)")
hm22.SetYTitle("Local #delta_{x} (mm)")
hp22.SetYTitle("Local #delta_{x} (mm)")
hm32.SetYTitle("Local #delta_{x} (mm)")
hp32.SetYTitle("Local #delta_{x} (mm)")

hm12.SetAxisRange(-30., 30., "Y")
hp12.SetAxisRange(-30., 30., "Y")
hm22.SetAxisRange(-30., 30., "Y")
hp22.SetAxisRange(-30., 30., "Y")
hm32.SetAxisRange(-30., 30., "Y")
hp32.SetAxisRange(-30., 30., "Y")

c1.Clear()
c1.Divide(3, 2)

c1.GetPad(1).cd()
hp12.Draw()
hp13.Draw("same")
LOCALp12.Draw("same")
tlegend1 = ROOT.TLegend(0.75, 0.8, 0.95, 0.95)
tlegend1.SetFillColor(ROOT.kWhite)
tlegend1.SetBorderSize(1)
tlegend1.AddEntry(hm12, "ME+1/2", "pl")
tlegend1.AddEntry(hm13, "ME+1/3", "pl")
tlegend1.Draw()

c1.GetPad(2).cd()
hp22.Draw()
LOCALp22.Draw("same")

c1.GetPad(3).cd()
hp32.Draw()
LOCALp32.Draw("same")

c1.GetPad(4).cd()
hm12.Draw()
hm13.Draw("same")
LOCALm12.Draw("same")
tlegend2 = ROOT.TLegend(0.75, 0.8, 0.95, 0.95)
tlegend2.SetFillColor(ROOT.kWhite)
tlegend2.SetBorderSize(1)
tlegend2.AddEntry(hm12, "ME-1/2", "pl")
tlegend2.AddEntry(hm13, "ME-1/3", "pl")
tlegend2.Draw()

c1.GetPad(5).cd()
hm22.Draw()
LOCALm22.Draw("same")

c1.GetPad(6).cd()
hm32.Draw()
LOCALm32.Draw("same")

c1.SaveAs("Jimsplots_localcoords.pdf")



# c1.Clear()
# hp12.Draw()
# hp13.Draw("same")
# LOCALp12.Draw("same")

# f = ROOT.TF1("f", "[0]*0 + 1.5 + 0.2*sin(x*2.*3.1415926/36.) - 10.*cos(x*2.*3.1415926/36.)", 0.5, 36.5)
# hm12.Fit(f)
# hm13.Draw("same")

DXm12.SetLineColor(ROOT.kRed)
DYm12.SetLineColor(ROOT.kRed)

c1.Clear()
DXm12.Draw()
DYm12.Draw()
