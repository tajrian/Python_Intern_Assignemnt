#alphaOnly is a function which will take a string as an input and remove everythings from that string without alphanumeric character .
import re

def alphaOnly(in_str):
  return re.sub(r'[^a-zA-Z0-9]', '', in_str)

if __name__ =="__main__":
   input_string =  "!~))cl__ea***n1__0=+1"
   print("Output String: ",alphaOnly(input_string))
   #Output String:  clean101
