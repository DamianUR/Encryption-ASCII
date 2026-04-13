"""The following methods are used for encryption:"""

def encrypt(base, msg_str):
    
    """This is the method called to encrypt a message into a string of numbers in a given base."""

    num_arr = scan_num_str(conv_to_ascii_string(msg_str)) #converts message into array containing ASCII code of each char
    num_arr = conv_arr_base(num_arr, base) #converts numbers in array into specified base
    return to_string(num_arr) #converts array to string of numbers separated by spaces and returns the string


def conv_to_ascii_string(s):

    """Returns a string replacing the characters of an inputted string with the ASCII value of it. """

    to_ret = ""
    s_len = len(s) - 1
    for c in range(s_len):
        to_ret = to_ret + str(ord(s[c])) + " "
    to_ret = to_ret + str(ord(s[s_len]))
    return to_ret


def conv_to_base(in_num, N):

    """Takes an integer, num, and converts it to its form in a specified base, N, and returns that as a string."""

    num = abs(int(in_num))
    num_vals = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ" #all the symbols for numbers in any base up to and incl. 36
    to_ret = ""
    temp = ""
    if num == 0:
        return "0"
    while not num == 0: #performs division section of base conversion
        mod = num % N
        temp = temp + num_vals[mod]
        num = num // N

    temp_len = len(temp)
    for i in range(1, temp_len + 1): #sets to_ret to the reverse of temp
        to_ret = to_ret + temp[temp_len - i]
    if int(in_num) < 0:
        to_ret = "-" + to_ret
    return to_ret


def conv_arr_base(arr, N):

    """Converts each integer element of an array to another base."""

    to_ret = arr
    for i in range(len(to_ret)):
        to_ret[i] = conv_to_base(to_ret[i], N)
    return to_ret


def to_string(arr):

    """Takes the elements of an array and outputs all of them in a string, with each element separated by a space."""

    to_ret = ""
    max_ele = len(arr) - 1
    for i in range(max_ele):
        to_ret = to_ret + arr[i] + " "
    to_ret = to_ret + arr[max_ele]
    return to_ret



"""The following methods are used for decryption:"""

def decrypt(base, num_str):

    """This method is called to decrypt a message encrypted using the encrypt() method's form of encryption."""

    arr = scan_num_str(num_str) #converts a string of numbers in any base into an array storing those numbers
    arr = conv_arr_to_dec(arr, base) #converts all the numbers in the array to base 10.
    to_ret = base10_arr_to_string(arr) #finds char corresponding to each array elements' ASCII code, and stores it in a string
    return to_ret


def conv_to_decimal(num_str, N):

    """Converts any positive integer in any base, up to base 36, to decimal."""

    num_vals = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    to_ret = 0
    num_len = len(num_str)
    for i in range(1, num_len + 1):
        dec_equiv = num_vals.index(num_str[num_len - i])
        to_ret += dec_equiv * (N**(i - 1))
    return to_ret


def conv_arr_to_dec(arr, arr_base):

    """Converts each element of an array containing integers in any base, up to base 36, to base 10."""

    to_ret = []
    for i in range(len(arr)):
        to_ret.append(conv_to_decimal(arr[i], arr_base))
    return to_ret


def base10_arr_to_string(arr):

    """Converts an array of base 10 integers into a string with characters using the ascii values of the integer elements."""
    
    to_ret = ""
    for i in arr:
        to_ret = to_ret + chr(i)
    return to_ret



"""The following methods are general methods:"""

def scan_num_str(num_str):

    """Takes a string containing numbers in any base seperated by spaces, stores each number 
    as an element of an array and outputs that array."""

    to_ret = []
    temp = ""
    for char in num_str:
        if char == " ":
            to_ret.append(temp)
            temp = ""
        else:
            temp = temp + char
    to_ret.append(temp)
    return to_ret



"""This is the main body of code:"""
print( "Do you want to encrypt or decrypt? Enter below:")
action = input()
print("Enter base of process (2-36): ", end="")
base = int(input())
print ("Enter the message below:")
string = input()
if action == "encrypt":
    print(encrypt(base, string))
elif action == "decrypt":
    print(decrypt(base, string))
    
# @ author: Udorilwela Ratshikhopha