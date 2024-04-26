# FFT Implementation

With a clear understanding of the principles behind the FFT, we're now ready to outline the core Fast Fourier Transform algorithm. The FFT will take in a coefficient representation of a degree $n-1$ polynomial, where $n$ is a power of two.

We define $\omega$ as $e^{\frac{2\pi i}{n}}$ to facilitate the definition of roots of unity.

## Base Case

The first case to handle is the base case, which occurs when $n = 1$. This simply means that we are evaluating the polynomial at one point.

## Recursive Case

The recursive case consists of two calls to the FFT: one on even degree terms and one on odd degree terms. The intention is that these polynomials are now half the degree of our original polynomial, so they only need to be evaluated at $\frac{n}{2}$ roots of unity.

Assuming the recursion works, the output of these calls will be the value representation of these even and odd degree term polynomials, which we will label as $y_e$ and $y_o$.

## Combining the Results

The tricky part is to take the output from these recursive calls and combine them to get the value representation of our original degree $n-1$ polynomial. The key idea is to use the relationship between positive and negative pairs, modified for our roots of unity inputs.

We know that the $j$-th input point corresponds to the $j$-th root of unity, resulting in the relationship:

$$ \omega^j = \text{the } j\text{-th root of unity} $$

Moreover, the paired point $-\omega^j$ is equal to $\omega^{j + \frac{n}{2}}$, due to the properties of the roots of unity.

Utilizing this fact, we can modify the second equation as follows, and also take advantage of the fact that the $j$ index in our $y_e$ and $y_o$ list corresponds to the even and odd polynomials evaluated at $\omega^{2j}$. This simplifies our equations significantly, making implementation more straightforward.

## Translation to Code

Now, let's translate this algorithmic logic into code. Our function `fft` will take an input $p$, which is the coefficient representation of a polynomial $P$. We start by defining $n$ as the length of $p$ and assume $n$ is a power of two.

Handling the base case is straightforward, as we return our original $p$ for a single element, effectively making $p$ a degree zero polynomial or a constant. Otherwise, we proceed with the recursive step.

The recursive step involves splitting the polynomial into even and odd degree terms, followed by calling the `fft` function recursively on these polynomials. We denote the outputs as $y_e$ and $y_o$, as per the outline.

We then initialize our output list for the final value representation. For all $j$ up to $\frac{n}{2}$, we calculate the value representations according to our outlined method. Once all values are populated in our list, we return that list, completing the FFT.

This process is an elegant convergence of all the ideas we've discussed, resulting in a concise yet powerful piece of code.

## Conclusion

The FFT allows us to efficiently convert coefficient representations to value representations. The remaining piece of the puzzle is the inverse process, converting value representations back to coefficient representations, a process formally known as interpolation.
