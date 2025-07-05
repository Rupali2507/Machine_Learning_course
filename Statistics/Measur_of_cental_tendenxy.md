### Measures of Central Tendency

Measures of central tendency are statistical measures that describe the center or typical value of a dataset. They provide a summary statistic that represents the entire distribution of data points. The most common measures of central tendency are:

1. Mean: The arithmetic average of a dataset, calculated by summing all values and dividing by the number of values.
2. Median: The middle value of a dataset when it is ordered from least to greatest. If there is an even number of values, the median is the average of the two middle values.
3. Mode: The most frequently occurring value in a dataset. A dataset may have one mode, more than one mode, or no mode at all.

### Mean

Formula:

mean = summation of all values / number of values

number of values = n (sample size)
number of values in population = N (population size)

Example:

```python
data = [10, 20, 30, 40, 50]
mean = sum(data) / len(data)
print("Mean:", mean) # Output: Mean: 30.0
```

Outliers can significantly affect the mean, as it is sensitive to extreme values. For example:

```python
data = [10, 20, 30, 40, 1000]  # Outlier at the end
mean = sum(data) / len(data)
print("Mean:", mean) # Output: Mean: 220.0
```

### Median

To find the median, follow these steps:

1. Sort the data in ascending order.
2. If the number of values (n) is odd, the median is the middle value.
3. If n is even, the median is the average of the two middle values.

Lets go through the same example as above:

```python
data = [40, 20, 50, 10, 30]
data.sort()  # Ensure the data is sorted
n = len(data)
if n % 2 == 1:
    median = data[n // 2]
else:
    median = (data[n // 2 - 1] + data[n // 2]) / 2
print("Median:", median) # Output: Median: 30.0
```

Outliers can affect the median, but it is less sensitive to extreme values compared to the mean.

example:

```python
data = [10, 20, 30, 40, 1000]  # Outlier at the end
data.sort()
n = len(data)
if n % 2 == 1:
    median = data[n // 2]
else:
    median = (data[n // 2 - 1] + data[n // 2]) / 2
print("Median:", median) # Output: Median: 30.0
```

### Mode

The mode is the value that appears most frequently in a dataset. A dataset may have one mode, more than one mode, or no mode at all.

```python
data = [4,3,2,1,1,4,4,5,2,2,100]
mode = max(set(data), key=data.count)
print("Mode:", mode) # Output: Mode: 4
```

Outliers do not affect the mode, as it is based on frequency rather than value. However, if there are multiple modes (bimodal or multimodal), it can complicate the interpretation.
