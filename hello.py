msg= "Hello, World!"
print(msg)
msg.capitalize()
print(msg)
msg = msg.split()
print(msg)

name = "The BodyGuard"
name

## Regular string 

regular_string = "C:\new_folder\file.txt"
print("Regular String:", regular_string)

## Raw string 

regular_string = r"C:\new_folder\file.txt"
print("Regular String:", regular_string)


# Replace the old substring with the new target substring is the segment has been found in the string

a = "The BodyGuard is the best album"
b = a.replace('BodyGuard', 'Janet')
print(b)


print(~(~2), end = None)

def validate_temperature(reading): 
    if 20 <= reading <= 40: 
        result = "Valid" 
    else: 
        result = "Invalid" 
    return result

print(validate_temperature(30))