# -*- coding: utf-8 -*-
"""
This module offers class for general machine learning algorithm 

Author:        Mirza Elahi (me5vp)
Changelog:     2017-10-31 v0.0
"""

import matplotlib
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from matplotlib.ticker import MultipleLocator
import matplotlib.pyplot as plt

import numpy as np
import pandas as pd
# oversampling
from imblearn.over_sampling import SMOTE
# machine learning
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, cohen_kappa_score
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt
#from math import pi, sqrt, sin, cos, tan
#from sets import Set
import pickle
import sys
import os
import shutil
import operator as op
import time
import argparse
import scipy.io as sio

class predictor(object):
    def __init__(self, height = None, width = None, ratio=None, type=None):
        """constructor of the class"""
        self.dF = []
        self.feature = []
        self.Class = []
        self.featureNumpy = []
        self.ClassNumpy = []
        
    def loadData( self, fileName, feaRowStart, feaRowEnd, colClass, 
                 delimitter=',' ):
        """loading data
           @param fileName - name of the csv file
           @param fearowStart - starting row of the feature or Class
           @param feaRowEnd - end row of the feature or Class
           @param colClass - number of the col for Class (indexing starts from 0)
           @param delimitter - default comma
        """
        self.dF = pd.read_csv( fileName, delimitter = ',')
        self.feature = df.iloc[feaRowStart:feaRowEnd, 0:colClass-1]
        self.Class = df.loc[feaRowStart:feaRowEnd, colClass]
        self.dataConvertToNumpy()
        
    def dataConvertToNumpy():
        """Convert feature and Class to numpy, this can also be used for 
           updating
        """
        self.featureNumpy = np.asarray( self.feature )
        self.ClassNumpy = np.asarray( self.Class )
        
    def overSampling( self, feature, Class, random_state = 0 ):
        """utility function for copying unbalanced data for multiple times 
           to balance dataset
           @param feature
           @param Class
           @param random_state - seeding random number
           @return resampled feature
           @return resampled Class
        """
        oversampler = SMOTE(random_state=0)
        feature_resample, Class_resample = oversampler.fit_sample(feature, 
                                                                      Class)
        print("Warning: You are increasing the dataset to balance the data\n")
        return feature_resample, Class_resample
    
    def confusionMetric( self, classTest, classPred):
        """copying unbalanced for multiple times to balance dataset
           @param classTest
           @param classPred
           @return accruacy - one number
           @return confMat - 2x2 matrix for 2 class classifier
           @return cohenKappaMat - TODO
        """
        # accuracy of the model - in one number
        accuracy = average_precision_score( classTest, classPred )
        # confusion matrix 2x2 matric
        confMat = confusion_matrix(classTest, classPred)
        # cohen Kappa is applicable for unbalanced data
        cohenKappaMat = cohen_kappa_score(classTest, classPred)
        
        return accuracy, confMat, cohenKappaMat

    