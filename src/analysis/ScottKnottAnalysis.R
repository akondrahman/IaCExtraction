cat("\014") 
options(max.print=1000000)
t1 <- Sys.time()

library(ScottKnottESD)
###reff: https://github.com/klainfo/ScottKnottESD
constructDataset <- function(dir_, org_)
{
  filPrefix <- "PRED_PERF_"
  p1Prefix  <- paste0(dir_, org_, sep="")
  p2Prefix  <- paste0(p1Prefix, filPrefix, sep="")
  
  
  CART_FILE  <- paste0(p2Prefix, "CART.csv")
  CART_PERF  <- read.csv(CART_FILE)
  
  NB_FILE   <- paste0(p2Prefix, "NB.csv")
  NB_PERF   <- read.csv(NB_FILE)
  
  RF_FILE   <- paste0(p2Prefix, "RF.csv")
  RF_PERF   <- read.csv(RF_FILE)
  
  SVC_FILE   <- paste0(p2Prefix, "SVC.csv")
  SVC_PERF   <- read.csv(SVC_FILE)
  
  LOGI_FILE   <- paste0(p2Prefix, "LOGIREG.csv")
  LOGI_PERF   <- read.csv(LOGI_FILE)

  cart_ <- CART_PERF$AUC
  nb_   <- NB_PERF$AUC
  rf_   <- RF_PERF$AUC
  svc_  <- SVC_PERF$AUC
  logi_ <- LOGI_PERF$AUC
  
  learner_auc    <- data.frame(cart_, nb_, rf_, svc_, logi_)
  return(learner_auc)
}


performSKPhaseOne <- function(dir_, org_)
{
  print("========================================")
  print(org_)
  datasetParam <- constructDataset(dir_, org_)
  print(head(datasetParam))
  sk <- sk_esd(datasetParam)
  orig_sk_result <- sk$original  # Original Groups
  print("Original Scott Knot Rank")
  print(orig_sk_result)
  eff_sk_result  <- sk$groups    # Corrected Groups with effect size wise
  print("Corrected With Effect Size Scott Knot Rank")
  print(eff_sk_result)
  print("========================================")
  eff_sk_result <- data.frame(eff_sk_result)
  return(eff_sk_result)
}

performSKPhaseTwo <- function(theManualFile)
{
  phaseOneRankDS  <- read.csv(theManualFile)
  print(head(phaseOneRankDS))
  sk <- sk_esd(phaseOneRankDS)
  orig_sk_result <- sk$original  # Original Groups
  print("Original Scott Knot Rank")
  print(orig_sk_result)
  eff_sk_result  <- sk$groups    # Corrected Groups with effect size wise
  print("Corrected With Effect Size Scott Knot Rank")
  print(eff_sk_result)

}

theDir <-"/Users/akond/Documents/AkondOneDrive/OneDrive/IaC-Defect-Prediction-Project/results/March01/"
# theDir <-"/Users/akond/Documents/AkondOneDrive/OneDrive/IaC-Defect-Prediction-Project/results/March13-Log-And-Tuning/"
theOrg <- "MOZ_"
moz_sk_phase_one_res  <- performSKPhaseOne(theDir, theOrg)
theOrg <- "WIKI_"
wiki_sk_phase_one_res <- performSKPhaseOne(theDir, theOrg)
### See phase one output and mnaually create teh follwoign file , otherwise error!
# theManuaFile <- "/Users/akond/Documents/AkondOneDrive/OneDrive/IaC-Defect-Prediction-Project/results/March01/ManualPhaseOne.csv"
# performSKPhaseTwo(theManuaFile)
### Abandoning phase 2 for the time being as all are ranked equally !

t2 <- Sys.time()
print(t2 - t1)  
rm(list = setdiff(ls(), lsf.str()))