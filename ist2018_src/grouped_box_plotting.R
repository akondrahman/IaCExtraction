cat("\014") 
options(max.print=1000000)
t1 <- Sys.time()
library(ggplot2)


makeBoxPLot <-function(ds_param, y_axis_index, ds_name_p)
{
  col_nam <- ds_colnames[[y_axis_index]]
  boxplot <- ggplot(ds_param, aes(x = defect_status, y = ds_param[[y_axis_index]], fill = defect_status)) + geom_boxplot(width=0.25, outlier.shape=16, outlier.size=1)   
  boxplot <- boxplot + theme(text = element_text(size=30),  plot.title = element_text(hjust = 0.5))   ##text size 35 gives the best view ... don't change it 
  boxplot <- boxplot + theme(axis.title.x=element_blank(), axis.title.y=element_blank()) + theme(legend.position="none")
  boxplot <- boxplot + scale_x_discrete(labels=c("Neutral", "Defective")) 
  boxplot <- boxplot + scale_fill_manual(breaks = c("0", "1"), values=c( "green", "red"))
  boxplot <- boxplot + ggtitle(ds_name_p)
  name_     <- paste0(col_nam, '_', sep='')
  name_     <- paste0(name_, ds_name_p, sep='_')
  file2save <- paste0(name_, '.pdf', sep='')
  pdf(file2save)
  print(boxplot)
  dev.off()

  file2save <- paste0(name_, '.png', sep='')
  png(file2save)
  print(boxplot)
  dev.off()

}


# ds_file <- '/Users/akond/Documents/AkondOneDrive/OneDrive/IaC-Defect-Prediction-Project/dataset/IST_MIR.csv'
# ds_name <- 'MIRANTIS'

# ds_file <- '/Users/akond/Documents/AkondOneDrive/OneDrive/IaC-Defect-Prediction-Project/dataset/IST_MOZ.csv'
# ds_name <- 'MOZILLA'

# ds_file <- '/Users/akond/Documents/AkondOneDrive/OneDrive/IaC-Defect-Prediction-Project/dataset/IST_OST.csv'
# ds_name <- 'OPENSTACK'

# ds_file <- '/Users/akond/Documents/AkondOneDrive/OneDrive/IaC-Defect-Prediction-Project/dataset/IST_WIK.csv'
# ds_name <- 'WIKIMEDIA'

ds_data <- read.csv(ds_file)   
ds_colnames <- colnames(ds_data)
ds_data$defect_status <- as.factor(ds_data$defect_status)
print(head(ds_data))
valid_indices <- c(3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)

for (the_index in valid_indices)
{
  makeBoxPLot(ds_data, the_index, ds_name)
}



t2 <- Sys.time()
print(t2 - t1)  
rm(list = setdiff(ls(), lsf.str()))