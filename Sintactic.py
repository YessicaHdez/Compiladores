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
        self.declaration_list()
        
        if self.tokensList[self.current] == '$':
            print("LA COMPILACION FUE ACEPTADA")
        else: 
            raise Exception("Error: $")

    #Function in charge of verifying that the tokens are the corresponding ones based on what is established, otherwise it gives an error.
    def Match(self,terminal):
        if type(self.tokensList[self.current]) == list:
            if self.tokensList[self.current][0] == terminal:
                self.current += 1
            else:
                
                print(self.tokensList[self.current])
                print(terminal)
                raise Exception("Error: $")
        else:
            if terminal == self.tokensList[self.current]:
                self.current += 1
            else: 
                raise Exception("Error: $")
  
    #Functions in charge of the first grammar, all with their respective names, used for the generation of statements and their distinction
    def declaration_list(self):
        if self.tokensList[self.current] == 'int' or  self.tokensList[self.current] == 'void':
           self.declaration()
           self.declaration_list_prime()
        else:
            print("error1")
            raise Exception("Error: n la compilacion")

    def declaration_list_prime(self):
        if self.tokensList[self.current] == 'int' or self.tokensList[self.current] == 'void' :
           self.declaration()
           self.declaration_list_prime()
        elif  self.tokensList[self.current] == '$':
            return
        else:
            print("error2")
            raise Exception("Error: en la compilacion")
    
    def declaration(self):
        if self.tokensList[self.current] == 'int' :
            if self.tokensList[self.current+2] == '(':
                self.fun_declaration()
            elif (self.tokensList[self.current +2] =='[' or self.tokensList[self.current +2] ==';'):
                self.var_declaration()      
        elif self.tokensList[self.current] == 'void':
            self.fun_declaration()
        else:
            print("error3")
            raise Exception("Error: en la compilacion")

    def var_declaration(self):
        if self.tokensList[self.current] == 'int' :
           self.Match('int')
           self.Match('id')
           self.var_declaration2()
        else:
            print("error5")
            raise Exception("Error: en la compilacion")

    def var_declaration2(self):
        if self.tokensList[self.current] == ';' :
            self.Match(';')
        elif self.tokensList[self.current] == '[' :
           self.Match('[')
           self.Match('num')
           self.Match(']')
           self.Match(';')
        else:
            print("error6") 
            raise Exception("Error: en la compilacion")

    def fun_declaration(self):
        if self.tokensList[self.current] == 'int' or self.tokensList[self.current] == 'void':
           self.current += 1 #type specifier
           self.Match('id')
           self.Match('(')
           self.params()
           self.Match(')')
           self.compound_stmt()
        else:
            print("error8") 
            raise Exception("Error: en la compilacion")
    
    def local_declarations(self):
        if  self.tokensList[self.current] == 'output' or self.tokensList[self.current] == 'input' or self.tokensList[self.current] == 'return'  or self.tokensList[self.current] == 'while' or self.tokensList[self.current] == 'if' or self.tokensList[self.current] == '{'  or self.tokensList[self.current] == 'int':
            self.local_declarations_prime()
        elif type(self.tokensList[self.current]) == list:
            if  self.tokensList[self.current][0] == 'id':
                self.local_declarations_prime()
        else:
            print("error15") 
            raise Exception("Error: en la compilacion")
        
    def local_declarations_prime(self):
        if self.tokensList[self.current] == 'int':
            self.var_declaration()
            self.local_declarations_prime()
        elif type(self.tokensList[self.current]) == list:
            if  self.tokensList[self.current][0] == 'id':
                return
        elif self.tokensList[self.current] == '}'or  self.tokensList[self.current] == '{' or self.tokensList[self.current] == 'if'  or  self.tokensList[self.current] == 'while' or  self.tokensList[self.current] == 'return' or self.tokensList[self.current] == 'input' or self.tokensList[self.current] == 'output':
            return
        else:
            print("error16")
            raise Exception("Error: en la compilacion")
    
    # Functions in charge of the first grammar, all with their respective names, used for the generation of params and their distinction
    def params(self):
        if self.tokensList[self.current] == 'int' :
           self.param_list()
        elif self.tokensList[self.current] == 'void' :
           self.Match('void')
        else:
            print("error9") 
            raise Exception("Error: en la compilacion")
    
    def param_list(self):
        if self.tokensList[self.current] == 'int' :
           self.param()
           self.param_list_prime()
        else:
            print("error10") 
            raise Exception("Error: en la compilacion")

    def param_list_prime(self):
        if self.tokensList[self.current] == ',' :
           self.Match(',')
           self.param()
           self.param_list_prime()
        elif self.tokensList[self.current] == ')' :
            return
        else:
            print("error11") 
            raise Exception("Error: en la compilacion")
    
    def param(self):
        if self.tokensList[self.current] == 'int' :
           self.Match('int')
           self.Match('id')
           self.param2()
        else:
            print("error12") 
            raise Exception("Error: en la compilacion")

    def param2(self):
        if self.tokensList[self.current] == '[' :
           self.Match('[')
           self.Match(']')
        elif self.tokensList[self.current] == ',' or self.tokensList[self.current] == ')':
            return
        else:
            print("error13") 
            raise Exception("Error: en la compilacion")

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
            print("error17")
            raise Exception("Error: en la compilacion")

    def addop(self):
        if self.tokensList[self.current] == '+' :
            self.Match('+')
        elif self.tokensList[self.current] == '-' :
            self.Match('-')
        else:
            print("error18")
            raise Exception("Error: en la compilacion")

    def mulop(self):
        if self.tokensList[self.current] == '*' :
            self.Match('*')
        elif self.tokensList[self.current] == '/' :
            self.Match('/')
        else:
            print("error19")
            raise Exception("Error: en la compilacion")

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
            print("error20")
            raise Exception("Error: en la compilacion")
    
    #Function with call logic
    def call(self):
        if type(self.tokensList[self.current]) == list :
            if self.tokensList[self.current][0] == 'id' :
                self.Match('id')
                self.Match('(')
                self.args()
                self.Match(')')
            else:
                print("error 21")
                raise Exception("Error: en la compilacion")
        else:
                print("error 22")
                raise Exception("Error: en la compilacion")

    #FFunctions with arguments logic
    def args(self):
        if type(self.tokensList[self.current]) == list :
            if self.tokensList[self.current][0] == 'id' or self.tokensList[self.current][0] == 'num'  :
                self.args_list()
            else:
                print("error 21")
                raise Exception("Error: en la compilacion")
        elif self.tokensList[self.current] == '(' :
            self.args_list()
        elif self.tokensList[self.current] == ')' :
            return
        else:
            print("error23")
            raise Exception("Error: en la compilacion")

    def args_list(self):
        if type(self.tokensList[self.current]) == list :
            if self.tokensList[self.current][0] == 'id' or self.tokensList[self.current][0] == 'num' :
                self.arithmetic_expression()
                self.args_list_prime()
            else:
                print("error 21")
                raise Exception("Error: en la compilacion")
        elif self.tokensList[self.current] == '(' :
            self.arithmetic_expression()
            self.args_list_prime()
        else:
            print("error23")
            raise Exception("Error: en la compilacion")

    def args_list_prime(self):
        if self.tokensList[self.current] == ',' :
            self.Match(',')
            self.arithmetic_expression()
            self.args_list_prime()
        elif self.tokensList[self.current] == ')' :
            return
        else:
            print("error23")
            raise Exception("Error: en la compilacion")
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
                print("error som")
                raise Exception("Error: en la compilacion")
        else:
            print("prblema")
            raise Exception("Error: en la compilacion")
    
    def term_prime(self):
        if self.tokensList[self.current] == '*' or  self.tokensList[self.current] == '/' :
            self.mulop()
            self.factor()
            self.term_prime()
        elif self.tokensList[self.current] == '+' or self.tokensList[self.current] == '-'  or self.tokensList[self.current] == ']' or self.tokensList[self.current] == '<=' or self.tokensList[self.current] == '<' or self.tokensList[self.current] == '>'  or self.tokensList[self.current] == '>='  or self.tokensList[self.current] == '=='  or self.tokensList[self.current] == '!='  or self.tokensList[self.current] == ';'  or self.tokensList[self.current] == ')'  or self.tokensList[self.current] == ',':
            return
        else:
            print("errorskjd")
            raise Exception("Error: en la compilacion")
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
                print("kljdaslkja")
                raise Exception("Error: en la compilacion")
        else:
            print("errorskjd")
            raise Exception("Error: en la compilacion")

    def arithmetic_expression_prime(self):
        if self.tokensList[self.current] == '+' or  self.tokensList[self.current] == '-' :
            self.addop()
            self.term()
            self.arithmetic_expression_prime()
        elif self.tokensList[self.current] == ']' or self.tokensList[self.current] == '<=' or self.tokensList[self.current] == '<' or self.tokensList[self.current] == '>'  or self.tokensList[self.current] == '>='  or self.tokensList[self.current] == '=='  or self.tokensList[self.current] == '!='  or self.tokensList[self.current] == ';'  or self.tokensList[self.current] == ')'  or self.tokensList[self.current] == ',':
            return
        else:
            print("errorskjd")
            raise Exception("Error: en la compilacion")

 #Functions with variables logic
    def var(self):
        if type(self.tokensList[self.current]) == list :
            if self.tokensList[self.current][0] == 'id':
                self.Match('id')
                self.var2()
            else:
                print("varError2")
                raise Exception("Error: en la compilacion")
        else:
                print("varError")
                raise Exception("Error: en la compilacion")
    
    def var2(self):
        if self.tokensList[self.current] == '[':
            self.Match('[')
            self.arithmetic_expression()
            self.Match(']')
        elif self.tokensList[self.current] == '='  or self.tokensList[self.current] == '/' or self.tokensList[self.current] == '*' or self.tokensList[self.current] == '+' or self.tokensList[self.current] == '-'  or self.tokensList[self.current] == ']' or self.tokensList[self.current] == '<=' or self.tokensList[self.current] == '<' or self.tokensList[self.current] == '>'  or self.tokensList[self.current] == '>='  or self.tokensList[self.current] == '=='  or self.tokensList[self.current] == '!='  or self.tokensList[self.current] == ';'  or self.tokensList[self.current] == ')'  or self.tokensList[self.current] == ',':
            return
        else:
            print("errorskjd")
            raise Exception("Error: en la compilacion")
    
 #Functions with expresions logic
    def expression(self):
        if type(self.tokensList[self.current]) == list :
            if self.tokensList[self.current][0] == 'id' or self.tokensList[self.current][0] == 'num':
                self.arithmetic_expression()
                self.expression2()
            else:
                print("expressionERROR ")
                raise Exception("Error: en la compilacion")
        elif self.tokensList[self.current] == '(':
            self.arithmetic_expression()
            self.expression2()
        else:
                print("ERROR ")
                raise Exception("Error: en la compilacion")

    def expression2(self):
        if self.tokensList[self.current] == '<=' or self.tokensList[self.current] == '<' or self.tokensList[self.current] == '>' or self.tokensList[self.current] == '>=' or self.tokensList[self.current] == '==' or self.tokensList[self.current] == '!=':
            self.relop()
            self.arithmetic_expression()

        elif self.tokensList[self.current] == ')'  or self.tokensList[self.current] == ';' :
            return
        else:
            print("errorskjd")
            raise Exception("Error: en la compilacion")
     
    #Functions with statements logic
    def compound_stmt(self):
        if self.tokensList[self.current] == '{' :
            self.Match('{')
            self.local_declarations()
            self.statement_list()
            self.Match('}')
        else:
            print("compound_stmterror") 
            raise Exception("Error: en la compilacion")
    
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
                    print("error som")
                    raise Exception("Error: en la compilacion")
            else:
                print("errorreturn2")
                raise Exception("Error: en la compilacion")
        else:
            print("errorreturn")
            raise Exception("Error: en la compilacion")
            
    def statement_list(self):
        if type(self.tokensList[self.current]) == list :
            if self.tokensList[self.current][0] == 'id' :
                self.statement()
                self.statement_list_prime()
            else:
                print("statementListERROR2")
                raise Exception("Error: en la compilacion")
        elif  self.tokensList[self.current] == '{' or self.tokensList[self.current] == 'if' or self.tokensList[self.current] == 'while' or self.tokensList[self.current] == 'input' or self.tokensList[self.current] == 'output' :
            self.statement()
            self.statement_list_prime()

        elif self.tokensList[self.current] == '}':
            self.statement_list_prime()
        else:
                print("statementListERROR")
                raise Exception("Error: en la compilacion")
    
    def statement_list_prime(self):
        if type(self.tokensList[self.current]) == list :
            if self.tokensList[self.current][0] == 'id' :
                self.statement()
                self.statement_list_prime()
                
            else:
                print("statement_list_prime ERROOOR")
                raise Exception("Error: en la compilacion")
        elif self.tokensList[self.current] == '{' or self.tokensList[self.current] == 'return' or self.tokensList[self.current] == 'if' or self.tokensList[self.current] == 'while' or self.tokensList[self.current] == 'input' or self.tokensList[self.current] == 'output' :
            self.statement()
            self.statement_list_prime()

        elif self.tokensList[self.current] == '}':
            return
        else:
            print("tatement_list_primeERROR")
            raise Exception("Error: en la compilacion")
        
    def assignment_stmt(self):
        if type(self.tokensList[self.current]) == list :
            if self.tokensList[self.current][0] == 'id' :
                self.var()
                if self.tokensList[self.current] == '=' :
                    self.Match('=')
                else: print("some error")
                self.expression()
                if self.tokensList[self.current] == ';' :
                    self.Match(';')
                else: print("some error2")
                
            else:
                print("assignment_stmt ERRROOOR")
                raise Exception("Error: en la compilacion")
        else:
            print("assignment_stmt errOR")
            raise Exception("Error: en la compilacion")
    
    def selection_stmt(self): 
        if self.tokensList[self.current] == 'if' :
            self.Match('if')
            self.Match('(')
            self.expression()
            self.Match(')')
            self.statement()
            self.selection_stmt2()
        else:
            print("selection_stmterror")
            raise Exception("Error: en la compilacion")

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
            print("selection_stm22terror")
            raise Exception("Error: en la compilacion")
    
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
                elif self.tokensList[self.current+1] == '=':
                    self.assignment_stmt()
                else:
                    print("ERROR")
                    raise Exception("Error: en la compilacion")
        else:
            print("errors")
            raise Exception("Error: en la compilacion")