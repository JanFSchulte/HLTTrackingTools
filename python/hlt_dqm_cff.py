import FWCore.ParameterSet.Config as cms

from DQMOffline.Trigger.TrackingMonitoring_cff import *
pixelTracksMonitoringHLT.beamSpot   = cms.InputTag("hltOnlineBeamSpot")
iter0TracksMonitoringHLT.beamSpot   = cms.InputTag("hltOnlineBeamSpot")
iter0HPTracksMonitoringHLT.beamSpot = cms.InputTag("hltOnlineBeamSpot")
iter1TracksMonitoringHLT.beamSpot   = cms.InputTag("hltOnlineBeamSpot")
iter1HPTracksMonitoringHLT.beamSpot = cms.InputTag("hltOnlineBeamSpot")
iter2TracksMonitoringHLT.beamSpot   = cms.InputTag("hltOnlineBeamSpot")
iter2HPTracksMonitoringHLT.beamSpot = cms.InputTag("hltOnlineBeamSpot")
iter4TracksMonitoringHLT.beamSpot   = cms.InputTag("hltOnlineBeamSpot")
iterHLTTracksMonitoringHLT.beamSpot = cms.InputTag("hltOnlineBeamSpot")
pixelTracksMonitoringHLT.primaryVertex   = cms.InputTag("hltPixelVertices")
iter0TracksMonitoringHLT.primaryVertex   = cms.InputTag("hltPixelVertices")
iter0HPTracksMonitoringHLT.primaryVertex = cms.InputTag("hltPixelVertices")
iter1TracksMonitoringHLT.primaryVertex   = cms.InputTag("hltPixelVertices")
iter1HPTracksMonitoringHLT.primaryVertex = cms.InputTag("hltPixelVertices")
iter2TracksMonitoringHLT.primaryVertex   = cms.InputTag("hltPixelVertices")
iter2HPTracksMonitoringHLT.primaryVertex = cms.InputTag("hltPixelVertices")
iter4TracksMonitoringHLT.primaryVertex   = cms.InputTag("hltPixelVertices")
iterHLTTracksMonitoringHLT.primaryVertex = cms.InputTag("hltPixelVertices")
pixelTracksMonitoringHLT.pvNDOF   = cms.int32(1)
iter0TracksMonitoringHLT.pvNDOF   = cms.int32(1)
iter0HPTracksMonitoringHLT.pvNDOF = cms.int32(1)
iter1TracksMonitoringHLT.pvNDOF   = cms.int32(1)
iter1HPTracksMonitoringHLT.pvNDOF = cms.int32(1)
iter2TracksMonitoringHLT.pvNDOF   = cms.int32(1)
iter2HPTracksMonitoringHLT.pvNDOF = cms.int32(1)
iter4TracksMonitoringHLT.pvNDOF   = cms.int32(1)
iterHLTTracksMonitoringHLT.pvNDOF = cms.int32(1)


hltTrackDQM = cms.Sequence(
    trackingMonitorHLTall
    + iter0HPTracksMonitoringHLT
)


hltTrackDQM04 = cms.Sequence(
    trackingMonitorHLTall
    + iter0HPTracksMonitoringHLT
    + iter4TracksMonitoringHLT
)

# SiStripCluster monitoring
SiStripDetInfoFileReader = cms.Service("SiStripDetInfoFileReader")
from DQM.SiStripMonitorCluster.SiStripMonitorCluster_cfi import *
HLTSiStripMonitorCluster = SiStripMonitorCluster.clone()
HLTSiStripMonitorCluster.ClusterProducerStrip = cms.InputTag("hltSiStripRawToClustersFacility")
HLTSiStripMonitorCluster.ClusterProducerPix   = cms.InputTag("hltSiPixelClusters")
HLTSiStripMonitorCluster.TopFolderName        = cms.string("HLT/SiStrip")
HLTSiStripMonitorCluster.TH1TotalNumberOfClusters.subdetswitchon   = cms.bool(True)
HLTSiStripMonitorCluster.TProfClustersApvCycle.subdetswitchon      = cms.bool(False)
HLTSiStripMonitorCluster.TProfTotalNumberOfClusters.subdetswitchon = cms.bool(True)
HLTSiStripMonitorCluster.TH2CStripVsCpixel.globalswitchon       = cms.bool(True)
HLTSiStripMonitorCluster.TH1MultiplicityRegions.globalswitchon  = cms.bool(True)
HLTSiStripMonitorCluster.TH1MainDiagonalPosition.globalswitchon = cms.bool(True)
HLTSiStripMonitorCluster.TH1StripNoise2ApvCycle.globalswitchon  = cms.bool(False)
HLTSiStripMonitorCluster.TH1StripNoise3ApvCycle.globalswitchon  = cms.bool(False)
HLTSiStripMonitorCluster.ClusterHisto = cms.bool(True)
HLTSiStripMonitorCluster.Mod_On            = cms.bool(False)
HLTSiStripMonitorCluster.BPTXfilter = cms.PSet(
        andOr         = cms.bool( False ),
            dbLabel       = cms.string("SiStripDQMTrigger"),
            l1Algorithms = cms.vstring( 'L1Tech_BPTX_plus_AND_minus.v0', 'L1_ZeroBias' ),
            andOrL1       = cms.bool( True ),
            errorReplyL1  = cms.bool( True ),
            l1BeforeMask  = cms.bool( True ) # specifies, if the L1 algorithm decision should be read as before (true) or after (false) masking is applied.
        )
HLTSiStripMonitorCluster.PixelDCSfilter = cms.PSet(
        andOr         = cms.bool( False ),
            dcsInputTag   = cms.InputTag( "scalersRawToDigi" ),
            dcsPartitions = cms.vint32 ( 28, 29),
            andOrDcs      = cms.bool( False ),
            errorReplyDcs = cms.bool( True ),
        )
HLTSiStripMonitorCluster.StripDCSfilter = cms.PSet(
        andOr         = cms.bool( False ),
            dcsInputTag   = cms.InputTag( "scalersRawToDigi" ),
            dcsPartitions = cms.vint32 ( 24, 25, 26, 27 ),
            andOrDcs      = cms.bool( False ),
            errorReplyDcs = cms.bool( True ),
        )

from RecoTracker.TrackProducer.TrackRefitter_cfi import *
hltTrackRefitterForSiStripMonitorTrack = TrackRefitter.clone()
hltTrackRefitterForSiStripMonitorTrack.beamSpot                = cms.InputTag("hltOnlineBeamSpot")
hltTrackRefitterForSiStripMonitorTrack.MeasurementTrackerEvent = cms.InputTag('MeasurementTrackerEvent')
hltTrackRefitterForSiStripMonitorTrack.TrajectoryInEvent       = cms.bool(True)
hltTrackRefitterForSiStripMonitorTrack.useHitsSplitting        = cms.bool(False)
hltTrackRefitterForSiStripMonitorTrack.src                     = cms.InputTag("hltIter2Merged") # scenario 1

from DQM.SiStripMonitorTrack.SiStripMonitorTrack_cfi import *
HLTSiStripMonitorTrack = SiStripMonitorTrack.clone()
#HLTSiStripMonitorTrack.TrackProducer     = 'hltTrackRefitterForSiStripMonitorTrack' 
HLTSiStripMonitorTrack.TrackProducer     = 'hltIter2Merged' 
HLTSiStripMonitorTrack.TrackLabel        = ''
HLTSiStripMonitorTrack.AlgoName          = cms.string("HLT")
HLTSiStripMonitorTrack.Cluster_src       = cms.InputTag('hltSiStripRawToClustersFacility')
HLTSiStripMonitorTrack.Trend_On          = cms.bool(True)
HLTSiStripMonitorTrack.TopFolderName     = cms.string('HLT/SiStrip')
HLTSiStripMonitorTrack.Mod_On            = cms.bool(False)

sistripMonitorHLTsequence = cms.Sequence(
    HLTSiStripMonitorCluster
#    * hltTrackRefitterForSiStripMonitorTrack
    * HLTSiStripMonitorTrack
)    


dqm = cms.Path(
    pixelTracksMonitoringHLT
    + iter0TracksMonitoringHLT
    + iter0HPTracksMonitoringHLT
    + iter1HPTracksMonitoringHLT
    + iter1TracksMonitoringHLT
    + iter2HPTracksMonitoringHLT
    + iter2TracksMonitoringHLT
    + iterHLTTracksMonitoringHLT
)
