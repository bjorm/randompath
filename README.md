# randompath
## use
Generates a random path on a game board of given `size`

```
$ python3 randompath.py --size=10
 1  0  .  .  .  .  .  .  .  . 
 2  .  .  .  .  .  .  .  .  . 
 3  4  5  6  7  8  .  .  .  . 
 .  .  .  .  .  9  .  .  .  . 
15 14 13 12 11 10  .  .  .  . 
16  .  .  .  .  .  .  .  .  . 
17 18 19 20 21 22 23 24 25 26 
 .  .  .  .  .  .  .  .  . 27 
 .  .  .  .  . 32 31 30 29 28 
 .  .  .  .  . 33  .  .  .  . 

```

## test
`python3 -m unittest discover tests`