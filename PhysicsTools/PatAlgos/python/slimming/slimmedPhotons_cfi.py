import FWCore.ParameterSet.Config as cms

slimmedPhotons = cms.EDProducer("PATPhotonSlimmer",
    src = cms.InputTag("selectedPatPhotons"),
    dropSuperCluster = cms.string("0"), # always keep SC?   # ! (r9()>0.8 || chargedHadronIso()<20 || chargedHadronIso()<0.3*pt())"), # you can put a cut to slim selectively, e.g. pt < 10
    dropBasicClusters = cms.string("0"), # you can put a cut to slim selectively, e.g. pt < 10
    dropPreshowerClusters = cms.string("0"), # you can put a cut to slim selectively, e.g. pt < 10
    dropSeedCluster = cms.string("0"), # you can put a cut to slim selectively, e.g. pt < 10
    dropRecHits = cms.string("0"), # you can put a cut to slim selectively, e.g. pt < 10
    linkToPackedPFCandidates = cms.bool(True),
    recoToPFMap = cms.InputTag("reducedEgamma","reducedPhotonPfCandMap"),
    packedPFCandidates = cms.InputTag("packedPFCandidates"),
    saveNonZSClusterShapes = cms.string("(r9()>0.8 || chargedHadronIso()<20 || chargedHadronIso()<0.3*pt())"), # save additional user floats: (sigmaIetaIeta,sigmaIphiIphi,sigmaIetaIphi,r9,e1x5_over_e5x5)_NoZS 
    reducedBarrelRecHitCollection = cms.InputTag("reducedEcalRecHitsEB"),
    reducedEndcapRecHitCollection = cms.InputTag("reducedEcalRecHitsEE"),
    modifyPhotons = cms.bool(True),
    modifierConfig = cms.PSet( modifications = cms.VPSet() ),
    PUPPIIsolationChargedHadrons = cms.InputTag("egmPhotonPUPPIIsolationForPhotons", "h+-DR030-","PAT"),
    PUPPIIsolationNeutralHadrons = cms.InputTag("egmPhotonPUPPIIsolationForPhotons", "h0-DR030-","PAT"),
    PUPPIIsolationPhotons = cms.InputTag("egmPhotonPUPPIIsolationForPhotons", "gamma-DR030-","PAT"),
)
