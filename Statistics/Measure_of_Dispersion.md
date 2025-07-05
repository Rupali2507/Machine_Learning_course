# Measure of Dispersion

Measure of dispersion is a statistical term that describes the extent to which data points in a dataset differ from each other. It provides insights into the variability or spread of the data. Common measures of dispersion include:

## 1. Variance

Variance is a measure of how much the values in a dataset differ from the mean. It is calculated as the average of the squared differences between each data point and the mean.

### Population data {N}

```markdown
Population variance = sigma^2 = sum((xi - mu)^2) / N

Where:

- ( sigma^2 ) is the population variance
- ( xi ) are the individual data points
- ( mu ) is the mean of the data points
```

#### Example

```python

Ages1 = [2, 2, 4, 4]
xi = individual data points
mu = mean of the data points

xi   mu    (xi - mu)^2
2    3.0   (2 - 3.0)^2 = 1
2    3.0   (2 - 3.0)^2 = 1
4    3.0   (4 - 3.0)^2 = 1
4    3.0   (4 - 3.0)^2 = 1

sumation of (xi - mu)^2 = 1 + 1 + 1 + 1 = 4
N = len(Ages1) # output: 4

variance = sum((xi - mu)^2) / N # output: 1.0
sigma^2 = 1.0

Ages2 = [1, 1, 5, 5]
xi   mu    (xi - mu)^2
1    3.0   (1 - 3.0)^2 = 4
1    3.0   (1 - 3.0)^2 = 4
5    3.0   (5 - 3.0)^2 = 4
5    3.0   (5 - 3.0)^2 = 4
sumation of (xi - mu)^2 = 4 + 4 + 4 + 4 = 16
N = len(Ages2) # output: 4
variance = sum((xi - mu)^2) / N # output: 4.0
sigma^2 = 4.0

```

### Sample data {n}

```markdown
Sample variance = s^2 = sum((xi - mean)^2) / (n - 1)

Where:

- ( s^2 ) is the sample variance
- ( xi ) are the individual data points
- ( mean ) is the sample mean of the data points
- ( n ) is the sample size
```

#### Example

```python

Ages1 = [2, 2, 4, 4]
n = len(Ages1) # output: 4
s^2 = sum((x - mean)^2) / (n - 1) # output: 1.0
Ages2 = [1, 1, 5, 5]
n = len(Ages2) # output: 4
s^2 = sum((x - mean)^2) / (n - 1) # output: 4.0
```
