## Loop Control Statements

## break - Stop the loop immediately

for i in range(1, 10):
    if i == 5:
        print("Stopping at 5") 
        break # stops at 5
    print(i)

## continue - skip the current round and go to next
print("")
for i in range(1, 6):
    if i == 3:
        continue # Skipped 3
    print(i)

## pass - ignore this for now, i will write later
for i in range(5):
    if i == 2:
        pass # maybe we will write somethind here later
    print(i)

# pass is just a placeholder. 
