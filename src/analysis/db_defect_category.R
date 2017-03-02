cat("\014") 
options(max.print=1000000)
t1 <- Sys.time()

library(RMySQL)
library(ggplot2)

mydb = dbConnect(MySQL(), user='root', password='SrcML#2016', dbname='IaC_DB', host='localhost')
#dbListTables(mydb)

categs     <-c('AL', 'AS', 'B', 'C', 'D', 'F', 'I', 'N', 'O', 'T')
len_categ  <-length(categs)
total_msgs <- 0
for(index_ in 1:len_categ)
{
  thecateg          <- categs[index_]
  print("The category is")
  print(thecateg)
  
  #query_part_one    <- "SELECT COUNT(*) FROM categ_for_db WHERE repo LIKE '%MOZ%' AND categ='"
  query_part_one    <- "SELECT COUNT(*) FROM categ_for_db WHERE categ='"
  query_part_two    <- paste0(query_part_one, thecateg, sep="")   
  query_part_three  <- paste0(query_part_two, "'", sep="")      
  
  rs_q_per_mon     <- dbSendQuery(mydb, query_part_three)
  out_q_per_mon    <- fetch(rs_q_per_mon, n=-1)
  print((out_q_per_mon))  
  ## keep track of total 
  total_msgs <- total_msgs + out_q_per_mon
}
print("=============================================")
print("Total messages")
print(total_msgs)
print("=============================================")
t2 <- Sys.time()
print(t2 - t1)  
rm(list = setdiff(ls(), lsf.str()))