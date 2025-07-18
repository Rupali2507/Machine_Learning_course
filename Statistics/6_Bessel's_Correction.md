# Why Sample Variance is Divided by n-1

Bessel's correction is the adjustment made to the formula for sample variance to account for the fact that we are estimating the population variance from a sample. 

Sample Variance , S^2, is calculated using the formula:

s^2 = sum((xi - mean)^2) / (n - 1)

Where:
- n is the sample size
- xi represents each value in the sample
- mean is the sample mean

The reason for dividing by (n - 1) instead of n is to correct the bias in the estimation of the population variance from a sample. This adjustment is known as Bessel's correction.
# It ensures that the sample variance is an unbiased estimator of the population variance.

Let's illustrate this with an example:

```python
data = [10, 20, 30, 40, 50, 60]

population_mean = sum(data) / len(data)  # Output: Population Mean: 35.0

population_variance = sum((x - population_mean) ** 2 for x in data) / len(data)  # Output: Population Variance: 350.0

sample_data = data[:4]  # Taking a sample of the first 4 elements

sample_mean = sum(sample_data) / len(sample_data) # Output: Mean: 25.0

#if we divide by n (4 in this case), we get a biased estimate of the variance
sample_variance_biased = sum((x - sample_mean) ** 2 for x in sample_data) / len(sample_data)  # Output: Biased Sample Variance: 50.0

# To correct this bias, we divide by (n - 1)
sample_variance = sum((x - sample_mean) ** 2 for x in sample_data) / (len(sample_data) - 1)  # Output: Sample Variance: 25.0

This shows that dividing by (n - 1) gives us a more accurate estimate of the population variance based on the sample data.
```

## 🔍 What This Proves
- The biased variance (50) overestimates the spread because it undercorrects for the fact that the mean (25) is not the true mean (35).

- The unbiased sample variance (25) gives a better estimate of the population's true spread — even though it's still based on a small sample.

- Bessel's correction (dividing by n−1) adjusts for this and gives us a more reliable, unbiased estimate.



