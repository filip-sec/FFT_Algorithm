# Introduction to FFT Algorithm

## Polynomial Representation

Given polynomials:
- \( A(x) = x^2 + 3x + 2 \) represented as \( A = [2, 3, 1] \)
- \( B(x) = 2x^2 + 1 \) represented as \( B = [1, 0, 2] \)
- \( C(x) = 2x^4 + 6x^3 + 5x^2 + 3x + 2 \) represented as \( C = [2, 3, 5, 6, 2] \)

## Algorithm Overview

The Fast Fourier Transform (FFT) algorithm provides an efficient method for polynomial multiplication. Given polynomials \( A(x) \) and \( B(x) \), the algorithm computes the product polynomial \( C(x) = A(x) \times B(x) \).

### Coefficient Representation

Polynomials are represented as arrays of coefficients, where the index \( k \) corresponds to the degree \( k \) term of the polynomial \( C(x) \). For example, \( C[k] \) represents the coefficient of the \( k \)-th degree term of polynomial \( C(x) \).

### Algorithm Implementation

The algorithm multiplies two polynomials \( A(x) \) and \( B(x) \) using the distributive property. The runtime of this approach is \( O(d^2) \), where \( d \) is the degree of the polynomial. This is because each term in polynomial \( A \) has to be multiplied by all terms in polynomial \( B \).

## Optimization with FFT

Can we achieve a better runtime for polynomial multiplication? The Fast Fourier Transform (FFT) algorithm provides an efficient solution by exploiting the properties of Fourier transforms.