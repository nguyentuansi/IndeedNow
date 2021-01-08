#!/bin/bash

git add . 
git commit -m "Updated Repository data"
date > log.txt
git add .
git commit -m  "`date`"
git push -u origin master