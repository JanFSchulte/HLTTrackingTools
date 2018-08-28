from ROOT import * 
from numpy import array as ar
from setTDRStyle import setTDRStyle
import os
gROOT.SetBatch()
import subprocess
def main():
	
	canv = TCanvas("c1","c1",800,800)

	plotPad = TPad("plotPad","plotPad",0,0,1,1)
	#~ ratioPad = TPad("ratioPad","ratioPad",0,0.,1,0.3)
	style = setTDRStyle()
	gStyle.SetOptStat(0)
	gStyle.SetPadRightMargin(0.2)
	gStyle.SetPalette(55)

	plotPad.UseCurrentStyle()
	#~ ratioPad.UseCurrentStyle()
	plotPad.Draw()	
	#~ ratioPad.Draw()	
	plotPad.cd()
	#~ plotPad.SetGrid()
	
	useName = "tracks"
	dir = "GeneralProperties"
	histName = "TrackEtaPhi_ImpactPoint_GenTk"

	
	f0 = TFile("DQM_V0001_R000316457__Global__CMSSW_X_Y_Z__RECO_Lq.root","OPEN")
	#~ f1 = TFile("DQM_V0011_R000315366__StreamHLTMonitor__Run2018A-Express-v1__DQMIO.root","OPEN")
	#~ f2 = TFile("DQM_V0010_R000315543__StreamHLTMonitor__Run2018A-Express-v1__DQMIO.root","OPEN")
	#~ f3 = TFile("DQM_V0014_R000315689__StreamHLTMonitor__Run2018A-Express-v1__DQMIO.root","OPEN")
	#~ f4 = TFile("DQM_V0007_R000315787__StreamHLTMonitor__Run2018A-Express-v1__DQMIO.root","OPEN")
	#~ f5 = TFile("DQM_V0004_R000315974__StreamHLTMonitor__Run2018A-Express-v1__DQMIO.root","OPEN")
	#~ f6 = TFile("DQM_V0009_R000316058__StreamHLTMonitor__Run2018A-Express-v1__DQMIO.root","OPEN")
	#~ f7 = TFile("DQM_V0010_R000316239__StreamHLTMonitor__Run2018A-Express-v1__DQMIO.root","OPEN")
	#~ f8 = TFile("DQM_V0003_R000316721__StreamHLTMonitor__Run2018A-Express-v1__DQMIO.root","OPEN")

	hist0 = f0.Get("DQMData/Run 316457/HLT/Run summary/Tracking/%s/%s/%s"%(useName,dir,histName))
	#~ hist1 = f1.Get("DQMData/Run 315366/HLT/Run summary/Tracking/%s/%s/%s"%(useName,dir,histName))
	#~ hist2 = f2.Get("DQMData/Run 315543/HLT/Run summary/Tracking/%s/%s/%s"%(useName,dir,histName))
	#~ hist3 = f3.Get("DQMData/Run 315689/HLT/Run summary/Tracking/%s/%s/%s"%(useName,dir,histName))
	#~ hist4 = f4.Get("DQMData/Run 315787/HLT/Run summary/Tracking/%s/%s/%s"%(useName,dir,histName))
	#~ hist5 = f5.Get("DQMData/Run 315974/HLT/Run summary/Tracking/%s/%s/%s"%(useName,dir,histName))
	#~ hist6 = f6.Get("DQMData/Run 316058/HLT/Run summary/Tracking/%s/%s/%s"%(useName,dir,histName))
	#~ hist7 = f7.Get("DQMData/Run 316239/HLT/Run summary/Tracking/%s/%s/%s"%(useName,dir,histName))
	#~ hist8 = f8.Get("DQMData/Run 316721/HLT/Run summary/Tracking/%s/%s/%s"%(useName,dir,histName))

	hist0.GetZaxis().SetTitle("N_{tracks}")
	hist0.GetZaxis().SetTitleOffset(1.6)

	hists = [hist0]
	runs = [316457]
	zHeight = [1650]

	

	for i,hist in enumerate(hists):
		hist.Draw("colz")
		hist.GetXaxis().SetRangeUser(-2.5,2.5)
		hist.GetZaxis().SetRangeUser(0,zHeight[i])
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
		
		cmsExtra = "Private Work"
		latexCMS.DrawLatex(0.19,0.96,"CMS")
		if "Simulation" in cmsExtra:
			yLabelPos = 0.81	
		else:
			yLabelPos = 0.96	

		latexCMSExtra.DrawLatex(0.32,yLabelPos,"%s Run %d"%(cmsExtra,runs[i]))				
			

		canv.Print("TrackEtaPhi_Run%d.pdf"%runs[i])
		
	useName = "iter2Merged"
	dir = "GeneralProperties"
	histName = "TrackEtaPhi_ImpactPoint_GenTk"


	histSave = hist0
	
	hist0 = f0.Get("DQMData/Run 316457/HLT/Run summary/Tracking/%s/%s/%s"%(useName,dir,histName))
	#~ hist1 = f1.Get("DQMData/Run 315366/HLT/Run summary/Tracking/%s/%s/%s"%(useName,dir,histName))
	#~ hist2 = f2.Get("DQMData/Run 315543/HLT/Run summary/Tracking/%s/%s/%s"%(useName,dir,histName))
	#~ hist3 = f3.Get("DQMData/Run 315689/HLT/Run summary/Tracking/%s/%s/%s"%(useName,dir,histName))
	#~ hist4 = f4.Get("DQMData/Run 315787/HLT/Run summary/Tracking/%s/%s/%s"%(useName,dir,histName))
	#~ hist5 = f5.Get("DQMData/Run 315974/HLT/Run summary/Tracking/%s/%s/%s"%(useName,dir,histName))
	#~ hist6 = f6.Get("DQMData/Run 316058/HLT/Run summary/Tracking/%s/%s/%s"%(useName,dir,histName))
	#~ hist7 = f7.Get("DQMData/Run 316239/HLT/Run summary/Tracking/%s/%s/%s"%(useName,dir,histName))
	#~ hist8 = f8.Get("DQMData/Run 316721/HLT/Run summary/Tracking/%s/%s/%s"%(useName,dir,histName))
	

	
	hists = [hist0]


	hist0.GetZaxis().SetTitle("N_{tracks}")
	hist0.GetZaxis().SetTitleOffset(1.6)

	for i,hist in enumerate(hists):
		hist.Draw("colz")
		hist.GetXaxis().SetRangeUser(-2.5,2.5)
		hist.GetZaxis().SetRangeUser(0,zHeight[i])
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
		
		cmsExtra = "Private Work"
		latexCMS.DrawLatex(0.19,0.96,"CMS")
		if "Simulation" in cmsExtra:
			yLabelPos = 0.81	
		else:
			yLabelPos = 0.96	

		latexCMSExtra.DrawLatex(0.32,yLabelPos,"%s Run %d"%(cmsExtra,runs[i]))				
			

		canv.Print("TrackEtaPhi_BeforeMitigation_Run%d.pdf"%runs[i])
	
	histSave.Divide(hist0)

	histSave.GetZaxis().SetTitle("N_{tracks} ratio mitigated/default")
	histSave.GetZaxis().SetTitleOffset(1.6)	
	histSave.Draw("colz")
	histSave.GetXaxis().SetRangeUser(-2.5,2.5)
	histSave.GetZaxis().SetRangeUser(0,3)
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
	
	cmsExtra = "Private Work"
	latexCMS.DrawLatex(0.19,0.96,"CMS")
	if "Simulation" in cmsExtra:
		yLabelPos = 0.81	
	else:
		yLabelPos = 0.96	

	latexCMSExtra.DrawLatex(0.32,yLabelPos,"%s Run %d"%(cmsExtra,runs[i]))				
		

	canv.Print("TrackEtaPhi_Ratio_Run%d.pdf"%runs[i])
		
main()
