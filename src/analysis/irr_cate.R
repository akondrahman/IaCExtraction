cat("\014") 
library(irr)
# my_cate <- c('AS', 'N', 'AS', 'B', 'AS', 'F', 'AS', 'B', 'F', 'AS', 'N', 'N', 'AS', 'AS', 'AS', 'AS', 'N', 'AS', 'AS', 'N', 'N', 'N', 'AS', 'N', 'N', 'AS', 'N', 'N', 'N', 'N', 'N', 'AS', 'N', 'N', 'AS', 'N', 'AS', 'N', 'AS', 'N', 'N', 'AS', 'N', 'F', 'N', 'N', 'N', 'N', 'AS', 'N', 'AS', 'N', 'N', 'AS', 'N', 'N', 'AS', 'N', 'N', 'N', 'N', 'AS', 'AS', 'F', 'N', 'I', 'AS', 'AS', 'N', 'N', 'AS', 'AS', 'N', 'N', 'AS', 'AS', 'N', 'N', 'N', 'N', 'N', 'AS', 'N', 'AS', 'AS', 'C', 'N', 'T', 'F', 'N', 'N', 'AS', 'N', 'AS', 'N', 'N', 'N', 'AS', 'AS', 'N', 'C', 'AS', 'N', 'N', 'N', 'AS', 'N', 'N', 'AS', 'AS', 'F', 'N', 'I', 'N', 'N', 'AS', 'N', 'AS', 'N', 'N', 'N', 'I', 'AS', 'AS', 'AS', 'C', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'AS', 'N', 'AS', 'AS', 'N', 'N', 'F', 'N', 'N', 'N', 'N', 'AS', 'C', 'N', 'N', 'N', 'AS', 'N', 'AS', 'AS', 'AS', 'AS', 'N', 'AS', 'AS', 'AS', 'AS', 'AS', 'AS', 'AS', 'N', 'N', 'AS', 'AS', 'N', 'AS', 'F', 'I', 'AS', 'N', 'N', 'AS', 'N', 'I', 'AS', 'AS', 'N', 'AS', 'AS', 'F', 'N', 'F', 'N', 'AS', 'N', 'N', 'I', 'I', 'N', 'N', 'AS', 'AS', 'AS', 'N', 'N', 'I', 'N', 'F', 'N', 'C', 'AS', 'N', 'N', 'AS', 'N', 'AS', 'N', 'F', 'AS', 'AS', 'T', 'AS', 'N', 'N', 'N', 'N', 'N', 'N', 'B', 'I', 'B', 'AS', 'N', 'F', 'N', 'N', 'N', 'AS', 'N', 'N', 'D', 'AS', 'AS', 'N', 'F', 'AS', 'I', 'N', 'AS', 'AS', 'N', 'AS', 'I', 'F', 'N', 'N', 'N', 'AS', 'AL', 'AS', 'AS', 'N', 'AS', 'AS', 'AS', 'AS', 'F', 'AS', 'N', 'AS', 'C', 'N', 'N', 'F', 'N', 'AS', 'N', 'N', 'AS', 'N', 'B', 'N', 'AS', 'N', 'N', 'AS', 'AS', 'N', 'AS', 'I', 'I', 'AS', 'N', 'N', 'AS', 'N', 'N', 'I', 'N', 'N', 'N', 'N', 'N', 'AS', 'I', 'AS', 'N', 'I', 'N', 'AS', 'N', 'N', 'AS', 'N', 'AS', 'N', 'N', 'AS', 'N', 'N', 'N', 'N', 'AS', 'N', 'AS', 'N', 'F', 'AS', 'N', 'N', 'AS', 'AS', 'AS', 'N', 'N', 'N', 'N', 'N', 'N')
# student_cate <- c('D', 'I', 'I', 'N', 'F', 'N', 'I', 'F', 'D', 'F', 'O', 'F', 'F', 'N', 'I', 'AS', 'AS', 'B', 'AS', 'N', 'F', 'F', 'N', 'I', 'F', 'I', 'T', 'O', 'AL', 'N', 'AS', 'C', 'AS', 'N', 'F', 'AL', 'F', 'O', 'I', 'T', 'B', 'N', 'I', 'F', 'AL', 'O', 'T', 'B', 'B', 'B', 'N', 'B', 'AS', 'B', 'AS', 'D', 'B', 'AS', 'O', 'N', 'O', 'T', 'F', 'AS', 'I', 'AS', 'B', 'B', 'F', 'B', 'N', 'AS', 'B', 'AS', 'AL', 'I', 'N', 'F', 'F', 'I', 'AS', 'AS', 'F', 'I', 'I', 'AS', 'F', 'N', 'T', 'N', 'N', 'AS', 'N', 'AS', 'AS', 'AS', 'AL', 'AL', 'B', 'F', 'AS', 'N', 'AS', 'O', 'AL', 'AL', 'AS', 'I', 'N', 'I', 'F', 'F', 'F', 'T', 'AS', 'F', 'T', 'D', 'B', 'N', 'N', 'AL', 'B', 'F', 'N', 'D', 'AS', 'N', 'AS', 'I', 'B', 'B', 'I', 'F', 'I', 'B', 'C', 'N', 'O', 'N', 'AS', 'AS', 'N', 'I', 'AL', 'B', 'O', 'AS', 'AL', 'N', 'N', 'T', 'D', 'I', 'N', 'B', 'B', 'B', 'AL', 'AL', 'T', 'F', 'F', 'AS', 'AS', 'I', 'AS', 'F', 'AS', 'AL', 'I', 'N', 'AS', 'O', 'AS', 'AS', 'AS', 'AL', 'O', 'D', 'B', 'AS', 'I', 'F', 'N', 'AS', 'F', 'N', 'AL', 'AS', 'B', 'AS', 'T', 'D', 'AS', 'T', 'AL', 'AS', 'D', 'AS', 'N', 'I', 'N', 'T', 'I', 'F', 'AL', 'O', 'F', 'I', 'N', 'N', 'AS', 'F', 'I', 'C', 'AS', 'AS', 'F', 'AS', 'N', 'I', 'AL', 'I', 'B', 'N', 'I', 'F', 'AL', 'D', 'C', 'C', 'B', 'F', 'N', 'I', 'AL', 'N', 'F', 'F', 'AS', 'B', 'B', 'N', 'N', 'B', 'F', 'O', 'AS', 'C', 'N', 'AS', 'D', 'AL', 'N', 'F', 'N', 'AL', 'F', 'F', 'I', 'N', 'F', 'B', 'I', 'B', 'AS', 'F', 'F', 'B', 'N', 'T', 'B', 'T', 'F', 'N', 'I', 'F', 'F', 'F', 'AL', 'N', 'F', 'D', 'AS', 'F', 'F', 'O', 'T', 'B', 'T', 'C', 'F', 'AS', 'O', 'AS', 'AS', 'I', 'C', 'I', 'D', 'N', 'AS', 'I', 'N', 'F', 'F', 'F', 'F', 'AL', 'I', 'AS', 'N', 'I', 'AL', 'D', 'AS', 'N', 'I', 'F', 'AS', 'AS', 'N', 'AS', 'B', 'AL', 'F', 'N', 'AL', 'T', 'AS', 'N')  
# full_dataframe_ <- data.frame(my_cate, student_cate)
# print("***Kappa Zone ***")
# kappa2(full_dataframe_, "unweighted")

# link: http://www.uni-kiel.de/psychologie/rexrepos/posts/interRaterICC.html
## apply the following for eah category: for example, for ctaegory : 'AS', all things that is marked by 'AS' as me in rtr1, 
## and 'AS' marked by all students in rtr2 

performKappaForOneCategory <- function(myRating_y, myRating_n, studentRating_y, studentRating_n, categoryName)
{
  print("*************************")
  categ <- c("Y", "N")
  lvls  <- factor(categ, levels=categ)
  rtr1  <- rep(lvls, c(myRating_y, myRating_n))
  rtr2  <- rep(lvls, c(studentRating_y, studentRating_n))
  cTab  <- table(rtr1, rtr2)
  addmargins(cTab)
  print("###############")
  print(categoryName)
  print("And the kappa score is ... ")
  kappa_output <- kappa2(cbind(rtr1, rtr2))  
  print(kappa_output)
  print("*************************")  
}
### params: first two my rating, last two student's taing 
# performKappaForOneCategory(165, 167, 55, 277, 'Not a defect (N)')
# performKappaForOneCategory(118, 214, 62, 270, 'Assignment (AS)')
# performKappaForOneCategory(18, 314, 58, 274, 'Function (F)')
# performKappaForOneCategory(16, 316, 40, 292, 'Interface (I)')
# performKappaForOneCategory(6, 326, 8, 324, 'Control (C)')
# performKappaForOneCategory(5, 327, 35, 297, 'Block/Package (B)')
# performKappaForOneCategory(2, 330, 17, 315, 'Time/Serialization (T)')
# performKappaForOneCategory(1, 331, 14, 318, 'Documentation (D)')
# performKappaForOneCategory(1, 331, 28, 304, 'Algorithm (AL)')
# performKappaForOneCategory(0, 332, 17, 315, 'Other (O)')
rm(list = setdiff(ls(), lsf.str()))
#### What is the cutoff: 

#### Poor agreement = Less than 0.20
#### Fair agreement = 0.20 to 0.40
#### Moderate agreement = 0.40 to 0.60
#### Good agreement = 0.60 to 0.80
#### Very good agreement = 0.80 to 1.00

#### link-1: https://www.medcalc.org/manual/kappa.php 
#### link-2: http://www.pmean.com/definitions/kappa.htm
#### link-3: https://www.stfm.org/fmhub/fm2005/May/Anthony360.pdf