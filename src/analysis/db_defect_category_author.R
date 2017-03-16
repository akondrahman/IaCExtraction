cat("\014") 
options(max.print=1000000)
t1 <- Sys.time()

library(RMySQL)
FileOut <-"/Users/akond/Documents/AkondOneDrive/OneDrive/IaC-Defect-Categ-Project/output/author_per_categ/"

mydb = dbConnect(MySQL(), user='root', password='SrcML#2016', dbname='IaC_DB', host='localhost')
#dbListTables(mydb)
fullContent <- c()
categs      <-c('AL', 'AS', 'B', 'C', 'D', 'F', 'I', 'N', 'O', 'T')
#categs      <-c('AL', 'AS', 'B', 'C', 'D', 'F', 'I', 'O', 'T')
len_categ   <-length(categs)
tot_def_cnt <-0
tot_lin_cnt <-0
for(index_ in 1:len_categ)
{
  thecateg          <- categs[index_]
  print("The category is")
  print(thecateg)
  print("========================================")
  query_part_one    <- "SELECT authorCount FROM categ_for_db WHERE categ='"
  query_part_two    <- paste0(query_part_one, thecateg, sep="")   
  query_part_three  <- paste0(query_part_two, "'", sep="")      
  
  res_q_per_categ   <- dbSendQuery(mydb, query_part_three)
  out_q_per_categ   <- fetch(res_q_per_categ, n=-1)
  uni_q_per_categ   <- unique(out_q_per_categ)
  #print(uni_q_per_categ) 
  
  ##Dump content to file 
  file2dump <- paste0(FileOut, thecateg, sep="_.csv")
  write.csv(uni_q_per_categ, file=file2dump, row.names=FALSE) 
  
  uni_q_per_categ   <- as.numeric(unlist(uni_q_per_categ))
  med_aut_per_cat   <- median(uni_q_per_categ, na.rm=TRUE)
  mean_aut_per_cat  <- mean(uni_q_per_categ, na.rm=TRUE)
  sum_aut_per_cat   <- sum(uni_q_per_categ, na.rm=TRUE)
  def_cnt_per_cat   <- length(uni_q_per_categ)
  tot_def_cnt       <- tot_def_cnt + def_cnt_per_cat
  tot_aut_cnt       <- tot_lin_cnt + sum_aut_per_cat
  mean_txt          <- paste0("Mean is:", mean_aut_per_cat, sep="")
  medi_txt          <- paste0("median is:", med_aut_per_cat, sep="")  
  print(mean_txt)  
  print(medi_txt)    
  
  aut_per_def_cat   <- sum_aut_per_cat/def_cnt_per_cat
  aut_per_def_txt   <- paste0("Author per defect categ. is:", aut_per_def_cat, sep="") 
  print(aut_per_def_txt)
  
  print("========================================")
}
print("**************************************************")
overall_aut_per_def_cat   <- tot_aut_cnt/tot_def_cnt
overall_aut_per_def_txt   <- paste0("Overall author per defect categ. is:", overall_aut_per_def_cat, sep="") 
print(overall_aut_per_def_txt)
print("**************************************************")



t2 <- Sys.time()
print(t2 - t1)  
rm(list = setdiff(ls(), lsf.str()))