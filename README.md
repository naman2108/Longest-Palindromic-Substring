# Longest-Palindromic-Substring
In this question, we have to find the longest palindrome in a string. We will see the most optimal way to solve this question. The question is solved without using Dynamic Programming in the overall time-complexity of  O(n^2) and Space complexity of O(1). 
We could have solved this problem by multiple methods. For Instance, first approach is extreme Naive in which we iterate through the elements and use two loops. The time complexity would be O(n^3) with the space complexity of O(1). 
The another method is, we can use the two pointers technique in which we put both of our pointers at same place and compare adjecent elements whether they are equal or not. If they are equal. We will note down their maxLength along with storing the answer in the declared empty string initially.
--> One of the biggest edge case one can face in this approach is the length of String. We have to handle odd and even length cases with this approach however both are quite simple.
Odd Case: If length of the string is odd, we will put both of our pointers at same position.
Even Case: If length of the string is even, we will put one of our pointer at ith place and another pointer at i+1 place.
