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

The `fracfact` function creates the two-level fractional factorial designs defined by the generator `gen`, which is a (case-sensitive) string listing the factors in the design, formed from the 52 case-sensitive letters *a*-*Z*, separated by spaces.
Standard convention notation indicates to use *a*-*z* for the first 26 factors, and, if necessary, *A*-*Z* for the remaining factors. 
A valid example would be: `gen = 'a b c abc'`.

Similar to the previous, the output is an *m*-by-*n* numpy array, where *m* is the number of treatments in the fractional-factorial design. 

Each row corresponds to a single treatment, and each column contains the settings for a single factor, with floating point scalars ranging from -1 to +1.

##### Example
The following generates an eight-run fractional factorial design for four factors, in which the fourth factor is the product of the first three:

```python
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

Note that more sophisticated generator strings can be created using the +" and "-" operators. The "-" operator will swap the column levels:

```python
>>> gen = 'a b c -abc'
>>> dbox.fracfact(gen)

array([[-1, -1, -1,  1],
       [-1, -1,  1, -1],
       [-1,  1, -1, -1],
       [-1,  1,  1,  1],
       [ 1, -1, -1, -1],
       [ 1, -1,  1,  1],
       [ 1,  1, -1,  1],
       [ 1,  1,  1, -1]])
```

#### fracfactgen

##### Description

The `fracfactgen` function uses the Franklin-Bailey algorithm to find generators for the smallest two-level fractional-factorial design.

It requires two inputs:
* `terms`: Is a string of factors formed formed from the 52 case-sensitive letters *a*-*Z*, separated by spaces.
Standard convention notation indicates to use 'a'-'z' for the first 26 factors, and, if necessary, 'A'-'Z' for the remaining factors. 
A valid example would be: `terms = 'a b c ab ac'`. 
Single-letter factors indicate the main effects to be estimated, whereas multiple-letter factors indicate the interactions to be estimated. 
You can pass the output generators of `fracfactgen` to `fracfact`, in order to produce the corresponding fractional-factorial design.
* `resolution`: Is an integer indicating the required resolution of the design. A design of resolution *R* is one in which no *n*-factor interaction is confounded with any other effect containing less than *R – n* factors. Thus, a resolution *III* design does not confound main effects with one another but may confound them with two-way interactions, while a resolution *IV* design does not confound either main effects or two-way interactions but may confound two-way interactions with each other. It is an optional argument, with the default value being equal to 3.

If `fracfactgen` is unable to find a design at the requested resolution, it tries to find a lower-resolution design sufficient to calibrate the model. If it is successful, it returns the generators for the lower-resolution design along with a warning. If it fails, an error is raised.

##### Example
The following will determine the effects of four two-level factors, for which there may be two-way interactions. A full-factorial design would require 2<sup>4</sup> = 16 runs. The `fracfactgen` function will generators for a resolution *IV* (separating main effects) fractional-factorial design that requires only 2<sup>3</sup> = 8 runs:


```python
>>> dbox.fracfactgen(terms = 'a b c d', resolution = 4)

'a b c abc'
```

### Response Surface Designs <a name="rsm"></a>

#### ccdesign

##### Description

Central Composite Designs (CCDs) can be generated using the `ccdesign` function. 
It needs the following input arguments:

* `numFactors`: Number of factors in the design. Must be an integer higher than *2*.

The following optional arguments can be set:
*  `fraction`: Integer indicating the fraction of full-factorial cube, expressed as an exponent of 1/2. If not set by the user, the default values are the following:


* `centerPoints`: Number of center points to be added in the factorial and axial parts of the design.
    Can be one of:
    * 'orthogonal' (default): Number of center points will be computed so that an orthogonal design will be provided.
    * 'uniform'   : Number of center points will be computed so that uniform precision will be achieved.
    * A strictly positive integer, specifying the number of center points directly.

* `designType`: It defines the type of the CCD. 
    Can be one of:
    * 'circumscribed' (default): It is the original type of CCD, where axial points are located at distance *a* from the center point.
    * 'inscribed' : The inscribed CCD is characterized by that axial points are 
                    located at factor levels *−1* and *1*, while the factorial points are brought into the interior of the design space and are located at distance *1/a* from the center point.
    * 'faced': In a face-centered CCD, the axial points are located at a distance equal to *1* from the center point, i.e. at the face of the design cube if the design involves three experimental factors.
        
       
For *n > 2* factors, the output DoE matrix has dimensions *m* by *n*, with *m* being the number of runs in the design. 
Each row represents one run, with settings for all factors represented in the corresponding columns. The resulting factor values are normalized, so that the cube points thaveake values between *-1* and *1*.

##### Example

### Latin Hypercube Sampling <a name="lhs"></a>

## References

Good starting points for additional information on each experimental design type:

* [Factorial designs](https://en.wikipedia.org/wiki/Factorial_experiment)
* [Box-Behnken designs](https://en.wikipedia.org/wiki/Box%E2%80%93Behnken_design)
* [Central composite designs](https://en.wikipedia.org/wiki/Central_composite_design)
* [Latin-Hypercube designs](https://en.wikipedia.org/wiki/Latin_hypercube_sampling)

In addition, a wealth of information about DoE can be found on the [NIST](https://www.itl.nist.gov/div898/handbook/pri/pri.htm) website, including discussion on how to choose and analyze various DoEs, as well as several case studies.