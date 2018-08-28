from ROOT import * 
from numpy import array as ar
from setTDRStyle import setTDRStyle

def main():
	
	canv = TCanvas("c1","c1",800,800)

	plotPad = TPad("plotPad","plotPad",0,0,1,1)
	style = setTDRStyle()
	gStyle.SetTitleYOffset(1.45)
	gStyle.SetOptStat(0)
	plotPad.UseCurrentStyle()
	plotPad.Draw()	
	plotPad.cd()
	plotPad.DrawFrame(0,0.2,1500,5000,";time [ms]; Events / 0.5 ms")
	plotPad.SetLogy()

	
	fIdeal = TFile("DQM_V0001_R000000001__HLT__FastTimerService__All_2018Ideal.root","OPEN")
	histIdeal = fIdeal.Get("DQMData/Run 1/HLT/Run summary/TimerService/process TEST paths/path MC_ReducedIterativeTracking_v11/path time_real")
	fv3 = TFile("DQM_V0001_R000000001__HLT__FastTimerService__All_2018v3.root","OPEN")
	histv3 = fv3.Get("DQMData/Run 1/HLT/Run summary/TimerService/process TEST paths/path MC_ReducedIterativeTracking_v11/path time_real")
	fa = TFile("DQM_V0001_R000000001__HLT__FastTimerService__All_2018a.root","OPEN")
	hista = fa.Get("DQMData/Run 1/HLT/Run summary/TimerService/process TEST paths/path MC_ReducedIterativeTracking_v11/path time_real")
	fb = TFile("DQM_V0001_R000000001__HLT__FastTimerService__All_2018b.root","OPEN")
	histb = fb.Get("DQMData/Run 1/HLT/Run summary/TimerService/process TEST paths/path MC_ReducedIterativeTracking_v11/path time_real")
	fc = TFile("DQM_V0001_R000000001__HLT__FastTimerService__All_2018c.root","OPEN")
	histc = fc.Get("DQMData/Run 1/HLT/Run summary/TimerService/process TEST paths/path MC_ReducedIterativeTracking_v11/path time_real")
	fd = TFile("DQM_V0001_R000000001__HLT__FastTimerService__All_2018d.root","OPEN")
	histd = fd.Get("DQMData/Run 1/HLT/Run summary/TimerService/process TEST paths/path MC_ReducedIterativeTracking_v11/path time_real")
	#~ print hist34
	histIdeal.Rebin(15)
	histv3.Rebin(15)
	hista.Rebin(15)
	histb.Rebin(15)
	histc.Rebin(15)
	histd.Rebin(15)

	histIdeal.Draw("samehist")
	histIdeal.SetLineColor(kRed)
	histv3.SetLineColor(kBlue)
	histv3.Draw("samehist")
	hista.Draw("samehist")
	hista.SetLineColor(kGreen+1)
	histb.Draw("samehist")
	histb.SetLineColor(kOrange)
	histc.Draw("samehist")
	histc.SetLineColor(kMagenta)
	histd.Draw("samehist")
	histd.SetLineColor(kCyan)
	

	leg = TLegend(0.42, 0.61, 0.89, 0.92,"HLT PF Tracking Timing","brNDC")
	leg.SetFillColor(10)
	leg.SetLineColor(10)
	leg.SetShadowColor(0)
	leg.SetBorderSize(1)		
	leg.AddEntry(histIdeal,"Ideal %.2f ms"%histIdeal.GetMean(),"l")
	leg.AddEntry(histv3,"Startup %.2f ms"%histv3.GetMean(),"l")
	leg.AddEntry(hista,"Failure A %.2f ms"%hista.GetMean(),"l")
	leg.AddEntry(histb,"Failure B %.2f ms"%histb.GetMean(),"l")
	leg.AddEntry(histc,"Failure C %.2f ms"%histc.GetMean(),"l")
	leg.AddEntry(histd,"Failure D %.2f ms"%histd.GetMean(),"l")
	#~ leg.AddEntry(hist34,"Dynamic Doublets in IO %.2f"%hist34.GetMean(),"l")
	#~ leg.AddEntry(hist37,"Dynamic Doublets in IO Loose %.2f"%hist37.GetMean(),"l")
	leg.Draw("same")
	
	latex = TLatex()
	latex.SetTextFont(42)
	latex.SetTextAlign(31)
	latex.SetTextSize(0.04)
	latex.SetNDC(True)
	latexCMS = TLatex()
	latexCMS.SetTextFont(61)
	latexCMS.SetTextSize(0.055)
	latexCMS.SetNDC(True)
	latexCMSExtra = TLatex()
	latexCMSExtra.SetTextFont(52)
	latexCMSExtra.SetTextSize(0.03)
	latexCMSExtra.SetNDC(True) 
		
	latex.DrawLatex(0.95, 0.96, "(13 TeV)")
	
	cmsExtra = "Preliminary"
	latexCMS.DrawLatex(0.19,0.88,"CMS")
	if "Simulation" in cmsExtra:
		yLabelPos = 0.81	
	else:
		yLabelPos = 0.84	

	latexCMSExtra.DrawLatex(0.19,yLabelPos,"%s"%(cmsExtra))				
	
	
	canv.Print("timingIO.pdf")
	
	
	
main()
