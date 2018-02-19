#!/bin/bash

# assuming all pictures have been obtained and classified:

crop_images.py -i ../data/train -o train
crop_images.py -i ../data/verify -o verify

prep_data.py -t ../data/train/target.txt -i train -o train
prep_data.py -t ../data/verify/target.txt -i verify -o verify

trainNpredict.py
