import ROOT, array, os, math
from math import *
execfile("/home/jpivarski/bin/tdrstyle.py")
c1 = ROOT.TCanvas()
set_palette("blues")

tdrStyle.SetOptTitle(1)
tdrStyle.SetTitleBorderSize(0)
tdrStyle.SetOptFit(0)

plotDirectory = "/home/jpivarski/work/results/CRAFTchambers2/CSCCRAFT2_plots/unaligned/"
plotDirectory = "/home/jpivarski/work/results/CRAFTchambers2/CSCcollisionsMC_plots/iter1/"
plotDirectory = "/home/jpivarski/work/results/CRAFTchambers2/CSCcosmicsMC_plots/misaligned/"
plotDirectory = "/home/jpivarski/work/results/CRAFTchambers2/CSCcosmicsMC_plots/ideal/"
plotDirectory = "/home/jpivarski/work/results/CRAFTchambers2/CSCCRAFT_phiy_only/BEFORE/"
plotDirectory = "/home/jpivarski/work/results/CRAFTchambers2/CSCCRAFT_phiy_only/AFTER/"
tfiles = [ROOT.TFile(plotDirectory + f) for f in os.listdir(plotDirectory) if f[-5:] == ".root"]

tfiles = tfiles[0:2]    # 1.14 pb-1
tfiles = tfiles[64:68]  # 2.27 pb-1
tfiles = tfiles[2:11]   # 5.11 pb-1
tfiles = tfiles[11:29]  # 10.27 pb-1
tfiles = tfiles[29:64]  # 19.89 pb-1
print len(tfiles)

phiedges_me11 = [0.087266462599716474, 0.26179938550504211, 0.43633230751381297, 0.61086524309298951, 0.78539818789089832, 0.95993106410343132, 1.13446400890134, 1.3089969444805165, 1.4835298664892873, 1.6580627893946129, 1.8325957122999386, 2.0071286343087094, 2.1816615698878858, 2.3561945146857948, 2.5307273908983277, 2.7052603356962366, 2.8797932712754131, 3.0543261932841839, -3.0543261909900767, -2.8797932680847511, -2.7052603460759803, -2.5307274104968038, -2.3561944656988949, -2.181661589486362, -2.0071286446884531, -1.8325957091092766, -1.6580627871005058, -1.4835298641951802, -1.3089969412898546, -1.1344640192810838, -0.95993108370190716, -0.78539813890399834, -0.61086526269146535, -0.43633231789355653, -0.26179938231437999, -0.087266460305609153]
phiedges_me12 = [0.087266462599716474, 0.26179938297741073, 0.43633231700542385, 0.61086526005981812, 0.78539815872971441, 0.95993109326461523, 1.1344639919345114, 1.3089969349889057, 1.4835298690169187, 1.6580627893946129, 1.8325957097723073, 2.0071286438003204, 2.1816615868547147, 2.3561944855246111, 2.5307274200595118, 2.7052603187294082, 2.879793261783802, 3.0543261958118153, -3.0543261909900767, -2.8797932706123825, -2.7052603365843693, -2.5307273935299754, -2.356194494860079, -2.1816615603251783, -2.0071286616552819, -1.8325957186008877, -1.6580627845728746, -1.4835298641951802, -1.308996943817486, -1.1344640097894729, -0.95993106673507855, -0.78539816806518226, -0.61086523353028144, -0.43633233486038514, -0.26179939180599088, -0.087266457777977771]
phiedges_me13 = [0.087266462599716474, 0.26179938235213535, 0.43633230952414037, 0.61086523916470359, 0.78539817763669606, 0.95993107435763347, 1.1344640128296259, 1.3089969424701891, 1.4835298696421941, 1.6580627893946129, 1.832595709147032, 2.0071286363190368, 2.1816615659596001, 2.3561945044315924, 2.53072740115253, 2.7052603396245227, 2.8797932692650856, 3.0543261964370907, -3.0543261909900767, -2.8797932712376579, -2.7052603440656529, -2.53072741442509, -2.3561944759530973, -2.1816615792321596, -2.0071286407601674, -1.8325957111196041, -1.6580627839475992, -1.4835298641951802, -1.3089969444427614, -1.1344640172707563, -0.95993108763019308, -0.7853981491582005, -0.61086525243726308, -0.43633231396527061, -0.2617993843247074, -0.087266457152702412]
phiedges_me14 = [0.087266462599716474, 0.26179938550504211, 0.43633230751381297, 0.61086524309298951, 0.78539818789089832, 0.95993106410343132, 1.13446400890134, 1.3089969444805165, 1.4835298664892873, 1.6580627893946129, 1.8325957122999386, 2.0071286343087094, 2.1816615698878858, 2.3561945146857948, 2.5307273908983277, 2.7052603356962366, 2.8797932712754131, 3.0543261932841839, -3.0543261909900767, -2.8797932680847511, -2.7052603460759803, -2.5307274104968038, -2.3561944656988949, -2.181661589486362, -2.0071286446884531, -1.8325957091092766, -1.6580627871005058, -1.4835298641951802, -1.3089969412898546, -1.1344640192810838, -0.95993108370190716, -0.78539813890399834, -0.61086526269146535, -0.43633231789355653, -0.26179938231437999, -0.087266460305609153]
phiedges_me21 = [0.26179938481428705, 0.6108652193791777, 0.95993108859688125, 1.3089969578145848, 1.6580627923794755, 2.0071286538798305, 2.356194498693418, 2.7052603320901376, 3.0543261769037247, -2.8797932687755066, -2.5307274342106156, -2.1816615649929121, -1.8325956957752083, -1.4835298612103178, -1.1344639997099626, -0.78539815489637521, -0.43633232149965551, -0.087266476686068212]
phiedges_me22 = [0.087266462599716474, 0.26179938871066555, 0.43633231557670243, 0.61086524129631259, 0.785398172964478, 0.95993107902985153, 1.1344640106980168, 1.308996936417627, 1.483529863283664, 1.6580627893946129, 1.8325957155055621, 2.0071286423715993, 2.1816615680912093, 2.3561944997593747, 2.5307274058247482, 2.7052603374929136, 2.8797932632125236, 3.0543261900785605, -3.0543261909900767, -2.8797932648791278, -2.7052603380130908, -2.5307274122934809, -2.3561944806253154, -2.1816615745599419, -2.0071286428917765, -1.8325957171721663, -1.6580627903061294, -1.4835298641951802, -1.3089969380842312, -1.1344640112181943, -0.95993108549858397, -0.78539815383041856, -0.61086524776504503, -0.43633231609687961, -0.26179939037726946, -0.087266463511232586]
phiedges_me31 = [0.26179938498198485, 0.61086523665761272, 0.95993108859688125, 1.3089969405361499, 1.6580627922117777, 2.0071286313120122, 2.3561944778405319, 2.7052603529430232, 3.0543261994715434, -2.8797932686078087, -2.530727416932181, -2.1816615649929121, -1.8325957130536434, -1.4835298613780155, -1.1344640222777811, -0.78539817574926085, -0.43633230064676976, -0.087266454118249653]
phiedges_me32 = [0.087266462599716474, 0.26179938871066555, 0.43633231557670243, 0.61086524129631259, 0.785398172964478, 0.95993107902985153, 1.1344640106980168, 1.308996936417627, 1.483529863283664, 1.6580627893946129, 1.8325957155055621, 2.0071286423715993, 2.1816615680912093, 2.3561944997593747, 2.5307274058247482, 2.7052603374929136, 2.8797932632125236, 3.0543261900785605, -3.0543261909900767, -2.8797932648791278, -2.7052603380130908, -2.5307274122934809, -2.3561944806253154, -2.1816615745599419, -2.0071286428917765, -1.8325957171721663, -1.6580627903061294, -1.4835298641951802, -1.3089969380842312, -1.1344640112181943, -0.95993108549858397, -0.78539815383041856, -0.61086524776504503, -0.43633231609687961, -0.26179939037726946, -0.087266463511232586]
phiedges_me41 = [0.26179938879942166, 0.61086525092924071, 0.95993108859688125, 1.3089969262645218, 1.6580627883943408, 2.0071286288299772, 2.3561945088997609, 2.7052603218837943, 3.0543262019535784, -2.8797932647903717, -2.5307274026605526, -2.1816615649929121, -1.8325957273252713, -1.4835298651954525, -1.1344640247598159, -0.785398144690032, -0.43633233170599861, -0.087266451636214853]

phiedges1 = [0.35228048120123945, 0.87587781482541827, 1.3994776462193192, 1.923076807996136, 2.4466741416203148, 2.970273973014216, -2.7893121723885534, -2.2657148387643748, -1.7421150073704739, -1.2185158455936571, -0.69491851196947851, -0.17131868057557731]
phiedges2 = [0.22000706229660855, 0.74360690430428489, 1.267204926935573, 1.7908033890915052, 2.3144032310991816, 2.8380012537304697, -2.9215855912931841, -2.3979857492855081, -1.8743877266542202, -1.3507892644982882, -0.82718942249061178, -0.30359139985932365]
phiedges3 = [0.29751957124275596, 0.82111826253905784, 1.3447162969496083, 1.8683158980376524, 2.3919145893339548, 2.915512623744505, -2.844073082347037, -2.3204743910507353, -1.7968763566401849, -1.2732767555521407, -0.74967806425583894, -0.22608002984528835]
phiedges4 = [3.0136655290752188, -2.7530905195097337, -2.2922883025568734, -1.9222915077192773, -1.5707963267948966, -1.2193011458705159, -0.84930435103291968, -0.38850213408005951, 0.127927124514574, 0.65152597487624719, 1.1322596819239259, 1.5707963267948966, 2.0093329716658674, 2.4900666787135459]

def philines(station, high, abscissa):
    global philine_tlines
    philine_tlines = []
    if station == "me11": phiedges = phiedges_me11
    if station == "me12": phiedges = phiedges_me12
    if station == "me13": phiedges = phiedges_me13
    if station == "me14": phiedges = phiedges_me14
    if station == "me21": phiedges = phiedges_me21
    if station == "me22": phiedges = phiedges_me22
    if station == "me31": phiedges = phiedges_me31
    if station == "me32": phiedges = phiedges_me32
    if station == "me41": phiedges = phiedges_me41
    if station == 1: phiedges = phiedges1
    if station == 2: phiedges = phiedges2
    if station == 3: phiedges = phiedges3
    if station == 4: phiedges = phiedges4
    for phi in phiedges:
        if abscissa is None or abscissa[0] < phi < abscissa[1]:
            philine_tlines.append(ROOT.TLine(phi, -high, phi, high))
            philine_tlines[-1].SetLineStyle(2)
            philine_tlines[-1].Draw()

def zlines(high):
    global zline_tlines
    zline_tlines = []
    for z in -401.625, -133.875, 133.875, 401.625:
        if abscissa is None or abscissa[0] < z < abscissa[1]:
            zline_tlines.append(ROOT.TLine(z, -high, z, high))
            zline_tlines[-1].SetLineStyle(2)
            zline_tlines[-1].Draw()

def rlines(disk, high):
    global rline_tlines
    rline_tlines = []
    if disk == 1: rl = [150., 270., 480.]
    else: rl = [350.]
    for r in rl:
        if abscissa is None or abscissa[0] < r < abscissa[1]:
            rline_tlines.append(ROOT.TLine(r, -high, r, high))
            rline_tlines[-1].SetLineStyle(2)
            rline_tlines[-1].Draw()

def plot(name, param, mode="from2d", high=40., abscissa=None, title="", widebins=False, fitsine=False):
    global hist, hist2d, hist2dweight, tline1, tline2, tline3
    prof = tfiles[0].Get("AlignmentMonitorMuonSystemMap1D/iter1/%s_%s_prof" % (name, param)).Clone()
    profPos = tfiles[0].Get("AlignmentMonitorMuonSystemMap1D/iter1/%s_%s_profPos" % (name, param)).Clone()
    profNeg = tfiles[0].Get("AlignmentMonitorMuonSystemMap1D/iter1/%s_%s_profNeg" % (name, param)).Clone()
    weights = tfiles[0].Get("AlignmentMonitorMuonSystemMap1D/iter1/%s_%s_weights" % (name, param)).Clone()
    valweights = tfiles[0].Get("AlignmentMonitorMuonSystemMap1D/iter1/%s_%s_valweights" % (name, param)).Clone()
    hist2d = tfiles[0].Get("AlignmentMonitorMuonSystemMap1D/iter1/%s_%s_2d" % (name, param)).Clone()
    hist2dweight = tfiles[0].Get("AlignmentMonitorMuonSystemMap1D/iter1/%s_%s_2dweight" % (name, param)).Clone()
    for tfile in tfiles[1:]:
        prof.Add(tfile.Get("AlignmentMonitorMuonSystemMap1D/iter1/%s_%s_prof" % (name, param)))
        profPos.Add(tfile.Get("AlignmentMonitorMuonSystemMap1D/iter1/%s_%s_profPos" % (name, param)))
        profNeg.Add(tfile.Get("AlignmentMonitorMuonSystemMap1D/iter1/%s_%s_profNeg" % (name, param)))
        weights.Add(tfile.Get("AlignmentMonitorMuonSystemMap1D/iter1/%s_%s_weights" % (name, param)))
        valweights.Add(tfile.Get("AlignmentMonitorMuonSystemMap1D/iter1/%s_%s_valweights" % (name, param)))
        hist2d.Add(tfile.Get("AlignmentMonitorMuonSystemMap1D/iter1/%s_%s_2d" % (name, param)))
        hist2dweight.Add(tfile.Get("AlignmentMonitorMuonSystemMap1D/iter1/%s_%s_2dweight" % (name, param)))

    if mode == "plain":
        hist = prof

    elif mode in ("from2d", "from2dweight"):
        if mode == "from2d": the2d = hist2d
        else: the2d = hist2dweight

        hist = weights.Clone()
        skip = 1
        if widebins:
            hist.Rebin(10)
            skip = 10

        for i in xrange(0, int(weights.GetNbinsX()), skip):
            tmp = the2d.ProjectionY("tmp", i+1, i + skip)
            if tmp.GetEntries() > 2:
                hist.SetBinContent(i/skip+1, tmp.GetMean())
                hist.SetBinError(i/skip+1, tmp.GetRMS() / sqrt(tmp.GetEntries()))
            else:
                hist.SetBinContent(i/skip+1, 2000.)
                hist.SetBinError(i/skip+1, 1000.)
        
    elif mode == "weighted":
        if weights.GetEntries() == 0:
            averageweight = 0.
        else:
            sumofweights = 0.
            for i in xrange(0, int(weights.GetNbinsX())+2):
                sumofweights += weights.GetBinContent(i)
            averageweight = sumofweights / weights.GetEntries()
        hist = weights.Clone()
        for i in xrange(1, int(weights.GetNbinsX())+1):
            if weights.GetBinContent(i) > 0:
                thisweight = weights.GetBinContent(i) / averageweight
                hist.SetBinContent(i, valweights.GetBinContent(i) / thisweight)
                hist.SetBinError(i, sqrt(1. / thisweight))
            else:
                hist.SetBinContent(i, 2000.)
                hist.SetBinError(i, 1000.)

    else:
        raise Exception

    if fitsine:
        f = ROOT.TF1("f", "[0] + [1]*sin(x) + [2]*cos(x)", -pi, pi)
        hist.Fit(f, "0")
        hist.GetFunction("f").SetLineColor(ROOT.kRed)
        global fitsine_const, fitsine_sin, fitsine_cos
        fitsine_const = hist.GetFunction("f").GetParameter(0), hist.GetFunction("f").GetParError(0)
        fitsine_sin = hist.GetFunction("f").GetParameter(1), hist.GetFunction("f").GetParError(1)
        fitsine_cos = hist.GetFunction("f").GetParameter(2), hist.GetFunction("f").GetParError(2)

    hist.SetAxisRange(-high, high, "Y")
    if abscissa is not None: hist.SetAxisRange(abscissa[0], abscissa[1], "X")
    hist.SetMarkerStyle(20)
    hist.SetMarkerSize(0.75)
    hist.GetXaxis().CenterTitle()
    hist.GetYaxis().CenterTitle()
    hist.GetYaxis().SetTitleOffset(0.75)
    hist.GetXaxis().SetTitleSize(0.05)
    hist.GetYaxis().SetTitleSize(0.05)
    hist.SetTitle(title)
    if "vsphi" in name: hist.SetXTitle("Global #phi position (rad)")
    elif "vsz" in name: hist.SetXTitle("Global z position (cm)")
    elif "vsr" in name: hist.SetXTitle("Global R position (cm)")
    if "DT" in name:
        if param == "x": hist.SetYTitle("Global x residual (mm)")
        if param == "dxdz": hist.SetYTitle("Global dx/dz residual (mrad)")
        if param == "y": hist.SetYTitle("Global y residual (mm)")
        if param == "dydz": hist.SetYTitle("Global dy/dz residual (mm)")
    if "CSC" in name:
        if param == "x": hist.SetYTitle("Global r#phi residual (mm)")
        if param == "dxdz": hist.SetYTitle("Global d(r#phi)/dz residual (mrad)")
    hist.SetMarkerColor(ROOT.kBlack)
    hist.SetLineColor(ROOT.kBlack)
    hist.Draw()
    hist2d.Draw("colzsame")
    if widebins: hist.Draw("samee1")
    else: hist.Draw("same")
    if fitsine: hist.GetFunction("f").Draw("same")
    if "vsphi" in name: 
        if ("mem11" in name or "mep11" in name) and not widebins: philines("me11", high, abscissa)
        if ("mem12" in name or "mep12" in name) and not widebins: philines("me12", high, abscissa)
        if ("mem13" in name or "mep13" in name) and not widebins: philines("me13", high, abscissa)
        if ("mem14" in name or "mep14" in name) and not widebins: philines("me14", high, abscissa)
        if ("mem21" in name or "mep21" in name) and not widebins: philines("me21", high, abscissa)
        if ("mem22" in name or "mep22" in name) and not widebins: philines("me22", high, abscissa)
        if ("mem31" in name or "mep31" in name) and not widebins: philines("me31", high, abscissa)
        if ("mem32" in name or "mep32" in name) and not widebins: philines("me32", high, abscissa)
        if ("mem41" in name or "mep41" in name) and not widebins: philines("me41", high, abscissa)
        if abscissa is None:
            tline1 = ROOT.TLine(-pi, 0, pi, 0); tline1.Draw()
            tline2 = ROOT.TLine(-pi, -high, pi, -high); tline2.SetLineWidth(2); tline2.Draw()
            tline3 = ROOT.TLine(-pi, high, pi, high); tline3.Draw()
        else:
            tline1 = ROOT.TLine(abscissa[0], 0, abscissa[1], 0); tline1.Draw()
            tline2 = ROOT.TLine(abscissa[0], -high, abscissa[1], -high); tline2.SetLineWidth(2); tline2.Draw()
            tline3 = ROOT.TLine(abscissa[0], high, abscissa[1], high); tline3.Draw()
    elif "vsz" in name:
        if not widebins: zlines(high, abscissa)
        if abscissa is None:
            tline1 = ROOT.TLine(-660, 0, 660, 0); tline1.Draw()
            tline2 = ROOT.TLine(-660, -high, 660, -high); tline2.SetLineWidth(2); tline2.Draw()
            tline3 = ROOT.TLine(-660, high, 660, high); tline3.Draw()
        else:
            tline1 = ROOT.TLine(abscissa[0], 0, abscissa[1], 0); tline1.Draw()
            tline2 = ROOT.TLine(abscissa[0], -high, abscissa[1], -high); tline2.SetLineWidth(2); tline2.Draw()
            tline3 = ROOT.TLine(abscissa[0], high, abscissa[1], high); tline3.Draw()
    elif "vsr" in name:
        if "mem1" in name or "mep1" in name and not widebins: rlines(1, high, abscissa)
        if "mem2" in name or "mep2" in name and not widebins: rlines(2, high, abscissa)
        if "mem3" in name or "mep3" in name and not widebins: rlines(3, high, abscissa)
        if "mem4" in name or "mep4" in name and not widebins: rlines(4, high, abscissa)
        if abscissa is None:
            tline1 = ROOT.TLine(100, 0, 700, 0); tline1.Draw()
            tline2 = ROOT.TLine(100, -high, 700, -high); tline2.SetLineWidth(2); tline2.Draw()
            tline3 = ROOT.TLine(100, high, 700, high); tline3.Draw()
        else:
            tline1 = ROOT.TLine(abscissa[0], 0, abscissa[1], 0); tline1.Draw()
            tline2 = ROOT.TLine(abscissa[0], -high, abscissa[1], -high); tline2.SetLineWidth(2); tline2.Draw()
            tline3 = ROOT.TLine(abscissa[0], high, abscissa[1], high); tline3.Draw()

###################################################

plot("CSCvsphi_mem32", "x")




###################################################

plot("CSCvsphi_mem22", "dxdz", "from2d", 10., (-pi, pi/36. - 0.01), "ME-2/2 \"d(r#phi)/dz\" angular residuals, measures #phi_{y} of chambers")
c1.SaveAs("datacsc_phiy_misalignment.pdf")

beamhalo = ROOT.TH1F("beamhalo", "", 19, -pi - (2.*pi/18./2.) + (2.*pi/18./2.)/2., pi + (2.*pi/18./2.) + (2.*pi/18./2.)/2.)
beamhalo.Fill(0.0, -1.79401004314)
beamhalo.Fill(0.349065850399, 0.0)
beamhalo.Fill(0.698131700798, -0.31902000308)
beamhalo.Fill(1.0471975512, 3.55473995209)
beamhalo.Fill(1.3962634016, -0.772029995918)
beamhalo.Fill(1.74532925199, -0.343499988317)
beamhalo.Fill(2.09439510239, -2.34067988396)
beamhalo.Fill(2.44346095279, 0.0)
beamhalo.Fill(2.79252680319, 2.10010004044)
beamhalo.Fill(3.14159265359, 2.86800003052)
beamhalo.Fill(-3.14159265359, 2.86800003052)
beamhalo.Fill(-2.79252680319, -1.58215999603)
beamhalo.Fill(-2.44346095279, 0.0)
beamhalo.Fill(-2.09439510239, 3.08811998367)
beamhalo.Fill(-1.74532925199, -0.344940006733)
beamhalo.Fill(-1.3962634016, 1.85907995701)
beamhalo.Fill(-1.0471975512, -1.38069999218)
beamhalo.Fill(-0.698131700798, -1.95274996758)
beamhalo.Fill(-0.349065850399, -2.78362989426)
beamhalo.SetLineColor(ROOT.kRed)
beamhalo.SetLineWidth(2)
# beamhalo.Draw(); philines("me21", 4, None)

plot("CSCvsphi_mem21", "dxdz", "from2d", 10., None, "ME-2/1 \"d(r#phi)/dz\" angular residuals, compared to beam-halo #phi_{y} (red)"); beamhalo.Draw("same")
c1.SaveAs("datacsc_phiy_andbeamhalo.pdf")

# import minuit
# def fun_YEm1(phi, deltax, deltay, deltaphiz):
#     return (+0.60 + deltaphiz)/1000.*(3697) + (-0.9 + deltax)*sin(phi) + (-1.0 + deltay)*cos(phi)
# def fun_YEm2(phi, deltax, deltay, deltaphiz):
#     return (-0.44 + deltaphiz)/1000.*(5265) + (-1.1 + deltax)*sin(phi) + (-0.4 + deltay)*cos(phi)
# def fun_YEp1(phi, deltax, deltay, deltaphiz):
#     return (+0.43 + deltaphiz)/1000.*(3697) + (-0.9 + deltax)*sin(phi) + (-0.5 + deltay)*cos(phi)
# def fun_YEp2(phi, deltax, deltay, deltaphiz):
#     return (+0.50 + deltaphiz)/1000.*(5265) + (-0.8 + deltax)*sin(phi) + (0.5 + deltay)*cos(phi)

# def chi2_objective(deltax, deltay, deltaphiz):
#     chi2 = 0.

#     plot("CSCvsphi_mep12", "x", widebins=True)
#     for i in xrange(1, int(hist.GetEntries())+1):
#         phi = hist.GetBinCenter(i)
#         value = hist.GetBinContent(i)
#         error = hist.GetBinError(i)
#         if error > 0.:
#             chi2 += (value - fun_YEp1(phi, deltax, deltay, deltaphiz))**2 / error**2

#     plot("CSCvsphi_mep22", "x", widebins=True)
#     for i in xrange(1, int(hist.GetEntries())+1):
#         phi = hist.GetBinCenter(i)
#         value = hist.GetBinContent(i)
#         error = hist.GetBinError(i)
#         if error > 0.:
#             chi2 += (value - fun_YEp2(phi, deltax, deltay, deltaphiz))**2 / error**2

#     plot("CSCvsphi_mep32", "x", widebins=True)
#     for i in xrange(1, int(hist.GetEntries())+1):
#         phi = hist.GetBinCenter(i)
#         value = hist.GetBinContent(i)
#         error = hist.GetBinError(i)
#         if error > 0.:
#             chi2 += (value - fun_YEp2(phi, deltax, deltay, deltaphiz))**2 / error**2

#     plot("CSCvsphi_mem12", "x", widebins=True)
#     for i in xrange(1, int(hist.GetEntries())+1):
#         phi = hist.GetBinCenter(i)
#         value = hist.GetBinContent(i)
#         error = hist.GetBinError(i)
#         if error > 0.:
#             chi2 += (value - fun_YEm1(phi, deltax, deltay, deltaphiz))**2 / error**2

#     plot("CSCvsphi_mem22", "x", widebins=True)
#     for i in xrange(1, int(hist.GetEntries())+1):
#         phi = hist.GetBinCenter(i)
#         value = hist.GetBinContent(i)
#         error = hist.GetBinError(i)
#         if error > 0.:
#             chi2 += (value - fun_YEm2(phi, deltax, deltay, deltaphiz))**2 / error**2

#     plot("CSCvsphi_mem32", "x", widebins=True)
#     for i in xrange(1, int(hist.GetEntries())+1):
#         phi = hist.GetBinCenter(i)
#         value = hist.GetBinContent(i)
#         error = hist.GetBinError(i)
#         if error > 0.:
#             chi2 += (value - fun_YEm2(phi, deltax, deltay, deltaphiz))**2 / error**2

#     return chi2

# m = minuit.Minuit(chi2_objective)
# m.migrad()
# print m.values, m.fval

# includes all four disks in the fit
YEm1 = ROOT.TF1("YEm1", "(+0.60 - 0.693466883171862)/1000.*(3697) + (-0.9 + 4.3419530487509457)*sin(x) + (-1.0 - 0.24542227565791219)*cos(x)", -pi, pi)
YEm2 = ROOT.TF1("YEm1", "(-0.44 - 0.693466883171862)/1000.*(5265) + (-1.1 + 4.3419530487509457)*sin(x) + (-0.4 - 0.24542227565791219)*cos(x)", -pi, pi)
YEp1 = ROOT.TF1("YEp1", "(+0.43 - 0.693466883171862)/1000.*(3697) + (-0.9 + 4.3419530487509457)*sin(x) + (-0.5 - 0.24542227565791219)*cos(x)", -pi, pi)
YEp2 = ROOT.TF1("YEp1", "(+0.50 - 0.693466883171862)/1000.*(5265) + (-0.8 + 4.3419530487509457)*sin(x) + (+0.5 - 0.24542227565791219)*cos(x)", -pi, pi)
YEm1.SetLineColor(ROOT.kGreen+2)
YEm2.SetLineColor(ROOT.kGreen+2)
YEp1.SetLineColor(ROOT.kGreen+2)
YEp2.SetLineColor(ROOT.kGreen+2)

plot("CSCvsphi_mep32", "x", "from2d", 20., title="ME+3/2 residuals, fitted (red) and compared with survey (green)", widebins=True, fitsine=True); YEp1.Draw("same")
c1.SaveAs("datacsc_survey_mep32.pdf")
plot("CSCvsphi_mep22", "x", "from2d", 20., title="ME+2/2 residuals, fitted (red) and compared with survey (green)", widebins=True, fitsine=True); YEp2.Draw("same")
c1.SaveAs("datacsc_survey_mep22.pdf")
plot("CSCvsphi_mep12", "x", "from2d", 20., title="ME+1/2 residuals, fitted (red) and compared with survey (green)", widebins=True, fitsine=True); YEp2.Draw("same")
c1.SaveAs("datacsc_survey_mep12.pdf")
plot("CSCvsphi_mem12", "x", "from2d", 20., title="ME-1/2 residuals, fitted (red) and compared with survey (green)", widebins=True, fitsine=True); YEm1.Draw("same")
c1.SaveAs("datacsc_survey_mem12.pdf")
plot("CSCvsphi_mem22", "x", "from2d", 20., title="ME-2/2 residuals, fitted (red) and compared with survey (green)", widebins=True, fitsine=True); YEm2.Draw("same")
c1.SaveAs("datacsc_survey_mem22.pdf")
plot("CSCvsphi_mem32", "x", "from2d", 20., title="ME-3/2 residuals, fitted (red) and compared with survey (green)", widebins=True, fitsine=True); YEm2.Draw("same")
c1.SaveAs("datacsc_survey_mem32.pdf")

###################################################

# these are in mm and mrad
mep11x, mep11y, mep11phiz = 0.0851502*10.,  -0.0656322*10.,  -2.61805e-05*1000.
mep12x, mep12y, mep12phiz = 0.0812609*10.,  -0.00285054*10.,  0.00181185*1000.
mep21x, mep21y, mep21phiz = -0.441475*10.,  -0.34772*10.,     0.00318885*1000.
mep22x, mep22y, mep22phiz = 0.111149*10.,   -0.113888*10.,   -0.00126515*1000.
mep31x, mep31y, mep31phiz = -0.00182324*10., 0.159697*10.,   -0.00232179*1000.
mep32x, mep32y, mep32phiz = -0.057986*10.,  -0.000253022*10., 0.000501659*1000.
mep41x, mep41y, mep41phiz = 0.0884364*10.,   0.111459*10.,    0.000378226*1000.
mem11x, mem11y, mem11phiz = 0.100908*10.,    0.270649*10.,   -0.000501631*1000.
mem12x, mem12y, mem12phiz = 0.127838*10.,   -0.23352*10.,    -0.00138611*1000.
mem21x, mem21y, mem21phiz = 0.055897*10.,    0.208887*10.,   -0.00029521*1000.
mem22x, mem22y, mem22phiz = -0.209874*10.,  -0.284235*10.,    0.000685969*1000.
mem31x, mem31y, mem31phiz = -0.356181*10.,   0.260991*10.,    0.0033451*1000.
mem32x, mem32y, mem32phiz = 0.268511*10.,   -0.137257*10.,   -0.00159779*1000.
mem41x, mem41y, mem41phiz = 0.329971*10.,    0.228704*10.,    0.00415548*1000.

# these are in mm
radius11 = 181.5*10.
radius12 = 369.7*10.
radius13 = 595.15*10.
radius21 = sqrt(21.15269852**2 + 241.77645874**2)*10.
radius22 = 526.50000000*10.
radius31 = sqrt(22.02425575**2 + 251.73840332**2)*10.
radius32 = 526.50000000*10.
radius41 = sqrt(22.89145660**2 + 261.65054321**2)*10.

# these are the true values
real_mep11 = ROOT.TF1("real_mep11", "(%g)/1000.*(%g) + -(%g)*sin(x) + (%g)*cos(x)" % (mep11phiz, radius11, mep11x, mep11y), -pi, pi); real_mep11.SetLineColor(ROOT.kGreen+2)
real_mep12 = ROOT.TF1("real_mep12", "(%g)/1000.*(%g) + -(%g)*sin(x) + (%g)*cos(x)" % (mep12phiz, radius12, mep12x, mep12y), -pi, pi); real_mep12.SetLineColor(ROOT.kGreen+2)
real_mep21 = ROOT.TF1("real_mep21", "(%g)/1000.*(%g) + -(%g)*sin(x) + (%g)*cos(x)" % (mep21phiz, radius21, mep21x, mep21y), -pi, pi); real_mep21.SetLineColor(ROOT.kGreen+2)
real_mep22 = ROOT.TF1("real_mep22", "(%g)/1000.*(%g) + -(%g)*sin(x) + (%g)*cos(x)" % (mep22phiz, radius22, mep22x, mep22y), -pi, pi); real_mep22.SetLineColor(ROOT.kGreen+2)
real_mep31 = ROOT.TF1("real_mep31", "(%g)/1000.*(%g) + -(%g)*sin(x) + (%g)*cos(x)" % (mep31phiz, radius31, mep31x, mep31y), -pi, pi); real_mep31.SetLineColor(ROOT.kGreen+2)
real_mep32 = ROOT.TF1("real_mep32", "(%g)/1000.*(%g) + -(%g)*sin(x) + (%g)*cos(x)" % (mep32phiz, radius32, mep32x, mep32y), -pi, pi); real_mep32.SetLineColor(ROOT.kGreen+2)
real_mep41 = ROOT.TF1("real_mep41", "(%g)/1000.*(%g) + -(%g)*sin(x) + (%g)*cos(x)" % (mep41phiz, radius41, mep41x, mep41y), -pi, pi); real_mep41.SetLineColor(ROOT.kGreen+2)
real_mem11 = ROOT.TF1("real_mem11", "(%g)/1000.*(%g) + -(%g)*sin(x) + (%g)*cos(x)" % (mem11phiz, radius11, mem11x, mem11y), -pi, pi); real_mem11.SetLineColor(ROOT.kGreen+2)
real_mem12 = ROOT.TF1("real_mem12", "(%g)/1000.*(%g) + -(%g)*sin(x) + (%g)*cos(x)" % (mem12phiz, radius12, mem12x, mem12y), -pi, pi); real_mem12.SetLineColor(ROOT.kGreen+2)
real_mem21 = ROOT.TF1("real_mem21", "(%g)/1000.*(%g) + -(%g)*sin(x) + (%g)*cos(x)" % (mem21phiz, radius21, mem21x, mem21y), -pi, pi); real_mem21.SetLineColor(ROOT.kGreen+2)
real_mem22 = ROOT.TF1("real_mem22", "(%g)/1000.*(%g) + -(%g)*sin(x) + (%g)*cos(x)" % (mem22phiz, radius22, mem22x, mem22y), -pi, pi); real_mem22.SetLineColor(ROOT.kGreen+2)
real_mem31 = ROOT.TF1("real_mem31", "(%g)/1000.*(%g) + -(%g)*sin(x) + (%g)*cos(x)" % (mem31phiz, radius31, mem31x, mem31y), -pi, pi); real_mem31.SetLineColor(ROOT.kGreen+2)
real_mem32 = ROOT.TF1("real_mem32", "(%g)/1000.*(%g) + -(%g)*sin(x) + (%g)*cos(x)" % (mem32phiz, radius32, mem32x, mem32y), -pi, pi); real_mem32.SetLineColor(ROOT.kGreen+2)
real_mem41 = ROOT.TF1("real_mem41", "(%g)/1000.*(%g) + -(%g)*sin(x) + (%g)*cos(x)" % (mem41phiz, radius41, mem41x, mem41y), -pi, pi); real_mem41.SetLineColor(ROOT.kGreen+2)

resids = []
plot("CSCvsphi_mem11", "x", "from2d", 20., title="ME-1/1 collisions MC with 5 pb^{-1}, fitted (red) and compared with truth (green)", widebins=True, fitsine=True); real_mem11.Draw("same")
resids.append((fitsine_const[0]*1000./radius11 - (mem11phiz), fitsine_sin[0] - (-mem11x), fitsine_cos[0] - (mem11y)))
plot("CSCvsphi_mem12", "x", "from2d", 20., title="ME-1/2 collisions MC with 5 pb^{-1}, fitted (red) and compared with truth (green)", widebins=True, fitsine=True); real_mem12.Draw("same")
resids.append((fitsine_const[0]*1000./radius12 - (mem12phiz), fitsine_sin[0] - (-mem12x), fitsine_cos[0] - (mem12y)))
c1.SaveAs("mccsc_example_5pb.pdf")
plot("CSCvsphi_mem21", "x", "from2d", 20., title="ME-2/1 collisions MC with 5 pb^{-1}, fitted (red) and compared with truth (green)", widebins=True, fitsine=True); real_mem21.Draw("same")
resids.append((fitsine_const[0]*1000./radius21 - (mem21phiz), fitsine_sin[0] - (-mem21x), fitsine_cos[0] - (mem21y)))
plot("CSCvsphi_mem22", "x", "from2d", 20., title="ME-2/2 collisions MC with 5 pb^{-1}, fitted (red) and compared with truth (green)", widebins=True, fitsine=True); real_mem22.Draw("same")
resids.append((fitsine_const[0]*1000./radius22 - (mem22phiz), fitsine_sin[0] - (-mem22x), fitsine_cos[0] - (mem22y)))
plot("CSCvsphi_mem31", "x", "from2d", 20., title="ME-3/1 collisions MC with 5 pb^{-1}, fitted (red) and compared with truth (green)", widebins=True, fitsine=True); real_mem31.Draw("same")
resids.append((fitsine_const[0]*1000./radius31 - (mem31phiz), fitsine_sin[0] - (-mem31x), fitsine_cos[0] - (mem31y)))
plot("CSCvsphi_mem32", "x", "from2d", 20., title="ME-3/2 collisions MC with 5 pb^{-1}, fitted (red) and compared with truth (green)", widebins=True, fitsine=True); real_mem32.Draw("same")
resids.append((fitsine_const[0]*1000./radius32 - (mem32phiz), fitsine_sin[0] - (-mem32x), fitsine_cos[0] - (mem32y)))
plot("CSCvsphi_mem41", "x", "from2d", 20., title="ME-4/1 collisions MC with 5 pb^{-1}, fitted (red) and compared with truth (green)", widebins=True, fitsine=True); real_mem41.Draw("same")
resids.append((fitsine_const[0]*1000./radius41 - (mem41phiz), fitsine_sin[0] - (-mem41x), fitsine_cos[0] - (mem41y)))
plot("CSCvsphi_mep11", "x", "from2d", 20., title="ME+1/1 collisions MC with 5 pb^{-1}, fitted (red) and compared with truth (green)", widebins=True, fitsine=True); real_mep11.Draw("same")
resids.append((fitsine_const[0]*1000./radius11 - (mep11phiz), fitsine_sin[0] - (-mep11x), fitsine_cos[0] - (mep11y)))
plot("CSCvsphi_mep12", "x", "from2d", 20., title="ME+1/2 collisions MC with 5 pb^{-1}, fitted (red) and compared with truth (green)", widebins=True, fitsine=True); real_mep12.Draw("same")
resids.append((fitsine_const[0]*1000./radius12 - (mep12phiz), fitsine_sin[0] - (-mep12x), fitsine_cos[0] - (mep12y)))
plot("CSCvsphi_mep21", "x", "from2d", 20., title="ME+2/1 collisions MC with 5 pb^{-1}, fitted (red) and compared with truth (green)", widebins=True, fitsine=True); real_mep21.Draw("same")
resids.append((fitsine_const[0]*1000./radius21 - (mep21phiz), fitsine_sin[0] - (-mep21x), fitsine_cos[0] - (mep21y)))
plot("CSCvsphi_mep22", "x", "from2d", 20., title="ME+2/2 collisions MC with 5 pb^{-1}, fitted (red) and compared with truth (green)", widebins=True, fitsine=True); real_mep22.Draw("same")
resids.append((fitsine_const[0]*1000./radius22 - (mep22phiz), fitsine_sin[0] - (-mep22x), fitsine_cos[0] - (mep22y)))
plot("CSCvsphi_mep31", "x", "from2d", 20., title="ME+3/1 collisions MC with 5 pb^{-1}, fitted (red) and compared with truth (green)", widebins=True, fitsine=True); real_mep31.Draw("same")
resids.append((fitsine_const[0]*1000./radius31 - (mep31phiz), fitsine_sin[0] - (-mep31x), fitsine_cos[0] - (mep31y)))
plot("CSCvsphi_mep32", "x", "from2d", 20., title="ME+3/2 collisions MC with 5 pb^{-1}, fitted (red) and compared with truth (green)", widebins=True, fitsine=True); real_mep32.Draw("same")
resids.append((fitsine_const[0]*1000./radius32 - (mep32phiz), fitsine_sin[0] - (-mep32x), fitsine_cos[0] - (mep32y)))
plot("CSCvsphi_mep41", "x", "from2d", 20., title="ME+4/1 collisions MC with 5 pb^{-1}, fitted (red) and compared with truth (green)", widebins=True, fitsine=True); real_mep41.Draw("same")
resids.append((fitsine_const[0]*1000./radius41 - (mep41phiz), fitsine_sin[0] - (-mep41x), fitsine_cos[0] - (mep41y)))

def mean(xlist):
  "Get the mean of a list."
  s, n = 0., 0.
  for x in xlist:
    s += x
    n += 1.
  return s/n

def rms(xlist):
  "Get the actual root mean square (not standard deviation!) of a list."
  s2, n = 0., 0.
  for x in xlist:
    s2 += x**2
    n += 1.
  return math.sqrt(s2/n)

def stdev(xlist):
  "Get the standard deviation of a list."
  s, s2, n = 0., 0., 0.
  for x in xlist:
    s += x
    s2 += x**2
    n += 1.
  return math.sqrt(s2/n - (s/n)**2)

print stdev([x for x, y, phiz in resids] + [y for x, y, phiz in resids]), stdev([phiz for x, y, phiz in resids])

lumiarray = array.array("d", [1.14, 2.27, 5.11, 10.27, 19.89])
xyarray = array.array("d", [0.875, 0.676, 0.356, 0.361, 0.170])
phizarray = array.array("d", [0.923, 0.919, 0.672, 0.425, 0.274])

def oneOverSqrtN(norm, x): return norm/sqrt(x)

def chi2_objective(norm):
    chi2 = 0.
    for x, y in zip(lumiarray, xyarray):
        chi2 += (y - oneOverSqrtN(norm, x))**2
    return chi2

m = minuit.Minuit(chi2_objective, norm=1.)
m.migrad()

graph = ROOT.TGraph(5, lumiarray, xyarray)
f = ROOT.TF1("f", "%g/sqrt(x)" % m.values["norm"], 0, 25.)
f.SetLineColor(ROOT.kBlack)
f.SetLineStyle(2)

backhist = ROOT.TH1F("backhist", "", 1, 0, 25)
backhist.SetAxisRange(0, 1.5, "Y")
backhist.SetXTitle("Integrated luminosity (pb^{-1})")
backhist.SetYTitle("Disk x-y resolution (mm)")
backhist.GetXaxis().CenterTitle()
backhist.GetYaxis().CenterTitle()
backhist.Draw()
graph.Draw("p")
f.Draw("same")
c1.SaveAs("mccsc_diskstats_xy.pdf")

def chi2_objective(norm):
    chi2 = 0.
    for x, y in zip(lumiarray, phizarray):
        chi2 += (y - oneOverSqrtN(norm, x))**2
    return chi2

m = minuit.Minuit(chi2_objective, norm=1.)
m.migrad()

graph = ROOT.TGraph(5, lumiarray, phizarray)
f = ROOT.TF1("f", "%g/sqrt(x)" % m.values["norm"], 0, 25.)
f.SetLineColor(ROOT.kBlack)
f.SetLineStyle(2)

backhist = ROOT.TH1F("backhist", "", 1, 0, 25)
backhist.SetAxisRange(0, 1.5, "Y")
backhist.SetXTitle("Integrated luminosity (pb^{-1})")
backhist.SetYTitle("Disk #phi_{z} resolution (mrad)")
backhist.GetXaxis().CenterTitle()
backhist.GetYaxis().CenterTitle()
backhist.Draw()
graph.Draw("p")
f.Draw("same")
c1.SaveAs("mccsc_diskstats_phiz.pdf")


########################################################

plot("CSCvsphi_mem12", "x", title="ME-1/2 x positions"); c1.SaveAs("datacsc_all_mem12x.pdf")
plot("CSCvsphi_mem22", "x", title="ME-2/2 x positions"); c1.SaveAs("datacsc_all_mem22x.pdf")
plot("CSCvsphi_mem32", "x", title="ME-3/2 x positions"); c1.SaveAs("datacsc_all_mem32x.pdf")

plot("CSCvsphi_mem12", "dxdz", title="ME-1/2 #phi_{y} angles"); c1.SaveAs("datacsc_all_mem12phiy.pdf")
plot("CSCvsphi_mem22", "dxdz", title="ME-2/2 #phi_{y} angles"); c1.SaveAs("datacsc_all_mem22phiy.pdf")
plot("CSCvsphi_mem32", "dxdz", title="ME-3/2 #phi_{y} angles"); c1.SaveAs("datacsc_all_mem32phiy.pdf")

plot("CSCvsphi_mep12", "x", title="ME+1/2 x positions"); c1.SaveAs("datacsc_all_mep12x.pdf")
plot("CSCvsphi_mep22", "x", title="ME+2/2 x positions"); c1.SaveAs("datacsc_all_mep22x.pdf")
plot("CSCvsphi_mep32", "x", title="ME+3/2 x positions"); c1.SaveAs("datacsc_all_mep32x.pdf")

plot("CSCvsphi_mep12", "dxdz", title="ME-1/2 #phi_{y} angles"); c1.SaveAs("datacsc_all_mep12phiy.pdf")
plot("CSCvsphi_mep22", "dxdz", title="ME-2/2 #phi_{y} angles"); c1.SaveAs("datacsc_all_mep22phiy.pdf")
plot("CSCvsphi_mep32", "dxdz", title="ME-3/2 #phi_{y} angles"); c1.SaveAs("datacsc_all_mep32phiy.pdf")






###################################################

plotDirectory = "/home/jpivarski/work/results/CRAFTchambers2/CSCCRAFT_phiy_only/BEFORE/"
tfiles = [ROOT.TFile(plotDirectory + f) for f in os.listdir(plotDirectory) if f[-5:] == ".root"]

plot("CSCvsphi_mem12", "dxdz", high=15., title="ME-1/2 before alignment"); c1.SaveAs("cscphiy_mem12_before.pdf")
plot("CSCvsphi_mem22", "dxdz", high=15., title="ME-2/2 before alignment"); c1.SaveAs("cscphiy_mem22_before.pdf")
plot("CSCvsphi_mem32", "dxdz", high=15., title="ME-3/2 before alignment"); c1.SaveAs("cscphiy_mem32_before.pdf")

plot("CSCvsphi_mep12", "dxdz", high=15., title="ME+1/2 before alignment"); c1.SaveAs("cscphiy_mep12_before.pdf")
plot("CSCvsphi_mep22", "dxdz", high=15., title="ME+2/2 before alignment"); c1.SaveAs("cscphiy_mep22_before.pdf")
plot("CSCvsphi_mep32", "dxdz", high=15., title="ME+3/2 before alignment"); c1.SaveAs("cscphiy_mep32_before.pdf")

plotDirectory = "/home/jpivarski/work/results/CRAFTchambers2/CSCCRAFT_phiy_only/AFTER/"
tfiles = [ROOT.TFile(plotDirectory + f) for f in os.listdir(plotDirectory) if f[-5:] == ".root"]

plot("CSCvsphi_mem12", "dxdz", high=15., title="ME-1/2 after alignment"); c1.SaveAs("cscphiy_mem12_after.pdf")
plot("CSCvsphi_mem22", "dxdz", high=15., title="ME-2/2 after alignment"); c1.SaveAs("cscphiy_mem22_after.pdf")
plot("CSCvsphi_mem32", "dxdz", high=15., title="ME-3/2 after alignment"); c1.SaveAs("cscphiy_mem32_after.pdf")
                                                                                                               
plot("CSCvsphi_mep12", "dxdz", high=15., title="ME+1/2 after alignment"); c1.SaveAs("cscphiy_mep12_after.pdf")
plot("CSCvsphi_mep22", "dxdz", high=15., title="ME+2/2 after alignment"); c1.SaveAs("cscphiy_mep22_after.pdf")
plot("CSCvsphi_mep32", "dxdz", high=15., title="ME+3/2 after alignment"); c1.SaveAs("cscphiy_mep32_after.pdf")

execfile("/home/jpivarski/work/results/CRAFTchambers2/CSCCRAFT_phiy_only/CSCCRAFTiter01_report.py")
reports_iter1 = reports

execfile("/home/jpivarski/work/results/CRAFTchambers2/CSCCRAFT_phiy_only/CSCCRAFTiter02_report.py")
reports_iter2 = reports

execfile("/home/jpivarski/work/results/CRAFTchambers2/CSCCRAFT_phiy_only/CSCCRAFTiter03_report.py")
reports_iter3 = reports

for endcap in 1, 2:
    for (station, ring) in (1,1), (1,4), (1,2), (1,3), (2,1), (2,2), (3,1), (3,2), (4,1):
        nchambers = 36
        if (station, ring) in [(2,1), (3,1), (4,1)]: nchambers = 18
        for chamber in range(1, nchambers+1):
            for r in reports_iter1:
                if r.postal_address == ("CSC", endcap, station, ring, chamber):
                    r1 = r
                    break
            for r in reports_iter2:
                if r.postal_address == ("CSC", endcap, station, ring, chamber):
                    r2 = r
                    break
            for r in reports_iter3:
                if r.postal_address == ("CSC", endcap, station, ring, chamber):
                    r3 = r
                    break
            if r1.status == "PASS" or r2.status == "PASS" or r3.status == "PASS":
                print "ME%s%d/%d, %d & " % (("$+$" if endcap == 1 else "$-$"), station, ring, chamber),
                if r1.status == "PASS":
                    print "$%5.2f$ & " % (r1.deltaphiy.value*1000.),
                else:
                    print "FAIL & ",
                if r2.status == "PASS":
                    print "$%5.2f$ & " % (r2.deltaphiy.value*1000.),
                else:
                    print "FAIL & ",
                if r3.status == "PASS":
                    print "$%5.2f$ \\\\" % (r3.deltaphiy.value*1000.)
                else:
                    print "FAIL \\\\"







###################################################

plot("CSCvsphi_mem11", "x")
plot("CSCvsphi_mem12", "x")
plot("CSCvsphi_mem13", "x")
plot("CSCvsphi_mem14", "x")
plot("CSCvsphi_mem21", "x")
plot("CSCvsphi_mem22", "x")
plot("CSCvsphi_mem31", "x")
plot("CSCvsphi_mem32", "x")
plot("CSCvsphi_mem41", "x")
plot("CSCvsphi_mep11", "x")
plot("CSCvsphi_mep12", "x")
plot("CSCvsphi_mep13", "x")
plot("CSCvsphi_mep14", "x")
plot("CSCvsphi_mep21", "x")
plot("CSCvsphi_mep22", "x")
plot("CSCvsphi_mep31", "x")
plot("CSCvsphi_mep32", "x")
plot("CSCvsphi_mep41", "x")

plot("CSCvsphi_mem11", "dxdz")
plot("CSCvsphi_mem12", "dxdz")
plot("CSCvsphi_mem13", "dxdz")
plot("CSCvsphi_mem14", "dxdz")
plot("CSCvsphi_mem21", "dxdz")
plot("CSCvsphi_mem22", "dxdz")
plot("CSCvsphi_mem31", "dxdz")
plot("CSCvsphi_mem32", "dxdz")
plot("CSCvsphi_mem41", "dxdz")
plot("CSCvsphi_mep11", "dxdz")
plot("CSCvsphi_mep12", "dxdz")
plot("CSCvsphi_mep13", "dxdz")
plot("CSCvsphi_mep14", "dxdz")
plot("CSCvsphi_mep21", "dxdz")
plot("CSCvsphi_mep22", "dxdz")
plot("CSCvsphi_mep31", "dxdz")
plot("CSCvsphi_mep32", "dxdz")
plot("CSCvsphi_mep41", "dxdz")

plot("CSCvsr_mem1ch01", "x")
plot("CSCvsr_mem1ch02", "x")
plot("CSCvsr_mem1ch03", "x")
plot("CSCvsr_mem1ch04", "x")
plot("CSCvsr_mem1ch05", "x")
plot("CSCvsr_mem1ch06", "x")
plot("CSCvsr_mem1ch07", "x")
plot("CSCvsr_mem1ch08", "x")
plot("CSCvsr_mem1ch09", "x")
plot("CSCvsr_mem1ch10", "x")
plot("CSCvsr_mem1ch11", "x")
plot("CSCvsr_mem1ch12", "x")
plot("CSCvsr_mem1ch13", "x")
plot("CSCvsr_mem1ch14", "x")
plot("CSCvsr_mem1ch15", "x")
plot("CSCvsr_mem1ch16", "x")
plot("CSCvsr_mem1ch17", "x")
plot("CSCvsr_mem1ch18", "x")
plot("CSCvsr_mem1ch19", "x")
plot("CSCvsr_mem1ch20", "x")
plot("CSCvsr_mem1ch21", "x")
plot("CSCvsr_mem1ch22", "x")
plot("CSCvsr_mem1ch23", "x")
plot("CSCvsr_mem1ch24", "x")
plot("CSCvsr_mem1ch25", "x")
plot("CSCvsr_mem1ch26", "x")
plot("CSCvsr_mem1ch27", "x")
plot("CSCvsr_mem1ch28", "x")
plot("CSCvsr_mem1ch29", "x")
plot("CSCvsr_mem1ch30", "x")
plot("CSCvsr_mem1ch31", "x")
plot("CSCvsr_mem1ch32", "x")
plot("CSCvsr_mem1ch33", "x")
plot("CSCvsr_mem1ch34", "x")
plot("CSCvsr_mem1ch35", "x")
plot("CSCvsr_mem1ch36", "x")

plot("CSCvsr_mem2ch01", "x")
plot("CSCvsr_mem2ch02", "x")
plot("CSCvsr_mem2ch03", "x")
plot("CSCvsr_mem2ch04", "x")
plot("CSCvsr_mem2ch05", "x")
plot("CSCvsr_mem2ch06", "x")
plot("CSCvsr_mem2ch07", "x")
plot("CSCvsr_mem2ch08", "x")
plot("CSCvsr_mem2ch09", "x")
plot("CSCvsr_mem2ch10", "x")
plot("CSCvsr_mem2ch11", "x")
plot("CSCvsr_mem2ch12", "x")
plot("CSCvsr_mem2ch13", "x")
plot("CSCvsr_mem2ch14", "x")
plot("CSCvsr_mem2ch15", "x")
plot("CSCvsr_mem2ch16", "x")
plot("CSCvsr_mem2ch17", "x")
plot("CSCvsr_mem2ch18", "x")
plot("CSCvsr_mem2ch19", "x")
plot("CSCvsr_mem2ch20", "x")
plot("CSCvsr_mem2ch21", "x")
plot("CSCvsr_mem2ch22", "x")
plot("CSCvsr_mem2ch23", "x")
plot("CSCvsr_mem2ch24", "x")
plot("CSCvsr_mem2ch25", "x")
plot("CSCvsr_mem2ch26", "x")
plot("CSCvsr_mem2ch27", "x")
plot("CSCvsr_mem2ch28", "x")
plot("CSCvsr_mem2ch29", "x")
plot("CSCvsr_mem2ch30", "x")
plot("CSCvsr_mem2ch31", "x")
plot("CSCvsr_mem2ch32", "x")
plot("CSCvsr_mem2ch33", "x")
plot("CSCvsr_mem2ch34", "x")
plot("CSCvsr_mem2ch35", "x")
plot("CSCvsr_mem2ch36", "x")

plot("CSCvsr_mem3ch01", "x")
plot("CSCvsr_mem3ch02", "x")
plot("CSCvsr_mem3ch03", "x")
plot("CSCvsr_mem3ch04", "x")
plot("CSCvsr_mem3ch05", "x")
plot("CSCvsr_mem3ch06", "x")
plot("CSCvsr_mem3ch07", "x")
plot("CSCvsr_mem3ch08", "x")
plot("CSCvsr_mem3ch09", "x")
plot("CSCvsr_mem3ch10", "x")
plot("CSCvsr_mem3ch11", "x")
plot("CSCvsr_mem3ch12", "x")
plot("CSCvsr_mem3ch13", "x")
plot("CSCvsr_mem3ch14", "x")
plot("CSCvsr_mem3ch15", "x")
plot("CSCvsr_mem3ch16", "x")
plot("CSCvsr_mem3ch17", "x")
plot("CSCvsr_mem3ch18", "x")
plot("CSCvsr_mem3ch19", "x")
plot("CSCvsr_mem3ch20", "x")
plot("CSCvsr_mem3ch21", "x")
plot("CSCvsr_mem3ch22", "x")
plot("CSCvsr_mem3ch23", "x")
plot("CSCvsr_mem3ch24", "x")
plot("CSCvsr_mem3ch25", "x")
plot("CSCvsr_mem3ch26", "x")
plot("CSCvsr_mem3ch27", "x")
plot("CSCvsr_mem3ch28", "x")
plot("CSCvsr_mem3ch29", "x")
plot("CSCvsr_mem3ch30", "x")
plot("CSCvsr_mem3ch31", "x")
plot("CSCvsr_mem3ch32", "x")
plot("CSCvsr_mem3ch33", "x")
plot("CSCvsr_mem3ch34", "x")
plot("CSCvsr_mem3ch35", "x")
plot("CSCvsr_mem3ch36", "x")

plot("CSCvsr_mem4ch01", "x")
plot("CSCvsr_mem4ch03", "x")
plot("CSCvsr_mem4ch05", "x")
plot("CSCvsr_mem4ch07", "x")
plot("CSCvsr_mem4ch09", "x")
plot("CSCvsr_mem4ch11", "x")
plot("CSCvsr_mem4ch13", "x")
plot("CSCvsr_mem4ch15", "x")
plot("CSCvsr_mem4ch17", "x")
plot("CSCvsr_mem4ch19", "x")
plot("CSCvsr_mem4ch21", "x")
plot("CSCvsr_mem4ch23", "x")
plot("CSCvsr_mem4ch25", "x")
plot("CSCvsr_mem4ch27", "x")
plot("CSCvsr_mem4ch29", "x")
plot("CSCvsr_mem4ch31", "x")
plot("CSCvsr_mem4ch33", "x")
plot("CSCvsr_mem4ch35", "x")

plot("CSCvsr_mep1ch01", "x")
plot("CSCvsr_mep1ch02", "x")
plot("CSCvsr_mep1ch03", "x")
plot("CSCvsr_mep1ch04", "x")
plot("CSCvsr_mep1ch05", "x")
plot("CSCvsr_mep1ch06", "x")
plot("CSCvsr_mep1ch07", "x")
plot("CSCvsr_mep1ch08", "x")
plot("CSCvsr_mep1ch09", "x")
plot("CSCvsr_mep1ch10", "x")
plot("CSCvsr_mep1ch11", "x")
plot("CSCvsr_mep1ch12", "x")
plot("CSCvsr_mep1ch13", "x")
plot("CSCvsr_mep1ch14", "x")
plot("CSCvsr_mep1ch15", "x")
plot("CSCvsr_mep1ch16", "x")
plot("CSCvsr_mep1ch17", "x")
plot("CSCvsr_mep1ch18", "x")
plot("CSCvsr_mep1ch19", "x")
plot("CSCvsr_mep1ch20", "x")
plot("CSCvsr_mep1ch21", "x")
plot("CSCvsr_mep1ch22", "x")
plot("CSCvsr_mep1ch23", "x")
plot("CSCvsr_mep1ch24", "x")
plot("CSCvsr_mep1ch25", "x")
plot("CSCvsr_mep1ch26", "x")
plot("CSCvsr_mep1ch27", "x")
plot("CSCvsr_mep1ch28", "x")
plot("CSCvsr_mep1ch29", "x")
plot("CSCvsr_mep1ch30", "x")
plot("CSCvsr_mep1ch31", "x")
plot("CSCvsr_mep1ch32", "x")
plot("CSCvsr_mep1ch33", "x")
plot("CSCvsr_mep1ch34", "x")
plot("CSCvsr_mep1ch35", "x")
plot("CSCvsr_mep1ch36", "x")

plot("CSCvsr_mep2ch01", "x")
plot("CSCvsr_mep2ch02", "x")
plot("CSCvsr_mep2ch03", "x")
plot("CSCvsr_mep2ch04", "x")
plot("CSCvsr_mep2ch05", "x")
plot("CSCvsr_mep2ch06", "x")
plot("CSCvsr_mep2ch07", "x")
plot("CSCvsr_mep2ch08", "x")
plot("CSCvsr_mep2ch09", "x")
plot("CSCvsr_mep2ch10", "x")
plot("CSCvsr_mep2ch11", "x")
plot("CSCvsr_mep2ch12", "x")
plot("CSCvsr_mep2ch13", "x")
plot("CSCvsr_mep2ch14", "x")
plot("CSCvsr_mep2ch15", "x")
plot("CSCvsr_mep2ch16", "x")
plot("CSCvsr_mep2ch17", "x")
plot("CSCvsr_mep2ch18", "x")
plot("CSCvsr_mep2ch19", "x")
plot("CSCvsr_mep2ch20", "x")
plot("CSCvsr_mep2ch21", "x")
plot("CSCvsr_mep2ch22", "x")
plot("CSCvsr_mep2ch23", "x")
plot("CSCvsr_mep2ch24", "x")
plot("CSCvsr_mep2ch25", "x")
plot("CSCvsr_mep2ch26", "x")
plot("CSCvsr_mep2ch27", "x")
plot("CSCvsr_mep2ch28", "x")
plot("CSCvsr_mep2ch29", "x")
plot("CSCvsr_mep2ch30", "x")
plot("CSCvsr_mep2ch31", "x")
plot("CSCvsr_mep2ch32", "x")
plot("CSCvsr_mep2ch33", "x")
plot("CSCvsr_mep2ch34", "x")
plot("CSCvsr_mep2ch35", "x")
plot("CSCvsr_mep2ch36", "x")

plot("CSCvsr_mep3ch01", "x")
plot("CSCvsr_mep3ch02", "x")
plot("CSCvsr_mep3ch03", "x")
plot("CSCvsr_mep3ch04", "x")
plot("CSCvsr_mep3ch05", "x")
plot("CSCvsr_mep3ch06", "x")
plot("CSCvsr_mep3ch07", "x")
plot("CSCvsr_mep3ch08", "x")
plot("CSCvsr_mep3ch09", "x")
plot("CSCvsr_mep3ch10", "x")
plot("CSCvsr_mep3ch11", "x")
plot("CSCvsr_mep3ch12", "x")
plot("CSCvsr_mep3ch13", "x")
plot("CSCvsr_mep3ch14", "x")
plot("CSCvsr_mep3ch15", "x")
plot("CSCvsr_mep3ch16", "x")
plot("CSCvsr_mep3ch17", "x")
plot("CSCvsr_mep3ch18", "x")
plot("CSCvsr_mep3ch19", "x")
plot("CSCvsr_mep3ch20", "x")
plot("CSCvsr_mep3ch21", "x")
plot("CSCvsr_mep3ch22", "x")
plot("CSCvsr_mep3ch23", "x")
plot("CSCvsr_mep3ch24", "x")
plot("CSCvsr_mep3ch25", "x")
plot("CSCvsr_mep3ch26", "x")
plot("CSCvsr_mep3ch27", "x")
plot("CSCvsr_mep3ch28", "x")
plot("CSCvsr_mep3ch29", "x")
plot("CSCvsr_mep3ch30", "x")
plot("CSCvsr_mep3ch31", "x")
plot("CSCvsr_mep3ch32", "x")
plot("CSCvsr_mep3ch33", "x")
plot("CSCvsr_mep3ch34", "x")
plot("CSCvsr_mep3ch35", "x")
plot("CSCvsr_mep3ch36", "x")

plot("CSCvsr_mep4ch01", "x")
plot("CSCvsr_mep4ch03", "x")
plot("CSCvsr_mep4ch05", "x")
plot("CSCvsr_mep4ch07", "x")
plot("CSCvsr_mep4ch09", "x")
plot("CSCvsr_mep4ch11", "x")
plot("CSCvsr_mep4ch13", "x")
plot("CSCvsr_mep4ch15", "x")
plot("CSCvsr_mep4ch17", "x")
plot("CSCvsr_mep4ch19", "x")
plot("CSCvsr_mep4ch21", "x")
plot("CSCvsr_mep4ch23", "x")
plot("CSCvsr_mep4ch25", "x")
plot("CSCvsr_mep4ch27", "x")
plot("CSCvsr_mep4ch29", "x")
plot("CSCvsr_mep4ch31", "x")
plot("CSCvsr_mep4ch33", "x")
plot("CSCvsr_mep4ch35", "x")

plot("CSCvsr_mem1ch01", "dxdz")
plot("CSCvsr_mem1ch02", "dxdz")
plot("CSCvsr_mem1ch03", "dxdz")
plot("CSCvsr_mem1ch04", "dxdz")
plot("CSCvsr_mem1ch05", "dxdz")
plot("CSCvsr_mem1ch06", "dxdz")
plot("CSCvsr_mem1ch07", "dxdz")
plot("CSCvsr_mem1ch08", "dxdz")
plot("CSCvsr_mem1ch09", "dxdz")
plot("CSCvsr_mem1ch10", "dxdz")
plot("CSCvsr_mem1ch11", "dxdz")
plot("CSCvsr_mem1ch12", "dxdz")
plot("CSCvsr_mem1ch13", "dxdz")
plot("CSCvsr_mem1ch14", "dxdz")
plot("CSCvsr_mem1ch15", "dxdz")
plot("CSCvsr_mem1ch16", "dxdz")
plot("CSCvsr_mem1ch17", "dxdz")
plot("CSCvsr_mem1ch18", "dxdz")
plot("CSCvsr_mem1ch19", "dxdz")
plot("CSCvsr_mem1ch20", "dxdz")
plot("CSCvsr_mem1ch21", "dxdz")
plot("CSCvsr_mem1ch22", "dxdz")
plot("CSCvsr_mem1ch23", "dxdz")
plot("CSCvsr_mem1ch24", "dxdz")
plot("CSCvsr_mem1ch25", "dxdz")
plot("CSCvsr_mem1ch26", "dxdz")
plot("CSCvsr_mem1ch27", "dxdz")
plot("CSCvsr_mem1ch28", "dxdz")
plot("CSCvsr_mem1ch29", "dxdz")
plot("CSCvsr_mem1ch30", "dxdz")
plot("CSCvsr_mem1ch31", "dxdz")
plot("CSCvsr_mem1ch32", "dxdz")
plot("CSCvsr_mem1ch33", "dxdz")
plot("CSCvsr_mem1ch34", "dxdz")
plot("CSCvsr_mem1ch35", "dxdz")
plot("CSCvsr_mem1ch36", "dxdz")
                               
plot("CSCvsr_mem2ch01", "dxdz")
plot("CSCvsr_mem2ch02", "dxdz")
plot("CSCvsr_mem2ch03", "dxdz")
plot("CSCvsr_mem2ch04", "dxdz")
plot("CSCvsr_mem2ch05", "dxdz")
plot("CSCvsr_mem2ch06", "dxdz")
plot("CSCvsr_mem2ch07", "dxdz")
plot("CSCvsr_mem2ch08", "dxdz")
plot("CSCvsr_mem2ch09", "dxdz")
plot("CSCvsr_mem2ch10", "dxdz")
plot("CSCvsr_mem2ch11", "dxdz")
plot("CSCvsr_mem2ch12", "dxdz")
plot("CSCvsr_mem2ch13", "dxdz")
plot("CSCvsr_mem2ch14", "dxdz")
plot("CSCvsr_mem2ch15", "dxdz")
plot("CSCvsr_mem2ch16", "dxdz")
plot("CSCvsr_mem2ch17", "dxdz")
plot("CSCvsr_mem2ch18", "dxdz")
plot("CSCvsr_mem2ch19", "dxdz")
plot("CSCvsr_mem2ch20", "dxdz")
plot("CSCvsr_mem2ch21", "dxdz")
plot("CSCvsr_mem2ch22", "dxdz")
plot("CSCvsr_mem2ch23", "dxdz")
plot("CSCvsr_mem2ch24", "dxdz")
plot("CSCvsr_mem2ch25", "dxdz")
plot("CSCvsr_mem2ch26", "dxdz")
plot("CSCvsr_mem2ch27", "dxdz")
plot("CSCvsr_mem2ch28", "dxdz")
plot("CSCvsr_mem2ch29", "dxdz")
plot("CSCvsr_mem2ch30", "dxdz")
plot("CSCvsr_mem2ch31", "dxdz")
plot("CSCvsr_mem2ch32", "dxdz")
plot("CSCvsr_mem2ch33", "dxdz")
plot("CSCvsr_mem2ch34", "dxdz")
plot("CSCvsr_mem2ch35", "dxdz")
plot("CSCvsr_mem2ch36", "dxdz")
                               
plot("CSCvsr_mem3ch01", "dxdz")
plot("CSCvsr_mem3ch02", "dxdz")
plot("CSCvsr_mem3ch03", "dxdz")
plot("CSCvsr_mem3ch04", "dxdz")
plot("CSCvsr_mem3ch05", "dxdz")
plot("CSCvsr_mem3ch06", "dxdz")
plot("CSCvsr_mem3ch07", "dxdz")
plot("CSCvsr_mem3ch08", "dxdz")
plot("CSCvsr_mem3ch09", "dxdz")
plot("CSCvsr_mem3ch10", "dxdz")
plot("CSCvsr_mem3ch11", "dxdz")
plot("CSCvsr_mem3ch12", "dxdz")
plot("CSCvsr_mem3ch13", "dxdz")
plot("CSCvsr_mem3ch14", "dxdz")
plot("CSCvsr_mem3ch15", "dxdz")
plot("CSCvsr_mem3ch16", "dxdz")
plot("CSCvsr_mem3ch17", "dxdz")
plot("CSCvsr_mem3ch18", "dxdz")
plot("CSCvsr_mem3ch19", "dxdz")
plot("CSCvsr_mem3ch20", "dxdz")
plot("CSCvsr_mem3ch21", "dxdz")
plot("CSCvsr_mem3ch22", "dxdz")
plot("CSCvsr_mem3ch23", "dxdz")
plot("CSCvsr_mem3ch24", "dxdz")
plot("CSCvsr_mem3ch25", "dxdz")
plot("CSCvsr_mem3ch26", "dxdz")
plot("CSCvsr_mem3ch27", "dxdz")
plot("CSCvsr_mem3ch28", "dxdz")
plot("CSCvsr_mem3ch29", "dxdz")
plot("CSCvsr_mem3ch30", "dxdz")
plot("CSCvsr_mem3ch31", "dxdz")
plot("CSCvsr_mem3ch32", "dxdz")
plot("CSCvsr_mem3ch33", "dxdz")
plot("CSCvsr_mem3ch34", "dxdz")
plot("CSCvsr_mem3ch35", "dxdz")
plot("CSCvsr_mem3ch36", "dxdz")
                               
plot("CSCvsr_mem4ch01", "dxdz")
plot("CSCvsr_mem4ch03", "dxdz")
plot("CSCvsr_mem4ch05", "dxdz")
plot("CSCvsr_mem4ch07", "dxdz")
plot("CSCvsr_mem4ch09", "dxdz")
plot("CSCvsr_mem4ch11", "dxdz")
plot("CSCvsr_mem4ch13", "dxdz")
plot("CSCvsr_mem4ch15", "dxdz")
plot("CSCvsr_mem4ch17", "dxdz")
plot("CSCvsr_mem4ch19", "dxdz")
plot("CSCvsr_mem4ch21", "dxdz")
plot("CSCvsr_mem4ch23", "dxdz")
plot("CSCvsr_mem4ch25", "dxdz")
plot("CSCvsr_mem4ch27", "dxdz")
plot("CSCvsr_mem4ch29", "dxdz")
plot("CSCvsr_mem4ch31", "dxdz")
plot("CSCvsr_mem4ch33", "dxdz")
plot("CSCvsr_mem4ch35", "dxdz")
                               
plot("CSCvsr_mep1ch01", "dxdz")
plot("CSCvsr_mep1ch02", "dxdz")
plot("CSCvsr_mep1ch03", "dxdz")
plot("CSCvsr_mep1ch04", "dxdz")
plot("CSCvsr_mep1ch05", "dxdz")
plot("CSCvsr_mep1ch06", "dxdz")
plot("CSCvsr_mep1ch07", "dxdz")
plot("CSCvsr_mep1ch08", "dxdz")
plot("CSCvsr_mep1ch09", "dxdz")
plot("CSCvsr_mep1ch10", "dxdz")
plot("CSCvsr_mep1ch11", "dxdz")
plot("CSCvsr_mep1ch12", "dxdz")
plot("CSCvsr_mep1ch13", "dxdz")
plot("CSCvsr_mep1ch14", "dxdz")
plot("CSCvsr_mep1ch15", "dxdz")
plot("CSCvsr_mep1ch16", "dxdz")
plot("CSCvsr_mep1ch17", "dxdz")
plot("CSCvsr_mep1ch18", "dxdz")
plot("CSCvsr_mep1ch19", "dxdz")
plot("CSCvsr_mep1ch20", "dxdz")
plot("CSCvsr_mep1ch21", "dxdz")
plot("CSCvsr_mep1ch22", "dxdz")
plot("CSCvsr_mep1ch23", "dxdz")
plot("CSCvsr_mep1ch24", "dxdz")
plot("CSCvsr_mep1ch25", "dxdz")
plot("CSCvsr_mep1ch26", "dxdz")
plot("CSCvsr_mep1ch27", "dxdz")
plot("CSCvsr_mep1ch28", "dxdz")
plot("CSCvsr_mep1ch29", "dxdz")
plot("CSCvsr_mep1ch30", "dxdz")
plot("CSCvsr_mep1ch31", "dxdz")
plot("CSCvsr_mep1ch32", "dxdz")
plot("CSCvsr_mep1ch33", "dxdz")
plot("CSCvsr_mep1ch34", "dxdz")
plot("CSCvsr_mep1ch35", "dxdz")
plot("CSCvsr_mep1ch36", "dxdz")
                               
plot("CSCvsr_mep2ch01", "dxdz")
plot("CSCvsr_mep2ch02", "dxdz")
plot("CSCvsr_mep2ch03", "dxdz")
plot("CSCvsr_mep2ch04", "dxdz")
plot("CSCvsr_mep2ch05", "dxdz")
plot("CSCvsr_mep2ch06", "dxdz")
plot("CSCvsr_mep2ch07", "dxdz")
plot("CSCvsr_mep2ch08", "dxdz")
plot("CSCvsr_mep2ch09", "dxdz")
plot("CSCvsr_mep2ch10", "dxdz")
plot("CSCvsr_mep2ch11", "dxdz")
plot("CSCvsr_mep2ch12", "dxdz")
plot("CSCvsr_mep2ch13", "dxdz")
plot("CSCvsr_mep2ch14", "dxdz")
plot("CSCvsr_mep2ch15", "dxdz")
plot("CSCvsr_mep2ch16", "dxdz")
plot("CSCvsr_mep2ch17", "dxdz")
plot("CSCvsr_mep2ch18", "dxdz")
plot("CSCvsr_mep2ch19", "dxdz")
plot("CSCvsr_mep2ch20", "dxdz")
plot("CSCvsr_mep2ch21", "dxdz")
plot("CSCvsr_mep2ch22", "dxdz")
plot("CSCvsr_mep2ch23", "dxdz")
plot("CSCvsr_mep2ch24", "dxdz")
plot("CSCvsr_mep2ch25", "dxdz")
plot("CSCvsr_mep2ch26", "dxdz")
plot("CSCvsr_mep2ch27", "dxdz")
plot("CSCvsr_mep2ch28", "dxdz")
plot("CSCvsr_mep2ch29", "dxdz")
plot("CSCvsr_mep2ch30", "dxdz")
plot("CSCvsr_mep2ch31", "dxdz")
plot("CSCvsr_mep2ch32", "dxdz")
plot("CSCvsr_mep2ch33", "dxdz")
plot("CSCvsr_mep2ch34", "dxdz")
plot("CSCvsr_mep2ch35", "dxdz")
plot("CSCvsr_mep2ch36", "dxdz")
                               
plot("CSCvsr_mep3ch01", "dxdz")
plot("CSCvsr_mep3ch02", "dxdz")
plot("CSCvsr_mep3ch03", "dxdz")
plot("CSCvsr_mep3ch04", "dxdz")
plot("CSCvsr_mep3ch05", "dxdz")
plot("CSCvsr_mep3ch06", "dxdz")
plot("CSCvsr_mep3ch07", "dxdz")
plot("CSCvsr_mep3ch08", "dxdz")
plot("CSCvsr_mep3ch09", "dxdz")
plot("CSCvsr_mep3ch10", "dxdz")
plot("CSCvsr_mep3ch11", "dxdz")
plot("CSCvsr_mep3ch12", "dxdz")
plot("CSCvsr_mep3ch13", "dxdz")
plot("CSCvsr_mep3ch14", "dxdz")
plot("CSCvsr_mep3ch15", "dxdz")
plot("CSCvsr_mep3ch16", "dxdz")
plot("CSCvsr_mep3ch17", "dxdz")
plot("CSCvsr_mep3ch18", "dxdz")
plot("CSCvsr_mep3ch19", "dxdz")
plot("CSCvsr_mep3ch20", "dxdz")
plot("CSCvsr_mep3ch21", "dxdz")
plot("CSCvsr_mep3ch22", "dxdz")
plot("CSCvsr_mep3ch23", "dxdz")
plot("CSCvsr_mep3ch24", "dxdz")
plot("CSCvsr_mep3ch25", "dxdz")
plot("CSCvsr_mep3ch26", "dxdz")
plot("CSCvsr_mep3ch27", "dxdz")
plot("CSCvsr_mep3ch28", "dxdz")
plot("CSCvsr_mep3ch29", "dxdz")
plot("CSCvsr_mep3ch30", "dxdz")
plot("CSCvsr_mep3ch31", "dxdz")
plot("CSCvsr_mep3ch32", "dxdz")
plot("CSCvsr_mep3ch33", "dxdz")
plot("CSCvsr_mep3ch34", "dxdz")
plot("CSCvsr_mep3ch35", "dxdz")
plot("CSCvsr_mep3ch36", "dxdz")
                               
plot("CSCvsr_mep4ch01", "dxdz")
plot("CSCvsr_mep4ch03", "dxdz")
plot("CSCvsr_mep4ch05", "dxdz")
plot("CSCvsr_mep4ch07", "dxdz")
plot("CSCvsr_mep4ch09", "dxdz")
plot("CSCvsr_mep4ch11", "dxdz")
plot("CSCvsr_mep4ch13", "dxdz")
plot("CSCvsr_mep4ch15", "dxdz")
plot("CSCvsr_mep4ch17", "dxdz")
plot("CSCvsr_mep4ch19", "dxdz")
plot("CSCvsr_mep4ch21", "dxdz")
plot("CSCvsr_mep4ch23", "dxdz")
plot("CSCvsr_mep4ch25", "dxdz")
plot("CSCvsr_mep4ch27", "dxdz")
plot("CSCvsr_mep4ch29", "dxdz")
plot("CSCvsr_mep4ch31", "dxdz")
plot("CSCvsr_mep4ch33", "dxdz")
plot("CSCvsr_mep4ch35", "dxdz")


