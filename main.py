
from Sintactic import Sintactic
from Lexical import Lexical
import sys
class Compiler:
    def printSymbolTable(self,symbolTable):
        i=0
        while i < len(symbolTable):
            print( str(i) +"---" + str(symbolTable[i]))
            i= i+1
            
    #For the printing of the list items, it detects the type of the list item and prints the item based on this type.
    def printTokenTable(self,tokens):
        for item in tokens:
            if type(item) == list:
                print("<" + str(item[0]) +"," + str(item[1])+">", end= " ")
            else:
                print("<" + str(item)+">", end= " ")
    
if __name__ == "__main__":
    
    analyzerLexical = Lexical()
    #sets the document to a string
    with open('test.txt', 'r') as file:
        data = file.read().replace('\n', ' ')
    
    #calls the lexical analyzer class, sending it to call the function that returns the list of tokens and the list of symbols, 
    # in case that when analyzing the list there is one of the errors, it interrupts the execution and prints the error.
    try:
        tokens2 = analyzerLexical.main_lexical(data)
        Symboltable = analyzerLexical.symbolTable
        print("SymbolTable")
        Compiler().printSymbolTable(Symboltable)
        print("TokenTable")
        Compiler().printTokenTable(tokens2)
        
    except Exception as error:
        print(error)

        
    #calls the sintactic analyzer class, sending as parameters the s the list of tokens and the list of symbols
    try:
      analyzerSintactic = Sintactic(tokens2,Symboltable) 
    except Exception as error:
        print(error)
    #analyzerSintactic = Sintactic(tokens2,Symboltable) 

    

    
         





       
