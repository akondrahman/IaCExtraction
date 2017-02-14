cat("\014") 
options(max.print=1000000)
t1 <- Sys.time()

library(RMySQL)


CategSizeFileOut <-"/Users/akond/Documents/AkondOneDrive/OneDrive/IaC-Defect-Categ-Project/output/size_per_categ/"
mydb = dbConnect(MySQL(), user='root', password='SrcML#2016', dbname='IaC_DB', host='localhost')
#dbListTables(mydb)
fullContent <- c()
#categs      <-c('AL', 'AS', 'B', 'C', 'D', 'F', 'I', 'N', 'O', 'T')
categs      <-c('AL', 'AS', 'B', 'C', 'D', 'F', 'I', 'O', 'T')
len_categ   <-length(categs)
tot_def_cnt <- 0
tot_siz_cnt <- 0



t2 <- Sys.time()
print(t2 - t1)  
rm(list = setdiff(ls(), lsf.str()))