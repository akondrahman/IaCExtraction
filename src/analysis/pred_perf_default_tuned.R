library(ggplot2)
library(effsize)
library(stats)
cat("\014") 
options(max.print=1000000)

t1 <- Sys.time()
dir2save="/Users/akond/Documents/AkondOneDrive/OneDrive/IaC-Defect-Prediction-Project/results/"

getWilcoxonTest<- function(highParam, lowParam, infoParam) 
{
  print(infoParam)  
  print("-------------------------")
  print("H != L")
  t_test_output <- wilcox.test(highParam, lowParam, alternative="two.sided", var.equal=FALSE, paired=FALSE) 
  print(t_test_output)
  print("-------------------------")  
  print("H > L")  
  t_test_output <- wilcox.test(highParam, lowParam, alternative="greater", var.equal=FALSE, paired=FALSE) 
  print(t_test_output)
  print("-------------------------")  
  print("H < L")    
  t_test_output <- wilcox.test(highParam, lowParam, alternative="less", var.equal=FALSE, paired=FALSE) 
  print(t_test_output )
  print("-------------------------")  
  getCohen(highParam, lowParam)
}

getCohen<- function(cohen_amount_high, cohen_amount_low) 
{
  
  print("---------------")
  print("Cohen's D: Mean of high")
  mean_high = mean(cohen_amount_high, na.rm=TRUE)
  print(mean_high)
  print("Cohen's D: Mean of low")
  mean_low = mean(cohen_amount_low, na.rm=TRUE)
  print(mean_low)  
  print("Cohen's D: S.D of high")
  sd_high = sd(cohen_amount_high, na.rm = TRUE)
  print(sd_high)
  print("Cohen's D: S.D. of low")
  sd_low = sd(cohen_amount_low, na.rm = TRUE) 
  print(sd_low)
  cohen_numerator = mean_high - mean_low 
  cohen_denominator = sqrt(( sd_high ^ 2 + sd_low ^ 2 ) / 2 )
  cohen_ = cohen_numerator / cohen_denominator 
  print("Finally:::Cohen's D:::")
  print(cohen_)
  print("---------------")  
}

plotBabyPlot <- function(data2plot, xLabelP, yLabelP, limitP)
{
  plot <- ggplot(data2plot, aes(x=group, y=value)) + geom_boxplot(width = 0.75) + labs(x=xLabelP, y=yLabelP)
  plot <- plot + theme_bw() + stat_summary(fun.y=mean, colour="black", geom="point", shape=18, size=3, show.legend = FALSE)
  plot <- plot + scale_y_continuous(limits=limitP)
  ###print(plot)
  file2save <-paste0(dir2save, yLabelP, sep="")
  file2save <-paste0(file2save, ".png", sep="")  
  ggsave(file=file2save)
}

getPerfValues <- function(dirParam, orgParam)
{
  filPrefix <- "PRED_PERF_"
  p1Prefix  <- paste0(dirParam, orgParam, sep="")
  p2Prefix  <- paste0(p1Prefix, filPrefix, sep="")  
  
  CART_FILE  <- paste0(p2Prefix, "CART.csv")
  CART_PERF  <- read.csv(CART_FILE)
  
  RF_FILE   <- paste0(p2Prefix, "RF.csv")
  RF_PERF   <- read.csv(RF_FILE)
  
  SVC_FILE   <- paste0(p2Prefix, "SVC.csv")
  SVC_PERF   <- read.csv(SVC_FILE)
  
  LOGI_FILE   <- paste0(p2Prefix, "LOGIREG.csv")
  LOGI_PERF   <- read.csv(LOGI_FILE)  
  
  cart_precision <- data.frame(group = "CART", value = CART_PERF$PRECISION)
  rf_precision   <- data.frame(group = "RF", value = RF_PERF$PRECISION)
  svc_precision  <- data.frame(group = "SVC", value  = SVC_PERF$PRECISION)
  logi_precision <- data.frame(group = "LOGI", value  = LOGI_PERF$PRECISION)
  
  precision_of_learners               <- rbind(cart_precision, rf_precision, svc_precision, 
                                               logi_precision)  
  
  plotBabyPlot(precision_of_learners, "Statistical Learners", "Precision", c(0.50, 0.75))    
  
  cart_recall <- data.frame(group = "CART", value = CART_PERF$RECALL)
  rf_recall   <- data.frame(group = "RF", value = RF_PERF$RECALL)
  svc_recall  <- data.frame(group = "SVC", value  = SVC_PERF$RECALL)
  logi_recall <- data.frame(group = "LOGI", value  = LOGI_PERF$RECALL)
  
  recall_of_learners               <- rbind(cart_recall, rf_recall, svc_recall, 
                                            logi_recall)  
  
  plotBabyPlot(recall_of_learners, "Statistical Learners", "Recall", c(0.50, 0.90))  
  
  cart_auc <- data.frame(group = "CART", value = CART_PERF$AUC)
  rf_auc   <- data.frame(group = "RF", value = RF_PERF$AUC)
  svc_auc  <- data.frame(group = "SVC", value  = SVC_PERF$AUC)
  logi_auc <- data.frame(group = "LOGI", value  = LOGI_PERF$AUC)
  
  auc_of_learners               <- rbind(cart_auc, rf_auc, svc_auc, 
                                         logi_auc)  
  plotBabyPlot(auc_of_learners, "Statistical Learners", "AUC", c(0.50, 0.80))  
  
  ### finally returning 
  auc_per_values_to_ret <-c(CART_PERF$AUC, RF_PERF$AUC, SVC_PERF$AUC, LOGI_PERF$AUC)
  
  return (auc_per_values_to_ret)
}
### get before  tranformation data 
dirPrefix <- "/Users/akond/Documents/AkondOneDrive/OneDrive/IaC-Defect-Prediction-Project/results/March01/"
orgPrefix <-"MOZ_"
before_all_pred_perf_values <- getPerfValues(dirPrefix, orgPrefix)
### get after tranformation data 
# dirPrefix <- "/Users/akond/Documents/AkondOneDrive/OneDrive/IaC-Defect-Prediction-Project/results/March13-Log-Tuning/"
# orgPrefix <-"WIKI_"
# after_all_pred_perf_values  <- getPerfValues(dirPrefix, orgPrefix)
### compare 
learners <-c("CART", "RF", "SVC", "AUC")
# for(index_ in 1: length(before_all_pred_perf_values))
# {
#      learner <- learners[index_]
#      print(learner)
#      before_ <- before_all_pred_perf_values[index_]
#      after_  <- after_all_pred_perf_values[index_]
#      ### comparison 
#      getWilcoxonTest(after_, before_, learner)
#      
# }



t2 <- Sys.time()
print(t2 - t1)  # 
rm(list = setdiff(ls(), lsf.str()))