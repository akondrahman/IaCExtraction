library(ggplot2)
cat("\014") 
options(max.print=1000000)

t1 <- Sys.time()
colsToRemove          <- c(1, 2) ## column 1 is org, column 2 is file name
file_to_read   <- "/Users/akond/Documents/AkondOneDrive/OneDrive/IaC-Defect-Prediction-Project/dataset/SYNTHETIC_WIKI_FULL_DATASET.csv"
pred_dataset   <- read.csv(file_to_read)
defects        <- as.factor(pred_dataset$defect_status)
feature_names  <- colnames(pred_dataset)
feature_names  <- feature_names[-colsToRemove] ## skip 'file' and 'org_'
#print(feature_names)
full_dataset     <- pred_dataset[, -colsToRemove]


print("=========================")
matched_defect_indices <- which(defects == '1')
print("Count of defective files")
print(length(matched_defect_indices))
defective_dataset     <- pred_dataset[matched_defect_indices, ] 
#print(head(defective_dataset))
defective_dataset     <- defective_dataset[, -colsToRemove]
print(head(defective_dataset))
print("=========================")

print("=========================")
matched_non_defect_indices <- which(defects == '0')
print("Count of non-defective files")
print(length(matched_non_defect_indices))
non_defective_dataset     <- pred_dataset[matched_non_defect_indices, ]
non_defective_dataset     <- non_defective_dataset[, -colsToRemove]
print(head(non_defective_dataset))
print("=========================")



plotDistr <- function(data2plot)
{
  number_of_cols <- ncol(data2plot)
  number_of_cols <- number_of_cols - 1 ## skip defects column 
  for(index_ in 1:number_of_cols)
  {
    col_data  <- data2plot[, index_]
    coln_name <- feature_names[index_]
    col_plot_ <- ggplot(data2plot, aes(x=col_data)) + geom_histogram(binwidth=.5, col="red", fill="green", alpha = .2) + labs(x='bins', y=coln_name) + geom_density(aes(x=col_data))
    print(col_plot_)
  }
}

# plotDistr(non_defective_dataset)
# plotDistr(defective_dataset)
plotDistr(full_dataset)

t2 <- Sys.time()
print(t2 - t1)  # 
rm(list = setdiff(ls(), lsf.str()))