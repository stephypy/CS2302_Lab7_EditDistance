# CS 2302 Data Structures: MW 1:30PM - 2:50PM
# Author: Stephanie Galvan
# Assignment: Lab 7 - Edit Distance
# Instructor: Diego Aguirre
# TA: Gerardo Barraza
# Date of last modification: December 2, 2019
# Purpose: Implement Edit Distance Algorithm

from lab7.EditDistance import ED


def test_cases():
    ed = ED()
    # Test Case 1: Normal Behavior
    print('Test Case 1: Normal Behavior')
    ans = ed.edit_distance('miner', 'money')  # Expected = 2
    print('miner, money = ', ans, '\n')

    # Test Case 2: Empty Strings
    print('Test Case 2: Empty Strings')
    ans = ed.edit_distance('', '')  # Expected = 0
    print(' ,  = ', ans, '\n')

    # Test Case 3: S1 Longer than S2
    print('Test Case 3: S1 longer than S2')
    ans = ed.edit_distance('seahorse', 'ears')  # Expected = 4
    print('seahorse, ears = ', ans, '\n')

    # Test Case 4: S2 longer than S1
    print('Test Case 4: S2 longer than S1')
    ans = ed.edit_distance('river', 'unriveting')  # Expected = 6
    print('river, unriveting = ', ans, '\n')

    # Test Case 5: Exact Same Strings
    print('Test Case 5: Exact Same Strings')
    ans = ed.edit_distance('phoenix', 'phoenix')  # Expected = 0
    print('phoenix, phoenix = ', ans, '\n')

    # Test Case 6: Completely Different Strings (same length)
    print('Test Case 6: Completely Different Strings (same length)')
    ans = ed.edit_distance('pounds', 'camper')  # Expected = 6
    print('pounds, camper = ', ans)


def main():
    test_cases()


main()
