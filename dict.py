d = {}
while True:
    action = input("Add name by 'a', retrive by 'r' and 'q' to quit: ").lower()
    
    if action == 'a':
        name = input("Enter a name: ")
        
        if name[0].lower() not in d:
            d[name[0].lower()] = []
        
        d[name[0].lower()].append(name)
        print(d)
        
    elif action == 'r':
        letter = input("Enter key retrieve names: ").lower()
        
        if letter in d:
            print(f"Names starting with '{letter}': {d[letter]}")
        else:
            print(f"Not found  '{letter}'.")
            
    elif action == 'q':
        print("End program")
        break
        
    else:
        print("Invalid option, please choose 'a', 'r', or 'q': ")



