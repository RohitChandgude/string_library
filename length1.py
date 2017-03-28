#!/usr/bin/python

#function for finding length of string
def strlength(s):
    return 1 + strlength(s[1:]) if s else 0


#function for concat two strings.
def strconcat(str1, str2):
	str1 = str1 + " "
	for i in str2:
		str1 = str1 + i
	return str1

def lower(line1):
    g = ""
    for ch in line1:
        if ord (ch) >= 97 and ord(ch) <= 122:
            x = ord(ch) - 32
            y = chr (x)
            g = g + y
		
    return g
	
	

def up(line1):
    return ("".join(chr(ord(x)+('@'<x<'[')*32)for x in line1))

    #g = ""
    #for ch in line1:
        #if ord (ch) >= 65 and ord(ch) <= 90:
       #     x = ord(ch) + 32
      #      y = chr (x)
     #       g = g + y
	#return g
    #print g



#fuction to reverse a string

def reverse(text):
    if strlength(text) <= 1:
        return text

    return reverse(text[1:]) + text[0]
	
	
	
# function to find substring
def findSubstring(s, sub):
    start = 0
    end = 0
    while start < len(s):
        if s[start+end] != sub[end]:
            start += 1
            end = 0
            continue
        end += 1
        if end == len(sub):
            return start
    return -1
