# Probablity

Definition of Probability:
Probability is a measure of the likelihood that an event will occur. It quantifies uncertainty and is expressed as a number between 0 and 1, where:

- 0 indicates impossibility (the event will not occur).
- 1 indicates certainty (the event will occur).
- Values between 0 and 1 indicate the degree of likelihood of the event occurring.

## Example

```python
Rolling a fair die:
import random

def roll_die():
    return random.randint(1, 6)

# Simulate rolling the die 10 times
rolls = [roll_die() for _ in range(10)]
print("Die rolls:", rolls)
```

## Mutual Exclusivity

Two events are **mutually exclusive** if they cannot occur at the same time. For example, when rolling a die, the events of rolling a 1 and rolling a 2 are mutually exclusive because both cannot happen in a single roll.

## Addition Rule of Mutual Exclusive Events

The addition rule states that if two events A and B are mutually exclusive, the probability of either event occurring is the sum of their individual probabilities:

P(A or B) = P(A) + P(B)

### Example

```python
# Probability of rolling a 1 or a 2 on a fair die
P_A = 1/6  # Probability of rolling a 1
P_B = 1/6  # Probability of rolling a 2
P_A_or_B = P_A + P_B
print("Probability of rolling a 1 or a 2:", P_A_or_B)
```

## Non-Mutually Exclusive Events

Two events are **non-mutually exclusive** if they can occur at the same time. For example, when drawing a card from a standard deck, the events of drawing a heart and drawing a face card are non-mutually exclusive because a face card can also be a heart.

## Addition Rule for Non-Mutually Exclusive Events

For non-mutually exclusive events A and B, the addition rule is:
P(A or B) = P(A) + P(B) - P(A and B)

### Example

```python
# Probability of drawing a heart or a face card from a standard deck
P_A = 13/52  # Probability of drawing a heart (13 hearts in a deck)
P_B = 12/52  # Probability of drawing a face card (3 face cards in each suit)
P_A_and_B = 3/52  # Probability of drawing the 3 face cards that are hearts
P_A_or_B = P_A + P_B - P_A_and_B
print("Probability of drawing a heart or a face card:", P_A_or_B)

```

## Summary

- **Mutually Exclusive Events**: P(A or B) = P(A) + P(B)
- **Non-Mutually Exclusive Events**: P(A or B) = P(A) + P(B) - P(A and B)
