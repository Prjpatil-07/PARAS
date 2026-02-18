new_string = "THIS IS A STRING"

new_string = new_string[::-1]   
print(new_string)

for i in range(len(new_string) -1, -1, -1):
    print(new_string[i], end="")

new_string = "".join(reversed(new_string)) 
print(new_string)   