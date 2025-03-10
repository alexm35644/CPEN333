Part 1:

As a possible solution to avoid deadlock, "our program as usual will spawn five processes to represent the five philosophers, but we only allow four philosophers to be sitting at the dining table (so to speak) to eat at any given time to limit the number of philosophers at the table. " 

You are to modify the code to implement the solution based on the above statement. Submit a .py file for this part (make sure your filename include part1).

Depending on your approach, you are allowed to add any additional synchronization primitives (only the ones we have discussed in class obviously) that you may need. But, don't use more than what is obsoletely necessary. If used, they must be defined in the main process and be passed to the child processes as one of the args elements for their use (e.g. similar to the chopstick semaphoreList). 

As usual, document very well your approach and reasoning by providing helpful comments.

=========================

Part 2:

We discussed that one possible solution to avoid deadlock is to "allow a philosopher to pick up her chopsticks only if both chopsticks are available".

You are to modify the code to implement the solution based on the above statement. Submit a .py file for this part (make sure your filename include part2).

Depending on your approach, you are allowed to add any additional synchronization primitives (only the ones we have discussed in class obviously) that you may need. But don't use more than what is obsoletely necessary. If used, they must be defined in the main process and be passed to the child processes as one of the args elements for their use (e.g. similar to the chopstick semaphoreList). 

As usual, document very well your approach and reasoning by providing helpful comments.

=========================

Part 3: 

We discussed that another possible solution to avoid deadlock is to "use an asymmetric solution, e.g. an odd philosopher picks up first her left chopstick and then her right chopstick, whereas an even philosopher picks up her right first and then her left chopstick".

You are to modify the code to implement the solution based on the above statement. Submit a .py file for this part (make sure your filename include part3).

As before, the philosophers are numbered 0 to 4, and for the philosopher id, her left chopstick is at index id, and her right chopstick is at (id+1)%5.  

========================

Notes and Hints:

Obviously, the shown sample output is just a possible sample.
Each philosopher does this circularly, that is, eat-think-eat-think-eat-think ... as long as the loop runs and under the synchronization constraints. 
A good starting point would be to identify what condition creates a deadlock in the original code and then examine that your solution (for either part) avoids deadlock.
The two inner functions are used solely for readability (so that the thinking state and the eating state stand out, instead of seeing the code used for simulating them). One can replace the function calls with the two liners in the body of those functions.
Use semaphores or locks only as specified (no other synchronization primitive), and only when needed. Make sure you are not using a method, property or function that is obsolete or platform-specific (as usual do check with the official python documentation).
For the marking, we check that the program works, has correct logic, follows the specs, and passes all our tests. The program should be readable (good choice of identifiers, acceptable structure and styling, useful comments wherever needed ...), and does not do any repetitive work or extra work unnecessarily. Write the best code you can.