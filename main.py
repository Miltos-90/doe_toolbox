#%%
import numpy as np


#%%
from factorial import fullfact, ff2n, fracfact # TODO: No more than 26 factors

full = fullfact(levels = [2, 2])
frac = fracfact('a b c abc')
ff2  = ff2n(3)
print(full)
print(frac)
print(ff2)

# %%
from factorial import fracfactgen

termStr = 'a b c d e f g h ab be bc bd bf be';
termStr = 'a b c d ab';
#termStr = 'a b c d';
#termStr = 'a b c d e ad de';
#termStr = 'a b c d e f ab be';
termStr = 'a b c d e f g h ad de';
#termStr = 'a b c d e f g h i gh gf ad de abc';

# Default values
for r in [3,4,5,6]:
    gens = fracfactgen(termStr, resolution = r)
    print(f'{r}: {gens}')



# %%
import response_surface as rs

rs.ccdesign(3, 1, designType = 'circumscribed')
rs.bbdesign(numFactors = 3)

# %%

from lhs import lhs

lhs(numSamples = 3, numVariables = 4, smooth = False, criterion = 'maxdist')

# %%

# %%
