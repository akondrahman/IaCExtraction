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
## Need to remove the file names by deleting the first column 
iac_pred_data <- iac_pred_data[, -c(1, 64)]
print("After filtering ...")
print(summary(iac_pred_data))
control_ <- trainControl(method="repeatedcv", number=10, repeats=5)
# train the model
#model <- train(defectStatus ~., data=iac_pred_data, method="lvq", preProcess="scale", trControl=control_)

t2 <- Sys.time()
time_diff <- t2 - t1 
print("Time taken ...")
print(time_diff)
