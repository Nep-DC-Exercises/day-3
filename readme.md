# Python Exercises (while loops)

This repository contains my answers to various python exercises from day 3 of DigitalCrafts. The prompts for each exercise are included as comment on line 1. The primary focus of these exercises were to practice using while loops.

I'm particularly proud of the `blastoff5.py` file where the challenge was to review python documentation and use the time module to implement a 1 second delay on the while loop count down.

Also glad that `factor.py` works because I'm not super strong in math. I find the logic in python very similar to plain english making it intuitive to write. For example:

```python
if i not in factors:
    factors.append(i)
```

translates pretty well to English. If the variable i is not in the factors list (we don't need duplicates), go ahead and add it in.

Lastly, the nested while loop functionality in `multiplication_table.py` was initially confusing but it made sense once I realized that the inner loop completes a full cycle before we iterate through the outer loop.
