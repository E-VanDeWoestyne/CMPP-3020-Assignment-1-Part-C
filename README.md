Python lexical analyser using LARK

## Requirements

Python 3.6+

LARK

## EBNF

```
<program> ::= { <statement> } 
<block> ::= "{" { <statement> } "}" 
<statement> ::= <for_stmt> | <set_stmt> | <assign_stmt> | <if_stmt> | <print_stmt> 

<word> ::= <letter> { <letter> } 
<number> ::= <integer> | <float> 
<type> ::= "int" | "float" | "string" | "list" 
<string> ::= """ <word> { " " <word> } """ 
<float> ::= <integer> "." <integer> 
<integer> ::= <digit> { <digit> } 
<letter> ::= "a" | "b" | "c" | "d" | "e" | "f" | "g" | "h" | "i" | "j" | "k" | "l" | "m" | "n" | "o" | "p" | "q" | "r" | "s" | "t" | "u" | "v" | "w" | "x" | "y" | "z" | "A" | "B" | "C" | "D" | "E" | "F" | "G" | "H" | "I" | "J" | "K" | "L" | "M" | "N" | "O" | "P" | "Q" | "R" | "S" | "T" | "U" | "V" | "W" | "X" | "Y" | "Z" 
<digit> ::= "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" 
<list> ::= "[" [<list_content>] "]" 
<list_content> ::= <number> { "," <number> } 

<identifier> ::= <word> 
<condition> ::= <identifier> ( ">" | "<" ) <number> 
<expression> ::= <value> [ <operation> <value> ] | <list> 
<value> ::= <identifier> | <integer> | <float> | <string> 
<operation> ::= ( "+" | "-" | "*" | "/" ) 

<set_stmt> ::= "set" <type> <identifier> "=" <expression> 
<assign_stmt> ::= <identifier> "=" <expression> 
<for_stmt> ::= "for each" <identifier> "in" <identifier> <block> 
<if_stmt> ::= "if" "(" <condition> ")" <block> "else" <block> 
<print_stmt> ::= "print" ( <identifier> | <string> ) 
```
