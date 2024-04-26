#Nth Roots of Unity

The nth roots of unity are the solutions to the equation $x^n = 1$. They are best visualized as equally spaced points on the unit circle, with the angle between these points being $\frac{2\pi}{n}$.

Using this fact, a nice way to compactly write these points is with complex exponential notation, through Euler's formula. One standard way to define the roots of unity is by defining this $\omega$ term as $e^{\frac{2\pi i}{n}}$, which allows us to define individual roots of unity quite compactly. Here are some examples:

- $\omega^0$
- $\omega^1$
- $\omega^2$
- ...
- $\omega^{n-1}$

So, when we say we want to evaluate a polynomial at the nth roots of unity, what we're really saying is we want to evaluate it at $\omega^0$, $\omega^1$, and so on, up until $\omega^{n-1}$.

So, going back to our original question of why evaluating the polynomial $P(x)$ at the nth roots of unity works for our recursive algorithm, there are two key properties at play. For one, our original set of points are positive-negative paired, where for the jth root $\omega^j$, $\omega^{j + \frac{n}{2}}$ is the corresponding pair.

Now, in our recursive step, we will be squaring each of these points and passing them on to the even and odd degree polynomials. This is what happens when we square our original n roots of unity. This reveals the second key property of the nth roots of unity: when we square the nth roots of unity, we end up with the $\frac{n}{2}$ roots of unity, which are also positive-negative paired and are just the right number of points for the two new polynomials of half the degree.

This same pattern holds at every level of the recursion until we end up with just one point. How beautiful is that?
