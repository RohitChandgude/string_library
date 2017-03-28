#!/usr/bin/python
import length1

print "enter string to find length\n"

object=raw_input()

obj_len = length1.strlength(object)
print "length=",obj_len

print "enter string to make it upper case="
line2=raw_input()
lw=length1.lower(line2)
print "lower to upper=",lw
print "enter string in upper case to make it lower case="
line1=raw_input()
upper_Case = length1.up(line1)
print "upper to lower=",upper_Case

line2 = length1.reverse(line1)
print line2,"reverse"


string = length1.strconcat(object, line1)
print string,"concated string"

print "enter string to find substring or not\n"
string1 = raw_input()
print "enter substring to find\n"
string2 = raw_input()
result = length1.findSubstring(string1, string2)
print "found at=",result
