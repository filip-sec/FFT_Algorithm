# Polynomial Multiplication

Given polynomials $( A(x) = x^2 + 3x + 2 )$, $( B(x) = 2x^2 + 1 )$, and $( C(x) = 2x^4 + 6x^3 + 5x^2 + 3x + 2 \)$, represented by coefficient lists:

$$
\begin{align*}
A &= [2, 3, 1] \\
B &= [1, 0, 2] \\
C &= [2, 3, 5, 6, 2]
\end{align*}
\
$$

## Coefficient Representation

When we represent a polynomial as a list of its coefficients, each index \( k \) in the list corresponds to the coefficient of the \( k \)-th degree term in the polynomial.

## Computing Polynomial Multiplication

We can compute the product polynomial \( C = A \times B \) as follows:

```python
def multiPoly(A, B):
    """
    Computes the product polynomial C = A * B.
    
    Args:
    A (list): Coefficients of polynomial A(x).
    B (list): Coefficients of polynomial B(x).
    
    Returns:
    list: Coefficients of polynomial C(x).
    """
    d = len(A) + len(B) - 1
    C = [0] * d
    
    for i in range(len(A)):
        for j in range(len(B)):
            C[i + j] += A[i] * B[j]
    
    return C

# Example Usage
A = [2, 3, 1]
B = [1, 0, 2]
C = multiPoly(A, B)
print(C)  # Output: [2, 3, 5, 6, 2] 
```

## Optimization with FFT

Can we achieve a better runtime for polynomial multiplication? The Fast Fourier Transform (FFT) algorithm provides an efficient solution by exploiting the properties of Fourier transforms.