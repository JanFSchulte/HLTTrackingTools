
import FWCore.ParameterSet.Config as cms

process = cms.Process( "Validation" )

process.load("Validation.RecoTrack.HLTmultiTrackValidator_cff")
process.load("setup_dev_CMSSW_10_0_0_GRun_cff")
doPixel = True
doTrack02 = True

process.hltTrackValidator.label = []
if doPixel:
	process.hltTrackValidator.label.extend([
    		"hltPixelTracks",
    		"hltPixelTracksFromTriplets",
    		"hltPixelTracksMerged"
	])
if doTrack02:
	process.hltTrackValidator.label.extend([
    		"hltIter0PFlowTrackSelectionHighPurity",
    		"hltIter1PFlowTrackSelectionHighPurity",
    		"hltIter1Merged",
     		"hltIter2PFlowTrackSelectionHighPurity",
    		"hltIter2Merged",
    		"hltTripletRecoveryPFlowTrackSelectionHighPurity",
    		"hltTripletRecoveryMerged",
  		"hltDoubletRecoveryPFlowTrackSelectionHighPurity",
    		"hltMergedTracks"
	])
process.load("SimGeneral.TrackingAnalysis.trackingParticleNumberOfLayersProducer_cfi")
#hltTracksValidationTruth = cms.Sequence(hltTPClusterProducer+hltTrackAssociatorByHits+trackingParticleRecoTrackAsssociation+VertexAssociatorByPositionAndTracks+trackingParticleNumberOfLayersProducer)
process.hltTracksValidationTruth = cms.Sequence(process.hltTPClusterProducer+process.hltTrackAssociatorByHits+process.trackingParticleNumberOfLayersProducer)


process.hltMultiTrackValidation = cms.Sequence(
    process.hltTracksValidationTruth
    + process.hltTrackValidator
)
#from Validation.RecoTrack.associators_cff import *

#hltTrackValidator.tip = cms.double(3.5)
#hltTrackValidator.lip = cms.double(30)
#hltTrackValidator.signalOnlyTP = cms.bool(True)


process.load("SimTracker.VertexAssociation.VertexAssociatorByPositionAndTracks_cfi")
process.hltVertexAssociatorByPositionAndTracks = process.VertexAssociatorByPositionAndTracks.clone()
process.hltVertexAssociatorByPositionAndTracks.trackAssociation = "tpToHLTpixelTrackAssociation"

process.load("Validation.RecoVertex.HLTmultiPVvalidator_cff")
process.hltMultiPVanalysis.verbose = False
#hltMultiPVanalysis.trackAssociatorMap = "tpToHLTpixelTrackAssociation"
#hltMultiPVanalysis.vertexAssociator   = "vertexAssociatorByPositionAndTracks4pixelTracks"
#tpToHLTpixelTrackAssociation.ignoremissingtrackcollection = False
process.hltPixelPVanalysis.trackAssociatorMap = "tpToHLTpixelTrackAssociation"
process.hltPixelPVanalysis.vertexAssociator = "vertexAssociatorByPositionAndTracks4pixelTracks" 

process.tpToHLTpixelTrackAssociation.label_tr = "hltPixelTracksMerged"

process.validation = cms.EndPath(
    process.hltMultiTrackValidation
    + process.hltTrackAssociatorByHits
    + process.tpToHLTpixelTrackAssociation
    + process.hltVertexAssociatorByPositionAndTracks
#    + hltMultiPVanalysis
    + process.hltMultiPVValidation
)
process.source = cms.Source( "PoolSource",
    fileNames = cms.untracked.vstring(
        'file:HLTResults.root',
    ),
    inputCommands = cms.untracked.vstring(
        'keep *'
    )
)

process.load( "DQMServices.Core.DQMStore_cfi" )
process.DQMStore.enableMultiThread = True


process.dqmOutput = cms.OutputModule("DQMRootOutputModule",
    fileName = cms.untracked.string("DQMIO.root")
)
process.DQMOutput = cms.EndPath( process.dqmOutput )

