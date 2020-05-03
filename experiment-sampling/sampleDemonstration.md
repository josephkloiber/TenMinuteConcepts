# Monte Carlo Versus Latin Square Sampling

## Introduction

Over the course of my career, I have observed many MS&A practitioners
use the phrase ``Monte Carlo'' without a true understanding of its intended 
application as a variance reduction technique as well as other methods of
variance reduction available.  This article demonstrates the advantages of 
an alternative method.

## The challenge
Estimate the value of &pi; using two different sampling methods:
+ Monte Carlo
+ Latin Square

## Defining the Sampling Methods

### Monte Carlo
Monte Carlo simulation is widely used to solve certain problems in statistics
that are not analytically tractable.  However, for the purposes of this
demonstration, a tractable problem is presented so as to place emphasis on the
methods without becoming distracted by the particular application.

![Monte Carlo Samples](./monte_carlo_points.png)
