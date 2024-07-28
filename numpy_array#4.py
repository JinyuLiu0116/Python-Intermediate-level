import numpy as np
import pandas as pd

a = np.array([
    [
        [1,2,3],
        [4,5,6]
    ],
    [
        [10,20,30],
        [40,50,60]
      # [2, 3]  if I add one me list here, I can't use a.shape because there is no shape
    ] # the output will be (2, ), has same problom with a.ndim, output will be 1
]#, dtype=float  will change the type of numpy array and a.dtype output will be float64
)

print(a.shape) #output: (2, 2, 3)
print(a.size) #output: 12
print(a.ndim) #output: 3 (dimensions)
print(a.dtype) #output: int32 (integer with 32 bits)
