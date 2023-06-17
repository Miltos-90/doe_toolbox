#%%
import doe_box as dbox
dbox.fullfact(levels = [5, 2])

#%%
dbox.fracfact('a b c -abc')

#%%

dbox.fracfactgen(terms = 'a b c d ab', resolution = 3)

#%%


#%%

dbox.ccdesign(numFactors = 2)


# %%

dbox.bbdesign(numFactors = 3)

# %%
import numpy as np
np.random.seed(10)
x = dbox.lhs(numSamples = 10, numVariables = 3, smooth = False)
x

# %%

corr  = np.corrcoef(x, rowvar = False) 
(sum(corr.flatten() ** 2) - 3)/2


# %%
np.random.seed(10)
x = dbox.lhs(numSamples = 10, numVariables = 3, smooth = False, criterion = 'mincorr')
corr  = np.corrcoef(x, rowvar = False) 
(sum(corr.flatten() ** 2) - 3)/2

# %%


# %%
