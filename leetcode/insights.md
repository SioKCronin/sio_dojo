# General Strategy
* What is the relationship between the problem and the sub-problem?
* What are units of measurement for measuring system efficiency?
* What patterns can you see in the mapping of input to output?
* What is your brain computer doing in solving the problem?
* If you know your brute force, what is the complexity below that? Does that
inspire a strategy? If you know your first idea is linear, how can you aim for
log n or constant time? What would be required?
* RE: Analysis - it was super helpful to question how common operations like sorted()
(which in Python uses Timsort, which is O(n log n) are implemented, as this
is what we have track when compiling complexity for a function. This is a great 
[quick reference](https://bradfieldcs.com/algos/analysis/performance-of-python-types/)

# Coding insights

* Don't make a list if your just going to use an iterator once
* If you're passing to a function like sum, why not just use [generator](http://book.pythontips.com/en/latest/generators.html)?

# Specific problems

## Pangram
* I learned about string.ascci_lowercase and s.lower() for all i.isalpha()
did most of my heavy lifting
* We discussed a bitwise solution that I'd like to explore further

## Hamming
* Knowing True = 1 allows us to check all pairs by index and sum up the 
the ones that are different
* I got stuck getting my try-except ValueError raising to register, and 
wasn't sure what was happening there

## Difference of Squares
* This one was funny, because in writing up a list comprehension to make 
sure I understood what was being asked, I solved the problem. I jumped the gun,
but it's a straightforward problem, so that's ok. 


