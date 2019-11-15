#!/bin/bash
#Andrea Hilborn, Oct 11 2019
#This script downloads level 1 Sentinel-3 files, given a list of filenames.
#Here, a list of L2 files is input and L1 counterpart is downloaded.

#Required: 
# - a textfile listing S3 files to download
# - wget, and the dhusget.sh script found here: https://scihub.copernicus.eu/userguide/BatchScripting. See bash dhusget.sh --help for all options

# The name of your file list:
filelist=./S3_filelist.txt
coda_username=<YOUR CODA USERNAME>
coda_password=<YOUR CODA PASSWORD>
product_type=product #Do you want to download the manifest .xml file or the product? Options are 'manifest' or 'product'

while read i
do 
bash dhusget.sh -d https://coda.eumetsat.int/ -u $coda_username -p $coda_password -m Sentinel-3 -T OL_1_E"${i:10:2}"___ -F filename:"${i:0:3}"*"${i:16:31}"* -o $product_type
done <$filelist
