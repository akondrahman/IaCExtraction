cat("\014") 
options(max.print=1000000)
t1 <- Sys.time()

library(RMySQL)
library(ggplot2)

CategSizeFileOut <-"/Users/akond/Documents/AkondOneDrive/OneDrive/IaC-Defect-Categ-Project/output/size_per_categ/"
mydb = dbConnect(MySQL(), user='root', password='SrcML#2016', dbname='IaC_DB', host='localhost')
#dbListTables(mydb)
fullContent <- c()
categs    <-c('AL', 'AS', 'B', 'C', 'D', 'F', 'I', 'N', 'O', 'T')
len_categ <-length(categs)
for(index_ in 1:len_categ)
{
  thecateg          <- categs[index_]
  print("The category is")
  print(thecateg)
  print("========================================")
  query_part_one    <- "SELECT size FROM categ_for_db WHERE categ='"
  query_part_two    <- paste0(query_part_one, thecateg, sep="")   
  query_part_three  <- paste0(query_part_two, "'", sep="")      
  
  res_q_per_categ   <- dbSendQuery(mydb, query_part_three)
  out_q_per_categ   <- fetch(res_q_per_categ, n=-1)
  uni_q_per_categ   <- unique(out_q_per_categ)
  #print(uni_q_per_categ) 
  
  ##Dump content to file 
  file2dump <- paste0(CategSizeFileOut, thecateg, sep="_.csv")
  write.csv(uni_q_per_categ, file=file2dump, row.names=FALSE) 

  uni_q_per_categ   <- as.numeric(unlist(uni_q_per_categ))
  med_size_per_cat  <- median(uni_q_per_categ, na.rm=TRUE)
  mean_size_per_cat <- mean(uni_q_per_categ, na.rm=TRUE)
  mean_txt          <- paste0("Mean is:", mean_size_per_cat, sep="")
  medi_txt          <- paste0("median is:", med_size_per_cat, sep="")  
  print(mean_txt)  
  print(medi_txt)    
  
  print("========================================")
}


t2 <- Sys.time()
print(t2 - t1)  
rm(list = setdiff(ls(), lsf.str()))