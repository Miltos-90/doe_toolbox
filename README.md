# DOE Toolbox

## Description

A simple Design of Experiments (DoE) toolbox written in python, which provides a range of tools and functions to facilitate the planning of experimental designs. It is intended to assist researchers, engineers, and analysts in efficiently exploring and optimizing systems, processes, and products by systematically varying factors and analyzing their effects on the response variable.

It includes:
1. [Factorial designs](#factorial)
    * *Generic full-factorial* (`fullfact`): A design in which every setting of every factor appears with every setting of every other factor, for all possible combinations.
    * *2-level full-factorial* (`ff2n`): Same as above, but the factors are constrained to have two levels each (high/low or +1 and -1).
    * *2-level fractional factorial* (`fracfact`): Similar to a full factorial DoE, but a subset of factor combinations is selected, based on specific rules to ensure that important main effects and interactions can still be estimated with a reduced number of experimental runs.
    * *2-level fractional factorial generator* (`fracfactgen`): Convenient design generator to control how the fraction (or subset of runs) iwill selected from the full set of runs in a fractional factorial design.
2. [Response surface designs](#rsm)
    * *Box-Wilson Central Composite Designs (CCD)* (`ccdesign`): CCD designs start with a factorial or fractional factorial design (with center points) and add "star" points to estimate curvature for the estimation of quadratic models.
    * *Box-Behnken* (`bbdesign`): An alternative to CCD, being an independent quadratic design in that it does not contain an embedded factorial or fractional factorial design. For three factors, the Box-Behnken design offers some advantage in requiring a fewer number of runs than a CCD. However, for four or more factors, this advantage disappears.
3. [Latin Hypercube sampling (LHS)](#lhs): An experimental design in which the range of each factor is divided into equal intervals or bins. Within each bin, one and only one sample point is selected randomly. The selection process ensures that the samples are evenly distributed across the parameter space and that each combination of factor levels occurs exactly once. It is especially useful for, and commonly employed in, simulation studies, sensitivity analysis, and optimization problems.

## Installation

The package can be easily installed with pip via a DOS or Unix command shell:

```bash
pip install XXXXXXXXXXXXXXXXXXXXXX
```

### Requirements
The following packages are required:
* numpy >= 1.24.2,
* scipy >= 1.10.1.

See `requirements.txt` file


## Usage

### Factorial Design of Experiments <a name="factorial"></a>

#### fullfact

##### Description

The `fullfact` function  outputs factor settings for a full factorial design with *n* factors, where the number of levels for each factor is given by the vector `levels` of length *n*. 

The output is an *m*-by-*n* numpy array, where *m* is the number of treatments in the full-factorial design. 

Each row corresponds to a single treatment, and each column contains the settings for a single factor, with floating point scalars ranging from -1 to +1.

##### Example
The following generates a ten-run full-factorial design with five levels for the first factor and two levels for the second factor:

```python
>>> import doe_box as dbox
>>> dbox.fullfact(levels = [5, 2])
array([[-1. , -1. ],
       [-1. ,  1. ],
       [-0.5, -1. ],
       [-0.5,  1. ],
       [ 0. , -1. ],
       [ 0. ,  1. ],
       [ 0.5, -1. ],
       [ 0.5,  1. ],
       [ 1. , -1. ],
       [ 1. ,  1. ]])
```

#### fracfact

##### Description

The `fracfact` function creates the two-level fractional factorial designs defined by the generator `gen`.

Similar to the previous, the output is an *m*-by-*n* numpy array, where *m* is the number of treatments in the fractional-factorial design. 

Each row corresponds to a single treatment, and each column contains the settings for a single factor, with floating point scalars ranging from -1 to +1.

##### Example
The following generates an eight-run fractional factorial design for four factors, in which the fourth factor is the product of the first three:

```python
>>> # import package if not imported.
>>> gen = 'a b c abc'
>>> dbox.fracfact(gen)

array([[-1, -1, -1, -1],
       [-1, -1,  1,  1],
       [-1,  1, -1,  1],
       [-1,  1,  1, -1],
       [ 1, -1, -1,  1],
       [ 1, -1,  1, -1],
       [ 1,  1, -1, -1],
       [ 1,  1,  1,  1]])
```

#### fracfactgen

##### Description

The `fracfactgen` function ...

##### Example


```python
>>> # import package if not imported.
>>> 
>>>  


```




### Response Surface Designs <a name="rsm"></a>

### Latin Hypercube Sampling <a name="lhs"></a>

## References

Good starting points for additional information on each experimental design type:

* [Factorial designs](https://en.wikipedia.org/wiki/Factorial_experiment)
* [Box-Behnken designs](https://en.wikipedia.org/wiki/Box%E2%80%93Behnken_design)
* [Central composite designs](https://en.wikipedia.org/wiki/Central_composite_design)
* [Latin-Hypercube designs](https://en.wikipedia.org/wiki/Latin_hypercube_sampling)

In addition, a wealth of information about DoE can be found on the [NIST](https://www.itl.nist.gov/div898/handbook/pri/pri.htm) website, including discussion on how to choose and analyze various DoEs, as well as several case studies.