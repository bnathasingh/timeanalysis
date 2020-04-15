"""
Module for implementing Lab 05 functions.

This module is broken up into to parts.  The first part contains two functions:
first_vowel and pigify. The first is a helper function of the second (which is the
primary function). The second function, pigify, convert English words to Pig-Latin.
You are to IMPLEMENT the second function.

The second part uses the Time class provided by the module time.  It contains a single
function: add_time.  You are to implement this function as well.

While you are encouraged to test your answers, you do not need to write  a unit test.
Simply demonstrate your functions to you instructor to get get credit

YOUR NAME AND NETID HERE
THE DATE COMPLETED HERE
"""
from clock import Time


# PART 1: Pig Latin

def first_vowel(w):
    """
    Returns: position of the first vowel; -1 if no vowels.

    There is a better way to do this function with for-loops,
    but we have not covered that topic yet.

    Parameter w: the word to search
    Precondition: w is a nonempty string with only lowercase letters
    """
    minpos = len(w) # invalid position; currently no vowels found

    # search for a
    pos = w.find('a')
    if pos != -1 and pos < minpos: # a found and is closest
        minpos = pos

    # search for e
    pos = w.find('e')
    if pos != -1 and pos < minpos: # e found and is closest
        minpos = pos

    # search for i
    pos = w.find('i')
    if pos != -1 and pos < minpos: # i found and is closest
        minpos = pos

    # search for o
    pos = w.find('o')
    if pos != -1 and pos < minpos: # o found and is closest
        minpos = pos

    # search for u
    pos = w.find('u')
    if pos != -1 and pos < minpos: # u found and is closest
        minpos = pos

    # search for y not at front
    pos = w.find('y',1)
    if pos != -1 and pos < minpos: # u found and is closest
        minpos = pos

    # found something if minpos moved from first assignment
    return minpos if minpos != len(w) else -1


def pigify(w):
    """
    Returns: copy of w converted to Pig Latin

    See the lab handout for the complete rules on Pig Latin.

    Parameter w: the word to change to Pig Latin
    Precondition: w is a nonempty string with only lowercase letters
    """
    pass # STUB. Implement me
    x = first_vowel(w)
    if x==0 :
        result= w+'hay'
    if w[0:2]=='qu' :
        qu = w[0:3]
        rest = w[3:]
        result= rest+qu+'ay'
    if x>0 :
        con = w[:x]
        rest = w[x:]
        result= rest+con+'ay'
    if x==-1:
        return w + 'ay'
    return result

# PART 2: Time

def add_time1(time1, time2):
    """
    Returns the sum of time1 and time2 as a new Time object

    DO NOT ALTER time1 or time2, even though they are mutable

    Examples:
        The sum of 12hr 13min and 13hr 12min is 25hr 25min
        The sum of 1hr 59min and 3hr 2min is 4hr 1min

    Parameter time1: the starting time
    Precondition: time1 is a Time object

    Parameter time2: the time to add
    Precondition: time2 is a Time object
    """
    pass # STUB. Implement me
    addhours= time1.hours + time2.hours
    addminutes = time1.minutes + time2.minutes
    if time1.minutes + time2.minutes > 60 :
        addhours += 1
        addminutes = addminutes - 60
    return Time(addhours, addminutes)


def add_time2(time1, time2):
    """
    Modifies time1 to be the sum of time1 and time2

    DO NOT RETURN a new time object. Modify the object time1 instead.

    Examples:
        The sum of 12hr 13min and 13hr 12min is 25hr 25min
        The sum of 1hr 59min and 3hr 2min is 5hr 1min

    Parameter time1: the starting time
    Precondition: time1 is a Time object

    Parameter time2: the time to add
    Precondition: time2 is a Time object
    """
    pass # STUB. Implement me
    addhours= time1.hours + time2.hours
    addminutes = time1.minutes + time2.minutes
    if time1.minutes + time2.minutes > 60 :
        addhours += 1
        addminutes = addminutes - 60
    time1= Time(addhours, addminutes)
