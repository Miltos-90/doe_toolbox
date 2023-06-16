"""
This module implements a generic parser for the fracfact and fracfactgen functions.
"""

import numpy as np
import re
from .fullfact import fullfact

def _isBaseFactor(s: str) -> bool:
    """ Checks if an input string is a base factor. 
        Inputs:
            s: string to be checked
        Outputs:
            boolean indicating whether it is a base factor
    """
    s = s.replace('-','').replace('+', '')
    return len(s) == 1


def _extractBaseFactors(s: str) -> list:
    """ Extracts base factors from the name of the generated factor. 
        Inputs:
            s: String containing the name of the generated factor
        Outputs:
            list of corresponding base factors
    """
    return [c for c in s if c not in ['+', '-']]


def _checkConsecutiveSigns(s: str) -> bool:
    """ Checks if multiple consecutive signs exist in the input string
        Inputs:
            s: string of (potentially) multiple sign characters (+, -)
        Outputs:
            Boolean indicating the presence of multiple signs
    """

    for subStr in ['++', '+-', '-+', '--']:
        if subStr in s: return True

    return False


def parse(s: str) -> list:
    """ Parses generator string to produce a list containing the base factors,
        and a list containing the generated (derived) factors from the base ones.
        Inputs:
            s: Generator string
        Outputs:
            factors : list of dictionaries, one for each factor containing the following
                information:
                    name  : String with the factor's name
                    isBase: Boolean indcating if the factor is a base factor (if not
                            it is implicilty assumed that it is a generated one)
        
        NOTE: + signs are optional between factors.
            eg. the generator strings 'a +b -c' and 'a b -c' are equivalent.
    """

    # Ensure proper spacing between factors: 
    # e.g. 'a-b' -> 'a -b', '-a-----b' -> 'a -b', 'a- b' -> 'a -b'
    s = re.sub(r'(?<=[ \w+])-+(?=[ \w])', r' -', s)  # For minus sign
    s = re.sub(r'(?<=[ \w+])\++(?=[ \w])', r' +', s) # For plus sign

    # Split on spaces
    factorNo   = 0
    allFactors = s.split()
    numFactors = len(allFactors)
    
    factors = [] # List of dictionaries with the parsed factors
    while factorNo < numFactors:

        factor = allFactors[factorNo] # Get current factor

        # Ensure a 'full' factor string is being processed (e.g. not merely a + or - sign)
        if factor in ['+', '-']:
            factorNo += 1
            factor   += allFactors[factorNo]
        
        # Check if consecutive signs exist
        if _checkConsecutiveSigns(factor):
            raise ValueError(f'Consecutive sign characters detected. Exiting.')
        
        f = { # Make output dictionary
            'name'  : factor.replace('+', ''), # Ignore + signs. They are implied
            'isBase': _isBaseFactor(factor)
            }
        
        # Extract base factor names if needed
        if not f['isBase']: f['baseNames'] = _extractBaseFactors(f['name'])

        # Append, increment and continue
        factors.append(f)
        factorNo += 1
    
    return factors

