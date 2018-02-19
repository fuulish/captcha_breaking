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
            help='how many distinct gray levels should be used')
    parser.add_argument('-i', '--image-directory', default='./', dest='imgdir',
            help='directory containing images to process')
    parser.add_argument('-c', '--coarsening', default=10, dest='coarse',
            help='level of coarsening of input pictures')
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

    for fn in fns:
        print 'working on image %s' %fn
        image = cv2.imread(fn, cv2.IMREAD_GRAYSCALE)
        gradient = np.gradient(image)

        final_image = np.ndarray((image.shape[0], image.shape[0]), dtype='int')

        if args.numcol != 256:
            image = colorization(image, args.numcol)

        delta_border = image.shape[1] - image.shape[0]
        delta_border_per_pixel = float(delta_border) / image.shape[0]

        for cnt, img in enumerate(image):
            offset = int((cnt+1) * delta_border_per_pixel)
            offset = delta_border - offset

            final_image[cnt,:] = img[offset:image.shape[0]+offset]

        newfile = args.outdir + '/' + fn.split('/')[-1]
        newfile = newfile.replace('.png', '_crop.png')

        print(newfile)
        cv2.imwrite(newfile, final_image)

        sliced = average_image(final_image, args.coarse)
        cv2.imwrite(newfile.replace('.png', '_sliced.png'), sliced)
