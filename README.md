
# Advent of Code 2022

I am trying to use Pandas for every puzzle. I've already given up on day 5 because of
the input data formatting (I did use numpy though so.. close?).

This should not be used as an example of how to do anything, this is just me working
stuff out as I go along.

## How to run

I'm using a 3.10 venv, other versions may or may not work.

To run a day do something like `python puzzles/day_01.py`

I run the tests in PyCharm using the config in `.run`, or they can be run from the command
line with `python -m pytest tests`

To create a new day run `sh setup/new_day.sh 02 `

## What was I thinking

### Day 01

Honestly, I had no idea before this how to group pandas rows using an empty row as a
delimiter, it's not a situation I've ever come across before. So I learnt how to do that
using `isnull` and `all` over the column, which gave me a `True` for a null row and a `False`
for a populated row. The it's just summing over the groups and getting the max.

Part 2 was basically the same but instead of getting the max, I ordered them then took
the top 3 and added them up.

### Day 02

A lot of mapping. Decoded both columns to the actual shapes used (more meaningful),
calculated the shape score with another map, then the winners by comparing the two
columns to a list of winning states.

Part 2 was just decoding the other way round then applying the same shape/winner scoring
as before.

### Day 03

Part 1 was speedy fast, split the string into two columns, find the common elements with
`intersection` (caveat here - it will crap out if there's more than one common element..)
then map the priorities.

Part 2 was a little more involved because grouping in pandas which is something I;ve not
done much, but I figured how to copy every 3rd row to a new column then used that to group
which worked well.

### Day 04

Most of the effort here went into setting up the dataframes, splitting the groups
into two columns of lists, then it was just a matter of `any` and `all` to get the
overlaps.

### Day 05

Sadly I had to abandon pandas for this one :(


I wrote a really nasty parser to separate out the stacks from the instructions.
I found the instructions by looking for the word 'move' at the start of the line
but the stacks were nasty - I iterated  over the lines til I found on that was
all numbers then stopped and took all the previous values.

I tried to turn the stacks in to lists instead of weird vertical piles by splitting
them up and padding them so they were all the same size then turned that into a matrix
so I could transpose and reverse easily.

From there it was easy enough to iterate through the instructions list and pop the boxes
off the stacks and move them around for part one, then slice and move for part 2.

It's messy af but I did this one in the evening after a long day so I'm just pleased
I got it done tbh.