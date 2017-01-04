#!/bin/bash 
echo "### This script extracts puppet related repsoitoiries from the internet###"
cnt_all_repos=0
cnt_repo=0
while IFS='' read -r line || [[ -n "$line" ]]; do
  size=${#line} 
  if [ "$size" -gt 0 ]; then ## always quote your avriables
     cnt_all_repos=$((cnt_all_repos + 1))       
     echo " " 
     repo_name=${line//[[:blank:]]/}
     repo_url="https://gerrit.wikimedia.org/r/"$repo_name   
     echo "Downloading wikimedia repository:"$repo_name
     git clone $repo_url 
     echo "Cloning done ... looking at count of puppet files in ..."$repo_name  
     most_recent_dir=`ls -t | head -1`
     echo "The most recent directory must be ..."$repo_name
     cnt=`find $most_recent_dir  -type f -name '*.pp' | wc -l`
     echo "Number fo puppet files in this repo:"$cnt 
     if [ "$cnt" -gt 0 ]; then ## always quote your avriables
        cnt_repo=$((cnt_repo + 1))  
        echo "This repository has puppet files. Keeping:"$repo_name
     else
        echo "This repository has no puppet files. Deleting:"$repo_name
        rm -rf $most_recent_dir 
     fi
     echo "---------------------------"     
     echo " "     
  fi
done < "$1"         




echo "In total we have downloaded legit $cnt_repo repositoires, of $cnt_all_repos. Yeeay!"