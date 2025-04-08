# CMPS 2200 Assignment 3
## Answers

**Name:**Zev Gaslin


Place all written answers from `assignment-03.md` here for easier grading.

1a)
The greedy algorithm works by continuously choosing the largest coin in the bank that is less than the remaining amount. then it subtracts that coins value from the total and repeats the process with the remaining amount until the remaining amount is zero. 

1b)
Greedy Choice Property:
This algorithm always selects the largest coin denomination that does not exceed the current amount. 
Proof that this greedy choice is optimal: In this currency system, each coin is exactly double the value of the next smaller denomination. If we were to replace one large coin with smaller denominations, we would need at least two smaller coins to match the value of the one larger coin. This increases the total number of coins used. Since we're trying to minimize the number of coins, replacing one coin with multiple smaller ones takes more coins, not less. Therefore, choosing the largest coin available at each step leads to an optimal result.


Optimal Substructure Property:
The problem fits the optimal substructure because an optimal solution for amount T can be made up from the optimal solution to the subproblem T1 = T - 2^k, where 2^k is the largest coin less than or equal to T. If the greedy choice gives the best result for T1, then adding the coin 2^k to it yields the best result for T. Since this reasoning applies recursively at each step, the full sequence of greedy choices builds up to an optimal solution.


2a. Greedy doesn't work for this becuase if for example the bank offerse $1, $4 and $5 and youre trying to make $8 with the least ammount of coins, greedy choice would pick the $5 first adn then have to pick 3 $1 coins, whereas if you picked 2 $4 coins you would use less coins. 
2b. The optimal substrucutre property means that a problem can be solved most efficianlty by brekaing it iunto smaller sub problems and solving each of those sub probelems individualy.
In this problem, you can start at 1 and work up to the number youre lookign for N, finidng the way of making each number with the least amount of coins as you go. For example if you were trying to get N = 5 and the bank has D of [1,2,4] you can make a table of the amount of change it takes to make each number from 1 up until your number N. you then have a list of the most optimal way of finding any number N built up of the most optimal ways of finding the smaller numbers, so your way of making N coins will be the most optimal one

2c. Make an array a of N+1 size
Set a[0] = 0
for i from 1->N:
  for c (each type of coin in the bank):
    if i -c >= 0: //so you dont use negative values of the table a
      a[i] = min(a[i], 1 + a[i-c]) // if the currect solution for making i value in the table a isn't the minimu, it will uptade it to be the mimium solution of making the value 1c less than i + the one additional coin c to get you to the value i. becuase we do this on every value i, the number in table a to get i-c is the minimum number, so the value of coins to get i will also be the minimum number

    we do this for every number until we reach N, so we get the minimum number for n


  In this function we loop through the outter for loop N times, and the inner for loop c times (once for each type of coins), so the work is O(N*C). We need to check the minimum value of each N value sequetially, so span is O(N)    