from random import choice

def thue_interpret(path):
    sub = {} # sub[lhs] = rhs
    
    with open(path) as f:
        for line in f:
            line = line.strip() # remove newline
            
            if "::=" in line and len(line) > 3: 
                cI = line.index("::=") #index up until the ::= operator
                sub[line[:cI]] = line[cI+3:]
            elif "::=" not in line:
                data = line
                
    subPossible = True
    while(subPossible):
        subPossible = False                
        availableSubs = [lhs for lhs in sub if lhs in data]
        
        if len(availableSubs) > 0:
            subPossible = True
                
        if subPossible:        
            subToMake = choice(availableSubs)
            data = data.replace(subToMake,sub[subToMake],1)
        
    print(data)  
