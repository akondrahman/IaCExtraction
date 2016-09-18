cat("\014")  

y_bug_file="/Users/akond/PUPP_REPOS/openstack_puppet_only/puppet-nova/y_metrics.csv"
n_bug_file="/Users/akond/PUPP_REPOS/openstack_puppet_only/puppet-nova/n_metrics.csv"

y_full_data   <- read.csv(file=y_bug_file, header=TRUE, sep=",")
n_full_data   <- read.csv(file=n_bug_file, header=TRUE, sep=",")
no_of_cols    <- ncol(y_full_data)
no_of_cols    <- no_of_cols - 1 # adjusted no of columsn because of extra column
y_full_matrix <- y_full_data[, 2:no_of_cols]


plotBugCountAsHisto <-function(vectorParam)
{
  h     <- hist(vectorParam,  col="red", breaks=max(vectorParam), xlab="Count of bugs", ylab="Count of files", main="Histogram of bug counts")
  xfit  <- seq(min(vectorParam), max(vectorParam), length=length(vectorParam))
  yfit  <- dnorm(xfit, mean=mean(vectorParam), sd=sd(vectorParam))
  yfit  <- yfit * diff(h$mids[1:2]) * length(vectorParam)
  lines(xfit, yfit, col="black", lwd=2)  
}

plotBugCountAsDensityPlot <- function(vectorParam)
{
  d <- density(vectorParam)
  plot(d, main="Kernel Density of Bug Count in IaC Files")
  polygon(d, col="red", border="blue") 
}

# No. of bug count #
y_vector_ = y_full_data$bugCnt
n_vector_ = n_full_data$bugCnt

#Get histograms 
all_num_bugs <- c(y_vector_, n_vector_)
plotBugCountAsHisto(all_num_bugs)
#Gte density plot 
plotBugCountAsDensityPlot(all_num_bugs)

# Clear Stuff
rm(list = setdiff(ls(), lsf.str()))