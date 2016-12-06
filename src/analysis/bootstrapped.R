cat("\014") 
t1 <- Sys.time()

pop <- c(30, 37, 36, 43, 42, 43, 43, 46, 41, 42)
len_pop <- length(pop)
mean_pop <- mean(pop)

no_of_samples <- 100
#Generate 20 bootstrap samples, i.e. an array of 20 samples  

# random resamples from x
tmp_data = sample(pop, len_pop*no_of_samples, replace=TRUE)
bootstrap_sample = matrix(tmp_data, nrow=len_pop, ncol=no_of_samples)
## this is a matrix of 'no_of_samples' of columns and 'len_pop' of rows
## entries in the matrix represent values given in pop, we can select the 
## values that are in bootstrap_sample and fall within the 95% CI 

# Compute the means
means_bootstrap_sample = colMeans(bootstrap_sample)

# Compute delta_star for each bootstrap sample
delta_star = means_bootstrap_sample - mean_pop

# Sort the results
sorted_delta_star = sort(delta_star)

# Look at the sorted results
# hist(sorted_delta_star, nclass=6)
elements_in_sorted_delta_star <- length(sorted_delta_star)
print("The elements in delta should be 20, as we requested 20 samples above")
print(elements_in_sorted_delta_star)

# Find the .1 (10%) and .9(90%) critical values of
d9 = sorted_delta_star[1]  ## 10% of the 20 samples, corresponds to the 2nd  element  
d1 = sorted_delta_star[99] ## 90% of the 20 samples, corresponds to the 18th element 


# Find and print the 80% confidence interval for the mean
CI = mean_pop - c(d1, d9)
print("And the CI is:")
print(CI)
#print(bootstrap_sample)
t2 <- Sys.time()
print(t2 - t1)  # 
rm(list = setdiff(ls(), lsf.str()))