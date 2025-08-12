

# Dictionary with empty values 
friends = {
    'harry' : '',
    'muneeb' : '',
    'hadi' : '',
    'salman' : '',
    'yash' : ''
}

# Now filling the dictionary with values 
for i in range(len(friends)):
    name = input("Enter name: ")
    friends[name] = input("Enter favorite language: ")
  

print(friends)


# As you see I have two same vales  so it is not avoided 