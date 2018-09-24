cat("\014") 
set.seed(7)
# load the library
library(mlbench)
library(caret)
t1 <- Sys.time()
iac_file_name <- "/Users/akond/Documents/AkondOneDrive/OneDrive/IaC_Mining/Dataset/wikimedia_vagrant_steroided_full.csv"
iac_pred_data <- read.csv(iac_file_name, header=TRUE, stringsAsFactors=F)
# print("Before filtering ...")
# print(summary(iac_pred_data))
# convertinf defect status to string 
defect_status <- iac_pred_data$defectStatus
defect_status <- as.character(defect_status) 
## Need to remove the file names by deleting the first column 
iac_pred_data_filtered <- iac_pred_data[, -c(1, 63, 64)]
# merging the 'defect status' as string vector 
iac_full_dataframe_ <- data.frame(iac_pred_data_filtered, defect_status)
print("After filtering ...")
print(summary(iac_full_dataframe_))
varImpFlag=TRUE 
if(varImpFlag)
{
  control_ <- trainControl(method="repeatedcv", number=10, repeats=5)
  # train the model
  theModel <- train(defect_status ~., data=iac_full_dataframe_, method="lvq", preProcess="scale", trControl=control_)
  # estimate variable importance
  importance <- varImp(theModel, scale=FALSE)
  # summarize importance
  print(importance)
  # plot importance
  plot(importance)  
}

t2 <- Sys.time()
time_diff <- t2 - t1 
print("Time taken ...")
print(time_diff)
rm(list = setdiff(ls(), lsf.str()))