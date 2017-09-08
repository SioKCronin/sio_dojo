# Emails

import Queue

q = Queue.PriorityQueue()

def store_message(message):
    q.put_nowait(message)

def return_message():
    try:
        item = q.get_nowait()
    except Queue.Empty:
        return "-1"
    return item[1]

def main():
    n = int(raw_input())
    for i in range(n):
        command = raw_input().strip().split(' ')
        if command[0] == 'store':
            store_message((-1 * int(command[2]), command[1]))
        elif command[0] == 'get_next_email':
            print return_message()

if __name__ == '__main__':
   main()
