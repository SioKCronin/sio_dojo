# Emails
storage = {}
max_urgency = 0

def store_message(message, urgency):
    global max_urgency
    max_urgency = max(max_urgency, urgency)
    if urgency in storage:
        storage[urgency].append(message)
    else:
        storage[urgency] = [message]

def return_message():
    global max_urgency
    if len(storage) == 0:
        return "-1"
    return_value = storage[max_urgency].pop(0)
    if storage[max_urgency] == []:
        del storage[max_urgency]
        if len(storage) > 0:
            max_urgency = max(storage.keys())
    return return_value

def main():
    n = int(raw_input())
    for i in range(n):
        command = raw_input().strip().split(' ')
        if command[0] == 'store':
            store_message(command[1], int(command[2]))
        elif command[0] == 'get_next_email':
            print return_message()

if __name__ == '__main__':
   main()
