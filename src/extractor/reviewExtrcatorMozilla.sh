#!/bin/bash 
pattern_='build-puppet</div></a'
repoName='/Users/akond/Desktop/code-review-raw/mozilla/build-puppet/'
file2save='changeID.txt'
echo "Extracting code review change IDs for "$repoName  ;
echo "================================================"
cd $repoName 
if [ -f $file2save ]
then	
	rm $file2save
fi
for f_ in *.html; do 
  echo "Processing $f_ ..." ;
  theIDs=($(grep $pattern_ $f_ | cut -d'<' -f2 | cut -d'/' -f5))
  for (( i=0; i<${#theIDs[@]}; i++ )); do 
    echo ${theIDs[i]} >> $file2save; 
  done
  #echo $theID >> $file2save
done
echo "================================================"