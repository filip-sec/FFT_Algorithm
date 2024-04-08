We can represent any line with exactly two coefficients. One for the degree zero term and one for the degree one term. The key part that makes this representation valid is that every representation has one-to-one mapping to a unique line. 

P(x) = p0 +p1x
    (-2,0),(2,2)
P(x) = 1 + 0.5x
    (3,0),(-1,4)
    P(x) = 3 - x

2 Points define a unique line 

$$
\begin{align*}
P(x) &= \frac{3}{4} x^2 + 2x + \frac{1}{4} \\
P(x) &= \frac{2}{3} x^3 - x^2 - \frac{2}{3}x + 1 \\
\{(x_0, P(x_0)), (x_1, P(x_1)), \ldots , (x_d, P(x_d)) \} \\
P(x) = p_0 + p_1x + p_2x^2 + \cdots + p_dx^d \\
P(x_0) = p_0 + p_1x_0 + p_2x_0^2 + \cdots + p_dx_0^d \\
P(x_1) = p_0 + p_1x_1 + p_2x_1^2 + \cdots + p_dx_1^d \\
P(x_d) = p_0 + p_1x_d + p_2x_d^2 + \cdots + p_dx_d^d \\
\end{align*}
$$

$$
\begin{bmatrix}
1 & x_0 & x_0^2 & \cdots & x_0^d \\
1 & x_1 & x_1^2 & \cdots & x_1^d \\
\vdots & \vdots & \vdots  & \ddots & \vdots  \\
1 & x_d & x_d^2 & \cdots & x_d^d 
\end{bmatrix}
$$
