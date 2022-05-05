OBJECTIVE

You will use your knowledge of functions, lists, and files to write a Python program that allows the user to manipulate the information from a list of integer sequences.

THE PROBLEM

Given the Python program provided in the template file, you must write the definition and implementation of the following user-defined functions:


isValidIndex (provided in the template file): this function receives the value of an index (integer) and the list that the user wants to access and returns a boolean value (True if the index is valid or False otherwise). For the user, a valid index value is between 1 and the size of the list.

printMenu (provided in the template file): this function does not receive any parameters and does not return a value. The function prints to STDOUT the following output messages
1. Print Integer Sequences
2. Print an Integer Sequence
3. Add a value to an Integer Sequence
4. Delete a value from an Integer Sequence
5. Modify a value from an Integer Sequence
6. Delete an Integer Sequence
7. Exit

readFromFile: this function receives as a parameter the filename (string). The function opens the input file using the parameter "filename". Each line of the input file represents an integer sequence. The format of the input file is as follows:
1 3 5 7 9 11
2 4 6 8
1 2 3 4 10 20 30 40 50
-1 -2 -3 -4 -5 -6
Each line has multiple integer values (positives and negatives, separated by a single white space) representing a sequence of numbers. The function creates a list of lists where each element of the list is a list that stores the information of an integer sequence (you must store each value in the sublists as integers). Finally, the function returns the list with all the integer sequences. Based on the previous input file, the list returned by the function is:

[[1, 3, 5, 7, 9, 11], [2, 4, 6, 8], [1, 2, 3, 4, 10, 20, 30, 40, 50], [-1, -2, -3, -4, -5, -6]]

printIntegerSequences: this function receives the list (list of lists) with the integer sequences and does not return a value. Given the previous input file, the function prints to STDOUT contents of the list of contacts using the following output messages (you must use the output messages presented below):
Sequence # 1
1 3 5 7 9 11 
Sequence # 2
2 4 6 8 
Sequence # 3
1 2 3 4 10 20 30 40 50 
Sequence # 4
-1 -2 -3 -4 -5 -6 

printIntegerSequenceInformation: this function receives as a parameter the list (list of integers) with an integer sequence and does not return any value. The function prints into STDOUT the following information (you must use the output messages presented below):
Values: 1 3 5 7 9 11 
# of Values: 6
# Positive Values: 6
# Negative Values: 0

addValueToSequence: this function receives as parameters the new element (integer) to be added to the sequence, the position (integer) where you want to add the new value (for this function, a valid position value is between 1 and the size of the sequence or -1 to add the value at the end of the sequence), and the list (list of integers) with the integer sequence.  This function does not return any value and inserts the new value in the selected integer sequence at the position specified by the user.

removeValueFromSequence: this function receives as parameters the position (integer) of the value you want to delete from the sequence (for this function, a valid position value is between 1 and the size of the sequence) and the list (list of integers) with the integer sequence.  This function does not return any value and removes the value from the selected integer sequence at the position specified by the user.

modifyValueFromSequence:  this function receives as parameters the value (integer) to be used to modify an element in the sequence, the position (integer) of the value in the sequence you want to modify (for this function, a valid position value is between 1 and the size of the sequence), and the list (list of integers) with the sequence of integers.  This function does not return any value and modifies the current value in the integer sequence at the position specified by the user with the value of the first parameter received by the function.

removeSequence: this function receives as a parameter the integer sequence number (integer) to be removed (for this function, a valid value for the integer sequence number is between 1 and the number of integer sequences) and the list (list of lists) with the integer sequences. This function does not return any value and removes the selected integer sequence from the list of sequences.
EXAMPLE:

Please note that the following example was produced using a desktop IDE, so the input is visible. In Moodle, the input will not be part of the program's output and therefore not visible.

Given the previous input file (input1.txt), the expected output of your program is:

Enter the file name: input1.txt

1. Print Integer Sequences
2. Print an Integer Sequence
3. Add a value to an Integer Sequence
4. Delete a value from an Integer Sequence
5. Modify a value from an Integer Sequence
6. Delete an Integer Sequence
7. Exit

Enter your option: 1
Sequence # 1
1 3 5 7 9 11 
Sequence # 2
2 4 6 8 
Sequence # 3
1 2 3 4 10 20 30 40 50 
Sequence # 4
-1 -2 -3 -4 -5 -6 

1. Print Integer Sequences
2. Print an Integer Sequence
3. Add a value to an Integer Sequence
4. Delete a value from an Integer Sequence
5. Modify a value from an Integer Sequence
6. Delete an Integer Sequence
7. Exit

Enter your option: 2
Enter the sequence number: 1
Values: 1 3 5 7 9 11 
# of Values: 6
# Positive Values: 6
# Negative Values: 0

1. Print Integer Sequences
2. Print an Integer Sequence
3. Add a value to an Integer Sequence
4. Delete a value from an Integer Sequence
5. Modify a value from an Integer Sequence
6. Delete an Integer Sequence
7. Exit

Enter your option: 3
Enter the sequence number: 1
Enter the position: 1
Enter the value: -1

1. Print Integer Sequences
2. Print an Integer Sequence
3. Add a value to an Integer Sequence
4. Delete a value from an Integer Sequence
5. Modify a value from an Integer Sequence
6. Delete an Integer Sequence
7. Exit

Enter your option: 2
Enter the sequence number: 1
Values: -1 1 3 5 7 9 11 
# of Values: 7
# Positive Values: 6
# Negative Values: 1

1. Print Integer Sequences
2. Print an Integer Sequence
3. Add a value to an Integer Sequence
4. Delete a value from an Integer Sequence
5. Modify a value from an Integer Sequence
6. Delete an Integer Sequence
7. Exit

Enter your option: 4
Enter the sequence number: 1
Enter the position: 1

1. Print Integer Sequences
2. Print an Integer Sequence
3. Add a value to an Integer Sequence
4. Delete a value from an Integer Sequence
5. Modify a value from an Integer Sequence
6. Delete an Integer Sequence
7. Exit

Enter your option: 2
Enter the sequence number: 1
Values: 1 3 5 7 9 11 
# of Values: 6
# Positive Values: 6
# Negative Values: 0

1. Print Integer Sequences
2. Print an Integer Sequence
3. Add a value to an Integer Sequence
4. Delete a value from an Integer Sequence
5. Modify a value from an Integer Sequence
6. Delete an Integer Sequence
7. Exit

Enter your option: 5
Enter the sequence number: 1
Enter the position: 6
Enter the value: 12

1. Print Integer Sequences
2. Print an Integer Sequence
3. Add a value to an Integer Sequence
4. Delete a value from an Integer Sequence
5. Modify a value from an Integer Sequence
6. Delete an Integer Sequence
7. Exit

Enter your option: 2
Enter the sequence number: 1
Values: 1 3 5 7 9 12 
# of Values: 6
# Positive Values: 6
# Negative Values: 0

1. Print Integer Sequences
2. Print an Integer Sequence
3. Add a value to an Integer Sequence
4. Delete a value from an Integer Sequence
5. Modify a value from an Integer Sequence
6. Delete an Integer Sequence
7. Exit

Enter your option: 6
Enter the sequence number: 1

1. Print Integer Sequences
2. Print an Integer Sequence
3. Add a value to an Integer Sequence
4. Delete a value from an Integer Sequence
5. Modify a value from an Integer Sequence
6. Delete an Integer Sequence
7. Exit

Enter your option: 1
Sequence # 1
2 4 6 8 
Sequence # 2
1 2 3 4 10 20 30 40 50 
Sequence # 3
-1 -2 -3 -4 -5 -6 

1. Print Integer Sequences
2. Print an Integer Sequence
3. Add a value to an Integer Sequence
4. Delete a value from an Integer Sequence
5. Modify a value from an Integer Sequence
6. Delete an Integer Sequence
7. Exit

Enter your option: 7


NOTES:

You can safely assume that the input will always be valid.
You can safely assume that the input file specified by filename will always exist in the Moodle server.
