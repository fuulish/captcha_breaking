#!/usr/bin/env python

import sys
import cv2
import numpy as np
from glob import glob

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--image-directory', default='./', dest='imgdir',
        help='directory containing images to process')
parser.add_argument('-t', '--target-file', default='target.txt', dest='target',
        help='file containing target values, if less targets than input data, assume only hits are given')
parser.add_argument('-o', '--output-directory', default='.', dest='outdir',
        help='directory for output of processed pictures')
parser.add_argument('-p', '--postfix', default='_crop_sliced', dest='postfix',
        help='unique postfix used in processed image data')
args = parser.parse_args()

if len(sys.argv) == 1:
    parser.print_help()

# this will not be sorted, and this sorting will only work if padded with 0's
fns = glob(args.imgdir + '/' + '*%s.png' %args.postfix)
fns.sort()
nfile = len(fns)

all_im = []
target = []

f = open(args.target)
for line in f.readlines():
    target.append(int(line))
f.close()

if nfile != len(target):
    hits = target[:]
    target = []

    for i in range(nfile):
        if i in hits:
            target.append(1)
        else:
            target.append(-1)

for fn in fns:
    image = cv2.imread(fn, cv2.IMREAD_GRAYSCALE)
    image = image.flatten()
    all_im.append(image.copy())

all_im = np.array(all_im)
target = np.array(target)

np.save('%s/all_images.npy' %args.outdir, all_im)
np.save('%s/all_target.npy' %args.outdir, target)
