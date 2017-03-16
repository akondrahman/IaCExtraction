cat("\014") 
options(max.print=1000000)
t1 <- Sys.time()
dir_file <- "/Users/akond/Documents/AkondOneDrive/OneDrive/IaC-Defect-Categ-Project/output/file_per_categ"
dir_sloc <- "/Users/akond/Documents/AkondOneDrive/OneDrive/IaC-Defect-Categ-Project/output/loc_per_categ/"
dir_size <- "/Users/akond/Documents/AkondOneDrive/OneDrive/IaC-Defect-Categ-Project/output/size_per_categ/"



t2 <- Sys.time()
print(t2 - t1)  
rm(list = setdiff(ls(), lsf.str()))