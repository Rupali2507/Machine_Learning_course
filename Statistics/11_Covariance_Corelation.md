# Covariance and Correlation

Covariance and correlation are two statistical measures that describe the relationship between two variables. Both are used to understand how changes in one variable are associated with changes in another variable.

## Covariance

Covariance is a measure of how much two random variables change together. It indicates the direction of the linear relationship between the variables. A positive covariance means that as one variable increases, the other variable tends to increase as well. Conversely, a negative covariance indicates that as one variable increases, the other variable tends to decrease.

### Example

Quantify the relationship between two sets of data:
X = {2,4,6,8}
Y = {3,5,7,9}

X is increasing and so y is also.

#### Formula

Cov(x,y) = Σ((xi - x̄)(yi - ȳ)) / (n - 1)

Where:

- Cov(x,y) is the covariance between variables x and y
- xi and yi are the individual sample points
- x̄ and ȳ are the sample means
- n is the number of data points

when x=x,
Cov(x,x) = Σ((xi - x̄)(xi - x̄)) / (n - 1) = Var(x)

Cov(x,x) is the variance of x.

#### Interpretation

- If Cov(x,y) > 0, x and y tend to increase together.
- If Cov(x,y) < 0, x and y tend to move in opposite directions.
- If Cov(x,y) = 0, there is no linear relationship between x and y.

Example:

```python

  x = HoursStudied = [2,3,4,5,6]
  y =  ExamScore = [50,60,70,80,90]

    Cov(x,y) = Σ((xi - x̄)(yi - ȳ)) / (n - 1)
    x̄ = (2+3+4+5+6)/5 = 4
    ȳ = (50+60+70+80+90)/5 = 70
    Cov(x,y) = ((2-4)*(50-70) + (3-4)*(60-70) + (4-4)*(70-70) + (5-4)*(80-70) + (6-4)*(90-70)) / (5 - 1)
              = (-2*-20 + -1*-10 + 0*0 + 1*10 + 2*20) / 4
              = (40 + 10 + 0 + 10 + 40) / 4
              = 100 / 4
              = 25

```

The Positive covariance of 25 indicates that as the number of hours studied increases, the exam score tends to increase as well.

### Advantages

1. Quantify the relationship between two variables.
2. Useful in portfolio management to understand how different assets move together.

### Disadvantages

1. Covariance does not have a specific limit value.
2. Does not provide a standardized measure, making it difficult to compare across different datasets.
3. Sensitive to the scale of the variables, which can affect interpretation.

## Correlation

Correlation is a standardized measure of the relationship between two variables. It quantifies both the strength and direction of the linear relationship between the variables. The correlation coefficient ranges from -1 to 1.

- A correlation of 1 indicates a perfect positive linear relationship. The more the value towards 1, the stronger the positive relationship.
- A correlation of -1 indicates a perfect negative linear relationship. The more the value towards -1, the stronger the negative relationship.
- A correlation of 0 indicates no linear relationship. The variables do not affect each other in a linear manner.

### Types of Correlation Coefficients

1. **Pearson Correlation Coefficient (r):** Measures the linear relationship between two continuous variables.

   - Formula: r = Cov(X, Y) / (σX \* σY)
   - Where σX and σY are the standard deviations of X and Y, respectively.

2. **Spearman's Rank Correlation Coefficient (ρ):** Measures the strength and direction of the monotonic relationship between two variables.
   - Used for ordinal data or when the assumptions of Pearson's correlation are not met.
   - Formula: ρ = 1 - (6 _ Σ(dᵢ²)) / (n _ (n² - 1))
   - Where dᵢ is the difference between the ranks of corresponding values and n is the number of observations.
