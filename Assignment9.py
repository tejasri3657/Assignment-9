# -*- coding: utf-8 -*-
"""Assignment-9.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16NWIX5bblB3wbo6UY_qJVQCpLeb9NVQF
"""

import numpy as np
A = ([[1,-1],[2,3]])
print("Original matrix:")
print(A)
result =  np.linalg.inv(A)
print("Inverse of the said matrix:")
print(result)

  
# Decomposition of the said matrix
q, r = np.linalg.qr(matrix1)
print('\nQ:\n', q)
print('\nR:\n', r)
