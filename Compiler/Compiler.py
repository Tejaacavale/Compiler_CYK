##################### BOILERPLATE BEGINS ############################
import numpy as np
import pandas as pd
import sys
# Token types enumeration
##################### YOU CAN CHANGE THE ENUMERATION IF YOU WANT #######################
class TokenType:
    IDENTIFIER = "IDENTIFIER"
    KEYWORD = "KEYWORD"
    INTEGER = "INTEGER"
    FLOAT = "FLOAT"
    SYMBOL = "SYMBOL"

# Token hierarchy dictionary
token_hierarchy = {
    "if": TokenType.KEYWORD,
    "else": TokenType.KEYWORD,
    "print": TokenType.KEYWORD
}
#T is statement
#C is condition
#P and Q and R are var1,var2,var3
#O is op1
T=["y","if","else","o"]
NT=["S","I","A","T","C","P","Q","R","E","O","X"]
CNF ={
    "S":['IA',"TT","y"],
    "T":['IA',"TT","y"],
    "A":["CT","PQ"],
    "P":["CT"],
    "Q":["ET"],
    "E":["else"],
    "I":["if"],
    "C":["XR","y"],
    "R":["OX"],
    "O":["o"],
    "X":["y","OX","XR"]
}
# helper function to check if it is a valid identifier
def is_valid_identifier(lexeme):
    if not lexeme:
        return False

    # Check if the first character is an underscore or a letter
    if not (lexeme[0].isalpha() or lexeme[0] == '_'):
        return False

    # Check the rest of the characters (can be letters, digits, or underscores)
    for char in lexeme[1:]:
        if not (char.isalnum() or char == '_'):
            return False

    return True


# Tokenizer function
def tokenize(source_code):
    tokens = []
    position = 0

    while position < len(source_code):
        # Helper function to check if a character is alphanumeric
        def is_alphanumeric(char):
            return char.isalpha() or char.isdigit() or (char=='_')

        char = source_code[position]

        # Check for whitespace and skip it
        if char.isspace():
            position += 1
            continue

        # Identifier recognition
        if char.isalpha():
            lexeme = char
            position += 1
            while position < len(source_code) and is_alphanumeric(source_code[position]):
                lexeme += source_code[position]
                position += 1

            if lexeme in token_hierarchy:
                token_type = token_hierarchy[lexeme]
            else:
                # check if it is a valid identifier
                if is_valid_identifier(lexeme):
                    token_type = TokenType.IDENTIFIER
                else:
                    raise ValueError(f"Invalid identifier: {lexeme}")

        # Integer or Float recognition
        elif char.isdigit():
            lexeme = char
            position += 1

            is_float = False
            while position < len(source_code):
                next_char = source_code[position]
                # checking if it is a float, or a full-stop
                if next_char == '.':
                    if (position + 1 < len(source_code)):
                        next_next_char = source_code[position+1]
                        if next_next_char.isdigit():
                            is_float = True

                # checking for illegal identifier
                elif is_alphanumeric(next_char) and not next_char.isdigit():
                    while position < len(source_code) and is_alphanumeric(source_code[position]):
                        lexeme += source_code[position]
                        position += 1
                    if not is_valid_identifier(lexeme):
                        raise ValueError(f"Invalid identifier: {str(lexeme)}\nIdentifier can't start with digits")

                elif not next_char.isdigit():
                    break

                lexeme += next_char
                position += 1

            token_type = TokenType.FLOAT if is_float else TokenType.INTEGER

        # Symbol recognition
        else:
            lexeme = char
            position += 1
            token_type = TokenType.SYMBOL

        tokens.append((token_type, lexeme))

    return tokens

########################## BOILERPLATE ENDS ###########################
def is_in_cartesian_prod(x, y, r):
    for i in x.split(','):
        for j in y.split(','):
            if i + j == r:
                return True
    return False
 
def accept_CYK(w, G):
    # if w == '':
    #     return '' in G[S]
    n = len(w)
    DP_table = []
    for _ in range(n):
        row = [''] * n
        DP_table.append(row)
    for i in range(n):
        for lhs in G.keys():
            for rhs in G[lhs]:
                 if w[i] == rhs: 
                    if not DP_table[i][i]:
                        DP_table[i][i] = lhs
                    else:
                        DP_table[i][i] += ',' + lhs

    # for i in range(n):
    #     print(DP_table[i][i])     
    for l in range(2, n+1):       
        for i in range(n-l+1):    
            j = i+l-1               
            for k in range(i, j):    
                for lhs in G.keys():
                    for rhs in G[lhs]:
                        if len(rhs) == 2 and not(rhs in T): 
                            if is_in_cartesian_prod(DP_table[i][k], DP_table[k+1][j], rhs):
                                if not lhs in DP_table[i][j]:
                                    if not DP_table[i][j]:
                                        DP_table[i][j] = lhs
                                    else:
                                        DP_table[i][j] += ',' + lhs
    # for i in range(n):
    #     for j in range(n):
    #         print(DP_table[i][j])
    # print(DP_table[0][n-1])
    return 'S' in DP_table[0][n-1]


def checkGrammar(tokens):
    newtok = []
    for token in tokens:
        if token[0] == TokenType().INTEGER or token[0] == TokenType().FLOAT:
            newtok += ["y"]
        elif token[0] == TokenType().IDENTIFIER or (token[0] == TokenType().KEYWORD and token[1] !="if" and token[1] != "else"):
            # print(token)
            newtok += ["y"]
        elif token[1] in "+-*/^<>=":
            newtok += ["o"]
        else:
            newtok += [token[1]]
    # for token in newtok:
    #     print(token)
    if(not(accept_CYK(newtok,CNF))):
        print("SYNTAX ERROR")
        sys.exit()


# Test the tokenizer
if __name__ == "__main__":
    source_code = str(input("Enter the line to be compiled:"))
    # source_code = "if x > 5 print 5"
    if(source_code==""):
        print("SYNTAX ERROR")
        sys.exit()
    tokens = tokenize(source_code)
    # for token in tokens:
    #     print(f"Token Type: {token[0]}, Token Value: {token[1]}")

    logs = checkGrammar(tokens)  # You are tasked with implementing the function checkGrammar
    for token in tokens:
        print(f"Token Type: {token[0]}, Token Value: {token[1]}")