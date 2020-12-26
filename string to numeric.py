# conver the input string to corresponding numric value
# Ex:- a/A =1 c/C =3......z/Z= 26
# # 96 to 122 lower
# # 65 to 90 capital

text = input("Enter The text")
a= text.replace(" ", "") 

for x in a:
    y=ord(x) 
    if y>=65 and y<=90:
        result =str(y-64)
    elif y>=96 and y<=122:
        result =str(y-96)
    print(result,end=" ")