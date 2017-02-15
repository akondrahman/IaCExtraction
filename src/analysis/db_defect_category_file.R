cat("\014") 
options(max.print=1000000)
t1 <- Sys.time()

library(RMySQL)


CategSizeFileOut <-"/Users/akond/Documents/AkondOneDrive/OneDrive/IaC-Defect-Categ-Project/output/size_per_categ/"
mydb = dbConnect(MySQL(), user='root', password='SrcML#2016', dbname='IaC_DB', host='localhost')
#dbListTables(mydb)
fullContent  <- c()
categs       <-c('AL', 'AS', 'B', 'C', 'D', 'F', 'I', 'N', 'O', 'T')
#categs      <-c('AL', 'AS', 'B', 'C', 'D', 'F', 'I', 'O', 'T')
len_categ    <-length(categs)
tot_def_cnt  <- 0
tot_fil_cnt  <- 0
tdef_fil_cnt <- 0
for(index_ in 1:len_categ)
{
  thecateg          <- categs[index_]
  print("The category is")
  print(thecateg)
  print("========================================")
  query_part_one    <- "SELECT filepath FROM categ_for_db WHERE categ='"
  query_part_two    <- paste0(query_part_one, thecateg, sep="")   
  query_part_three  <- paste0(query_part_two, "'", sep="")      
  
  res_q_per_categ   <- dbSendQuery(mydb, query_part_three)
  out_q_per_categ   <- fetch(res_q_per_categ, n=-1)
  def_cnt_per_cat   <- length(unlist(out_q_per_categ))
  #print(uni_q_per_categ) 
  
  ##Dump content to file 
  #file2dump <- paste0(CategSizeFileOut, thecateg, sep="_.csv")
  #write.csv(uni_q_per_categ, file=file2dump, row.names=FALSE) 
  uni_q_per_categ     <- unique(out_q_per_categ)  
  fil_cnt_per_categ   <- length(unlist(uni_q_per_categ))

  tot_fil_cnt         <- tot_fil_cnt + fil_cnt_per_categ

  if(grepl(thecateg, 'N')==FALSE)
  {
    tdef_fil_cnt <- tdef_fil_cnt + fil_cnt_per_categ 
  }
  
  def_per_fil_cat     <- def_cnt_per_cat/fil_cnt_per_categ
  def_per_fil_txt     <- paste0("Defect per file is:", def_per_fil_cat, sep="") 
  print(def_per_fil_txt)
  print("========================================")
}

tot_fil_txt         <- paste0("Total number of files:", tot_fil_cnt, sep="") 
tot_def_fil_txt     <- paste0("Total number of defected files:", tdef_fil_cnt, sep="") 
print(tot_fil_txt)
print(tot_def_fil_txt)

t2 <- Sys.time()
print(t2 - t1)  
rm(list = setdiff(ls(), lsf.str()))