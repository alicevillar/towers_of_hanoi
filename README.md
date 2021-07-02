# Tower of Hanoi task - use of recursion

The Tower of Hanoi puzzle was invented by the French mathematician Edouard Lucas in 1883. There is some pattern to the puzzle and with each increment in disks. Thus, the pattern can be followed recursively. This repository contains an assignment from Module 3...

### Description 

One of the classic programming problems that is often solved by recursion is the towers of Hanoi problem. A good explanation and walkthrough are provided by Cormen & Balkcom (n.d.) - the link is in the reading list. (the code they used for their visual example is provided on their website as well).

* Read the explanation, study the code and then create your own version using Python (if you want to make it more interesting you can use asterisks to represent the disks). 
* Create a version that asks for the number of disks and then executes the moves, and then finally displays the number of moves executed.
* What is the (theoretical) maximum number of disks that your program can move without generating an error?
* What limits the number of iterations? What is the implication for application and system security?

### What is the game of Tower of Hanoi?

Tower of Hanoi consists of three pegs or towers with n disks placed one over the other.

The objective of the puzzle is to move the stack to another peg following these simple rules.

* Only one disk can be moved at a time.
* No disk can be placed on top of the smaller disk.

This is a classical example of Recursion (which happens when a function calls itself). Recursion is useful in solving problems which can be broken down into smaller problems of the same kind.

### Results 

In this repository, I have created a version of Tower of Hanoi using asterisks to represent the disks. The number of steps exponentially increases every time I insert another disk in the stack. While the 3-disk puzzle required 7 steps. 4-disk requires 7+1+7 = 15 steps to be solved. 

![print](disks&moves.PNG)


To move N disks from one peg to another, I need 2^N - 1. Thus, if N-1 > 1, then it's necessary to repeat this breakdown for smaller N until N-1 = 1. In short, the total number of moves required to solve the puzzle with N disks is 2^N - 1. 
 
### Resources:

* Levy, Uri. The Magnetic Tower of Hanoi. Available from: https://arxiv.org/ftp/arxiv/papers/1003/1003.0225.pdf

* Mishra, Arpit. Tower of Hanoi recursion game algorithm explained. Available from: https://www.hackerearth.com/blog/developers/tower-hanoi-recursion-game-algorithm-explained/

