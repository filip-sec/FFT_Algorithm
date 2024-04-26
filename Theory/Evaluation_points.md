# Evaluation Points

When dealing with the evaluation of polynomials, particularly in the context of using the Fast Fourier Transform (FFT) for efficient computation, the choice of evaluation points is crucial. 

## Which Evaluation Points?

Consider we have a degree 3 polynomial, which requires at least \( n = 4 \) points for its value representation. These points need to be positive-negative pairs, so we can denote them as \( x_1, -x_1, x_2, \) and \( -x_2 \).

The recursive step in FFT will require that we evaluate the odd and even splits of the polynomial at two points: \( x_1^2 \) and \( x_2^2 \). A key constraint here is that for the recursion to work, these two points also need to be positive-negative pairs, giving us an equivalence between \( x_2^2 \) and \( -x_1^2 \).

At the bottom level of recursion, we will have a single point, \( x_1^4 \). What's convenient is that we get to choose these points. If we select our initial \( x_1 \) to be 1, it simplifies our problem significantly because the points at each recursive step remain as 1 and -1.

Now, to satisfy our condition, what should \( x_2 \) be chosen as? It turns out that the answer is the complex number \( i \), as squaring it gives \( -1 \). This leads us to the realization that the four points needed to evaluate the polynomial are \( 1, -1, i, \) and \( -i \).

An alternate perspective is that we are essentially solving the equation \( x^4 = 1 \). The solutions to this equation are known as the fourth roots of unity.

## Generalization

If we have a degree 5 polynomial, we will need more than 6 points. Since our recursive method splits each problem in half, it is convenient to choose \( n \) as a power of 2, such as \( n = 8 \). To satisfy the FFT requirements, we need to find eight points that, when raised to the eighth power, are equal to one. These points are known as the eighth roots of unity.

In general, for a degree \( d \) polynomial, we will select \( n \) points where \( n \) is greater than or equal to \( d + 1 \) and is also a power of 2. The optimal points for polynomial evaluation are the \( n \)-th roots of unity.

## Why Does This Work?

Before diving deeper, it's important to understand why selecting the \( n \)-th roots of unity as evaluation points works for FFT. This topic deserves a thorough explanation, which will be covered as we formalize our understanding of the FFT and its properties.

