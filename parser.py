from lark import Lark

ebnf = r"""
    // EBNF grammer translated into LARK syntax
    program: statement*
    block: "{" statement* "}"
    ?statement: for_stmt | set_stmt | assign_stmt | if_stmt | print_stmt
    
    word: LETTER+
    ?number: float | integer
    type: "int" | "float" | "string" | "list"
    string: "\"" word (" " word)* "\""
    float: integer "." integer
    integer: DIGIT+
    LETTER: "a".."z" | "A".."Z"
    DIGIT: "0".."9"
    list: "[" [list_content] "]"
    list_content: number ("," number)*

    identifier: word
    condition: identifier (">" | "<") number
    expression: value (operation value)? | list
    ?value: identifier | float | integer | string
    operation: "+" | "-" | "*" | "/"

    set_stmt: "set" type identifier "=" expression
    assign_stmt: identifier "=" expression
    for_stmt: "for" "each" identifier "in" identifier block
    if_stmt: "if" "(" condition ")" block "else" block
    print_stmt: "print" (identifier | string)
    
    // Ignore whitespace so it doesn't interfere with parsing using common lib in Lark
    %import common.WS
    %ignore WS
"""