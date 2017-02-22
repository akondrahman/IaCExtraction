library(ggplot2)
cat("\014") 
options(max.print=1000000)

t1 <- Sys.time()
dirPrefix <- "/Users/akond/Documents/AkondOneDrive/OneDrive/IaC-Defect-Prediction-Project/results/"
orgPrefix <- "MOZ_"
filPrefix <- "PRED_PERF_"
p1Prefix  <- paste0(dirPrefix, orgPrefix, sep="")
p2Prefix  <- paste0(p1Prefix, filPrefix, sep="")


CART_FILE  <- paste0(p2Prefix, "CART.csv")
CART_PERF  <- read.csv(CART_FILE)

KNN_FILE   <- paste0(p2Prefix, "KNN.csv")
KNN_PERF   <- read.csv(KNN_FILE)

RF_FILE   <- paste0(p2Prefix, "RF.csv")
RF_PERF   <- read.csv(RF_FILE)

SVC_FILE   <- paste0(p2Prefix, "SVC.csv")
SVC_PERF   <- read.csv(SVC_FILE)

LOGI_FILE   <- paste0(p2Prefix, "LOGIREG.csv")
LOGI_PERF   <- read.csv(LOGI_FILE)


plotBabyPlot <- function(data2plot, xLabelP, yLabelP, limitP)
{
  precision_plot <- ggplot(data2plot, aes(x=group, y=value)) + geom_boxplot(width = 0.75) + labs(x=xLabelP, y=yLabelP)
  precision_plot <- precision_plot + theme_bw() + stat_summary(fun.y=mean, colour="black", geom="point", shape=18, size=3, show.legend = FALSE)
  precision_plot + scale_y_continuous(limits=limitP)
}


########## Precision Zone Start ##############
cart_precision <- data.frame(group = "CART", value = CART_PERF$PRECISION)
knn_precision  <- data.frame(group = "KNN", value  = KNN_PERF$PRECISION)
rf_precision   <- data.frame(group = "RF", value = RF_PERF$PRECISION)
svc_precision  <- data.frame(group = "SVC", value  = SVC_PERF$PRECISION)
logi_precision <- data.frame(group = "LOGI", value  = LOGI_PERF$PRECISION)

precision_of_learners               <- rbind(cart_precision, knn_precision, 
                                             rf_precision, svc_precision, 
                                             logi_precision)
#print(precision_of_learners)
plotBabyPlot(precision_of_learners, "Statistical Learners", "Precision", c(0.50, 0.80))
########## Precision Zone End ##############

########## AUC Zone Start ##############
cart_auc <- data.frame(group = "CART", value = CART_PERF$AUC)
knn_auc  <- data.frame(group = "KNN", value  = KNN_PERF$AUC)
rf_auc   <- data.frame(group = "RF", value = RF_PERF$AUC)
svc_auc  <- data.frame(group = "SVC", value  = SVC_PERF$AUC)
logi_auc <- data.frame(group = "LOGI", value  = LOGI_PERF$AUC)

auc_of_learners               <- rbind(cart_auc, knn_auc, 
                                       rf_auc, svc_auc, 
                                       logi_auc)
plotBabyPlot(auc_of_learners, "Statistical Learners", "AUC", c(0.50, 0.80))
########## AUC Zone End ##############

########## RECALL Zone Start ##############
cart_recall <- data.frame(group = "CART", value = CART_PERF$RECALL)
knn_recall  <- data.frame(group = "KNN", value  = KNN_PERF$RECALL)
rf_recall   <- data.frame(group = "RF", value = RF_PERF$RECALL)
svc_recall  <- data.frame(group = "SVC", value  = SVC_PERF$RECALL)
logi_recall <- data.frame(group = "LOGI", value  = LOGI_PERF$RECALL)

auc_of_learners               <- rbind(cart_recall, knn_recall, 
                                       rf_recall, svc_recall, 
                                       logi_recall)
plotBabyPlot(auc_of_learners, "Statistical Learners", "Recall", c(0.50, 0.90))
########## RECALL Zone End ##############


t2 <- Sys.time()
print(t2 - t1)  # 
rm(list = setdiff(ls(), lsf.str()))