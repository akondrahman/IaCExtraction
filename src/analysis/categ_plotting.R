cat("\014") 
options(max.print=1000000)
library(vioplot)
t1 <- Sys.time()
#y_limit  <- 13000 ### for size of bytes
y_limit  <- 600  ### for sloc


#y_label   <- "Size(Bytes)"
y_label  <- "LOC"


#dir_name  <- "/Users/akond/Documents/AkondOneDrive/OneDrive/IaC-Defect-Categ-Project/output/size_per_categ/"
dir_name  <- "/Users/akond/Documents/AkondOneDrive/OneDrive/IaC-Defect-Categ-Project/output/loc_per_categ/"


T_file  <- paste0(dir_name, "T_.csv", sep="")
T_data  <- read.csv(T_file, stringsAsFactors=F)
T_size  <- T_data[[1]]
t_no_na <- na.omit(T_size)

I_file  <- paste0(dir_name, "I_.csv", sep="")
I_data  <- read.csv(I_file, stringsAsFactors=F)
I_size  <- I_data[[1]]
i_no_na <- na.omit(I_size)

D_file  <- paste0(dir_name, "D_.csv", sep="")
D_data  <- read.csv(D_file, stringsAsFactors=F)
D_size  <- D_data[[1]]
d_no_na <- na.omit(D_size)

F_file  <- paste0(dir_name, "F_.csv", sep="")
F_data  <- read.csv(F_file, stringsAsFactors=F)
F_size  <- F_data[[1]]
f_no_na <- na.omit(F_size)

C_file  <- paste0(dir_name, "C_.csv", sep="")
C_data  <- read.csv(C_file, stringsAsFactors=F)
C_size  <- C_data[[1]]
c_no_na <- na.omit(C_size)

B_file  <- paste0(dir_name, "B_.csv", sep="")
B_data  <- read.csv(B_file, stringsAsFactors=F)
B_size  <- B_data[[1]]
b_no_na <- na.omit(B_size)

O_file  <- paste0(dir_name, "O_.csv", sep="")
O_data  <- read.csv(O_file, stringsAsFactors=F)
O_size  <- O_data[[1]]
o_no_na <- na.omit(O_size)

N_file  <- paste0(dir_name, "N_.csv", sep="")
N_data  <- read.csv(N_file, stringsAsFactors=F)
N_size  <- N_data[[1]]
n_no_na <- na.omit(N_size)

AS_file  <- paste0(dir_name, "AS_.csv", sep="")
AS_data  <- read.csv(AS_file, stringsAsFactors=F)
AS_size  <- AS_data[[1]]
as_no_na <- na.omit(AS_size)

AL_file  <- paste0(dir_name, "AL_.csv", sep="")
AL_data  <- read.csv(AL_file, stringsAsFactors=F)
AL_size  <- AL_data[[1]]
al_no_na <- na.omit(AL_size)


plotData <- function(T_size_P, I_size_P, D_size_P, F_size_P, C_size_P, B_size_P, O_size_P, N_size_P, AS_size_P, AL_size_P, yLab_P, yLimP)
{

  dir2compile   <- "/Users/akond/Documents/AkondOneDrive/OneDrive/IaC_Mining/IaCExtraction/src/analysis/"
  dir2SavePlots <- dir_name
  # make sure the plots are saved in the output directory 
  setwd(dir2SavePlots)
  # set the box plot name file 
  box_plot_file_name <- paste(yLab_P, "box.png", sep=".")  
  png(box_plot_file_name, width=8, height=6, units="in", res=750)
  boxplot(T_size_P, I_size_P, D_size_P, F_size_P, C_size_P, B_size_P, O_size_P, AS_size_P, AL_size_P, 
          col=c("magenta", "cyan", "yellow", "orange", "peachpuff3", "cornflowerblue", "green", "red", "purple"), 
          names=c("T","I", "D", "F", "C", "B", "O", "AS", "AL"), xlab="Defect Categories", 
          ylab=yLab_P, ylim=yLimP
        )
  all_the_means <-c(mean(T_size_P, na.rm=TRUE), mean(I_size_P, na.rm=TRUE), mean(D_size_P, na.rm=TRUE), 
                mean(F_size_P, na.rm=TRUE), mean(C_size_P, na.rm=TRUE), 
                mean(B_size_P, na.rm=TRUE), mean(O_size_P, na.rm=TRUE),  
                mean(AS_size_P, na.rm=TRUE), mean(AL_size_P, na.rm=TRUE))
  points(x = 1:9, y=all_the_means, pch=15)
  
  dev.off()
  # saving box plot done 
  # set the violin plot name 
  vio_plot_file_name <- paste(yLab_P, ".vio.png", sep=".")  
  png(vio_plot_file_name, width=8, height=6, units="in", res=750)
  vioplot(T_size_P, I_size_P, D_size_P, F_size_P, C_size_P, B_size_P, O_size_P,  AS_size_P, AL_size_P, 
          names=c("T","I", "D", "F", "C", "B", "O",  "AS", "AL"), col="yellow", ylim=yLimP)
  title(yLab_P)
  # saving violin plot done   
  dev.off()
  ## go back to src directory 
  setwd(dir2compile)
}


plotData(t_no_na, i_no_na, d_no_na, f_no_na, c_no_na, b_no_na, o_no_na, n_no_na, as_no_na, al_no_na, y_label, c(0, y_limit))



t2 <- Sys.time()
print(t2 - t1)  # 
rm(list = setdiff(ls(), lsf.str()))
# for plotting: https://www.stat.ubc.ca/~jenny/STAT545A/block14_colors.html