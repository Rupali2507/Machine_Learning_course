# Histogram
A histogram is a graphical representation of the distribution of numerical data. It is created by dividing the data into intervals, called bins, and counting the number of data points that fall into each bin. The bins are usually specified as consecutive, non-overlapping intervals of a variable.

## Key Points
- **X-axis:** Represents the bins (ranges of values).
- **Y-axis:** Represents the frequency (count) of data points in each bin.
- **Bars:** The height of each bar shows how many data points fall within each bin.

## Example

Suppose you have the following data set:  
`[2, 3, 3, 5, 7, 8, 8, 9, 10, 10, 10, 12]`

A histogram for this data might look like:

```
Bin   Frequency
2-4   3
5-7   2
8-10  5
11-13 2
```

## When to Use a Histogram
- To visualize the distribution of a dataset.
- To identify patterns such as skewness, modality, or outliers.
- To compare distributions between different groups.

## Example in Python (using matplotlib)

```python
import matplotlib.pyplot as plt

data = [2, 3, 3, 5, 7, 8, 8, 9, 10, 10, 10, 12]
plt.hist(data, bins=[2, 5, 8, 11, 14], edgecolor='black')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram Example')
plt.show()
```

## Probability Distribution Function (PDF)

A Probability Distribution Function (PDF) describes the likelihood of a random variable taking on a particular value. For continuous data, the PDF shows the probability density, not the actual probability, at each value.

- The area under the PDF curve within a range represents the probability of the variable falling within that range.
- The total area under the PDF curve is always 1.

### Relation to Histogram

A histogram provides a discrete approximation of the PDF. As the number of data points increases and the bin width decreases, the histogram more closely resembles the underlying PDF.

### Example: Plotting a PDF in Python

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Generate data
data = np.random.normal(loc=0, scale=1, size=1000)

# Plot histogram
plt.hist(data, bins=30, density=True, alpha=0.6, color='g', edgecolor='black')

# Plot PDF
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, 0, 1)
plt.plot(x, p, 'k', linewidth=2)
plt.xlabel('Value')
plt.ylabel('Density')
plt.title('Histogram and Probability Distribution Function')
plt.show()
```