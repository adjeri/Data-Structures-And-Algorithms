# Identify the base case
# Identify the recursive case
# Get closer and closer and return when needed. Usually you have 2 returns
counter = 0

def inception(count):
    if count > 3:
        return 'done'
    count += 1
    return inception(count)

print(inception(counter))