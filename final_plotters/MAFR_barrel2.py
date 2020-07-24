import ROOT, os, minuit
from math import *
execfile("/home/jpivarski/bin/tdrstyle.py")
c1 = ROOT.TCanvas()

directory_aligned = "/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_sync1_residdiff/withCenteredTracker/"
tfiles_aligned = [ROOT.TFile(directory_aligned + f) for f in os.listdir(directory_aligned) if f[-5:] == ".root"]
baddies = [(-1, 1, 12), (-1, 2, 8), (1, 2, 2), (1, 3, 8)] + [(wheel, station, sector) for wheel in -1, 0, 1 for station in 1, 2, 3, 4 for sector in 1, 7]
outfile_part = "may29"

directory_aligned = "/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_sync1_residdiff/withOldTracker/"
tfiles_aligned = [ROOT.TFile(directory_aligned + f) for f in os.listdir(directory_aligned) if f[-5:] == ".root"]
baddies = [(-1, 2, 8), (1, 2, 2), (1, 3, 8)] + [(wheel, station, sector) for wheel in -1, 0, 1 for station in 1, 2, 3, 4 for sector in 1, 7]
outfile_part = "may25"

directory_aligned = "/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_sync1_residdiff/v11/"
tfiles_aligned = [ROOT.TFile(directory_aligned + f) for f in os.listdir(directory_aligned) if f[-5:] == ".root"]
execfile("previously_aligned.py")
baddies = []
for wheel in -1, 0, 1:
    for station in 1, 2, 3, 4:
        for sector in 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12:
            if ("DT", wheel, station, sector) not in previously_aligned:
                baddies.append((wheel, station, sector))
outfile_part = "v11"

directory_aligned = "/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_sync1_residdiff/v4/"
tfiles_aligned = [ROOT.TFile(directory_aligned + f) for f in os.listdir(directory_aligned) if f[-5:] == ".root"]
baddies = []
outfile_part = "v4"

def diff12x(which, wheel, sector):
    global hist
    hist = ROOT.TH1F("hist", "", 100, -30., 30.)
    if wheel == -2: wheelletter = "A"
    elif wheel == -1: wheelletter = "B"
    elif wheel == 0: wheelletter = "C"
    elif wheel == 1: wheelletter = "D"
    elif wheel == 2: wheelletter = "E"
    for tfile in which:
        hist.Add(tfile.Get("AlignmentMonitorMuonResidualsSummary/iter1/DTdiff12x_%s_%d" % (wheelletter, sector)))
    return hist

def diff23x(which, wheel, sector):
    global hist
    hist = ROOT.TH1F("hist", "", 100, -30., 30.)
    if wheel == -2: wheelletter = "A"
    elif wheel == -1: wheelletter = "B"
    elif wheel == 0: wheelletter = "C"
    elif wheel == 1: wheelletter = "D"
    elif wheel == 2: wheelletter = "E"
    for tfile in which:
        hist.Add(tfile.Get("AlignmentMonitorMuonResidualsSummary/iter1/DTdiff23x_%s_%d" % (wheelletter, sector)))
    return hist

def diff34x(which, wheel, sector):
    global hist
    hist = ROOT.TH1F("hist", "", 100, -30., 30.)
    if wheel == -2: wheelletter = "A"
    elif wheel == -1: wheelletter = "B"
    elif wheel == 0: wheelletter = "C"
    elif wheel == 1: wheelletter = "D"
    elif wheel == 2: wheelletter = "E"
    for tfile in which:
        hist.Add(tfile.Get("AlignmentMonitorMuonResidualsSummary/iter1/DTdiff34x_%s_%d" % (wheelletter, sector)))
    return hist

def diff12phi(which, wheel, sector):
    global hist
    hist = ROOT.TH1F("hist", "", 100, -30., 30.)
    if wheel == -2: wheelletter = "A"
    elif wheel == -1: wheelletter = "B"
    elif wheel == 0: wheelletter = "C"
    elif wheel == 1: wheelletter = "D"
    elif wheel == 2: wheelletter = "E"
    for tfile in which:
        hist.Add(tfile.Get("AlignmentMonitorMuonResidualsSummary/iter1/DTdiff12phi_%s_%d" % (wheelletter, sector)))
    return hist

def diff23phi(which, wheel, sector):
    global hist
    hist = ROOT.TH1F("hist", "", 100, -30., 30.)
    if wheel == -2: wheelletter = "A"
    elif wheel == -1: wheelletter = "B"
    elif wheel == 0: wheelletter = "C"
    elif wheel == 1: wheelletter = "D"
    elif wheel == 2: wheelletter = "E"
    for tfile in which:
        hist.Add(tfile.Get("AlignmentMonitorMuonResidualsSummary/iter1/DTdiff23phi_%s_%d" % (wheelletter, sector)))
    return hist

def diff34phi(which, wheel, sector):
    global hist
    hist = ROOT.TH1F("hist", "", 100, -30., 30.)
    if wheel == -2: wheelletter = "A"
    elif wheel == -1: wheelletter = "B"
    elif wheel == 0: wheelletter = "C"
    elif wheel == 1: wheelletter = "D"
    elif wheel == 2: wheelletter = "E"
    for tfile in which:
        hist.Add(tfile.Get("AlignmentMonitorMuonResidualsSummary/iter1/DTdiff34phi_%s_%d" % (wheelletter, sector)))
    return hist

def fitvoigt(h):
    global func
    def chi2(norm, mean, sigma, gamma):
        output = 0.
        for i in xrange(1, h.GetNbinsX()+1):
            xi = h.GetBinCenter(i)
            yi = h.GetBinContent(i)
            yerri = h.GetBinError(i)
            if yerri > 0.:
                output += (yi - norm*ROOT.TMath.Voigt(xi - mean, sigma, gamma))**2/yerri**2
        return output
    m = minuit.Minuit(chi2)
    m.values["norm"] = h.GetEntries()*60./100.
    m.values["mean"] = h.GetMean()
    m.values["sigma"] = h.GetRMS()
    m.values["gamma"] = h.GetRMS()*0.1
    try:
        m.migrad()
    except minuit.MinuitError:
        return None, None, None
    func = ROOT.TH1F("func", "", 100, -30., 30.)
    for i in xrange(1, func.GetNbinsX()+1):
        xi = func.GetBinCenter(i)
        func.SetBinContent(i, m.values["norm"]*ROOT.TMath.Voigt(xi - m.values["mean"], m.values["sigma"], m.values["gamma"]))
    func.SetLineColor(ROOT.kRed)
    func.SetLineWidth(2)
    return func, m.values["mean"], m.errors["mean"]

diff12xplot = ROOT.TH1F("diff12xplot", "", 36, 0.5, 36.5)
diff12xplot_mean = ROOT.TH1F("diff12xplot_mean", "", 36, 0.5, 36.5)
diff12xplot_mean.SetMarkerStyle(29)
diff12xplot.SetMarkerColor(ROOT.kBlue)
diff12xplot.SetLineColor(ROOT.kBlue)
diff12xplot_mean.SetMarkerColor(ROOT.kBlue)
diff12xplot_mean.SetLineColor(ROOT.kBlue)
diff12xhist = ROOT.TH1F("diff12xhist", "", 100, -10., 10.)

diff23xplot = ROOT.TH1F("diff23xplot", "", 36, 0.5, 36.5)
diff23xplot_mean = ROOT.TH1F("diff23xplot_mean", "", 36, 0.5, 36.5)
diff23xplot_mean.SetMarkerStyle(29)
diff23xplot.SetMarkerColor(ROOT.kRed)
diff23xplot.SetLineColor(ROOT.kRed)
diff23xplot_mean.SetMarkerColor(ROOT.kRed)
diff23xplot_mean.SetLineColor(ROOT.kRed)
diff23xhist = ROOT.TH1F("diff23xhist", "", 100, -10., 10.)

diff34xplot = ROOT.TH1F("diff34xplot", "", 36, 0.5, 36.5)
diff34xplot_mean = ROOT.TH1F("diff34xplot_mean", "", 36, 0.5, 36.5)
diff34xplot_mean.SetMarkerStyle(29)
diff34xplot.SetMarkerColor(ROOT.kGreen+2)
diff34xplot.SetLineColor(ROOT.kGreen+2)
diff34xplot_mean.SetMarkerColor(ROOT.kGreen+2)
diff34xplot_mean.SetLineColor(ROOT.kGreen+2)
diff34xhist = ROOT.TH1F("diff34xhist", "", 100, -10., 10.)

diff12phiplot = ROOT.TH1F("diff12phiplot", "", 36, 0.5, 36.5)
diff12phiplot_mean = ROOT.TH1F("diff12phiplot_mean", "", 36, 0.5, 36.5)
diff12phiplot_mean.SetMarkerStyle(29)
diff12phiplot.SetMarkerColor(ROOT.kBlue)
diff12phiplot.SetLineColor(ROOT.kBlue)
diff12phiplot_mean.SetMarkerColor(ROOT.kBlue)
diff12phiplot_mean.SetLineColor(ROOT.kBlue)
diff12phihist = ROOT.TH1F("diff12phihist", "", 100, -10., 10.)

diff23phiplot = ROOT.TH1F("diff23phiplot", "", 36, 0.5, 36.5)
diff23phiplot_mean = ROOT.TH1F("diff23phiplot_mean", "", 36, 0.5, 36.5)
diff23phiplot_mean.SetMarkerStyle(29)
diff23phiplot.SetMarkerColor(ROOT.kRed)
diff23phiplot.SetLineColor(ROOT.kRed)
diff23phiplot_mean.SetMarkerColor(ROOT.kRed)
diff23phiplot_mean.SetLineColor(ROOT.kRed)
diff23phihist = ROOT.TH1F("diff23phihist", "", 100, -10., 10.)

diff34phiplot = ROOT.TH1F("diff34phiplot", "", 36, 0.5, 36.5)
diff34phiplot_mean = ROOT.TH1F("diff34phiplot_mean", "", 36, 0.5, 36.5)
diff34phiplot_mean.SetMarkerStyle(29)
diff34phiplot.SetMarkerColor(ROOT.kGreen+2)
diff34phiplot.SetLineColor(ROOT.kGreen+2)
diff34phiplot_mean.SetMarkerColor(ROOT.kGreen+2)
diff34phiplot_mean.SetLineColor(ROOT.kGreen+2)
diff34phihist = ROOT.TH1F("diff34phihist", "", 100, -10., 10.)

for wheel in -1, 0, 1:
    for sector in 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12:
        for makehist, plot1, plot2, plot3, stA, stB in ((diff12x, diff12xplot, diff12xplot_mean, diff12xhist, 1, 2),
                                                        (diff23x, diff23xplot, diff23xplot_mean, diff23xhist, 2, 3),
                                                        (diff34x, diff34xplot, diff34xplot_mean, diff34xhist, 3, 4),
                                                        (diff12phi, diff12phiplot, diff12phiplot_mean, diff12phihist, 1, 2),
                                                        (diff23phi, diff23phiplot, diff23phiplot_mean, diff23phihist, 2, 3),
                                                        (diff34phi, diff34phiplot, diff34phiplot_mean, diff34phihist, 3, 4)):
            bin = (wheel+1)*12 + sector
            if (wheel, stA, sector) in baddies or (wheel, stB, sector) in baddies:
                plot1.SetBinContent(bin, 2000.)
                plot1.SetBinError(bin, 1000.)
                plot2.SetBinContent(bin, 2000.)
                plot2.SetBinError(bin, 1000.)
            else:
                hist = makehist(tfiles_aligned, wheel, sector)
                func, mean, meanerr = fitvoigt(hist)
                if func is not None:
                    plot1.SetBinContent(bin, mean)
                    plot1.SetBinError(bin, meanerr)
                else:
                    plot1.SetBinContent(bin, 2000.)
                    plot1.SetBinError(bin, 1000.)
                mean = hist.GetMean()
                plot2.SetBinContent(bin, mean)
                plot2.SetBinError(bin, 1e-10)
                plot3.Fill(mean)

tlegend = ROOT.TLegend(0.75, 0.7, 0.95, 0.95)
tlegend.SetFillColor(ROOT.kWhite)
tlegend.SetBorderSize(1)
tlegend.AddEntry(diff12xplot, "MB2-MB1 fit", "pl")
tlegend.AddEntry(diff12xplot_mean, "MB2-MB1 mean", "p")
tlegend.AddEntry(diff23xplot, "MB3-MB2 fit", "pl")
tlegend.AddEntry(diff23xplot_mean, "MBd3-MB2 mean", "p")
tlegend.AddEntry(diff34xplot, "MB4-MB3 fit", "pl")
tlegend.AddEntry(diff34xplot_mean, "MB4-MB3 mean", "p")

diff12xplot.SetAxisRange(-9., 9., "Y")
diff12xplot.GetXaxis().SetBinLabel(1, "wh-1")
diff12xplot.GetXaxis().SetBinLabel(2, "")
diff12xplot.GetXaxis().SetBinLabel(3, "")
diff12xplot.GetXaxis().SetBinLabel(4, "4")
diff12xplot.GetXaxis().SetBinLabel(5, "5")
diff12xplot.GetXaxis().SetBinLabel(6, "6")
diff12xplot.GetXaxis().SetBinLabel(7, "7")
diff12xplot.GetXaxis().SetBinLabel(8, "8")
diff12xplot.GetXaxis().SetBinLabel(9, "9")
diff12xplot.GetXaxis().SetBinLabel(10, "10")
diff12xplot.GetXaxis().SetBinLabel(11, "11")
diff12xplot.GetXaxis().SetBinLabel(12, "")
diff12xplot.GetXaxis().SetBinLabel(12+1, "wh 0")
diff12xplot.GetXaxis().SetBinLabel(12+2, "")
diff12xplot.GetXaxis().SetBinLabel(12+3, "")
diff12xplot.GetXaxis().SetBinLabel(12+4, "4")
diff12xplot.GetXaxis().SetBinLabel(12+5, "5")
diff12xplot.GetXaxis().SetBinLabel(12+6, "6")
diff12xplot.GetXaxis().SetBinLabel(12+7, "7")
diff12xplot.GetXaxis().SetBinLabel(12+8, "8")
diff12xplot.GetXaxis().SetBinLabel(12+9, "9")
diff12xplot.GetXaxis().SetBinLabel(12+10, "10")
diff12xplot.GetXaxis().SetBinLabel(12+11, "11")
diff12xplot.GetXaxis().SetBinLabel(12+12, "")
diff12xplot.GetXaxis().SetBinLabel(24+1, "wh+1")
diff12xplot.GetXaxis().SetBinLabel(24+2, "")
diff12xplot.GetXaxis().SetBinLabel(24+3, "")
diff12xplot.GetXaxis().SetBinLabel(24+4, "4")
diff12xplot.GetXaxis().SetBinLabel(24+5, "5")
diff12xplot.GetXaxis().SetBinLabel(24+6, "6")
diff12xplot.GetXaxis().SetBinLabel(24+7, "7")
diff12xplot.GetXaxis().SetBinLabel(24+8, "8")
diff12xplot.GetXaxis().SetBinLabel(24+9, "9")
diff12xplot.GetXaxis().SetBinLabel(24+10, "10")
diff12xplot.GetXaxis().SetBinLabel(24+11, "11")
diff12xplot.GetXaxis().SetBinLabel(24+12, "12")
diff12xplot.SetYTitle("Local x residuals difference (mm)")
diff12xplot.GetYaxis().CenterTitle()
diff12xplot.GetYaxis().SetTitleOffset(0.8)

diff12xplot.Draw("e1")
diff12xplot_mean.Draw("same")
diff23xplot.Draw("samee1")
diff23xplot_mean.Draw("same")
diff34xplot.Draw("samee1")
diff34xplot_mean.Draw("same")
tlegend.Draw()
c1.SaveAs("diffxsector_" + outfile_part + ".pdf")

diff12phiplot.SetAxisRange(-9., 9., "Y")
diff12phiplot.GetXaxis().SetBinLabel(1, "wh-1")
diff12phiplot.GetXaxis().SetBinLabel(2, "")
diff12phiplot.GetXaxis().SetBinLabel(3, "")
diff12phiplot.GetXaxis().SetBinLabel(4, "4")
diff12phiplot.GetXaxis().SetBinLabel(5, "5")
diff12phiplot.GetXaxis().SetBinLabel(6, "6")
diff12phiplot.GetXaxis().SetBinLabel(7, "7")
diff12phiplot.GetXaxis().SetBinLabel(8, "8")
diff12phiplot.GetXaxis().SetBinLabel(9, "9")
diff12phiplot.GetXaxis().SetBinLabel(10, "10")
diff12phiplot.GetXaxis().SetBinLabel(11, "11")
diff12phiplot.GetXaxis().SetBinLabel(12, "")
diff12phiplot.GetXaxis().SetBinLabel(12+1, "wh 0")
diff12phiplot.GetXaxis().SetBinLabel(12+2, "")
diff12phiplot.GetXaxis().SetBinLabel(12+3, "")
diff12phiplot.GetXaxis().SetBinLabel(12+4, "4")
diff12phiplot.GetXaxis().SetBinLabel(12+5, "5")
diff12phiplot.GetXaxis().SetBinLabel(12+6, "6")
diff12phiplot.GetXaxis().SetBinLabel(12+7, "7")
diff12phiplot.GetXaxis().SetBinLabel(12+8, "8")
diff12phiplot.GetXaxis().SetBinLabel(12+9, "9")
diff12phiplot.GetXaxis().SetBinLabel(12+10, "10")
diff12phiplot.GetXaxis().SetBinLabel(12+11, "11")
diff12phiplot.GetXaxis().SetBinLabel(12+12, "")
diff12phiplot.GetXaxis().SetBinLabel(24+1, "wh+1")
diff12phiplot.GetXaxis().SetBinLabel(24+2, "")
diff12phiplot.GetXaxis().SetBinLabel(24+3, "")
diff12phiplot.GetXaxis().SetBinLabel(24+4, "4")
diff12phiplot.GetXaxis().SetBinLabel(24+5, "5")
diff12phiplot.GetXaxis().SetBinLabel(24+6, "6")
diff12phiplot.GetXaxis().SetBinLabel(24+7, "7")
diff12phiplot.GetXaxis().SetBinLabel(24+8, "8")
diff12phiplot.GetXaxis().SetBinLabel(24+9, "9")
diff12phiplot.GetXaxis().SetBinLabel(24+10, "10")
diff12phiplot.GetXaxis().SetBinLabel(24+11, "11")
diff12phiplot.GetXaxis().SetBinLabel(24+12, "12")
diff12phiplot.SetYTitle("#phi_{y} residuals difference (mrad)")
diff12phiplot.GetYaxis().CenterTitle()
diff12phiplot.GetYaxis().SetTitleOffset(0.8)

diff12phiplot.SetAxisRange(-9., 9., "Y")
diff12phiplot.Draw("e1")
diff12phiplot_mean.Draw("same")
diff23phiplot.Draw("samee1")
diff23phiplot_mean.Draw("same")
diff34phiplot.Draw("samee1")
diff34phiplot_mean.Draw("same")
tlegend.Draw()
c1.SaveAs("diffphisector_" + outfile_part + ".pdf")

diff12xhist.SetLineColor(ROOT.kBlue)
diff23xhist.SetLineColor(ROOT.kRed)
diff34xhist.SetLineColor(ROOT.kGreen+2)
diff12xhist.SetXTitle("Local x residuals difference (mm)")
diff12xhist.GetXaxis().CenterTitle()
diff12xhist.SetAxisRange(0, diff12xhist.GetMaximum() * 1.6, "Y")
diff12xhist.Draw()
diff23xhist.Draw("same")
diff34xhist.Draw("same")
tlegend = ROOT.TLegend(0.5, 0.75, 0.98, 0.98, "mean, RMS (mm)")
tlegend.SetFillColor(ROOT.kWhite)
tlegend.SetBorderSize(1)
tlegend.AddEntry(diff12xhist, "MB2-MB1 %4.2f %4.2f" % (diff12xhist.GetMean(), diff12xhist.GetRMS()), "l")
tlegend.AddEntry(diff23xhist, "MB3-MB2 %4.2f %4.2f" % (diff23xhist.GetMean(), diff23xhist.GetRMS()), "l")
tlegend.AddEntry(diff34xhist, "MB4-MB3 %4.2f %4.2f" % (diff34xhist.GetMean(), diff34xhist.GetRMS()), "l")
tlegend.SetTextSize(0.04)
tlegend.Draw()
c1.SaveAs("diffxhist_" + outfile_part + ".pdf")

diff12phihist.SetLineColor(ROOT.kBlue)
diff23phihist.SetLineColor(ROOT.kRed)
diff34phihist.SetLineColor(ROOT.kGreen+2)
diff12phihist.SetXTitle("#phi_{y} residuals difference (mrad)")
diff12phihist.GetXaxis().CenterTitle()
diff12phihist.SetAxisRange(0, diff12phihist.GetMaximum() * 1.6, "Y")
diff12phihist.Draw()
diff23phihist.Draw("same")
diff34phihist.Draw("same")
tlegend = ROOT.TLegend(0.5, 0.75, 0.98, 0.98, "mean, RMS (mrad)")
tlegend.SetFillColor(ROOT.kWhite)
tlegend.SetBorderSize(1)
tlegend.AddEntry(diff12phihist, "MB2-MB1 %4.2f %4.2f" % (diff12phihist.GetMean(), diff12phihist.GetRMS()), "l")
tlegend.AddEntry(diff23phihist, "MB3-MB2 %4.2f %4.2f" % (diff23phihist.GetMean(), diff23phihist.GetRMS()), "l")
tlegend.AddEntry(diff34phihist, "MB4-MB3 %4.2f %4.2f" % (diff34phihist.GetMean(), diff34phihist.GetRMS()), "l")
tlegend.SetTextSize(0.04)
tlegend.Draw()
c1.SaveAs("diffphihist_" + outfile_part + ".pdf")

############################################################

tdrStyle.SetOptStat("emr")
tdrStyle.SetStatW(0.30)
tdrStyle.SetStatFontSize(0.05)

def plotone(makehist, label, units, which, wheel, sector, xrange):
    hist = makehist(which, wheel, sector)
    hist.SetXTitle("%s for wheel %d sector %d (%s)   " % (label, wheel, sector, units))
    hist.GetXaxis().CenterTitle()
    hist.SetAxisRange(-xrange, xrange, "X")
    hist.Draw()
    func, mean, meanerr = fitvoigt(hist)
    if func is not None:
        func.Draw("samec")

plotone(diff34x, "MB4-MB3", "mm", tfiles_aligned, 1, 1, 10.); c1.SaveAs("diffindivx_1_34_1.pdf")
plotone(diff34x, "MB4-MB3", "mm", tfiles_aligned, 1, 2, 10.); c1.SaveAs("diffindivx_1_34_2.pdf")
plotone(diff34x, "MB4-MB3", "mm", tfiles_aligned, 1, 3, 10.); c1.SaveAs("diffindivx_1_34_3.pdf")
plotone(diff34x, "MB4-MB3", "mm", tfiles_aligned, 1, 4, 10.); c1.SaveAs("diffindivx_1_34_4.pdf")
plotone(diff34x, "MB4-MB3", "mm", tfiles_aligned, 1, 5, 10.); c1.SaveAs("diffindivx_1_34_5.pdf")
plotone(diff34x, "MB4-MB3", "mm", tfiles_aligned, 1, 6, 10.); c1.SaveAs("diffindivx_1_34_6.pdf")
plotone(diff34x, "MB4-MB3", "mm", tfiles_aligned, 1, 7, 10.); c1.SaveAs("diffindivx_1_34_7.pdf")
plotone(diff34x, "MB4-MB3", "mm", tfiles_aligned, 1, 8, 10.); c1.SaveAs("diffindivx_1_34_8.pdf")
plotone(diff34x, "MB4-MB3", "mm", tfiles_aligned, 1, 9, 10.); c1.SaveAs("diffindivx_1_34_9.pdf")
plotone(diff34x, "MB4-MB3", "mm", tfiles_aligned, 1, 10, 10.); c1.SaveAs("diffindivx_1_34_10.pdf")
plotone(diff34x, "MB4-MB3", "mm", tfiles_aligned, 1, 11, 10.); c1.SaveAs("diffindivx_1_34_11.pdf")
plotone(diff34x, "MB4-MB3", "mm", tfiles_aligned, 1, 12, 10.); c1.SaveAs("diffindivx_1_34_12.pdf")

plotone(diff34phi, "MB4-MB3", "mm", tfiles_aligned, 1, 1, 30.); c1.SaveAs("diffindivphi_1_34_1.pdf")
plotone(diff34phi, "MB4-MB3", "mm", tfiles_aligned, 1, 2, 30.); c1.SaveAs("diffindivphi_1_34_2.pdf")
plotone(diff34phi, "MB4-MB3", "mm", tfiles_aligned, 1, 3, 30.); c1.SaveAs("diffindivphi_1_34_3.pdf")
plotone(diff34phi, "MB4-MB3", "mm", tfiles_aligned, 1, 4, 30.); c1.SaveAs("diffindivphi_1_34_4.pdf")
plotone(diff34phi, "MB4-MB3", "mm", tfiles_aligned, 1, 5, 30.); c1.SaveAs("diffindivphi_1_34_5.pdf")
plotone(diff34phi, "MB4-MB3", "mm", tfiles_aligned, 1, 6, 30.); c1.SaveAs("diffindivphi_1_34_6.pdf")
plotone(diff34phi, "MB4-MB3", "mm", tfiles_aligned, 1, 7, 30.); c1.SaveAs("diffindivphi_1_34_7.pdf")
plotone(diff34phi, "MB4-MB3", "mm", tfiles_aligned, 1, 8, 30.); c1.SaveAs("diffindivphi_1_34_8.pdf")
plotone(diff34phi, "MB4-MB3", "mm", tfiles_aligned, 1, 9, 30.); c1.SaveAs("diffindivphi_1_34_9.pdf")
plotone(diff34phi, "MB4-MB3", "mm", tfiles_aligned, 1, 10, 30.); c1.SaveAs("diffindivphi_1_34_10.pdf")
plotone(diff34phi, "MB4-MB3", "mm", tfiles_aligned, 1, 11, 30.); c1.SaveAs("diffindivphi_1_34_11.pdf")
plotone(diff34phi, "MB4-MB3", "mm", tfiles_aligned, 1, 12, 30.); c1.SaveAs("diffindivphi_1_34_12.pdf")
