import random

newIDs = 10000
difinitionEnder = ";_name_;x;;;;;;;;;;;;;;;;;;;,\n"

defInput = open("Input/definition.csv")

RGBlist = []

for line in defInput:
    try:
        if int (line.split(";")[0]):
            RGBlist.append((line.split(";")[1],line.split(";")[2],line.split(";")[3]))
    except:
        pass
print(len(RGBlist))
i=len(RGBlist)+newIDs

defOutput = open("New_IDs_definition.csv","w")

lastID = len(RGBlist)
while(len(RGBlist)<i):
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    if(not (r,g,b) in RGBlist):
        RGBlist.append((r,g,b))
        #write def to file id;red;green;blue;_name_;x;;;;;;;;;;;;;;;;;;;,
        lastID+=1
        defOutput.write("%i;%i;%i;%i"%(lastID,r,g,b)+difinitionEnder)
        
#save file
defOutput.close()
