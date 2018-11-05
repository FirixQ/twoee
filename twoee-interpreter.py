import sys

#def operator(rhs,i):

def inp(sd): #input, returns and inputed value to replace something in the data string    
    return input()

def promptedinp(sd): #input, returns and inputed value to replace something in the data string
    return input(sd)    

def out(sd):
    print(sd)
    return ""

def debugs(s,variable=""):
    global debug
    if debug:
        print("Debuging",variable,":",s)

def twoee_interpret(path):
    sub = {} # sub[lhs] = rhs
    opsList = {":::":inp,"~::":promptedinp,"~~~":out}
    global debug
  
    with open(path) as f:
        for line in f:
            line = line.strip() # remove newline

            # not regex
            
            if "::=" in line and len(line) > 3: 
                cI = line.index("::=") #index up until the ::= operator
                sub[line[:cI]] = line[cI+3:]
            elif ";;=" == line[:3]:
                # data = line.replace(";;=","") # DO NOT DO THIS (it was Tom)
                data = line[3:]
                
    subPossible = True
    while(subPossible):
        subPossible = False                
        subToRun = [lhs for lhs in sub if lhs in data]
        debugs(subToRun,"subToRun")
        
        if len(subToRun) > 0:
            subToRun = subToRun[0]
            subPossible = True 
            rhs = sub[subToRun]
            output = ""     
            sourceData = rhs   

            while len(sourceData) > 0:
                debugs(sourceData, "sourceData before")
                next3 = sourceData[:3]
                if next3 in opsList:
                    output += opsList[next3](sourceData[3:])
                    sourceData = sourceData[3:]
                    break
                else:
                    output += sourceData[0]
                    sourceData = sourceData[1:]
                debugs(sourceData, "sourceData after")


            data = data.replace(subToRun,output,1)
        debugs(data,"data")
        
    print(data) 

if __name__ == "__main__":
    if len(sys.argv) == 3:
        debug = sys.argv[2]
        if type(debug) == str and debug == "debug":
            debug = True
        else:
            debug = False
            print("The only supported flag is debug. Continuing anyway\n\n")
        twoee_interpret(sys.argv[1])
    elif len(sys.argv) == 2:
        twoee_interpret(sys.argv[1])
    else:
        print("Usage: twoee-interpreter.py [filename] [debug]")
