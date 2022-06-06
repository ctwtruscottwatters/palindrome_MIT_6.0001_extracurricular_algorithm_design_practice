# -*- coding: utf-8 -*-
"""
runfile('C:/Users/Charles_Truscott/Desktop/CharlesTruscottWattersExtraCurricularMITAlgorithmPractice.py', wdir='C:/Users/Charles_Truscott/Desktop')
All letters should presumably match from 0 to 14
All letters should presumably match from 1 to 13
All letters should presumably match from 2 to 12
All letters should presumably match from 3 to 11
All letters should presumably match from 4 to 10
All letters should presumably match from 5 to 9
All letters should presumably match from 6 to 39
All letters should presumably match from 7 to 38
All letters should presumably match from 15 to 61
All letters should presumably match from 16 to 60
All letters should presumably match from 17 to 29
All letters should presumably match from 18 to 72
All letters should presumably match from 19 to 27
All letters should presumably match from 20 to 26
All letters should presumably match from 21 to 25
All letters should presumably match from 22 to 39
All letters should presumably match from 23 to 38
All letters should presumably match from 27 to 72
All letters should presumably match from 29 to 47
All letters should presumably match from 30 to 46
All letters should presumably match from 31 to 70
All letters should presumably match from 32 to 44
All letters should presumably match from 33 to 43
All letters should presumably match from 34 to 42
All letters should presumably match from 35 to 41
All letters should presumably match from 36 to 40
All letters should presumably match from 44 to 71
All letters should presumably match from 45 to 61
All letters should presumably match from 46 to 60
All letters should presumably match from 47 to 59
All letters should presumably match from 48 to 58
All letters should presumably match from 49 to 57
All letters should presumably match from 50 to 56
All letters should presumably match from 51 to 55
All letters should presumably match from 56 to 59
All letters should presumably match from 57 to 58
All letters should presumably match from 58 to 57
All letters should presumably match from 59 to 56
All letters should presumably match from 60 to 46
All letters should presumably match from 61 to 70
All letters should presumably match from 62 to 78
All letters should presumably match from 63 to 77
All letters should presumably match from 64 to 76
All letters should presumably match from 65 to 75
All letters should presumably match from 66 to 74
All letters should presumably match from 67 to 73
All letters should presumably match from 68 to 72
All letters should presumably match from 71 to 72
Authored by Charles Truscott Watters from scratch finishing up at 7:53 a.m. 6/06/2022 Australian Eastern Standard Time
Thank you so much MIT for allowing me to do a unit from the world's #1 ranked college in Computer Science and also Mathematics
Thank you edX.org staff
List of Found Palindromes (case sensitive): [['Charles SelrahC'], ['harles Selrah'], ['arles Selra'], ['rles Selr'], ['les Sel'], ['es Se'], ['s SelrahC Watters Srettaw Thomas S'], [' SelrahC Watters Srettaw Thomas '], [' Watters Srettaw Thomas Samoht Wallace eCaLlAw '], ['Watters Srettaw Thomas Samoht Wallace eCaLlAw'], ['atters Sretta'], ['tters Srettaw Thomas Samoht Wallace eCaLlAw Truscott TT'], ['ters Sret'], ['ers Sre'], ['rs Sr'], ['s Srettaw Thomas S'], [' Srettaw Thomas '], ['ttaw Thomas Samoht Wallace eCaLlAw Truscott TT'], ['aw Thomas Samoht Wa'], ['w Thomas Samoht W'], [' Thomas Samoht Wallace eCaLlAw Truscott '], ['Thomas Samoht'], ['homas Samoh'], ['omas Samo'], ['mas Sam'], ['as Sa'], ['t Wallace eCaLlAw Truscott T'], [' Wallace eCaLlAw '], ['Wallace eCaLlAw'], ['allace eCaLlA'], ['llace eCaLl'], ['lace eCaL'], ['ace eCa'], ['ce eC'], ['aLlA'], ['Ll'], [''], [''], [''], [' Truscott '], ['Truscott TTOCSURT'], ['ruscott TTOCSUR'], ['uscott TTOCSU'], ['scott TTOCS'], ['cott TTOC'], ['ott TTO'], ['tt TT'], ['TT']]

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
    spaces = 0
    for x in range(0, len(string_input), 1):
        for y in range(len(string_input) - 1, 0, -1):
           #print("{} {}".format(string_input[x], string_input[y]))
           if str(string_input[x].lower()) == str(string_input[y].lower()) and x is not y:
               # Are all letters below these two values matching
               q = x
               r = y
               temp1 = x
               temp2 = y
               for n in range(q, r, 1):
                   if str(string_input[q].lower()) == str(string_input[r].lower()) and q is not r:
                       Found_Negation = False
                   else:
                       Found_Negation = True
                   if string_input[x] == str(" "):
                       spaces += 1
                       if string_input[y] == str(" "):
                           spaces += 1
                           
                   q += 1
                   r -= 1
               if Found_Negation == False:
                   print("All letters should presumably match from {} to {}".format(temp1, temp2))
                   if spaces % 2 == 0:
                       found_palindromes.append([string_input[temp1:temp2 + 1]])
                       spaces = 0
                       break
               matches += [[string_input[x], x, y]]
    return found_palindromes


def main():                
    string = "Charles SelrahC Watters Srettaw Thomas Samoht Wallace eCaLlAw Truscott TTOCSURT"
    found_palindromes = find_palindrome(string)
    print("Authored by Charles Truscott Watters from scratch finishing up at 7:53 a.m. 6/06/2022 Australian Eastern Standard Time")
    print("Thank you so much MIT for allowing me to do a unit from the world's #1 ranked college in Computer Science and also Mathematics")
    print("Thank you edX.org staff")
    print("List of Found Palindromes (case sensitive): {}".format(found_palindromes))

if __name__ == "__main__": main()