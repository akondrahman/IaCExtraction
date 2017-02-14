cat("\014") 
options(max.print=1000000)
library(vioplot)
t1 <- Sys.time()
categ_size_file <- "/Users/akond/Documents/AkondOneDrive/OneDrive/IaC-Defect-Categ-Project/output/size_per_categ/Categ_Size_.csv"
categ_size_data <- read.csv(categ_size_file, stringsAsFactors=F)

T_size  <- categ_size_data$T
t_no_na <- na.omit(T_size)

I_size  <- categ_size_data$I
i_no_na <- na.omit(I_size)

D_size    <- categ_size_data$D
d_no_na   <- na.omit(D_size)

F_size    <- categ_size_data$F
f_no_na   <- na.omit(F_size)

C_size    <- categ_size_data$C
c_no_na   <- na.omit(C_size)

B_size    <- categ_size_data$B
b_no_na   <- na.omit(B_size)

O_size    <- categ_size_data$O
o_no_na   <- na.omit(O_size)

N_size    <- categ_size_data$N
n_no_na   <- na.omit(N_size)

AS_size   <- categ_size_data$AS
as_no_na  <- na.omit(AS_size)

AL_size   <- categ_size_data$AL
al_no_na  <- na.omit(AL_size)


plotData <- function(T_size_P, I_size_P, D_size_P, F_size_P, C_size_P, B_size_P, O_size_P, N_size_P, AS_size_P, AL_size_P, yLab_P, yLimP)
{

  dir2compile="/Users/akond/Documents/AkondOneDrive/OneDrive/IaC_Mining/IaCExtraction/src/analysis/"
  dir2SavePlots="/Users/akond/Documents/AkondOneDrive/OneDrive/IaC-Defect-Categ-Project/output/size_per_categ/"
  # make sure the plots are saved in the output directory 
  setwd(dir2SavePlots)
  # set the box plot name file 
  box_plot_file_name <- paste(yLab_P, ".box.png", sep=".")  
  png(box_plot_file_name, width=8, height=6, units="in", res=750)
  boxplot(T_size_P, I_size_P, D_size_P, F_size_P, C_size_P, B_size_P, O_size_P, N_size_P, AS_size_P, AL_size_P, 
          col=c("grey","blue","green", "yellow", "red", "grey","blue","green", "yellow", "red"), 
          names=c("T","I", "D", "F", "C", "B", "O", "N", "AS", "AL"), xlab="Defect Categories", 
          ylab=yLab_P, ylim=yLimP
        )
  dev.off()
  # saving box plot done 
  # set the violin plot name 
  vio_plot_file_name <- paste(yLab_P, ".vio.png", sep=".")  
  png(vio_plot_file_name, width=8, height=6, units="in", res=750)
  vioplot(T_size_P, I_size_P, D_size_P, F_size_P, C_size_P, B_size_P, O_size_P, N_size_P, AS_size_P, AL_size_P, 
          names=c("T","I", "D", "F", "C", "B", "O", "N", "AS", "AL"), col="yellow", ylim=yLimP)
  title(yLab_P)
  # saving violin plot done   
  dev.off()
  ## go back to src directory 
  setwd(dir2compile)
}


plotData(t_no_na, i_no_na, d_no_na, f_no_na, c_no_na, b_no_na, o_no_na, n_no_na, as_no_na, al_no_na,  "Size (Bytes)", c(0, 10000))



t2 <- Sys.time()
print(t2 - t1)  # 
rm(list = setdiff(ls(), lsf.str()))