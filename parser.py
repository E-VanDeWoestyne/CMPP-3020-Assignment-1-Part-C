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

def run_parser():
    # Gets the filename from the user.
    print("\nWelcome to the EBNF Parser tool for CMPP-3020 Assignment 1.\nThis tool will parse a file containing code written in a specific EBNF grammar and display the parse tree.")
    print("Multiple code examples are provided. 'code1.txt' contains the matching pseudocode from Part B, while other files contain other variations for testing.")
    filename = input("Enter the filename: ")

    # Try to open the file and read its contents. If the file is not found, catch the exception and print an error message.
    try:
        with open(filename, 'r') as file:
            user_code = file.read()
            
        # Defines a Lark parser using the EBNF grammer to run from 'program' starting point.
        parser = Lark(ebnf, start='program')

        try:
            # Parses the code for correct grammer and then prints a parse tree if successful.
            print(f"\nParsing file: {filename}\n")
            print(user_code)
            parse_tree = parser.parse(user_code)
            print("\nParse successful and raised no exceptions.")

            print(parse_tree.pretty())

        except Exception as e:
            print(f"Error parsing the code: {e}")

    except FileNotFoundError:
        print(f"File {filename} not found. Please check the filename and try again.")
        return

if __name__ == "__main__":
    run_parser()