library(ggplot2)
cat("\014") 
options(max.print=1000000)

t1 <- Sys.time()

file_to_read   <- "/Users/akond/Documents/AkondOneDrive/OneDrive/IaC-Defect-Prediction-Project/dataset/ONLY_MOZILLA_FULL_DATASET.csv"
pred_dataset   <- read.csv(file_to_read)
defects        <- as.factor(pred_dataset$defect_status)
thePredictors  <- colnames(pred_dataset)
thePredictors  <- thePredictors[2:44]
#thePredictors
# Basic box plot

tot_churn_cnt_plot_           <- ggplot(pred_dataset, aes(x=factor(defects), y=tot_churn_cnt)) + geom_boxplot(aes(fill=defects))
churnday_per_SLOC_plot_       <- ggplot(pred_dataset, aes(x=factor(defects), y=churnday_per_SLOC)) + geom_boxplot(aes(fill=defects))
churn_del_per_SLOC_plot_      <- ggplot(pred_dataset, aes(x=factor(defects), y=churn_del_per_SLOC)) + geom_boxplot(aes(fill=defects))
tot_churn_per_del_churn_plot_ <- ggplot(pred_dataset, aes(x=factor(defects), y=tot_churn_per_del_churn)) + geom_boxplot(aes(fill=defects))
  
churn_per_SLOCt_plot_     <- ggplot(pred_dataset, aes(x=factor(defects), y=churn_per_SLOC)) + geom_boxplot(aes(fill=defects))
tot_churn_SLOC_plot_      <- ggplot(pred_dataset, aes(x=factor(defects), y=tot_churn_SLOC)) + geom_boxplot(aes(fill=defects))
net_cnt_per_SLOC_plot_    <- ggplot(pred_dataset, aes(x=factor(defects), y=net_cnt_per_SLOC)) + geom_boxplot(aes(fill=defects))
net_cnt_plot_             <- ggplot(pred_dataset, aes(x=factor(defects), y=net_cnt)) + geom_boxplot(aes(fill=defects))

vert_cnt_plot_        <- ggplot(pred_dataset, aes(x=factor(defects), y=virt_cnt)) + geom_boxplot(aes(fill=defects))
ip_cnt_plot_          <- ggplot(pred_dataset, aes(x=factor(defects), y=ip_cnt)) + geom_boxplot(aes(fill=defects))
nameserver_cnt_plot_  <- ggplot(pred_dataset, aes(x=factor(defects), y=nameserver_cnt)) + geom_boxplot(aes(fill=defects))
svc_cnt_plot_         <- ggplot(pred_dataset, aes(x=factor(defects), y=svc_cnt)) + geom_boxplot(aes(fill=defects))

secu_cnt_per_SLOC_plot_     <- ggplot(pred_dataset, aes(x=factor(defects), y=secu_cnt_per_SLOC)) + geom_boxplot(aes(fill=defects))
secu_cnt_plot_              <- ggplot(pred_dataset, aes(x=factor(defects), y=secu_cnt)) + geom_boxplot(aes(fill=defects))
role_cnt_plot_              <- ggplot(pred_dataset, aes(x=factor(defects), y=role_cnt)) + geom_boxplot(aes(fill=defects))
file_mode_cnt_plot_         <- ggplot(pred_dataset, aes(x=factor(defects), y=file_mode_cnt)) + geom_boxplot(aes(fill=defects))

hard_code_plot_             <- ggplot(pred_dataset, aes(x=factor(defects), y=hard_code)) + geom_boxplot(aes(fill=defects))
hard_code_per_sloc_plot_    <- ggplot(pred_dataset, aes(x=factor(defects), y=hard_code_per_sloc)) + geom_boxplot(aes(fill=defects))
comment_cnt_plot_           <- ggplot(pred_dataset, aes(x=factor(defects), y=comment_cnt)) + geom_boxplot(aes(fill=defects))
comm_cnt_per_SLOC_plot_     <- ggplot(pred_dataset, aes(x=factor(defects), y=comm_cnt_per_SLOC)) + geom_boxplot(aes(fill=defects))

run_int_plot_         <- ggplot(pred_dataset, aes(x=factor(defects), y=run_int)) + geom_boxplot(aes(fill=defects))
command_cnt_plot_     <- ggplot(pred_dataset, aes(x=factor(defects), y=command_cnt)) + geom_boxplot(aes(fill=defects))
path_cnt_plot_        <- ggplot(pred_dataset, aes(x=factor(defects), y=path_cnt)) + geom_boxplot(aes(fill=defects))
ssh_auth_cnt_plot_    <- ggplot(pred_dataset, aes(x=factor(defects), y=ssh_auth_cnt)) + geom_boxplot(aes(fill=defects))
  		
cond_usg_plot_        <- ggplot(pred_dataset, aes(x=factor(defects), y=cond_usg)) + geom_boxplot(aes(fill=defects))
namenode_usg_plot_    <- ggplot(pred_dataset, aes(x=factor(defects), y=namenode_usg)) + geom_boxplot(aes(fill=defects))
cron_usg_plot_        <- ggplot(pred_dataset, aes(x=factor(defects), y=cron_usg)) + geom_boxplot(aes(fill=defects))
param_usg_plot_       <- ggplot(pred_dataset, aes(x=factor(defects), y=param_usg)) + geom_boxplot(aes(fill=defects))  		  		

dependency_plot_             <- ggplot(pred_dataset, aes(x=factor(defects), y=dependency)) + geom_boxplot(aes(fill=defects))
dependency_per_sloc_plot_    <- ggplot(pred_dataset, aes(x=factor(defects), y=dependency_per_sloc)) + geom_boxplot(aes(fill=defects))
define_usg_plot_             <- ggplot(pred_dataset, aes(x=factor(defects), y=define_usg)) + geom_boxplot(aes(fill=defects))
reff_usg_plot_               <- ggplot(pred_dataset, aes(x=factor(defects), y=reff_usg)) + geom_boxplot(aes(fill=defects))  

req_usg_plot_      <- ggplot(pred_dataset, aes(x=factor(defects), y=req_usg)) + geom_boxplot(aes(fill=defects))
ens_usg_plot_      <- ggplot(pred_dataset, aes(x=factor(defects), y=ens_usg)) + geom_boxplot(aes(fill=defects))
unless_usg_plot_   <- ggplot(pred_dataset, aes(x=factor(defects), y=unless_usg)) + geom_boxplot(aes(fill=defects))
before_usg_plot_   <- ggplot(pred_dataset, aes(x=factor(defects), y=before_usg)) + geom_boxplot(aes(fill=defects))  
  		
location_usg_plot_        <- ggplot(pred_dataset, aes(x=factor(defects), y=location_usg)) + geom_boxplot(aes(fill=defects))
SLOC_plot_                <- ggplot(pred_dataset, aes(x=factor(defects), y=SLOC)) + geom_boxplot(aes(fill=defects))
location_per_sloc_plot_   <- ggplot(pred_dataset, aes(x=factor(defects), y=location_per_sloc)) + geom_boxplot(aes(fill=defects))
incl_usg_plot_            <- ggplot(pred_dataset, aes(x=factor(defects), y=incl_usg)) + geom_boxplot(aes(fill=defects))  

file_usg_plot_  <- ggplot(pred_dataset, aes(x=factor(defects), y=file_usg)) + geom_boxplot(aes(fill=defects))
url_usg_plot_   <- ggplot(pred_dataset, aes(x=factor(defects), y=url_usg)) + geom_boxplot(aes(fill=defects))
pkg_usg_plot_   <- ggplot(pred_dataset, aes(x=factor(defects), y=pkg_usg)) + geom_boxplot(aes(fill=defects))

LINT_WARN_RATE_plot_  <- ggplot(pred_dataset, aes(x=factor(defects), y=LINT_WARN_RATE)) + geom_boxplot(aes(fill=defects))
LINT_WARN_CNT_plot_   <- ggplot(pred_dataset, aes(x=factor(defects), y=LINT_WARN_CNT)) + geom_boxplot(aes(fill=defects))
LINT_ERR_RATE_plot_   <- ggplot(pred_dataset, aes(x=factor(defects), y=LINT_ERR_RATE)) + geom_boxplot(aes(fill=defects))
LINT_ERR_CNT_plot_    <- ggplot(pred_dataset, aes(x=factor(defects), y=LINT_ERR_CNT)) + geom_boxplot(aes(fill=defects))  
  		

tot_churn_cnt_plot_
churnday_per_SLOC_plot_
churn_del_per_SLOC_plot_
tot_churn_per_del_churn_plot_
churn_per_SLOCt_plot_
tot_churn_SLOC_plot_
net_cnt_per_SLOC_plot_
net_cnt_plot_
vert_cnt_plot_
ip_cnt_plot_
nameserver_cnt_plot_
svc_cnt_plot_
secu_cnt_per_SLOC_plot_
secu_cnt_plot_
role_cnt_plot_
file_mode_cnt_plot_
run_int_plot_
command_cnt_plot_
path_cnt_plot_
ssh_auth_cnt_plot_
hard_code_plot_
hard_code_per_sloc_plot_
comment_cnt_plot_
comm_cnt_per_SLOC_plot_
cond_usg_plot_
namenode_usg_plot_
cron_usg_plot_
param_usg_plot_
dependency_plot_
dependency_per_sloc_plot_
define_usg_plot_
reff_usg_plot_
req_usg_plot_
ens_usg_plot_
unless_usg_plot_
before_usg_plot_
location_usg_plot_
SLOC_plot_
location_per_sloc_plot_
incl_usg_plot_
file_usg_plot_
url_usg_plot_
pkg_usg_plot_
LINT_WARN_RATE_plot_
LINT_WARN_CNT_plot_
LINT_ERR_RATE_plot_
LINT_ERR_CNT_plot_

t2 <- Sys.time()
print(t2 - t1)  # 
rm(list = setdiff(ls(), lsf.str()))