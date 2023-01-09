import re;
string = "'HELLO MY FRIEND THIS IS HIMANSHU', he said. and he is Really a good person "
print(string)
string = string + "96 721 - 051 34"
new = re.sub('[^a-z,A-Z,0-9]',' ',string)
print(string)
print(new)