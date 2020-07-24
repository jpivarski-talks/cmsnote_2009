Double_t extendedvoigt(Double_t *xvec, Double_t *par) {
  return par[0] * TMath::Power(TMath::Voigt(xvec[0] - par[1], par[2], par[3]), par[4]/2.);
}

Double_t voigt(Double_t *xvec, Double_t *par) {
  return par[0] * TMath::Voigt(xvec[0] - par[1], par[2], par[3]);
}

void fitfunc() {}
