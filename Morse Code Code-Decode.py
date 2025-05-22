morseDict = {
    'a': '.-',
    'b': '-...',
    'c': '-.-.',
    'd': '-..',
    'e': '.',
    'f': '..-.',
    'g': '--.',
    'h': '....',
    'i': '..',
    'j': '.---',
    'k': '-.-',
    'l': '.-..',
    'm': '--',
    'n': '-.',
    'o': '---',
    'p': '.--.',
    'q': '--.-',
    'r': '.-.-',
    's': '...',
    't': '-',
    'u': '..-',
    'v': '...-',
    'w': '.--',
    'x': '-..-',
    'y': '-.--',
    'z': '--..',
    ' ': ' '  
    }




def code(userInput):
    userInput = userInput.lower()
    for i in userInput:
        print(morseDict[i], end=" ")



def decode(userInput):
    userList = userInput.split()
    for i in range(0, len(userList)):
        for j in morseDict:
            if(morseDict[j]==userList[i]):
                print(j, end=" ")
            else:
                continue


def userChoice():
    
    print("Hello Sir\n", "Welcome to Coding and Decoding Tool of Morse Code!\n", "If you prefer to code your words into Morse Code, Type '1' \n", "If you want to decode your Morse Code into wordings, Type '2' \n")
    userNeed = int(input("How do you want to proceed: "))
    if(userNeed==1):
        user1 = input("Enter your Words: ")
        print(code(user1))
    elif(userNeed==2):
        user2 = input("Enter your Morse Code: ")
        print(decode(user2))
    else:
        return "You failed to enter '1' or '2'"
    
print(userChoice())



