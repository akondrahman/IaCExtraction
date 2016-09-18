cat("\014")  
library(effsize)
library(stats)
library(corrplot)

# Start writing to an output file

# y_bug_file="/Users/akond/PUPP_REPOS/mozilla_releng_only/puppet/y_metrics.csv"
# n_bug_file="/Users/akond/PUPP_REPOS/mozilla_releng_only/puppet/n_metrics.csv"

y_bug_file="/Users/akond/PUPP_REPOS/mozilla_releng_only/relabs-puppet/y_metrics.csv"
n_bug_file="/Users/akond/PUPP_REPOS/mozilla_releng_only/relabs-puppet/n_metrics.csv"

# y_bug_file="/Users/akond/PUPP_REPOS/wikimedia_operations_puppet_only/kafkatee/y_metrics.csv"
# n_bug_file="/Users/akond/PUPP_REPOS/wikimedia_operations_puppet_only/kafkatee/n_metrics.csv"
file_to_save_log="stat_analysis_wikimedia-only-kafkatee.txt"
file_to_save_pic1="corr_num_wikimedia-only-kafkatee.png"
file_to_save_pic2="corr_pie_wikimedia-only-kafkatee.png"

sink(file_to_save_log)
y_full_data   <- read.csv(file=y_bug_file, header=TRUE, sep=",")
n_full_data   <- read.csv(file=n_bug_file, header=TRUE, sep=",")
no_of_cols    <- ncol(y_full_data)
no_of_cols    <- no_of_cols - 1 # adjusted no of columsn because of extra column
y_full_matrix <- y_full_data[, 2:no_of_cols]
#print(y_full_matrix)

getExtractedDetails<- function(y_param, n_param, infoParam) 
{
  print(infoParam)
  print("---------------")
  print("Extraction: Mean of buggy")
  mean_y = mean(y_param, na.rm=TRUE)
  print(mean_y)
  print("Extraction: Mean of non-buggy")
  mean_n = mean(n_param, na.rm=TRUE)
  print(mean_n)  
  print("Extraction: S.D of buggy")
  sd_y = sd(y_param, na.rm = TRUE)
  print(sd_y)
  print("Extraction: S.D of non-buggy")
  sd_n = sd(n_param, na.rm = TRUE) 
  print(sd_n)  
  print("---------------")  
}




perform_compa_tests <- function(highParam, lowParam, infoParam) 
{

  print("Statistical Comparison using Wilcoxon rank sum test")
  print(infoParam)  
  print("-------------------------")
  print("Yes != No ?")
  t_test_output <- wilcox.test(highParam, lowParam, alternative="two.sided", var.equal=FALSE, paired=FALSE) 
  print(t_test_output)
  print("-------------------------")  
  print("Yes > No ?")  
  t_test_output <- wilcox.test(highParam, lowParam, alternative="greater", var.equal=FALSE, paired=FALSE) 
  print(t_test_output)
  print("-------------------------")  
  print("Yes < No ?")    
  t_test_output <- wilcox.test(highParam, lowParam, alternative="less", var.equal=FALSE, paired=FALSE) 
  print(t_test_output )
  print("-------------------------")  
}


getCliffs <- function(yes_param, no_param, infoParam)
{
  print(":::::Cliffs-Delta:::::")
  print(infoParam)
  res_effect_ = cliff.delta(yes_param,  no_param, return.dm=FALSE)
  print(res_effect_)  
}

getA12 <- function(yParam, nParam, infoParam)
{
  print(infoParam)
  print("---------------")
  print(":::::VD-A12:::::")
  print(VD.A( yParam, nParam))    
  print("---------------")  
}

performStatAnalysis<- function(yes_values_param, no_values_param, feature_param)
{
  print("********************************************************************")    
  #mean and std. extraction 
  getExtractedDetails(yes_values_param, no_values_param, feature_param)
  # statistical comparison 
  perform_compa_tests(yes_values_param, no_values_param, feature_param)
  # Cliffs Delta 
  getCliffs(yes_values_param, no_values_param, feature_param)  
  # Varghay Delanay A12
  getA12(yes_values_param, no_values_param, feature_param)
  print("********************************************************************")    
}
PerformCorrelation <- function(matrixParam)
{
  print("Correlation  Started")
  corr_mat <- cor(matrixParam, use="complete.obs", method="spearman") 
  #print(corr_mat)
  ### the number plot 
  png(file=file_to_save_pic1, width=600, height=800)
  corrplot(corr_mat, method="number", type="full")    
  dev.off()  
  #corrplot(corr_mat, method="circle", type="full")  
  ### the pie plot 
  png(file=file_to_save_pic2, width=600, height=800)
  corrplot(corr_mat, method="pie", type="full")    
  dev.off()  
  print("Correlation  Ended")    
}

### get vectors by header ### 
# Max. Nested Depth #
y_vector_ = y_full_data$max_nest_depth
n_vector_ = n_full_data$max_nest_depth
performStatAnalysis(y_vector_, n_vector_, "Max. Nested Depth")

# Class Declaration #
y_vector_ = y_full_data$class_dec
n_vector_ = n_full_data$class_dec
performStatAnalysis(y_vector_, n_vector_, "Class Declaration")

# Define Declaration #
y_vector_ = y_full_data$def_dec
n_vector_ = n_full_data$def_dec
performStatAnalysis(y_vector_, n_vector_, "Define Declaration")


# Package Declaration #
y_vector_ = y_full_data$pack_dec
n_vector_ = n_full_data$pack_dec
performStatAnalysis(y_vector_, n_vector_, "Package Declaration")

# File Declaration #
y_vector_ = y_full_data$file_dec
n_vector_ = n_full_data$file_dec
performStatAnalysis(y_vector_, n_vector_, "File Declaration")

# Service Declaration #
y_vector_ = y_full_data$serv_dec
n_vector_ = n_full_data$serv_dec
performStatAnalysis(y_vector_, n_vector_, "Service Declaration")

# Exec Declaration #
y_vector_ = y_full_data$exec_dec
n_vector_ = n_full_data$exec_dec
performStatAnalysis(y_vector_, n_vector_, "Exec Declaration")

# Cohesion Per Method #
y_vector_ = y_full_data$cohe_meth
n_vector_ = n_full_data$cohe_meth
performStatAnalysis(y_vector_, n_vector_, "Cohesion Per Method")

# Body text size #
y_vector_ = y_full_data$body_txt_size
n_vector_ = n_full_data$body_txt_size
performStatAnalysis(y_vector_, n_vector_, "Body Text Size")

# Lines with comment #
y_vector_ = y_full_data$lines_w_comm
n_vector_ = n_full_data$lines_w_comm
performStatAnalysis(y_vector_, n_vector_, "Lines with comment")

# Lines without comment #
y_vector_ = y_full_data$lines_wo_comm
n_vector_ = n_full_data$lines_wo_comm
performStatAnalysis(y_vector_, n_vector_, "Lines without comment")

# Outer Elements #
y_vector_ = y_full_data$outerelems
n_vector_ = n_full_data$outerelems
performStatAnalysis(y_vector_, n_vector_, "Outer Elements")

# No. of File Resources #
y_vector_ = y_full_data$file_reso
n_vector_ = n_full_data$file_reso
performStatAnalysis(y_vector_, n_vector_, "No. of File Resources")

# No. of Service Resources #
y_vector_ = y_full_data$service_reso
n_vector_ = n_full_data$service_reso
performStatAnalysis(y_vector_, n_vector_, "No. of Service Resources")

# No. of Package Resources #
y_vector_ = y_full_data$package_reso
n_vector_ = n_full_data$package_reso
performStatAnalysis(y_vector_, n_vector_, "No. of Package Resources")

# No. of Hard Coded Statement #
y_vector_ = y_full_data$hard_coded_stmt
n_vector_ = n_full_data$hard_coded_stmt
performStatAnalysis(y_vector_, n_vector_, "No. of Hard Coded Statement")

# No. of Node Declarations #
y_vector_ = y_full_data$node_decl
n_vector_ = n_full_data$node_decl
performStatAnalysis(y_vector_, n_vector_, "No. of Node Declarations")

# No. of Parent Classes #
y_vector_ = y_full_data$parent_class
n_vector_ = n_full_data$parent_class
performStatAnalysis(y_vector_, n_vector_, "No. of Parent Classes")

# Churn for file #
y_vector_ = y_full_data$churn
n_vector_ = n_full_data$churn
performStatAnalysis(y_vector_, n_vector_, "Churn for file")

# No. of developer count #
y_vector_ = y_full_data$devCnt
n_vector_ = n_full_data$devCnt
performStatAnalysis(y_vector_, n_vector_, "No. of developer count")

# No. of bug count #
y_vector_ = y_full_data$bugCnt
n_vector_ = n_full_data$bugCnt
performStatAnalysis(y_vector_, n_vector_, "No. of bug count")


# Correlation of values 
PerformCorrelation(y_full_matrix)

# Stop writing to the file
sink()

# Clear Stuff
rm(list = setdiff(ls(), lsf.str()))


