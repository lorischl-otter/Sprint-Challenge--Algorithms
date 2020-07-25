#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) The runtime complexity of this algorithm is O(n), or linear. Essentially, the algorithm is saying that while `a` (beginning at zero) is less than n^3, `a` will increment by n^2. And how many loops does it take to get from n^2 to n^3? n loops. So the runtime is exactly O(n).

b) The runtime complexity of this algorithm is O(n log n). The first for loop itself is O(n) runtime, because it iterates through each of `n` values. The while loop nested inside the for loop, however, is O(log n) runtime, because `j`, which is the value that compares to `n` to stop the loop, is doubled every loop, and the while loop only runs until `j` surprasses `n`.


c) The runtime complexity of this algorithm is simply O(n), or linear runtime, because even though it is a recursive function, it simply decreases the value of `n` by 1 with each iteration, until `n` is zero. (this is assuming that `bunnies` is the input equivalent of `n` the problem is asking about)

## Exercise II

Essentially, in order to solve this problem, I'm trying to search for the highest floor at which I can drop an egg that will not break. 

If I were just trying to minimize *broken* eggs, but not dropped eggs, I would just start at floor 1, and drop one egg off each floor until the egg broke. This would leave me with only one broken egg, but many dropped ones. This would be runtime O(n), because worst case scenario, you would have to loop through all floors.

As I interpret it, this question is also asking to minimize the number of dropped eggs. This is essentially equivalent to the exact purpose of a binary search -- how can we find the value we're searching for in the least amount of time? And since the floors are "sorted", this works perfectly. Unfortunately, we won't necessarily know when we've reached the correct floor until we've tried the floor above or below it, so the search will have to run in its entirety.

Given that this is a binary search implementation, the runtime would be O(log n).

Here's an example of pseudocode I would implement:

def egg_drop(stories, f):
    # start range at the first index, or first floor
    bottom = 0
    # top floor is the last index
    top = len(stories) - 1

    # loop through until f floor is found
    while bottom < top:
        # start in the middle floor
        mid = (top + bottom) // 2
        
        if egg doesn't break:
            # remove lower half & move to top half
            low = mid + 1
        
        if egg does break:
            # we've gone too high, and need to move  down
            high = mid - 1

    # once both top & bottom floor pointers are at the same floor, confirm whether we're on floor f (where the egg would break) or the floor below, and be sure to return f
    if bottom == top:
        if egg does break:
            return top
        if egg does not break:
            return top + 1

