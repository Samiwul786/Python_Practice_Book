# -*- coding: utf-8 -*-
"""
Created on Thu May 26 18:08:44 2022
@author: smuss
"""
import os
import sys







    
    
def countries_greeting(country:str):
    print(f"Hello from {country}")

    
countries = ["UAE", "Palestine", "Turkey", "USA", "India", "Pakistan"]

for i in countries:
    countries_greeting(i)
    
# Problem: Parse all the countries declared in an array and only print the countries that contain the letter I or U   
for i in countries:
    if ("I" in i or "U" in i):
        print(i)

def markPercentage():
    percent = int(input("What percentage did that student get"))
    
    if(percent > 0 and percent < 100):
        
        if (percent < 50):
            print("You have achived a third class")

        elif (percent >= 50 and percent <= 59):
            print("You acheived a upper third class")
        
        elif(percent <= 69):
            print("You have acheived a 2:1")
        
        else: 
            print("You achieved a first class")
 
    else:
        print("You can only go to 0-100%")
     

        
def lastLetterVowel():
    countryName = input("Please type in a country name")
    countryName = countryName.lower()
    lastCharacter = countryName.strip()[-1]
    
    if ("a" in lastCharacter):
        print("Vowel found")
    elif("e" in lastCharacter):
        print("Vowel found")
    elif("i" in lastCharacter):
        print("Vowel found")
    elif("o" in lastCharacter):
        print("Vowel found")
    elif("u" in lastCharacter):
        print("Vowel found")
    else:
        print("No vowel was found")
    
def checkGreaterNumber(number1:int , number2:int):
        
    if (number1 > number2):
        return number1
    else:
        return number2

def checkLowerNumber(num1:int, num2:int):
    
    if (num1 < num2):
        return num1
    else:
        return num2

def checkStatement():
    
    count = 0
    
    while True:
        
        print(f"The count is {count}")        
        if count > 5:
            break
        count += 1
        
def uniqueNums(theList):
    
    new_nums = set(theList)
    new_nums_list = list(new_nums)
    
    print(new_nums_list)

def duplicateNums(theList):
    
    seen = set()
    
    dup = []
 
    for i in theList:
        
        if (i in seen):
            dup.append(i)
        else:
            seen.add(i)   
            
    print(dup)
           
 
print("The unique numbers are")    
uniqueNums([1,2,2,3,4,5,4,6,7])

print("The duplicate nums are")
duplicateNums([1,2,2,3,4,5,4,6,7])

print("The lowest number is", checkLowerNumber(5, 2))