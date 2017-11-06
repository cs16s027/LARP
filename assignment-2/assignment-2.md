### LARP : Assignment-2

#### Problem-1

Each random variable $$X_i$$  is distributed with mean $\mu$ and variance $\sigma^{2}$. Then, the mean of the random variables is also a random variable:
$$
\bar{X} = \frac{1}{N} \sum \limits_{i = 1}^{N} X_{i}
$$
Since expectation is a linear operator and given that the $N$ random variables are identically distributed.
$$
E(\bar{X}) = \frac{1}{N} \sum \limits_{i=1}^{N} E(X_{i}) = \mu
$$
We make use of the independence assumption to get the variance:
$$
\text{Var}(\bar{X}) = \frac{1}{N^2} \sum \limits_{i = 1}^{N} \sigma^2 = \frac{\sigma^2}{N}
$$

---

#### Problem-2

Letting $\delta = 2\ \text{exp}\bigg(-\frac{2N\epsilon^2}{(b - a)^2}\bigg)$ ,
$$
\mathbb{P}(\bar{X} - \mu \geq \epsilon) \leq \frac{\delta}{2}\\
\mathbb{P}(\bar{X} - \mu \leq -\epsilon) \leq \frac{\delta}{2}
$$
Since the events $\bar{X} - \mu \geq \epsilon$ and $\bar{X} - \mu \leq -\epsilon$ are mutually exclusive, we get:
$$
\mathbb{P}(\bar{X} - \mu \geq \epsilon \text{ and } \bar{X} - \mu \leq -\epsilon) \leq 2\ \frac{\delta}{2} = \delta
$$
Rewriting the above inequality, we get
$$
\mathbb{P}(|\bar{X} - \mu| \geq \epsilon) \leq \delta
$$
The complementary event is $|\bar{X} - \mu| \leq \epsilon$. The corresponding probability is:
$$
\mathbb{P}(|\bar{X} - \mu| \leq \epsilon) = 1 - \mathbb{P}(|\bar{X} - \mu| \geq \epsilon) \geq 1 - \delta
$$
The event $|\bar{X} - \mu| \leq \epsilon$ can be rewritten as $\mu \in [\bar{X} - \epsilon, \bar{X} + \epsilon]$.

Thus, the required probability becomes:
$$
\mathbb{P}(\mu \in [\bar{X} - \epsilon, \bar{X} + \epsilon])  \geq 1 - \delta
$$

Since $\delta = 2\ \text{exp}\bigg(-\frac{2N\epsilon^2}{(b - a)^2}\bigg)$ , 
$$
\epsilon = \sqrt{\frac{(b-a)^2}{2N} ln\bigg(\frac{2}{\delta}\bigg)}
$$

---

#### Problem-3

(a) The sample mean is close to the true mean. From the first question, we know that the sample mean of $N$ i.i.d random variables, each having mean $\mu$ and variance $\sigma^2$, is also a random variable with mean $\mu$ and variance $\frac{\sigma^2}{N}$. For any given experiment with $N$ samples, their mean is one realisation of this random variable.

(b) 

|   N   | [9.9, 10.1] | [9.99, 10.01] |
| :---: | :---------: | :-----------: |
|  10   |     409     |      409      |
|  100  |    2389     |      122      |
| 1000  |    6796     |      785      |
| 10000 |    9986     |     2438      |

(c) 

|   N   | % of intervals with $\mu \in [a, b]$ |
| :---: | :----------------------------------: |
|  10   |                 4.12                 |
|  100  |                15.95                 |
| 1000  |                46.65                 |
| 10000 |                95.27                 |

(d) The random variables given in problem-1 have a bounded support, $[a, b]$, whereas Poisson random variables have an unbounded support, $[0, \infty]$.

Let $X_i ~ Bin(n, \frac{\lambda}{n})$ be the $i^{th}$ random variable with $\mu = \lambda, \sigma^2 = \lambda(1-\frac{\lambda}{n})$. 

The sample mean has $\mu = \lambda, \sigma^2 = \frac{\lambda}{N}(1-\frac{\lambda}{n})$. 

For a $95\%$ confidence interval, we need the $\delta = 1 - 0.95 = 0.05$. Using the equation for $\epsilon$, by substituting the values as follows:

$a = 0, b = n, \delta = 0.05$
$$
\epsilon = \sqrt{\frac{(b-a)^2}{2N} ln\bigg(\frac{2}{\delta}\bigg)} = 1.36 \frac{n}{\sqrt{N}}
$$
For a large value of $n$, the Binomial distribution is quite a good approximation of the Poisson. The numerical estimate of $\epsilon = 0.06$. To get an equivalent theoretical estimate, we need:
$$
\frac{n}{\sqrt{N}} = \frac{0.06}{1.36} = 0.04 \implies N = 625 n^2
$$
If we replace the Poisson with the Binomial for our numerical experiments, we wil have to sample several more examples to replicate the results.

(e)

| Accuracy |     N     |
| :------: | :-------: |
|   0.1    |   2700    |
|   0.01   |  677000   |
|  0.001   | 109000000 |

$$
n = \bigg(\frac{z \sigma}{\text{accuracy}}\bigg) ^2
$$

where, $z= -F^{-1}(\frac{\text{accuracy}}{2})$. $F^{-1}$ is the inverse of the Gaussian c.d.f. Every decimal drop in accuracy contributes to at least an order of magnitude increase in the number of samples required.

---

#### Problem-4

(a)
$$
f(k) = \frac{A}{k^2}, k \in \mathbb{Z} - \{0\}
$$
For $f$ to be a valid p.m.f, its sum over the support should be one.
$$
\sum \limits_{k = -\infty}^{\infty} \frac{A}{k^2} = 1 \implies A \frac{\pi^2}{3} = 1 \implies A = \frac{3}{\pi^2}
$$
(b)

**Method** :  To sample from this p.m.f, we consider a modified distribution with a positive support:
$$
f^{+}(k) = \frac{A^{+}}{k^2}, k \in \mathbb{Z^{+}}
$$
where $A^{+} = \frac{6}{\pi^2}$. Let $S$ be a bernou