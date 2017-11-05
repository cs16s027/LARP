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


