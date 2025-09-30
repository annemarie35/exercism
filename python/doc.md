# About Numbers
Python has three different types of built-in numbers: integers (int), floating-point (float), and complex (complex). Fractions (fractions.Fraction) and Decimals (decimal.Decimal) are also available via import from the standard library.

Whole numbers including hexadecimal (hex()), octal (oct()) and binary (bin()) numbers without decimal places are also identified as ints.

Python fully supports arithmetic between these different number types, and will convert narrower numbers to match their less narrow counterparts when used with the binary arithmetic operators (+, -, *, /, //, and %).
https://exercism.org/tracks/python/concepts/numbers

# Notes on exercices learning
## Protein translations

I still need to improve all the potential of `List comprehension` using range built-in function.
Like in this [alternative solution](https://exercism.org/tracks/python/exercises/protein-translation/solutions/delamoe)

```python
strand = "UUU"
codonList = [(strand[i:i+3]) for i in range(0, len(strand), 3)]
```
There is a video showing [11 Ways to Solve Protein Translation on Exercism](https://www.youtube.com/watch?v=i7SEtqVlWUU&t=33s)


## Leap exercices

[Dig deeper](https://exercism.org/tracks/python/exercises/leap/dig_deeper) :  You can use:
- a chain of boolean expressions to test the conditions ([boolean chain approach](https://exercism.org/tracks/python/exercises/leap/approaches/boolean-chain)
)
- a ternary operator, or built-in methods from the datetime
- calendar modules. ([calendar approach](https://exercism.org/tracks/python/exercises/leap/approaches/calendar-isleap)
)
```python
from calendar import isleap

def leap_year(year):
    return isleap(year)
```

[Performance deep dive](https://exercism.org/tracks/python/exercises/leap/articles/performance)
Ternary is a little bit faster than using the if statement

## Meltdown mitigation
In Python, if, elif (a contraction of 'else and if') and else statements are used to control the flow of execution and make decisions in a program. 
Unlike many other programming languages, Python versions 3.9 and below do not offer a formal case-switch statement, instead using multiple elif statements to serve a similar purpose.


## Raindrops
See others approaches [here](https://exercism.org/tracks/python/exercises/raindrops/dig_deeper) 
If too many `if` statement, use a loop 
For performance deep dive look at [here](https://exercism.org/tracks/python/exercises/raindrops/articles/performance)

# Little Sister's Vocabulary
[exercice url](https://exercism.org/tracks/python/exercises/little-sisters-vocab)
A `str` in Python is an [immutable sequence](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str) of [Unicode code points](https://stackoverflow.com/questions/27331819/whats-the-difference-between-a-character-a-code-point-a-glyph-and-a-grapheme). These could include letters, diacritical marks, positioning characters, numbers, currency symbols, emoji, punctuation, space and line break characters, and more. Being immutable, a `str` object's value in memory doesn't change; methods that appear to modify a string return a new copy or instance of that `str object.

Listen to the Fugees's Vocab song while coding (The acoustic version is da best!)