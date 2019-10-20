import Grammars.LedgerGrammar as ledgerParser
import sys

def parse_index(indexPath):
    filePaths =[]
    index = open(indexPath,'r')
    for line in index:
        result = line.strip("\n ")
        result = result.split(" ")
        if result[0] != '':
            print("Result"+ str(result)) 
            if len(result) > 1:
                if result[0] == '!include':
                    filePaths.append(result[1])
                else:
                    pass
            else:
                raise Exception("While parsing file {} \n directive '{}' requires an argument".format(indexPath, result[0]))    
  
    for filePath in filePaths:
        if not os.path.isfile(filePath):
            raise Exception("While parsing file {} \n file to include was not found '{}'".format(indexPath, filePath))
    return filePaths


while True:
    userInput = raw_input("[] ")
    
    try:
        tree = ledgerParser.parse(userInput)
        for node in tree:
            print(node.offset, node.text)
    except ledgerParser.ParseError, e:
        print('Error: Unrecognized command, '+ str(e))
