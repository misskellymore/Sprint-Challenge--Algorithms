#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(log(n)) - As the size of the input increases, the runtime or space used will grow at a slightly slower rate than O(1). O(log n) is the second best solution.


b) O(n^c) - Nested loops. As the size of the input increases, the runtime used will grow quickly and is not scalable.


c) O(c^n) - As the size of the input increases, the runtime or space used will grow at a much faster rate; O(c^n) is inefficient 

## Exercise II

U - inputs: eggs, n

    outputs: value of f

    topic: Algo

    relationship: if eggs are thown off floor >= f break.Else don't.

    expectations: determine the value of f, so that everytime an egg is thrown, the number of times eggs break will be minimized

P - tools: if/else, <>=!, break, while

    how to use: make it so that we only break one egg while trying to find the value of f with if/else

    tools for conditional: if n >= f break or return to 0 or ground floor

    steps: 
    1. start at ground floor
    2. make a conditional 
    3. make conditional return the value of f once egg breaks


E - Pseudo code: 
Building height is 10 floors
Begin on the ground floor, throw 1 egg.
Climb 1 floor, throw one egg.
Repeat this until an egg breaks
once egg breaks, return value of f

R - Problem is Linear O(n). Perhaps can make it better by using binary search O(log n) and begin starting to throw eggs halfway up the building, but exercise's goal was to make the number of broken eggs as minimal as possible. Starting halfway up could increase the number of broken eggs












