# -*- coding: utf-8 -*-
"""
runfile('C:/Users/Charles_Truscott/Desktop/newpalinctwt.py', wdir='C:/Users/Charles_Truscott/Desktop')
All letters should presumably match from 0 to 18
All letters should presumably match from 1 to 17
All letters should presumably match from 2 to 16
All letters should presumably match from 3 to 15
All letters should presumably match from 4 to 14
All letters should presumably match from 5 to 13
All letters should presumably match from 6 to 12
All letters should presumably match from 7 to 11
All letters should presumably match from 20 to 28
All letters should presumably match from 21 to 27
All letters should presumably match from 22 to 26
Authored by Charles Truscott Watters from scratch finishing up at 7:53 a.m. 6/06/2022 Australian Eastern Standard Time
Thank you so much MIT for allowing me to do a unit from the world's #1 ranked college in Computer Science and also Mathematics
Thank you edX.org staff
List of Found Palindromes (case sensitive): [['None ever reve enoN'], ['one ever reve eno'], ['ne ever reve en'], ['e ever reve e'], [' ever reve '], ['ever reve'], ['ver rev'], ['er re'], ['Also oslA'], ['lso osl'], ['so os']]
Enjoyed my HarvardX Study which is still valuable to this day ...
I'm going to be a Python software engineer one day :-D

"""
def match_and_mix(list_of_letter_matches_and_positions, string_input):
    list_of_consecutive_numbers = []
    presumed = []
    for entry in list_of_letter_matches_and_positions:
        if entry[2] >= entry[1]:
            for q in range(entry[2], entry[1] - 1, -1):
                list_of_consecutive_numbers.append(q)
        presumed += [list_of_consecutive_numbers]
        list_of_consecutive_numbers = []
#    for remove_empties in range(0, len(presumed)):
#        if presumed[remove_empties] == []:
#            presumed[remove_empties] = "\x00"
    print(presumed)
    presumed_two = presumed

 #   for entry in presumed:
 #       print(entry[0:len(entry)])
 #       for new_entry in presumed_two:
 #           if entry.__contains__(new_entry) and entry != new_entry:
 #               print(entry)
     #   for new_entry in presumed_two:
 #           if entry[0:len(entry)] == new_entry[0:len(new_entry)]:
 #               print(entry, new_entry)

#    for numerical_range in presumed:
#        for second_numerical_range in numerical_range:
#            print(second_numerical_range)
            
 #       for x in range(0, len(string_input), 1):
  #          for y in range(len(string_input) - 1, 0, -1):
                
#        if list_of_letter_matches_and_positions[[]
def find_palindrome(string_input):
    found_palindromes = []
    first_match = False
    matches = []
    Found_Negation = False
    Found_Error = False
    for x in range(0, len(string_input), 1):
        for y in range(len(string_input) - 1, 0, -1):
           #print("{} {}".format(string_input[x], string_input[y]))
           if string_input[x] is string_input[y] and x is not y:
               # Are all letters below these two values matching
               q = x
               r = y
               temp1 = x
               temp2 = y
               for n in range(q, r, 1):
                   if string_input[q] == string_input[r] and q is not r:
                       Found_Negation = False
                   else:
                       Found_Negation = True
                   q += 1
                   r -= 1
               if Found_Negation == False:
                   print("All letters should presumably match from {} to {}".format(temp1, temp2))
                   found_palindromes.append([string_input[temp1:temp2 + 1]])
                   break
               matches += [[string_input[x], x, y]]
    return found_palindromes


def main():                
    string = "None ever reve enoN Also oslA"
    found_palindromes = find_palindrome(string)
    print("Authored by Charles Truscott Watters from scratch finishing up at 7:53 a.m. 6/06/2022 Australian Eastern Standard Time")
    print("Thank you so much MIT for allowing me to do a unit from the world's #1 ranked college in Computer Science and also Mathematics")
    print("Thank you edX.org staff")
    print("List of Found Palindromes (case sensitive): {}".format(found_palindromes))

if __name__ == "__main__": main()