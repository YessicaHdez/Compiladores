from os import error
from re import I, S
import sys
'''
This class was created based on the calculation previously performed with First plus on the established grammar, 
each function was created based on a grammar and they are called based on these.

'''
class Sintactic:
    #Start of the class, the initial values are established and the first call to run the code
    def __init__(self,tokenList,symbolTable):
        self.current = 0
        sys.setrecursionlimit(5000)
        self.tokensList = tokenList
        self.simbols = symbolTable
        self.tokensList.append('$')
        print("")
        print(tokenList)
        self.declaration_list()
        
        if self.tokensList[self.current] == '$':
            print("LA COMPILACION FUE ACEPTADA")
            
        else: 
            raise Exception("Error: $")
        
        self.printSimbolTable(self.simbols) 
    

    def printSimbolTable(self,simbols):
        for item in simbols:
            if type(item) == list:
                print( item, end= " ")
            else:
                print(item, end= " ")

    #Function in charge of verifying that the tokens are the corresponding ones based on what is established, otherwise it gives an error.
    def Match(self,terminal):
        if type(self.tokensList[self.current]) == list:
            if self.tokensList[self.current][0] == terminal:
                self.current += 1
            else:
                print(self.tokensList[self.current])
                print(terminal)
                raise Exception("Error: waiting for", terminal)
        else:
            if terminal == self.tokensList[self.current]:
                self.current += 1
            else: 
                raise Exception("Error: waiting for", terminal)
  
    #Functions in charge of the first grammar, all with their respective names, used for the generation of statements and their distinction
    def declaration_list(self):
        if self.tokensList[self.current] == 'int' or  self.tokensList[self.current] == 'void':
           self.declaration()
           self.declaration_list_prime()
        else:
            raise Exception("Error: bad start")

    def declaration_list_prime(self):
        if self.tokensList[self.current] == 'int' or self.tokensList[self.current] == 'void' :
           self.declaration()
           self.declaration_list_prime()
        elif  self.tokensList[self.current] == '$':
            return
        else:
            raise Exception("Error: bad start declaration or final")
    
    def declaration(self):
        if self.tokensList[self.current] == 'int' :
            if self.tokensList[self.current+2] == '(':
                self.fun_declaration()
            elif (self.tokensList[self.current +2] =='[' or self.tokensList[self.current +2] ==';'):
                self.var_declaration()      
        elif self.tokensList[self.current] == 'void':
            self.fun_declaration()
        else:
            raise Exception("Error: bad declaration")

    def var_declaration(self):
        if self.tokensList[self.current] == 'int' :
          # id = self.tokensList[self.current+1]
          # print(id)
          # if list == type(self.tokensList[self.current]):
          #      self.simbols[id[1]] == [self.tokensList[self.current],"var"]
           self.Match('int')
           self.Match('id')
           self.var_declaration2()
        else:
            raise Exception("Error: var declaration")

    def var_declaration2(self):
        if self.tokensList[self.current] == ';' :
            self.Match(';')
        elif self.tokensList[self.current] == '[' :
           self.Match('[')
           self.Match('num')
           self.Match(']')
           self.Match(';')
        else:
            raise Exception("Error: bad var declaration")

    def fun_declaration(self):
        if self.tokensList[self.current] == 'int' or self.tokensList[self.current] == 'void':
           self.current +=1 #type specifier
           #id = self.tokensList[self.current+1]
           #print(id)
           #if list == type(self.tokensList[self.current]):
           #     self.simbols[id[1]] == [self.tokensList[self.current],"fun"]
           self.Match('id')
           self.Match('(')
           self.params()
           self.Match(')')
           self.compound_stmt()
        else:
            raise Exception("Error: bad fun declaration")
    
        
    def local_declarations_prime(self):
        if self.tokensList[self.current] == 'int':
            self.var_declaration()
            self.local_declarations_prime()
        elif type(self.tokensList[self.current]) == list:
            if  self.tokensList[self.current][0] == 'id':
                return
        elif  self.tokensList[self.current] == '{' or self.tokensList[self.current] == 'if'  or  self.tokensList[self.current] == 'while' or  self.tokensList[self.current] == 'return' or self.tokensList[self.current] == 'input' or self.tokensList[self.current] == 'output':
            return
        #AQUI 
        elif  self.tokensList[self.current] == '}':
            return
        else:
            raise Exception("Error: bad local declaration")
    
    # Functions in charge of the first grammar, all with their respective names, used for the generation of params and their distinction
    def params(self):
        if self.tokensList[self.current] == 'int' :
           self.param_list()
        elif self.tokensList[self.current] == 'void' :
           self.Match('void')
        else:
            raise Exception("Error: bad defined param, missing type")
    
    def param_list(self):
        if self.tokensList[self.current] == 'int' :
           self.param()
           self.param_list_prime()
        else:
            raise Exception("Error: bad writed params")

    def param_list_prime(self):
        if self.tokensList[self.current] == ',' :
           self.Match(',')
           self.param()
           self.param_list_prime()
        elif self.tokensList[self.current] == ')' :
            return
        else:
            raise Exception("Error: bad writed param")
    
    def param(self):
        if self.tokensList[self.current] == 'int' :
           self.Match('int')
           self.Match('id')
           self.param2()
        else:
            raise Exception("Error: var bad defined")

    def param2(self):
        if self.tokensList[self.current] == '[' :
           self.Match('[')
           self.Match(']')
        elif self.tokensList[self.current] == ',' or self.tokensList[self.current] == ')':
            return
        else:
            raise Exception("Error: bad writed param")

    #Functions that represent the grammar of operators.
    def relop(self):
        if self.tokensList[self.current] == '<=' :
            self.Match('<=')
        elif self.tokensList[self.current] == '<' :
            self.Match('<')
        elif self.tokensList[self.current] == '>' :
            self.Match('>')
        elif self.tokensList[self.current] == '>=' :
            self.Match('>=')
        elif self.tokensList[self.current] == '==' :
            self.Match('==')
        elif self.tokensList[self.current] == '!=' :
            self.Match('!=')
        else:
            raise Exception("Error: missing symbol")

    def addop(self):
        if self.tokensList[self.current] == '+' :
            self.Match('+')
        elif self.tokensList[self.current] == '-' :
            self.Match('-')
        else:
            raise Exception("Error: missing arithmetic symbol")

    def mulop(self):
        if self.tokensList[self.current] == '*' :
            self.Match('*')
        elif self.tokensList[self.current] == '/' :
            self.Match('/')
        else:
            raise Exception("Error: missing arithmetic symbol")

    #Function with factor logic
    def factor(self):
        if self.tokensList[self.current] == '(' :
            self.Match('(')
            self.arithmetic_expression()
            self.Match(')')
        elif type(self.tokensList[self.current]) == list :
            if self.tokensList[self.current][0] == 'id' :
                if self.tokensList[self.current+1] == '(':
                    self.call()
                else:
                    self.var()
            elif self.tokensList[self.current][0] == 'num':
                self.Match('num')
        else:
            raise Exception("Error: bad writed factor")
    
    #Function with call logic
    def call(self):
        if type(self.tokensList[self.current]) == list :
            if self.tokensList[self.current][0] == 'id' :
                self.Match('id')
                self.Match('(')
                self.args()
                self.Match(')')
            else:
                raise Exception("Error: missig id")
        else:
                raise Exception("Error:  missig value")

    #FFunctions with arguments logic
    def args(self):
        if type(self.tokensList[self.current]) == list :
            if self.tokensList[self.current][0] == 'id' or self.tokensList[self.current][0] == 'num'  :
                self.args_list()
            else:
                raise Exception("Error: missing value")
        elif self.tokensList[self.current] == '(' :
            self.args_list()
        elif self.tokensList[self.current] == ')' :
            return
        else:
            raise Exception("Error: bad defined args")

    def args_list(self):
        if type(self.tokensList[self.current]) == list :
            if self.tokensList[self.current][0] == 'id' or self.tokensList[self.current][0] == 'num' :
                self.arithmetic_expression()
                self.args_list_prime()
            else:
                raise Exception("Error: missing value")
        elif self.tokensList[self.current] == '(' :
            self.arithmetic_expression()
            self.args_list_prime()
        else:
            raise Exception("Error: bad started args")

    def args_list_prime(self):
        if self.tokensList[self.current] == ',' :
            self.Match(',')
            self.arithmetic_expression()
            self.args_list_prime()
        elif self.tokensList[self.current] == ')' :
            return
        else:
            raise Exception("Error: bad definided args")
    #Functions with term logic
    def term(self):
        if self.tokensList[self.current] == '(' :
            self.factor()
            self.term_prime()
        elif type(self.tokensList[self.current]) == list :
            if self.tokensList[self.current][0] == 'id' or self.tokensList[self.current][0] == 'num' :
                self.factor()
                self.term_prime()
            else:
                raise Exception("Error: bad termn expression")
        else:
            raise Exception("Error: bad start termn")
    
    def term_prime(self):
        if self.tokensList[self.current] == '*' or  self.tokensList[self.current] == '/' :
            self.mulop()
            self.factor()
            self.term_prime()
        elif self.tokensList[self.current] == '+' or self.tokensList[self.current] == '-'  or self.tokensList[self.current] == ']' or self.tokensList[self.current] == '<=' or self.tokensList[self.current] == '<' or self.tokensList[self.current] == '>'  or self.tokensList[self.current] == '>='  or self.tokensList[self.current] == '=='  or self.tokensList[self.current] == '!='  or self.tokensList[self.current] == ';'  or self.tokensList[self.current] == ')'  or self.tokensList[self.current] == ',':
            return
        else:
            raise Exception("Error: missing symbol termn")

    #Functions with arithmetic logic
    def arithmetic_expression(self):
        if self.tokensList[self.current] == '(':
            self.term()
            self.arithmetic_expression_prime()
        elif type(self.tokensList[self.current]) == list :
            if self.tokensList[self.current][0] == 'id' or self.tokensList[self.current][0] == 'num':
                self.term()
                self.arithmetic_expression_prime()
            else:
                raise Exception("Error: bad writed arithmetic expression")
        else:
            raise Exception("Error: bad writed arithmetic expression")

    def arithmetic_expression_prime(self):
        if self.tokensList[self.current] == '+' or  self.tokensList[self.current] == '-' :
            self.addop()
            self.term()
            self.arithmetic_expression_prime()
        elif self.tokensList[self.current] == ']' or self.tokensList[self.current] == '<=' or self.tokensList[self.current] == '<' or self.tokensList[self.current] == '>'  or self.tokensList[self.current] == '>='  or self.tokensList[self.current] == '=='  or self.tokensList[self.current] == '!='  or self.tokensList[self.current] == ';'  or self.tokensList[self.current] == ')'  or self.tokensList[self.current] == ',':
            return
        else:
            raise Exception("Error: missing symbol ")

 #Functions with variables logic
    def var(self):
        if type(self.tokensList[self.current]) == list :
            if self.tokensList[self.current][0] == 'id':
                self.Match('id')
                self.var2()
            else:
                raise Exception("Error: missing id")
        else:
                raise Exception("Error: bad defined variable")
    
    def var2(self):
        if self.tokensList[self.current] == '[':
            self.Match('[')
            self.arithmetic_expression()
            self.Match(']')
        elif self.tokensList[self.current] == '='  or self.tokensList[self.current] == '/' or self.tokensList[self.current] == '*' or self.tokensList[self.current] == '+' or self.tokensList[self.current] == '-'  or self.tokensList[self.current] == ']' or self.tokensList[self.current] == '<=' or self.tokensList[self.current] == '<' or self.tokensList[self.current] == '>'  or self.tokensList[self.current] == '>='  or self.tokensList[self.current] == '=='  or self.tokensList[self.current] == '!='  or self.tokensList[self.current] == ';'  or self.tokensList[self.current] == ')'  or self.tokensList[self.current] == ',':
            return
        else:
            raise Exception("Error: missing symbol")
    
 #Functions with expresions logic
    def expression(self):
        if type(self.tokensList[self.current]) == list :
            if self.tokensList[self.current][0] == 'id' or self.tokensList[self.current][0] == 'num':
                self.arithmetic_expression()
                self.expression2()
            else:
                raise Exception("Error: en la compilacion")
        elif self.tokensList[self.current] == '(':
            self.arithmetic_expression()
            self.expression2()
        else:
                raise Exception("Error: bad defined expresion")

    def expression2(self):
        if self.tokensList[self.current] == '<=' or self.tokensList[self.current] == '<' or self.tokensList[self.current] == '>' or self.tokensList[self.current] == '>=' or self.tokensList[self.current] == '==' or self.tokensList[self.current] == '!=':
            self.relop()
            self.arithmetic_expression()

        elif self.tokensList[self.current] == ')'  or self.tokensList[self.current] == ';' :
            return
        else:
            raise Exception("Error: bad defined expression")
     
    #Functions with statements logic
    def compound_stmt(self):
        if self.tokensList[self.current] == '{' :
            self.Match('{')
            self.local_declarations_prime()
            self.statement_list_prime()
            self.Match('}')
        else:
            raise Exception("Error: missing { ")
    
    def return_stmt(self):
        if self.tokensList[self.current] == 'return' :
            self.Match('return')
            if self.tokensList[self.current] == ';' :
                self.Match(';')
            elif self.tokensList[self.current] == '(':
                self.expression()
                self.Match(';')
            elif type(self.tokensList[self.current]) == list :
                if self.tokensList[self.current][0] == 'id' or self.tokensList[self.current][0] == 'num':  
                    self.expression()
                    self.Match(';')
                else:
                    raise Exception("Error: missing expression")
            else:
                raise Exception("Error: bad defined return statment ")
        else:
            raise Exception("Error: bad return statment, return is missing")
            
    
    def statement_list_prime(self):
        if type(self.tokensList[self.current]) == list :
            if self.tokensList[self.current][0] == 'id' :
                self.statement()
                self.statement_list_prime()
            else:
                raise Exception("Error: bad declarated statemen ")
        elif self.tokensList[self.current] == '{' or self.tokensList[self.current] == 'return' or self.tokensList[self.current] == 'if' or self.tokensList[self.current] == 'while' or self.tokensList[self.current] == 'input' or self.tokensList[self.current] == 'output' :
            self.statement()
            self.statement_list_prime()
        elif self.tokensList[self.current] == '}':
            return
        elif self.tokensList[self.current] == ';':
            self.Match(";")
            self.statement()
            self.statement_list_prime()
        else:
            raise Exception("Error: bad declarated statement")
        
    def assignment_stmt(self):
        if type(self.tokensList[self.current]) == list :
            if self.tokensList[self.current][0] == 'id' :
                self.var()
                if self.tokensList[self.current] == '=' :
                    self.Match('=')
                else: 
                    raise Exception("Error: bad assignment, missig =")
                self.expression()
                if self.tokensList[self.current] == ';' :
                    self.Match(';')
                else: 
                    raise Exception("Error: bad assignment missing ;")
                
            else:
                raise Exception("Error: bad assignment, num instead of id")
        else:
            raise Exception("Error: bad assignment, is not an assignment")
    
    def selection_stmt(self): 
        if self.tokensList[self.current] == 'if' :
            self.Match('if')
            self.Match('(')
            self.expression()
            self.Match(')')
            self.statement()
            self.selection_stmt2()
        else:
            raise Exception("Error: bad if statment")

    def selection_stmt2(self):
        if self.tokensList[self.current] == 'else' :
            self.Match('else')
            self.statement()
        elif type(self.tokensList[self.current]) == list:
            if self.tokensList[self.current][0] == 'id':
                return
        elif self.tokensList[self.current] == 'else' or self.tokensList[self.current] == 'return' or self.tokensList[self.current] == '{' or self.tokensList[self.current] == '}'or self.tokensList[self.current] == 'if' or self.tokensList[self.current] == 'while' or self.tokensList[self.current] == 'input' or self.tokensList[self.current] == 'output' :
            return
        else:
            raise Exception("Error: bad else statement")
    
    def statement(self):
        if self.tokensList[self.current] == '{' :
            self.compound_stmt()
        elif self.tokensList[self.current] == 'if' :
            self.selection_stmt()
        elif self.tokensList[self.current] == 'while' :
            self.Match('while')
            self.Match('(')
            self.expression()
            self.Match(')')
            self.statement()
        elif self.tokensList[self.current] == 'return' :
            self.return_stmt()
        elif self.tokensList[self.current] == 'input' :
            self.Match('input')
            self.var()
            self.Match(';')
        elif self.tokensList[self.current] == 'output' :
            self.Match('output')
            self.expression()
            self.Match(';')
        elif type(self.tokensList[self.current]) == list:
            if self.tokensList[self.current][0] == 'id' :
                if self.tokensList[self.current+1] == '(':
                   self.call()
                elif self.tokensList[self.current+1] == '=' or self.tokensList[self.current+1] == '[' :
                    self.assignment_stmt()
                else:
                    raise Exception("Error: bad assignment")
        else:
            raise Exception("Error: bad start statement ")
