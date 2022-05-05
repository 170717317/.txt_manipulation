def isValidIndex(value, usrlst):
    if (index - 1) >= 0 and (index - 1) < len(lst):
        return True
    return False

def printMenu():
    print('1. Print Integer Sequences')
    print('2. Print an Integer Sequence')
    print('3. Add a value to an Integer Sequence')
    print('4. Delete a value from an Integer Sequence')
    print('5. Modify a value from an Integer Sequence')
    print('6. Delete an Integer Sequence')
    print('7. Exit')


def readFromFile(filename):
    # filename = input('Enter File Name: ')
    handle = open(filename)
    global newlst
    newlst = []
    for x in handle:
        x = x.strip()
        new_x = x.split(' ')
        # print(new_x, type(new_x))
        newlst.append(new_x)
    # print(newlst)
    i = 0
    for lst in newlst:
        lst = list(map(int, lst))
        # here we replace each list within newlst with the variable above: lst
        newlst[i] = lst
        i += 1
    # print(newlst)


def printIntegerSequences(newlst):
    for lst in newlst:
        number = newlst.index(lst)
        number += 1
        # sequence = ''.join(map(str, lst))
        # for n in range(len(lst)):
        print(f"Sequence # {number}", '\n', *lst)        


def printIntegerSequenceInformation(newlst, seq_number):
    wlst = newlst[seq_number]
    neg_count = 0
    pos_count = 0
    for w in wlst:
        w = int(w)
        if w < 0:
            neg_count += 1
        elif w >= 0:
            pos_count += 1

    print(f"# of Values: {len(wlst)}")
    print(f"# Positive Values: {pos_count}")
    print(f"# Negative Values: {neg_count}")


def addValueToSequence(newlst, lst_pos, new_pos, new_int):
    new_seq = newlst[lst_pos]
    new_seq.insert(new_pos, new_int)


def removeValueFromSequence(newlst, del_seq, del_int):
    n_seq = newlst[del_seq]
    n_seq.pop(del_int)


def modifyValueFromSequence(newlst, mod_seq, pos_mod, value):
    sequence = newlst[mod_seq]
    sequence[pos_mod] = value

def removeSequence(newlst, del_seq):
    newlst.pop(del_seq)


filename = input('Enter the file name: ')
option = 0

while option != 7:
    printMenu()
    readFromFile(filename)
    option = int(input('Enter your option: '))
    if option == 1:
        print(printIntegerSequences(newlst))
    elif option == 2:
        seq_option = int(input('Enter the sequence number: ')) - 1
        print(printIntegerSequenceInformation(newlst, seq_option))
    elif option == 3:
        seq_option = int(input('Enter the sequence number: ')) - 1
        int_pos = int(input('Enter the position: ')) - 1     # subtract 1 if we are assuming the position we want to insert starts at 1 and not the index aka 0 if not remove -1
        new_value = int(input('Enter the value: '))
        print(addValueToSequence(newlst, seq_option, int_pos, new_value))
    elif option == 4:
        seq_option = int(input('Enter the sequence number: ')) - 1
        del_pos = int(input('Enter the position: ')) - 1    # subtract 1 if we are assuming the position we want to insert starts at 1 and not the index aka 0 if not remove -1
        print(removeValueFromSequence(newlst, seq_option, del_pos))
    elif option == 5:
        seq_option = int(input('Enter the sequence number: ')) - 1
        mod_pos = int(input('Enter the position: ')) - 1
        mod_val = int(input('Enter the value: '))
        print(modifyValueFromSequence(newlst, seq_option, mod_pos, mod_val))
    elif option == 6:
        seq_option = int(input('Enter the sequence number: ')) - 1
        print(removeSequence(newlst, seq_option))
