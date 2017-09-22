#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#Question 1 C0-Variance:
reader = pd.read_csv("dataset.csv")

df = pd.DataFrame(reader)
rows, cols = df.shape
print("Rows=", rows, " Col=", cols)
type(df)
samples = np.array(df.loc[:,:])
type(samples)
np.cov(samples[0],samples[1])
np.cov(samples[1],samples[2])

#Question 2 Variance:
np.var(samples[0])
np.var(samples[1])
np.var(samples[2])

#Question 3:
import numpy as np
mat1 = np.empty([2, 2], dtype = int)
mat1 = np.array([[0, -1],
       [2,  3]])  
mat1 = np.matrix(mat1)
eigen_val, eigen_vec  = np.linalg.eig(mat1)
print(eigen_val)
print(eigen_vec)



