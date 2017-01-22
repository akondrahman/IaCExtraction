#!/bin/bash
##reff: http://www.phontron.com/kylm/
echo "***This script performs n gram models [START] ***"
echo " "
echo "===================================================================================================="
trainFileName='train.txt'
testFileName='test.txt'
unknownWordsCutoff=250
theJarFile="kylm.jar"
# declare -a models=( 1 2 3 4 5 )
declare -a models=( 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 )

for i in ${models[@]}; do
  ngram_=$i  
  trainModel="model_"$ngram_".arpa"
  ##time to execuet the tarining command 
  java -cp $theJarFile kylm.main.CountNgrams -ukcutoff $unknownWordsCutoff -n $ngram_ $trainFileName $trainModel
  echo "Created $ngram_ model. Saved as $trainModel. Next step is to evaluate the test model in forms of cross entropy and perplexity"
  echo "===================================================================================================="
  ## time to evaluate the test command 
  java -cp $theJarFile  kylm.main.CrossEntropy -arpa $trainModel $testFileName 
  echo "===================================================================================================="
done
#echo "The command that will be executed: $trainCommand"
echo "***This script performs n gram models [END] ***"
echo " "
echo "===================================================================================================="

###remove existing models 
rm *.arpa