# from numpy import array
import numpy as np

fam = ["liz", 1.73, "emma", 1.68,
       "mom", 1.71, "dad", 1.89]

fam_ext = fam + ["me", 1.79]
print(str(len(fam_ext)) + " elements in fam_ext")

...

np_fam = np.array(fam_ext)