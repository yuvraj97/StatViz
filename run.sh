#!/bin/bash

# This script run a docker container for specified "Algo" on specified "PORT"
function run() {
  id=$1
  port=$2
  name=$(echo $id | sed -e "s/_/-/g")
  printf "import streamlit as st\\nfrom run import main;\\ntry:\\n\\tmain()\\nexcept:\\n\\tst.error('Something went wrong!')" > $name.py
  cat Dockerfile > Dockerfile.$id
  sed -i "s/Chapter-ID/$id/g" Dockerfile.$id
  sed -i "s/Chapter-Name/$name/g" Dockerfile.$id

  lower=$(echo "$name" | awk '{print tolower($0)}')
  sudo docker build -f Dockerfile.$id -t $lower .
  sudo docker rm -f $lower
  sudo docker run --name="$lower" -d --restart=unless-stopped -p $port:8501 $lower
  rm $name.py
  rm Dockerfile.$id
}

run "Statistics" 8501
run "Introduction" 8502
run "Law_of_Large_Number" 8503
run "Central_Limit_Theorem" 8504
run "Gaussian_Distribution" 8505
