# Darts Checkout Calculator

This is a slightly silly little project, mostly the result of some fairly serious procrastination when I should have been revising for an exam.

I watched the Darts World Championship for the first time on New Year’s Day and was genuinely impressed by the players’ rapid mental arithmetic. I’d never really appreciated that they calculate their *checkout* routes in their heads, on the fly (pun fully intended). I naively assumed the players see the various scoring options that viewers at home see on TV while they throw (e.g. "T20 D20 D8). 

## What’s going on?

- Players start on **501**
- Each turn consists of **three darts**
- Each throw chips away at the score
- To *checkout* (finish on exactly 0), the **final dart must be a double**

I fancied a small project as an excuse to do some basic Python again, and this is the end result of a day’s work.

## What this does

You input:
- Your current score
- The number of darts you have left in the turn

The script returns a list of possible checkout combinations.

I used a recursive approach to generate the combinations. This almost certainly made life more complicated than it needed to be, but it was a fun logic problem to tackle in revision breaks.

### Example

```text
What's your current total? 156

How many darts do you have left on this turn? 3

Output: [[('T', 20), ('T', 20), ('D', 18)]]


What's your current total? 57

How many darts do you have left on this turn? 2

Output: [[('T', 17), ('D', 3)], [('T', 15), ('D', 6)], [('T', 13), ('D', 9)], [('T', 11), ('D', 12)], [('T', 9), ('D', 15)], [('S', 25), ('D', 16)]...
