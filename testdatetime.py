import re,os
import sys

#filename = input("filename: ")

filename = "showq.txt"
whatYouSay = (input("enter a text to be saved in the file \n"))

with open(filename, "a+") as f: #the a+ will append the data and it will create a file if there is no existing file already
  f.write(str(whatYouSay)+'\n')
