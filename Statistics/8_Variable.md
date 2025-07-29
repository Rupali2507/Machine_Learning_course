# 📦 Variable

A variable is a property or characteristic that can take on different values.

Examples in Python:

```python
Copy code
Age = 25                 # Integer
Ages = [12, 20, 36, 70]  # List of integers
height = 7.2             # Float
```

# 🔢 Types of Variables

### 1. Quantitative Variable:

These represent numeric values that can be measured.

a. Discrete Variable

- Can take only whole number values (integers).

- Examples:

  - age = 45

  - number_of_students = 10

b. Continuous Variable

- Can take any value within a range, including decimals.

- Examples:

  - height = 175.5 (cm)

  - weight = 26.4 (kg)

### 2. Qualitative Variable (Categorical)

- These represent categories or qualities, not numbers.

- Examples:

  - gender = "Female"

  - color = "Red"

# 🎲 Random Variables

A Random Variable is a variable whose possible values are numerical outcomes of a random phenomenon.

A Random Variable (RV) maps outcomes of a random process to numerical values.

### 🪙 Example 1: Tossing a Coin

Let the random variable X represent the outcome of tossing a coin.

```makefile
 X = {
  0 → Heads (H)
  1 → Tails (T)
}

```

Here

- The sample space is {H, T}

- The random variable X assigns:

  - 0 to Heads

  - 1 to Tails

✅ X is a Discrete Random Variable because it takes countable values (0 or 1).

### 🎲 Example 2: Rolling a Fair Die

Let the random variable X represent the outcome when rolling a fair 6-sided die.

We define:

```ini

X = {1, 2, 3, 4, 5, 6}
```

Each number corresponds to the number on the top face after the die is rolled.

✅ Again, X is a Discrete Random Variable because it can only take specific integer values.

## Types of Random Variable

1. Discrete Random Variable

Takes countable values (often integers).

Examples:

- Number of heads when flipping 3 coins.

- Number of students absent in a class.

```python

# Python example
import random

# Simulating number of heads in 3 coin flips
def num_heads():
    return sum(random.choice([0, 1]) for _ in range(3))  # 0 for tails, 1 for heads

```

2. Continuous Random Variable
   Takes uncountably infinite values (typically from an interval).

   Values are measured, not counted.

Examples:

- Height of students in a class.

- Time taken to run a race.

```python
# Python example using uniform distribution
import random

# Simulating a continuous variable like height (in cm)
height = random.uniform(150.0, 200.0)
```
