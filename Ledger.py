import Grammars.LedgerGrammar as ledgerParser
import sys


while True:
    userInput = raw_input("[] ")
    
    try:
        tree = ledgerParser.parse(userInput)
        for node in tree:
            print(node.offset, node.text)
    except ledgerParser.ParseError, e:
        print('Error: Unrecognized command, '+ str(e))
