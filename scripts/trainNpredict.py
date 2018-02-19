#!/usr/bin/env python

import sys
import cv2
import numpy as np
from mlc.perceptron import Perceptron
import matplotlib.pyplot as plt

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--training-data', default='train/', dest='trndir',
        help='directory containing images and targets to train MLC on')
parser.add_argument('-v', '--verification-data', default='verify/', dest='vrfdir',
        help='directory containing images and targets to verify MLC on')
args = parser.parse_args()

if len(sys.argv) == 1:
    parser.print_help()

y = np.load(args.trndir + 'all_target.npy')
X = np.load(args.trndir + 'all_images.npy')

print X.shape

y_test = np.load(args.vrfdir + 'all_target.npy')
X_test = np.load(args.vrfdir + 'all_images.npy')

ppn = Perceptron(eta=0.1, niter=10)
ppn.fit(X, y)

plt.figure()
plt.plot(range(1, len(ppn.errors_) + 1), ppn.errors_, marker='o')

plt.xlabel('Epochs')
plt.ylabel('Number of misclassifications')

ypred = []
print y_test
for Xi, yi in zip(X_test, y_test):
    # print ppn.predict(Xi), yi
    ypred.append(ppn.predict(Xi) - yi)
ypred = np.array(ypred)

fail = np.where(ypred != 0)[0]
nfail = len(fail)
print 'Number of failures: ', nfail, fail
# print ypred

dim = int(np.sqrt(Xi.shape[0]))

weight_pos = ppn.w_.copy()
weight_neg = ppn.w_.copy()

weight_pos[np.where(ppn.w_ < 0)[0]] = 0.
weight_neg[np.where(ppn.w_ > 0)[0]] = 0.
weight_neg *= -1

# print weight_pos.reshape((dim, dim)) / np.max(weight_pos) * 256

cv2.imshow('weights positive', weight_pos.reshape((dim, dim)) / np.max(weight_pos) * 256)
cv2.imshow('weights negative', weight_neg.reshape((dim, dim)) / np.max(weight_neg) * 256)
cv2.waitKey(0)

plt.show()
