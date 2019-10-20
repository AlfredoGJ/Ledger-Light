import Grammars.LedgerGrammar as ledgerParser
import sys

def parse_index(filepath):
    files =[]
    index = open(filepath,'r')
    for line in index:
        if line != '\n':
            result= line.strip()
            result=result.split(" ")
            if len(result) > 1:
                if result[0] =='!include':
                    files.append(result[1])
                else:
                    pass
            else:
                raise Exception("While parsing file {} \n directive '{}' requires an argument".format(filepath, result[0]))    


while True:
    userInput = raw_input("[] ")
    
    try:
        tree = ledgerParser.parse(userInput)
        for node in tree:
            print(node.offset, node.text)
    except ledgerParser.ParseError, e:
        print('Error: Unrecognized command, '+ str(e))
