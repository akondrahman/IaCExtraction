cat("\014")  
options(max.print=1000000)
library(lda)
library(tm)
library(LDAvis)
library(SnowballC)
library(topicmodels)
library(Rmpfr)
library(slam)
t1 <- Sys.time()

defect_msg_file <- "/Users/akond/Documents/AkondOneDrive/OneDrive/IaC_Mining/output/type-bugs-prelim/bug_wikimedia.csv"
full_data   <- read.csv(file=defect_msg_file, header=TRUE, sep=",")
rows_ <- nrow(full_data)     
cols_ <- ncol(full_data)    
all_vector_bug_msg =""

for(ind_ in 1:cols_)
{
  tmp_ <-  full_data[[ind_]] 
  #print(tmp_)
  all_vector_bug_msg = paste(all_vector_bug_msg, tmp_)
  #print("Current bug vector length:")
  #print(length(all_vector_bug_msg))
}

##print((all_vector_bug_msg))


### Topic Modeling Zone ###
stop_words <- stopwords("SMART")
stop_file ="/Users/akond/Documents/AkondOneDrive/OneDrive/IaC_Mining/output/bug_extra_stop_word_list.csv"
stop_words_data <- read.csv(stop_file)
extra_stop_words = stop_words_data$stop_



all_text_from_posts <- all_vector_bug_msg
all_text_from_posts <- iconv(all_text_from_posts, "ASCII", "UTF-8", sub="")

# pre-processing:
all_text_from_posts <- gsub("'", "", all_text_from_posts)  # remove apostrophes
all_text_from_posts <- gsub("[[:punct:]]", " ", all_text_from_posts)  # replace punctuation with space
all_text_from_posts <- gsub("[[:cntrl:]]", " ", all_text_from_posts)  # replace control characters with space
all_text_from_posts <- gsub("^[[:space:]]+", "", all_text_from_posts) # remove whitespace at beginning of documents
all_text_from_posts <- gsub("[[:space:]]+$", "", all_text_from_posts) # remove whitespace at end of documents
all_text_from_posts <- tolower(all_text_from_posts)  # force to lowercase
all_text_from_posts <- gsub("\\b\\w{1,2}\\b", "", all_text_from_posts)

# tokenize on space and output as a list:
string_list <- strsplit(all_text_from_posts, "[[:space:]]+")
string_list <- wordStem(string_list, language="porter")

### Code to filter out zero length strings and numerals 

checkIfInteger <- function(param)
{
  output <- as.integer(param)
  return(output) 
}
len_string_list <- length(string_list)
formatted_string_list <- vector(mode="numeric", length=len_string_list)
for(ind_ in 1:len_string_list)
{
  #print("***")
  str_=""
  elem <- string_list[ind_]
  splitted_list <- strsplit(elem, ",")
  all_splitted_Str <- splitted_list[[1]]
  for(sec_ind in 1:length(all_splitted_Str))
  {
    indi_str <- all_splitted_Str[sec_ind]
    #print(indi_str)
    core_str= unlist(strsplit(indi_str, split='\"', fixed=TRUE))[2]
    #print(core_str)
    numeric_status <- checkIfInteger(core_str) 
    #print(numeric_status)
    # & (numeric_status==NA) & (core_str!="pre") & (core_str!="code")
    if( (length(core_str)>0) & (!identical(core_str, "pre")) & (!identical(core_str, "code"))  )
    {
      #       if(
      #            (!identical(core_str, "ansible")) & (!identical(core_str, "openstack")) & (!identical(core_str, "cfengine")) &
      #            (!identical(core_str, "chef")) & (!identical(core_str, "docker")) & (!identical(core_str, "capistrano")) & 
      #            (!identical(core_str, "kubernetes")) & (!identical(core_str, "puppet")) & (!identical(core_str, "saltstack")) & 
      #            (!identical(core_str, "vagrant")) & (!identical(core_str, "bluemix")) & (!identical(core_str, "amazon")) & 
      #            (!identical(core_str, "openshift")) & (!identical(core_str, "jenkins"))              
      #          )
      #       {
      if(is.na(numeric_status))
      {
        #print(core_str)
        str_ <- paste(str_, core_str)
      }        
      #       }
      
    }
  }
  formatted_string_list[ind_] <- str_
  #print(str_)
  str_ = ""
}

print("After formatting ... length should be same as before")
print(length(formatted_string_list))

docs <- Corpus(VectorSource(formatted_string_list))
docs <- tm_map(docs, removeWords, stopwords("english"))
docs <- tm_map(docs, removeWords, extra_stop_words)
#writeLines(as.character(docs[[30]]))
#dtm <- DocumentTermMatrix(docs)
#dtm <- DocumentTermMatrix(docs, control = list(stemming = TRUE, stopwords = TRUE, removeNumbers = TRUE, removePunctuation = TRUE))
dtm <- DocumentTermMatrix(docs, control = list(stopwords = TRUE, removeNumbers = TRUE, removePunctuation = TRUE))
dim_dtm <- dim(dtm)
print("Dimension before sparese pre-processing")
print(dim_dtm)
#print(head(dtm))
max_sparsity_allowed <- 0.99
dtm <-  removeSparseTerms(dtm, max_sparsity_allowed)
dim_dtm <- dim(dtm)
print("Dimension after sparese pre-processing")
print(dim_dtm)
rowTotals <- apply(dtm , 1, sum) #Find the sum of words in each Document
dtm   <- dtm[rowTotals> 0, ]           #remove all docs without words

#collapse matrix by summing over columns
freq <- colSums(as.matrix(dtm))
#print(length(freq))

#create sort order (descending)
ord <-order(freq, decreasing=TRUE)
#print(freq[ord])
write.csv(freq[ord],"bug_msg_word_freq_tm.csv")

##Number of topics
k <- 10

##Set parameters for Gibbs sampling
burnin_ <- 1000
iter_ <- 1000
thin <- 250
seed <-list(2003, 5, 63, 100001, 765)
nstart <- 5
best <- TRUE
#That done, we can now do the actual work – run the topic modelling algorithm on our corpus. 
#Here is the code:
#Run LDA using Gibbs sampling
ldaOut <-LDA( dtm, k, method="Gibbs", control=list(nstart=nstart, seed = seed, best=best, burnin = burnin_, iter = iter_, thin=thin))


#write out results
#docs to topics
ldaOut.topics <- as.matrix(topics(ldaOut))
write.csv(ldaOut.topics,file=paste("final_formatted_", k, "_DocsToTopics.csv"))

#top 15 terms in each topic
terms2out <- 15
ldaOut.terms <- as.matrix(terms(ldaOut, terms2out))
write.csv(ldaOut.terms,file=paste("final_formatted_", k, "_TopicsToTerms.csv"))

#probabilities associated with each topic assignment
topicProbabilities <- as.data.frame(ldaOut@gamma)
write.csv(topicProbabilities,file=paste("final_formatted_", k, "_TopicProb.csv"))

t2 <- Sys.time()
print(t2 - t1)  # 

# Clear Stuff
rm(list = setdiff(ls(), lsf.str()))