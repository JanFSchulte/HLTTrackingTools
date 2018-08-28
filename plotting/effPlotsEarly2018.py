from ROOT import * 
from numpy import array as ar
from setTDRStyle import setTDRStyle
import ROOT

def main():
	
	canv = TCanvas("c1","c1",800,800)
	plotPad = TPad("plotPad","plotPad",0,0,1,1)
	style = setTDRStyle()
	ROOT.gStyle.SetOptStat(0)
	plotPad.UseCurrentStyle()
	plotPad.Draw()	
	plotPad.cd()
	plotPad.cd()
	plotPad.SetGrid()
	gStyle.SetTitleXOffset(1.45)

	f0 = TFile("DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO_Good.root","OPEN")


	
	
	trackCols = ["hltPixel_hltAssociatorByHits","hltIter2PFlowTrackSelectionHighPurity_hltAssociatorByHits","hltIter2Merged_hltAssociatorByHits","hltIter1PFlowTrackSelectionHighPurity_hltAssociatorByHits","hltIter0PFlowTrackSelectionHighPurity_hltAssociatorByHits"]
	trackLabels = ["pixelTracks","iter2","iter2Merged","iter1","iter0"]
	
	variables = ['efficPt','effic','effic_vs_dr','effic_vs_phi','effic_vs_pu','effic_vs_dxy','fakerate','fakeratePt','fakerate_vs_phi','duplicatesRate','duplicatesRate_Pt']

	
	for var in variables:
		plotPad.cd()
		plotPad.SetLogx(0)
		plotPad.SetLogy(0)
		yMax = 1.2
		if 'effic' in var:
			yLabel = 'HLT Tracking Efficiency'
		elif 'fake' in var:	
			yLabel = 'Fake Rate'
			plotPad.SetLogy()			
			yMax = 5
		elif 'dupli' in var:	
			yLabel = 'Duplicate Rate'
			
		if "Pt" in var:
			plotPad.SetLogx()
			plotPad.DrawFrame(0,0.001,200,yMax,";track p_{T} [GeV]; %s"%yLabel)
		elif "dr" in var:
			plotPad.SetLogx()
			plotPad.DrawFrame(0,0.001,1,yMax,";dR; %s"%yLabel)
		elif "pu" in var:
			#~ plotPad.SetLogx()
			plotPad.DrawFrame(20,0.001,80,yMax,";PU; %s"%yLabel)
		elif "dxy" in var:
			#~ plotPad.SetLogx()
			plotPad.DrawFrame(-1,0.002,1,yMax,";dxy; %s"%yLabel)
		elif "phi" in var:
			#~ plotPad.SetLogx()
			plotPad.DrawFrame(-3,0.001,3,yMax,";#Phi; %s"%yLabel)
		else:
			plotPad.DrawFrame(-2.5,0.001,2.5,yMax,";track #eta; %s"%yLabel)

		hist0 = f0.Get("DQMData/Run 1/HLT/Run summary/Tracking/ValidationWRTtp/%s/%s"%("hltIter0PFlowTrackSelectionHighPurity_hltAssociatorByHits",var))
		hist1 = f0.Get("DQMData/Run 1/HLT/Run summary/Tracking/ValidationWRTtp/%s/%s"%("hltIter1Merged_hltAssociatorByHits",var))
		hist2 = f0.Get("DQMData/Run 1/HLT/Run summary/Tracking/ValidationWRTtp/%s/%s"%("hltIter2Merged_hltAssociatorByHits",var))
		hist3 = f0.Get("DQMData/Run 1/HLT/Run summary/Tracking/ValidationWRTtp/%s/%s"%("hltMerged_hltAssociatorByHits",var))

		
		hist0.SetMarkerColor(ROOT.kAzure-9)
		hist1.SetMarkerColor(ROOT.kAzure+5)
		hist2.SetMarkerColor(ROOT.kAzure+4)
		hist3.SetMarkerColor(ROOT.kViolet+1)
		hist0.SetFillColor(ROOT.kAzure-9)
		hist1.SetFillColor(ROOT.kAzure+5)
		hist2.SetFillColor(ROOT.kAzure+4)
		hist3.SetFillColor(ROOT.kViolet+1)
		if "fake" in var:
			hist0.SetLineColor(ROOT.kAzure-9)
			hist1.SetLineColor(ROOT.kAzure+5)
			hist2.SetLineColor(ROOT.kAzure+4)
			hist3.SetLineColor(ROOT.kViolet+1)

		if "fake" in var:
			hist2.Draw("samep")
			hist3.Draw("samep")
			hist3.SetBinError(0,0)
			hist3.SetBinError(1,0)
			hist3.SetBinError(2,0)
			hist3.SetBinError(3,0)
			hist2.SetBinError(0,0)
			hist2.SetBinError(1,0)
			hist2.SetBinError(2,0)
			hist2.SetBinError(3,0)			
		else:
			hist3.Draw("samehist")
			hist2.Draw("samehist")
			hist1.Draw("samehist")
			hist0.Draw("samehist")
		

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
			
		latex.DrawLatex(0.95, 0.96, "2018 (13 TeV)")
		
		cmsExtra = "#splitline{Simulation}{}"
		latexCMS.DrawLatex(0.19,0.88,"CMS")
		if "Simulation" in cmsExtra:
			yLabelPos = 0.83	
		else:
			yLabelPos = 0.84	

		latexCMSExtra.DrawLatex(0.19,yLabelPos,"%s"%(cmsExtra))				

		
		leg = TLegend(0.42, 0.72, 0.89, 0.92,"June 2018 Conditions","brNDC")
		leg.SetFillColor(10)
		leg.SetFillStyle(0)
		leg.SetLineColor(10)
		leg.SetShadowColor(0)
		leg.SetBorderSize(1)		
		if "fake" in var:
			leg.AddEntry(hist2,"default tracking","p")
			leg.AddEntry(hist3,"with doublet iteration","p")
		else:
			leg.AddEntry(hist0,"High p_{T} quadruplets","f")
			leg.AddEntry(hist1,"+ Low p_{T} quadruplets","f")
			leg.AddEntry(hist2,"+ Triplets in jets","f")
			leg.AddEntry(hist3,"+ Doublet recovery","f")

		if var == "effic":
			latex.DrawLatex(0.74,0.2,"#splitline{t#bar{t} event tracks <PU> = 50}{|#eta| < 2.5, p_{T} > 0.4 GeV}")		
		elif var =="effic_vs_phi":
			latex.DrawLatex(0.59,0.2,"#splitline{t#bar{t} event tracks <PU> = 50}{|#eta| < 2.5, p_{T} > 0.4 GeV}")		
		else:	
			latex.DrawLatex(0.89,0.25,"#splitline{t#bar{t} event tracks <PU> = 50}{|#eta| < 2.5, p_{T} > 0.4 GeV}")		
		leg.Draw()	

		plotPad.RedrawAxis()
	


		canv.Print("HLTTrackingPerformanceEarly2018_%s.pdf"%(var))
		canv.Print("HLTTrackingPerformanceEarly2018_%s.png"%(var))

	
	
main()
