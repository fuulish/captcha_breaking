#!/usr/bin/env python

import os
import sys
import cv2
import numpy as np
from glob import glob

import argparse

def average_image(image, cfac):
    sliced = np.zeros((image.shape[0]/cfac, image.shape[1]/cfac))

    # print sliced.shape

    for i in range(cfac):
        for j in range(cfac):
            sliced += image[i::cfac,j::cfac]

    sliced /= cfac*cfac

    return sliced

def colorization(image, bits):
    num = 256 / bits
    image = image / num * num # eight gray scales
    cv2.imwrite(fn.replace('.png', '_8bit.png'), image)

    return image

if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument('-n', '--number-of-graylevels', default=256, dest='numcol',
            help='how many distinct gray levels should be used', type=int)
    parser.add_argument('-i', '--image-directory', default='./', dest='imgdir',
            help='directory containing images to process')
    parser.add_argument('-c', '--coarsening', default=10, dest='coarse',
            help='level of coarsening of input pictures', type=int)
    parser.add_argument('-o', '--output-directory', default='./', dest='outdir',
            help='directory for output of processed pictures')

    args = parser.parse_args()

    if len(sys.argv) == 1:
        parser.print_help()

    if not os.path.exists(args.imgdir):
        raise RuntimeError('Image directory not found')

    if not os.path.exists(args.outdir):
        os.mkdir(args.outdir)

    fns = glob(args.imgdir + '/*.png')
    fns.sort()

    for fn in fns:
        print 'working on image %s' %fn
        image = cv2.imread(fn, cv2.IMREAD_GRAYSCALE)

        if args.numcol != 256:
            image = colorization(image, args.numcol)

        if image.shape[1] != image.shape[0]:
            skewed = np.float32([[image.shape[1]-image.shape[0],0], [0,image.shape[0]], [image.shape[0], image.shape[0]]] )
            straight = np.float32([[0,0], [0,image.shape[0]], [image.shape[0], image.shape[0]]])

            M = cv2.getAffineTransform(skewed,straight)
            final_image = cv2.warpAffine(image,M,(image.shape[1],image.shape[0]))

            last_out = -(image.shape[1]-image.shape[0])
        else:
            final_image = image
            last_out = None

        newfile = args.outdir + '/' + fn.split('/')[-1]
        cv2.imwrite(newfile.replace('.png', '_sheared.png'), final_image[:,:last_out])

        sliced = average_image(final_image[:,:last_out], args.coarse)
        cv2.imwrite(newfile.replace('.png', '_sliced.png'), sliced)
