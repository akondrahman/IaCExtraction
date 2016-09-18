cat("\014")  

category_file <- "/Users/akond/Documents/AkondOneDrive/OneDrive/IaC_Mining/output/type-bugs-prelim/sample_defect_category.csv"
full_data   <- read.csv(file=category_file, header=TRUE, sep=",")
mozilla_releng <- full_data$Mozilla_Relabs
print("*** Mozilla Releng ***")
print(length(mozilla_releng))
print(summary(mozilla_releng))
openstack <-  full_data$Openstack_Nova
print("*** Openstack ***")
print(summary(openstack))    
print(length(openstack))

openstack_odc <- full_data$Openstack_Nova_ODC
print("*** Openstack:ODC ***")
print(summary(openstack_odc))    
print(length(openstack_odc))

# Clear Stuff
rm(list = setdiff(ls(), lsf.str()))