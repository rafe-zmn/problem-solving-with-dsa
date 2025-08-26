"""
Problem: Plus Minus
Difficulty: Easy
Platform: HackerRank (https://www.hackerrank.com/challenges/plus-minus/problem)

Time Complexity: O(n)  
Space Complexity: O(1)

Description:
Given an array of integers, calculate the ratios of its elements that are positive, 
negative, and zero. Print the decimal value of each fraction with 6 places after the decimal.

Example:
Input:  [1, 1, 0, -1, -1]
Output: 0.400000, 0.400000, 0.200000
"""

def plusMinus(arr):
    # Counters for positive, negative, and zero elements
    count_pos = 0
    count_neg = 0
    count_zero = 0
    total = len(arr)  # total elements in the array

    # Count positive, negative, and zero values
    for i in arr:
        if i < 0:
            count_neg += 1
        elif i > 0:
            count_pos += 1
        else:
            count_zero += 1
    
    # Return the ratios in formatted string with 6 decimal places
    return (f"{count_pos/total:.6f}, {count_neg/total:.6f}, {count_zero/total:.6f}")


# Example usage
arr = [1, 1, 0, -1, -1]
print(plusMinus(arr))
