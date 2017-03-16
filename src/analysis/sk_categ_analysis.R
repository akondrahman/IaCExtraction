library(ScottKnottESD)
cat("\014") 
options(max.print=1000000)
t1 <- Sys.time()
dir_file <- "/Users/akond/Documents/AkondOneDrive/OneDrive/IaC-Defect-Categ-Project/output/file_per_categ/"
dir_sloc <- "/Users/akond/Documents/AkondOneDrive/OneDrive/IaC-Defect-Categ-Project/output/loc_per_categ/"
dir_size <- "/Users/akond/Documents/AkondOneDrive/OneDrive/IaC-Defect-Categ-Project/output/size_per_categ/"



performScottKnott <- function(dirParam, infoParam)
{
  print(infoParam)
  print("==============================")
  ## Categ 1 
  file_AL <- paste0(dirParam, "AL_.csv", sep="")
  data_AL <- read.csv(file_AL , stringsAsFactors=F) 
  data_AL <- data_AL[[1]]
  ## Categ 2
  file_AS <- paste0(dirParam, "AS_.csv", sep="")
  data_AS <- read.csv(file_AS, stringsAsFactors=F)   
  data_AS <- data_AS[[1]]
  ## Categ 3
  file_B <- paste0(dirParam, "B_.csv", sep="")
  data_B <- read.csv(file_B, stringsAsFactors=F)   
  data_B <- data_B[[1]]  
  ## Categ 4
  file_C <- paste0(dirParam, "C_.csv", sep="")
  data_C <- read.csv(file_C , stringsAsFactors=F)     
  data_C <- data_C[[1]]  
  ## Categ 5
  file_D <- paste0(dirParam, "D_.csv", sep="")
  data_D <- read.csv(file_D, stringsAsFactors=F)   
  data_D <- data_D[[1]]
  ## Categ 6
  file_F <- paste0(dirParam, "F_.csv", sep="")
  data_F <- read.csv(file_F , stringsAsFactors=F)
  data_F <- data_F[[1]]
  ## Categ 7
  file_I <- paste0(dirParam, "I_.csv", sep="")
  data_I <- read.csv(file_I , stringsAsFactors=F) 
  data_I <- data_I[[1]]
  ## Categ 8
  file_O <- paste0(dirParam, "O_.csv", sep="")
  data_O <- read.csv(file_O , stringsAsFactors=F)   
  data_O <- data_O[[1]]
  ## Categ 9
  file_T <- paste0(dirParam, "T_.csv", sep="")
  data_T <- read.csv(file_T , stringsAsFactors=F)     
  data_T <- data_T[[1]]  
  
  max.len <- max(length(data_AL), length(data_AS), length(data_B), length(data_C), length(data_D), length(data_F), 
                 length(data_I), length(data_O), length(data_T))
  ###print(max.len)
  
  data_AL <- c(data_AL, rep(NA, max.len - length(data_AL)))
  data_AS <- c(data_AS, rep(NA, max.len - length(data_AS)))  
  data_B  <- c(data_B,  rep(NA, max.len - length(data_B)))
  data_C  <- c(data_C,  rep(NA, max.len - length(data_C)))    
  data_D  <- c(data_D,  rep(NA, max.len - length(data_D)))
  data_F  <- c(data_F,  rep(NA, max.len - length(data_F)))  
  data_I  <- c(data_I,  rep(NA, max.len - length(data_I)))
  data_O  <- c(data_O,  rep(NA, max.len - length(data_O)))    
  data_T  <- c(data_T,  rep(NA, max.len - length(data_T)))      
  
  theDataFrame <- data.frame(data_AL, data_AS, data_B, data_C, data_D, data_F, data_I, data_O, data_T)
  print(head(theDataFrame))
  
  sk <- sk_esd(theDataFrame)
  orig_sk_result <- sk$original  # Original Groups
  print("Original Scott Knot Rank")
  print(orig_sk_result)
  eff_sk_result  <- sk$groups    # Corrected Groups with effect size wise
  print("Corrected With Effect Size Scott Knot Rank")
  print(eff_sk_result)  
  print("==============================")
}


performScottKnott(dir_sloc, "SLOC")

t2 <- Sys.time()
print(t2 - t1)  
rm(list = setdiff(ls(), lsf.str()))