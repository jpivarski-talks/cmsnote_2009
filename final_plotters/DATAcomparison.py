import ROOT, array
from math import *
execfile("/home/jpivarski/bin/tdrstyle.py")
c1 = ROOT.TCanvas()
execfile("geometryXMLparser.py")

hipresult = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_sync1_realtracker/DTCRAFTiter03.xml")
# millepederesult = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/AlignmentAlgorithmSaga.xml")
millepederesult = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/MP_Craft08_2p0.xml")
v4result = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/V4alignment.xml")
# v4result = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/Alignments_CRAFT_ALL_V4.xml")
# v4result = MuonGeometry("/tmp/lucas_v4_videal.xml")
execfile("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_sync1_realtracker/DTCRAFTiter03_report.py")

hipresult_v4 = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_sync1_realtracker/DTCRAFTiter03_vsV4.xml")
millepederesult_v4 = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/AlignmentAlgorithmSaga_vsV4.xml")
hipresult_glob = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/DTCRAFT1_sync1_realtracker/DTCRAFTiter03_global.xml")
millepederesult_glob = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/AlignmentAlgorithmSaga_global.xml")

######## for MC comparison
hipresult = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/DTMC1_sync1_fullyrandom/DTMCiter03.xml")
millepederesult = MuonGeometry("/home/jpivarski/work/results/CRAFTchambers2/MP_MonteCarlo_2p0.xml")
execfile("/home/jpivarski/work/results/CRAFTchambers2/DTMC1_sync1_fullyrandom/DTMCiter03_report.py")
######## for MC comparison

for r in reports:
    if r.status == "PASS":
        hip_ideal = hipresult.dt[r.postal_address[1:]]
        mp_ideal = millepederesult.dt[r.postal_address[1:]]
        v4_ideal = v4result.dt[r.postal_address[1:]]
        hip_v4 = hipresult_v4.dt[r.postal_address[1:]]
        mp_v4 = millepederesult_v4.dt[r.postal_address[1:]]
        hip_glob = hipresult_glob.dt[r.postal_address[1:]]
        mp_glob = millepederesult_glob.dt[r.postal_address[1:]]

#         if r.deltaz is not None and r.deltaz.error != 0:
#             if (hip_ideal.z - v4_ideal.z)*10. < -2.: print "hip_ideal.z - v4_ideal.z", (hip_ideal.z - v4_ideal.z)*10.
#             if (mp_ideal.z - v4_ideal.z)*10. < -2.: print "mp_ideal.z - v4_ideal.z", (mp_ideal.z - v4_ideal.z)*10.
#             if hip_v4.z*10. < -2.: print "hip_v4.z", hip_v4.z*10.
#             if mp_v4.z*10. < -2.: print "mp_v4.z", mp_v4.z*10.

        print "wheel %d, station %d, sector %d" % r.postal_address[1:4]
        print "HIP relative to ideal (mm, mrad): %g, %g, %g, %g, %g, %g" % (hip_ideal.x*10., hip_ideal.y*10., hip_ideal.z*10., hip_ideal.phix*1000., hip_ideal.phiy*1000., hip_ideal.phiz*1000.)
        print "MP relative to ideal (mm, mrad): %g, %g, %g, %g, %g, %g" % (mp_ideal.x*10., mp_ideal.y*10., mp_ideal.z*10., mp_ideal.phix*1000., mp_ideal.phiy*1000., mp_ideal.phiz*1000.)
        print "V4 relative to ideal (mm, mrad): %g, %g, %g, %g, %g, %g" % (v4_ideal.x*10., v4_ideal.y*10., v4_ideal.z*10., v4_ideal.phix*1000., v4_ideal.phiy*1000., v4_ideal.phiz*1000.)
        print "HIP relative to V4 (mm, mrad): %g, %g, %g, %g, %g, %g" % (hip_v4.x*10., hip_v4.y*10., hip_v4.z*10., hip_v4.phix*1000., hip_v4.phiy*1000., hip_v4.phiz*1000.)
        print "MP relative to V4 (mm, mrad): %g, %g, %g, %g, %g, %g" % (mp_v4.x*10., mp_v4.y*10., mp_v4.z*10., mp_v4.phix*1000., mp_v4.phiy*1000., mp_v4.phiz*1000.)
        print "HIP global (cm, rad): %g, %g, %g, %g, %g, %g" % (hip_glob.x, hip_glob.y, hip_glob.z, hip_glob.phix, hip_glob.phiy, hip_glob.phiz)
        print "MP global (cm, rad): %g, %g, %g, %g, %g, %g" % (mp_glob.x, mp_glob.y, mp_glob.z, mp_glob.phix, mp_glob.phiy, mp_glob.phiz)
        print ""
      
hipdx = []
hipdy = []
hipdz = []
hipdphix = []
hipdphiy = []
hipdphiz = []
mpdx = []
mpdy = []
mpdz = []
mpdphix = []
mpdphiy = []
mpdphiz = []
hdiffx = ROOT.TH1F("hdiffx", "", 100, -5., 5.)
hdiffy = ROOT.TH1F("hdiffy", "", 100, -5., 5.)
hdiffz = ROOT.TH1F("hdiffz", "", 100, -10., 10.)
hdiffphix = ROOT.TH1F("hdiffphix", "", 100, -10., 10.)
hdiffphiy = ROOT.TH1F("hdiffphiy", "", 100, -7., 7.)
hdiffphiz = ROOT.TH1F("hdiffphiz", "", 100, -4., 4.)
for r in reports:
    if r.status == "PASS":
        hip = hipresult.dt[r.postal_address[1:]]
        mp = millepederesult.dt[r.postal_address[1:]]
        v4 = v4result.dt[r.postal_address[1:]]
        if r.deltax is not None and r.deltax.error != 0.:
            hipdx.append((hip.x - v4.x)*10.)
            mpdx.append((mp.x - v4.x)*10.)
            hdiffx.Fill((hip.x - mp.x)*10.)
        if r.deltay is not None and r.deltay.error != 0.:
            hipdy.append((hip.y - v4.y)*10.)
            mpdy.append((mp.y - v4.y)*10.)
            hdiffy.Fill((hip.y - mp.y)*10.)
        if r.deltaz is not None and r.deltaz.error != 0.:
            hipdz.append((hip.z - v4.z)*10.)
            mpdz.append((mp.z - v4.z)*10.)
            hdiffz.Fill((hip.z - mp.z)*10.)
        if r.deltaphix is not None and r.deltaphix.error != 0.:
            hipdphix.append((hip.phix - v4.phix)*1000.)
            mpdphix.append((mp.phix - v4.phix)*1000.)
            hdiffphix.Fill((hip.phix - mp.phix)*1000.)
        if r.deltaphiy is not None and r.deltaphiy.error != 0.:
            hipdphiy.append((hip.phiy - v4.phiy)*1000.)
            mpdphiy.append((mp.phiy - v4.phiy)*1000.)
            hdiffphiy.Fill((hip.phiy - mp.phiy)*1000.)
        if r.deltaphiz is not None and r.deltaphiz.error != 0.:
            hipdphiz.append((hip.phiz - v4.phiz)*1000.)
            mpdphiz.append((mp.phiz - v4.phiz)*1000.)
            hdiffphiz.Fill((hip.phiz - mp.phiz)*1000.)

tlines15 = [ROOT.TLine(-15, -15, 15, 15)]; tlines15[0].SetLineColor(ROOT.kGray)
for x, y in ((-15, 10), (-15, 5), (-15, 0), (-15, -5), (-15, -10), (-10, -15), (-5, -15), (0, -15), (5, -15), (10, -15)):
    tlines15.append(ROOT.TLine(x, y, -y, -x))
    tlines15[-1].SetLineColor(ROOT.kGray)
    tlines15[-1].SetLineStyle(3)

tlines75 = [ROOT.TLine(-7.5, -7.5, 7.5, 7.5)]; tlines75[0].SetLineColor(ROOT.kGray)
for x, y in ((-7.5, 6), (-7.5, 4), (-7.5, 2), (-7.5, 0), (-7.5, -2), (-7.5, -4), (-7.5, -6), (-6, -7.5), (-4, -7.5), (-2, -7.5), (0, -7.5), (2, -7.5), (4, -7.5), (6, -7.5)):
    tlines75.append(ROOT.TLine(x, y, -y, -x))
    tlines75[-1].SetLineColor(ROOT.kGray)
    tlines75[-1].SetLineStyle(3)

c1.Clear()
c1.Divide(3, 2)

c1.GetPad(1).cd()
hx = ROOT.TH1F("hx", "", 1, -15, 15)
hx.SetXTitle("x^{Reference-Target} (mm)")
hx.SetYTitle("x^{Millepede} (mm)")
hx.GetXaxis().CenterTitle()
hx.GetYaxis().CenterTitle()
hx.GetYaxis().SetTitleOffset(0.8)
hx.SetBinContent(1, -100)
hx.SetAxisRange(-15, 15, "Y")
hx.Draw()
for tline in tlines15: tline.Draw()
gx = ROOT.TGraph(len(hipdx), array.array("d", hipdx), array.array("d", mpdx))
gx.Draw("p")

c1.GetPad(2).cd()
hy = ROOT.TH1F("hy", "", 1, -15, 15)
hy.SetXTitle("y^{Reference-Target} (mm)")
hy.SetYTitle("y^{Millepede} (mm)")
hy.GetXaxis().CenterTitle()
hy.GetYaxis().CenterTitle()
hy.GetYaxis().SetTitleOffset(0.8)
hy.SetBinContent(1, -100)
hy.SetAxisRange(-15, 15, "Y")
hy.Draw()
for tline in tlines15: tline.Draw()
gy = ROOT.TGraph(len(hipdy), array.array("d", hipdy), array.array("d", mpdy))
gy.Draw("p")

c1.GetPad(3).cd()
hz = ROOT.TH1F("hz", "", 1, -15, 15)
hz.SetXTitle("z^{Reference-Target} (mm)")
hz.SetYTitle("z^{Millepede} (mm)")
hz.GetXaxis().CenterTitle()
hz.GetYaxis().CenterTitle()
hz.GetYaxis().SetTitleOffset(0.8)
hz.SetBinContent(1, -100)
hz.SetAxisRange(-15, 15, "Y")
hz.Draw()
for tline in tlines15: tline.Draw()
gz = ROOT.TGraph(len(hipdz), array.array("d", hipdz), array.array("d", mpdz))
gz.Draw("p")

c1.GetPad(4).cd()
hphix = ROOT.TH1F("hphix", "", 1, -7.5, 7.5)
hphix.SetXTitle("#phi_{x}^{Reference-Target} (mrad)")
hphix.SetYTitle("#phi_{x}^{Millepede} (mrad)")
hphix.GetXaxis().CenterTitle()
hphix.GetYaxis().CenterTitle()
hphix.GetYaxis().SetTitleOffset(0.8)
hphix.SetBinContent(1, -100)
hphix.SetAxisRange(-7.5, 7.5, "Y")
hphix.Draw()
for tline in tlines75: tline.Draw()
gphix = ROOT.TGraph(len(hipdphix), array.array("d", hipdphix), array.array("d", mpdphix))
gphix.Draw("p")

c1.GetPad(5).cd()
hphiy = ROOT.TH1F("hphiy", "", 1, -7.5, 7.5)
hphiy.SetXTitle("#phi_{y}^{Reference-Target} (mrad)")
hphiy.SetYTitle("#phi_{y}^{Millepede} (mrad)")
hphiy.GetXaxis().CenterTitle()
hphiy.GetYaxis().CenterTitle()
hphiy.GetYaxis().SetTitleOffset(0.8)
hphiy.SetBinContent(1, -100)
hphiy.SetAxisRange(-7.5, 7.5, "Y")
hphiy.Draw()
for tline in tlines75: tline.Draw()
gphiy = ROOT.TGraph(len(hipdphiy), array.array("d", hipdphiy), array.array("d", mpdphiy))
gphiy.Draw("p")

c1.GetPad(6).cd()
hphiz = ROOT.TH1F("hphiz", "", 1, -7.5, 7.5)
hphiz.SetXTitle("#phi_{z}^{Reference-Target} (mrad)")
hphiz.SetYTitle("#phi_{z}^{Millepede} (mrad)")
hphiz.GetXaxis().CenterTitle()
hphiz.GetYaxis().CenterTitle()
hphiz.GetYaxis().SetTitleOffset(0.8)
hphiz.SetBinContent(1, -100)
hphiz.SetAxisRange(-7.5, 7.5, "Y")
hphiz.Draw()
for tline in tlines75: tline.Draw()
gphiz = ROOT.TGraph(len(hipdphiz), array.array("d", hipdphiz), array.array("d", mpdphiz))
gphiz.Draw("p")

# c1.SaveAs("DATAcomparison_hip_Millepede.pdf")



c1.Clear()
c1.Divide(3, 2)

c1.GetPad(1).cd(); hdiffx.Draw(); print hdiffx.GetRMS()
c1.GetPad(2).cd(); hdiffy.Draw(); print hdiffy.GetRMS()
c1.GetPad(3).cd(); hdiffz.Draw(); print hdiffz.GetRMS()
c1.GetPad(4).cd(); hdiffphix.Draw(); print hdiffphix.GetRMS()
c1.GetPad(5).cd(); hdiffphiy.Draw(); print hdiffphiy.GetRMS()
c1.GetPad(6).cd(); hdiffphiz.Draw(); print hdiffphiz.GetRMS()



