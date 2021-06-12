import re
"""
This class contains the logic to perform the analysis. 
The implemented code is strongly based on the designed automaton,
 it runs through the program received for each char and defines a state, 
 based on each state it will add tokens and symbols to their corresponding list. 
"""
class Lexical:
    #Initializes the lists of tokens, symbol table, keywords, and special keywords, with their respective values.
    def __init__(self):
        self.keyword = ["int", "if", "void","else", "while", "input", "output", "return"] 
        self.specialSymbol = ["!",";", ",", "=", "+", "-", "*", "/", "(", ")", "[", "]", "{", "}", "<", ">" ]
        #A list is used for tokens and symbols since these are ordered and flexible elements that will support the program to store complex elements.
        self.tokens = []
        self.symbolTable = []
        
    def main_lexical(self, textCode): 
        #the string is traversed and the initial and variable states are set.
        state = 0
        index = 0
        sizeProgram = len(textCode)
        while index<sizeProgram: 
            #The states that raise errors are defined, each with the reason for the error
            if state == 29:
                raise Exception('no acceptable Symbol')
            if state == 30:
                raise Exception("Error: Comentary not closed")

            #The initial state it defines the new state depending of the char 
            if state == 0:
                #calls the defineType function 
                charType = self.defineType(textCode[index])
             
                if charType == "letter":
                    state = 1
                elif charType == "digit":
                    state = 2
                elif charType == "specialSymbol":
                    state = 3
                elif charType == "blank":
                    index = index + 1
                else:
                    state = 29
            #The first state is for letter characters since id can be composed of one or more characters,
            # this state is saving each character with the help of a while to form the word
            if state == 1:
                word = textCode[index]
                while state == 1:
                    index = index+1
                    charType = self.defineType(textCode[index])
                    #Is checked if it exists within the reserved words, if it does, it is introduced into the token table to maintain the order, 
                    # otherwise, it is checked for its existence in the symbol table
                    if charType != "letter":
                        if word not in self.keyword:
                            #The existence of the character in the table is checked, if it does not exist, it is added to the list as a new element 
                            if word not in self.symbolTable:
                                key = len(self.symbolTable)
                                if key != 0:
                                    key = key-1 
                                self.symbolTable.append(word)
                                self.tokens.append(["id", key])
                            else: 
                                #its index is obtained to avoid repetition and it is added to the token table
                                key = self.symbolTable.index(word)
                                self.tokens.append(["id", key])
                        else: 
                            self.tokens.append(word)
                        state = 0
                    else:
                        word = word + textCode[index]
            #State 2, which manages the digits, similar to state 1, is used a while that runs through the string until 
            # a character does not match and saves the final number.
            #   once the number is checked it is automatically saved in both tables.
            if state == 2:
                num = textCode[index]
                while state == 2:
                    index = index+1
                    charType = self.defineType(textCode[index])
                    if charType != "digit":
                        key = len(self.symbolTable)
                        self.symbolTable.append(num)
                        self.tokens.append(["num", key])
                        state = 0
                    else:
                        num = num + textCode[index]
            #State 3 is defined to manage how the program will process some of the symbols
            if state == 3:
                #Since there are two possibilities with the / symbol, it checks the next element and if it meets the conditions of a comment,
                #  it is treated like this and activates state 4
                if textCode[index] == "/":
                    if textCode[index+1] == "*":
                        index = index +2
                        state = 4
                    else: 
                        self.tokens.append(textCode[index+1])
                        index = index +1
                        state= 0
                #! symbol is not accepted as a symbol only,
                #  it is checked if it meets the conditions to become an accepted state, an error is raised otherwise
                elif textCode[index] == "!": 
                    if textCode[index+1] == "=":
                        self.tokens.append(textCode[index] + textCode[index+1])
                        index = index +2
                        state =0
                    else: 
                        state = 29   

                elif textCode[index] == "<": 
                    if textCode[index+1] == "=":
                        self.tokens.append(textCode[index] + textCode[index+1])
                        index = index +2
                        state =0
                    else: 
                        self.tokens.append(textCode[index])
                        index = index +1
                        state=0
                elif textCode[index] == ">": 
                    if textCode[index+1] == "=":
                        self.tokens.append(textCode[index] + textCode[index+1])
                        index = index +2
                        state =0
                    else: 
                        self.tokens.append(textCode[index])
                        index = index +1
                        state=0
                elif textCode[index] == "=": 
                    if textCode[index+1] == "=":
                        self.tokens.append(textCode[index] + textCode[index+1])
                        index = index +2
                        state =0
                    else: 
                        self.tokens.append(textCode[index])
                        index = index +1
                        state=0
                else:
                #if the symbol does not represent any of the two previous cases, it is added to the token table
                    self.tokens.append(textCode[index])
                    index = index +1
                    state=0
            #State 4 represents when we are inside a comment, it checks the characters in search of the closing of the comment, 
            # in case of reaching the end of the file without finding a suitable closing raise an error
            if state == 4:
                if index == sizeProgram-1:
                    state = 30
                elif textCode[index] == "*":
                    if textCode[index + 1] == "/":
                        index = index +2
                        state = 0
                    else:
                        index = index +1
                else:
                    index = index +1
        return self.tokens
            
    #based on the received element it uses regex to define the element based on what is specified in the document and returns the type, 
    # in the case of being an unrecognized character it will return an error type
    def defineType(self,character):
        
        letter = re.findall("[a-zA-Z]", character)
        digit = re.findall("[0-9]", character)
        if letter:
            return "letter"
        elif digit:
            return "digit"
        elif character == " ":
            return "blank"
        elif character in self.specialSymbol:
            return "specialSymbol"
        else: 
            return "error"
      