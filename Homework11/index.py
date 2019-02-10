"""
Student code for Word Wrangler game
"""

import urllib2
import codeskulptor
import poc_wrangler_provided as provided

WORDFILE = "assets_scrabble_words3.txt"


# Functions to manipulate ordered word lists

def remove_duplicates(list1):
    """
    Eliminate duplicates in a sorted list.

    Returns a new sorted list with the same elements in list1, but
    with no duplicates.

    This function can be iterative.
    """
    tample = [float('inf')]
    for elem in list1:
        if elem in tample:
            continue
        tample.append(elem)    
    return tample[1:]

def intersect(list1, list2):
    """
    Compute the intersection of two sorted lists.

    Returns a new sorted list containing only elements that are in
    both list1 and list2.

    This function can be iterative.
    """
    new_list = []
    if len(list1) > len(list2):
        max_list = list1
        min_list = list2
    else:
        max_list = list2
        min_list = list1
        
    for elem in max_list:
        if elem in min_list:
            new_list.append(elem)
    return new_list

# Functions to perform merge sort

def merge(list1, list2):
    """
    Merge two sorted lists.

    Returns a new sorted list containing those elements that are in
    either list1 or list2.

    This function can be iterative.
    """   
    res =[]
    index_i , index_j = 0, 0
    while index_i < len(list1) and index_j < len(list2):
        if list1[index_i] <= list2[index_j]:
            res.append(list1[index_i])
            index_i+= 1
        else:
            res.append(list2[index_j])
            index_j+= 1
    res+= list1[index_i:]
    res+= list2[index_j:]
    return res	
                
def merge_sort(list1):
    """
    Sort the elements of list1.

    Return a new sorted list with the same elements as list1.

    This function should be recursive.
    """
    if len(list1) <= 1:
        return list1
    left = merge_sort(list1[:len(list1)/2])
    right = merge_sort(list1[len(list1)/2:])
    return merge(left,right)

# Function to generate all strings for the word wrangler game

def gen_all_strings(word):
    """
    Generate all strings that can be composed from the letters in word
    in any order.

    Returns a list of all strings that can be formed from the letters
    in word.

    This function should be recursive.
    """
    if word == '':
        return ['']
    else:
        first = word[0]
        rest = word[1:]
        rest_strings = gen_all_strings(rest)
        all_words = []
        for string in rest_strings:
            for leter in range(len(string)+1):
                all_words.append(string[0:leter]+first+string[leter:])
                
        return rest_strings + all_words        

# Function to load words from a file

def load_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
    return []

def run():
    """
    Run game.
    """
    words = load_words(WORDFILE)
    wrangler = provided.WordWrangler(words, remove_duplicates, 
                                     intersect, merge_sort, 
                                     gen_all_strings)
    provided.run_game(wrangler)

# Uncomment when you are ready to try the game
# run()

    
    