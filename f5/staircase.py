'''
Created on Oct 4, 2015

@author: ljiang
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT

def draw_staircase(height):
    i = 1
    line = ""
    while i <= height:
        j = 1
        while j <= height - i:
            line += ' '
            j += 1
        x = 1
        while x <= i:
            line += '#'
            if x == height:
                break
            if x == i:
                line += '\n'
            x +=1
        i += 1
    print line
  
 
