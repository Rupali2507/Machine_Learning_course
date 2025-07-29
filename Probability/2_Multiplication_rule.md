# Multiplication Rule

The multiplication rule is used to find the probability of the intersection of two events, either independent or dependent. It combines the individual probabilities of the events and their conditional probabilities (if applicable) to give the overall probability of both events occurring together.

## Independent Events

Two events A and B are **independent** if the occurrence of one does not affect the occurrence of the other. In other words, the probability of A occurring is the same regardless of whether B occurs or not, and vice versa.

### Example

```python
# Flipping a coin and rolling a die
import random

def flip_coin():
    return random.choice(['Heads', 'Tails'])

def roll_die():
    return random.randint(1, 6)

# Simulate flipping the coin and rolling the die
coin = flip_coin()
die = roll_die()
print("Coin flip:", coin)
print("Die roll:", die)
```

## Multiplication Rule for Independent Events

The multiplication rule states that if two events A and B are independent, the probability of both events occurring is the product of their individual probabilities:
P(A and B) = P(A) \* P(B)

## Dependent Events

Two events A and B are **dependent** if the occurrence of one affects the occurrence of the other. In this case, the probability of A occurring is influenced by whether B occurs or not, and vice versa.

### Example

```python
# Drawing cards from a deck without replacement
import random
def draw_card(deck):
    return deck.pop(random.randint(0, len(deck) - 1))
deck = ['Ace of Spades', '2 of Spades', '3 of Spades', '4 of Spades', '5 of Spades']
# Simulate drawing two cards
first_card = draw_card(deck)
second_card = draw_card(deck)
print("First card drawn:", first_card)
print("Second card drawn:", second_card)
```

## Multiplication Rule for Dependent Events

For dependent events A and B, the multiplication rule is:
P(A and B) = P(A) \* P(B|A)

Where P(B|A) is the conditional probability of B given that A has occurred.
