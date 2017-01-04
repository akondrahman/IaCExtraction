#!/bin/bash 
pattern_='class="gwt-InlineHyperlink" href="https://gerrit.wikimedia.org/r/'
repoName='/Users/akond/Desktop/code-review-raw/wikimedia/wikimedia-translatewiki/'
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
  theIDs=($(grep $pattern_ $f_ |  cut -d'<' -f11 | cut -d'>' -f2))
  for (( i=0; i<${#theIDs[@]}; i++ )); do 
    echo ${theIDs[i]} >> $file2save; 
  done
  #echo $theID >> $file2save
done
echo "================================================"