

# Dictionary with empty values 
friends = {
    'harry' : '',
    'muneeb' : '',
    'shahrukh' : '',
    'salman' : '',
    'yash' : ''
}

# Now filling the dictionary with values 
for i in range(len(friends)):
    name = input("Enter name: ")
    friends[name] = input("Enter favorite language: ")
  

print(friends)