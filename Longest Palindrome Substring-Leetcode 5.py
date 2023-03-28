'''
First we have to understand the problem statement of this question and then we will move to the solution.
We are given a certain string and we have to find the palindromic substring from the string with max length. 
Example: s="babad" and the longest palindromic substring in the given statement is "bab" of length=3. So we will return the substring.
Let's head to the solution part..

'''

#approach 1---> Extreme Naive
'''
we will be using two loops and iterate through the string. So we will find the max palindromic substring in O(n^3) with Constant Time however the approach is not very efficient and we can definitely do better than this"

'''
#approach 2--> Taking two pointers at the certain points and compare both the adjacent items whether they are similar or not. We will also take a variable that stores the length of the substring. Apart from this, we will declare an empty string that will store our final answer.

lass Solution:
    def longestPalindrome(self, s: str) -> str:
    res= ""
        resLen= 0
        for i in range(len(s)):
            # odd length
            l,r=i,i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1)>resLen:
                    res=s[l:r+1]
                    resLen=r-l+1
                l-=1
                r+=1
                # even lenght
            l,r=i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1)>resLen:
                    res=s[l:r+1]
                    resLen=r-l+1
                l-=1
                r+=1
        return res  
        
        
    
