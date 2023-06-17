#%%
import doe_box as dbox
dbox.fullfact(levels = [5, 2])

#%%
dbox.fracfact('a b c -abc')

#%%

dbox.fracfactgen(terms = 'a b c d ab', resolution = 3)

#%%

# %%

termStr = 'a b c d e f g h ab be bc bd bf be';
termStr = 'a b c d ab';
#termStr = 'a b c d';
#termStr = 'a b c d e ad de';
#termStr = 'a b c d e f ab be';
termStr = 'a b c d e f g h ad de';
#termStr = 'a b c d e f g h i gh gf ad de abc';

# Default values
for r in [3,4,5,6]:
    gens = dbox.fracfactgen(termStr, resolution = r)
    print(f'{r}: {gens}')


#%%

dbox.ccdesign(numFactors = 2)


# %%

dbox.bbdesign(numFactors = 3)

# %%

dbox.lhs(numSamples = 10, numVariables = 4, smooth = True, criterion = 'maxdist')

# %%

# %%
