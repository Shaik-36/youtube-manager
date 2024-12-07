# There are two methods to open a file.


# Method - 1
file = open('youtube.txt', 'w')

try:
    file.write('chai aur code')

finally:
    file.close()



# Method - 2 - Easy way
with open('youtube.txt', 'w') as file:
    file.write('chai aur python')

    