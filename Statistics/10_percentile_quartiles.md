# Percentile and Quartiles

## Percentile



A **percentile** is a measure that indicates the value below which a given percentage of observations in a group falls. For example, the 25th percentile is the value below which 25% of the observations may be found.


Percentage = (No of favourable outcome / Total no of outcome) * 100
  - e.g. {1,2,3,4,5,6}
    - no of Odd num = 3
    - Percentage of odd num in given numbers  = (3/6)*100 = 50%

Percentile = (No of values below x / n) * 100;
  - e.g. {2,23,4,5,5,6,7,8,8,8,8,9,9,10}
     - x = 9
     - Percentile of value x = (11/14)*100 = 78.57 percentile

value = (Percentile/100 )*(n+1)  

## Quartiles

**Quartiles** divide a dataset into four equal parts:

- **Q1 (First Quartile):** 25% of data falls below this value (same as 25th percentile).
- **Q2 (Second Quartile):** 50% of data falls below this value (median, or 50th percentile).
- **Q3 (Third Quartile):** 75% of data falls below this value (75th percentile).

**Calculation:**
1. Sort the data in ascending order.
2. Find the positions for Q1, Q2, and Q3 using the percentile formula.

---

**Example:**

Given data: 2, 4, 7, 10, 12, 15, 18, 21

- Q1 (25th percentile): 5.25 (between 4 and 7)
- Q2 (Median, 50th percentile): 11
- Q3 (75th percentile): 16.5 (between 15 and 18)

---

**Summary Table:**

| Quartile | Percentile | Description         |
|----------|------------|---------------------|
| Q1       | 25th       | Lower Quartile      |
| Q2       | 50th       | Median              |
| Q3       | 75th       | Upper Quartile      |

## Five Number Summary

The **five number summary** provides a quick overview of the distribution of a dataset. It consists of:

1. **Minimum** – The smallest value in the dataset.
2. **Q1 (First Quartile)** – The 25th percentile.
3. **Median (Q2)** – The 50th percentile.
4. **Q3 (Third Quartile)** – The 75th percentile.
5. **Maximum** – The largest value in the dataset.

**Example:**

Given data: 2, 4, 7, 10, 12, 15, 18, 21

- Minimum: 2
- Q1: 5.25
- Median: 11
- Q3: 16.5
- Maximum: 21

**Summary Table:**

| Statistic | Value  |
|-----------|--------|
| Minimum   | 2      |
| Q1        | 5.25   |
| Median    | 11     |
| Q3        | 16.5   |
| Maximum   | 21     |

## Lower and Upper Fence

The **lower fence** and **upper fence** are boundaries used to detect outliers in a dataset. They are calculated using the interquartile range (IQR):

- **IQR (Interquartile Range):** IQR = Q3 - Q1

- **Lower Fence:** Q1 - 1.5 × IQR
- **Upper Fence:** Q3 + 1.5 × IQR

Any data points outside these fences are considered potential outliers.

**Example:**

Given Q1 = 5.25, Q3 = 16.5:

- IQR = 16.5 - 5.25 = 11.25
- Lower Fence = 5.25 - 1.5 × 11.25 = -11.375
- Upper Fence = 16.5 + 1.5 × 11.25 = 33.125

Values below -11.375 or above 33.125 are outliers.

## Example: Outlier Detection and Five Number Summary

Given data: 1, 2, 2, 2, 2, 3, 3, 4, 5, 5, 5, 6, 6, 6, 6, 7, 8, 8, 9, 27

**Step 1: Five Number Summary**

- Minimum: **1**
- Q1 (25th percentile):  
  Position = 0.25 × (20 + 1) = 5.25  
  Q1 = 2 (5th value) + 0.25 × (6th value - 5th value) = 2 + 0.25 × (3 - 2) = **2.25**
- Median (Q2, 50th percentile):  
  Position = 0.5 × (20 + 1) = 10.5  
  Median = 5 (10th value) + 0.5 × (11th value - 10th value) = 5 + 0.5 × (5 - 5) = **5**
- Q3 (75th percentile):  
  Position = 0.75 × (20 + 1) = 15.75  
  Q3 = 6 (15th value) + 0.75 × (16th value - 15th value) = 6 + 0.75 × (7 - 6) = **6.75**
- Maximum: **27**

| Statistic | Value  |
|-----------|--------|
| Minimum   | 1      |
| Q1        | 2.25   |
| Median    | 5      |
| Q3        | 6.75   |
| Maximum   | 27     |

**Step 2: Outlier Detection**

- IQR = Q3 - Q1 = 6.75 - 2.25 = **4.5**
- Lower Fence = Q1 - 1.5 × IQR = 2.25 - 1.5 × 4.5 = 2.25 - 6.75 = **-4.5**
- Upper Fence = Q3 + 1.5 × IQR = 6.75 + 1.5 × 4.5 = 6.75 + 6.75 = **13.5**

**Outliers:**  
Any value below -4.5 or above 13.5 is an outlier.  
In this dataset, **27** is an outlier.

**Summary:**  
- Five number summary: 1, 2.25, 5, 6.75, 27  
- Outlier: 27
## Example: Five Number Summary and Box Plot (Without Outlier)

Let's remove the outlier (27) from the dataset:

New data: 1, 2, 2, 2, 2, 3, 3, 4, 5, 5, 5, 6, 6, 6, 6, 7, 8, 8, 9

**Step 1: Five Number Summary**

- Minimum: **1**
- Q1 (25th percentile):  
  Position = 0.25 × (19 + 1) = 5  
  Q1 = 3 (5th value)
- Median (Q2, 50th percentile):  
  Position = 0.5 × (19 + 1) = 10  
  Median = 5 (10th value)
- Q3 (75th percentile):  
  Position = 0.75 × (19 + 1) = 15  
  Q3 = 6 (15th value)
- Maximum: **9**

| Statistic | Value |
|-----------|-------|
| Minimum   | 1     |
| Q1        | 3     |
| Median    | 5     |
| Q3        | 6     |
| Maximum   | 9     |

**Step 2: Box Plot**

A box plot visually represents the five number summary:

```
|----|=======|=======|=======|----|
1    3       5       6       9
```

- The box spans from Q1 (3) to Q3 (6), with a line at the median (5).
- Whiskers extend to the minimum (1) and maximum (9).
- No outliers are present in this dataset.