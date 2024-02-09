#REMOVE PASS AND FIX THIS FUNCTION
def palindrome(word):
    length = len(word)
    if (length % 2) == 0:
        half_length = int(length / 2)
    else:
        half_length = int((length - 1) / 2)
    front_index = 0
    back_index = length - 1
    for i in range(half_length):
        if word[front_index] == word[back_index]:
            continue
        else:
            return False
        front_index += 1
        back_index -= 1
    return True
        

    

if __name__ == '__main__': 
    #REMOVE PASS AND YOUR CODE GOES HERE
    user_input = input()
    print(palindrome(user_input))
