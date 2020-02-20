#! /usr/bin/env python3

# Muhammad Noman Junaid
# G00351754
# Calculate the sq. root of a number.

def sqrt(x): 
  """
  Calculate the Sq. root of argument x.
  """
  
  #Check that x is positive.
  if x < 0:
    print ("Error: negative value supplied")
    return -1
  else:
    print("Here we go..")
  
  #Initial guess for the Sq. root.
  z = x / 2.0

  #Continuously improve the guess.
  #Adapted from https://tour.golang.org/flowcontrol/8
  while abs(x - (z*z)) > 0.000001:
    z = z - (((z * z) - x) / (2 * z))
  return z

myval = 64.0
print ("The Sq. Root of",myval, "is",sqrt(myval))

