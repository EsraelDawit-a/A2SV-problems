if __name__ == '__main__':
    N = int(input())
    
    custom_list = []
    for i in range(N):
        command = input().split()
        if len(command) == 1:
            if command[0] == "print":
                print(custom_list)
            elif command[0] == "sort":
                custom_list.sort()
            elif command[0] == "pop":
                if custom_list:
                    custom_list.pop()
            elif command[0] == "reverse":
                custom_list = custom_list[::-1]
        else:
            # print(command)
            if command[0] == "insert":
                custom_list.insert(int(command[1]),int(command[-1]))
            elif command[0] == "remove":
                custom_list.remove(int(command[-1]))
            else:
                custom_list.append(int(command[-1]))
