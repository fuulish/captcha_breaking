#!/bin/bash

# assuming all pictures have been obtained and classified:

shear_image.py -i ../data/train -o train -c 5
shear_image.py -i ../data/verify -o verify -c 5

prep_data.py -t ../data/train/target.txt -i train -o train -p sliced
prep_data.py -t ../data/verify/target.txt -i verify -o verify -p sliced

trainNpredict.py
