"""
Problem: Given a list of integers representing the height of candles, 
         find how many of them are the tallest.
Difficulty: Easy
Source: [HackerRank - Birthday Cake Candles] (https://www.hackerrank.com/challenges/birthday-cake-candles/problem?isFullScreen=true)
Time Complexity: O(n)
Space Complexity: O(1)
"""

candles = [4, 4, 1, 3]

def birthdayCakeCandles(candles):
    find_tallest = max(candles) #step 1: find the tallest candle
    count = 0
    
    for i in candles: # step 2: loop through each candles
        if i == find_tallest: #step 3: if the candle matches the tallest, increse count
            count += 1 
          
    return count #step 4: returing how many tallest candle are there

print(birthdayCakeCandles(candles))  # Output: 2
