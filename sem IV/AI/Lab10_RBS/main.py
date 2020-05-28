from controller import Controller


def loadData():
    '''
    read data from file
    '''
    file = open("input.txt")
    
    data=[]
    
    for line in file:
        
        line = line.strip("\n")
        num = line.split(" ")
        n = []
        
        for i in range(len(num)):
            n.append(float(num[i]))
            
        data.append(n)

            
    return data
        
def main():
    
    data=loadData()
    #print(data)
    i=1
    for line in data:
        print("Input no",i,":")
        i=i+1
        c = Controller(line[0], line[1])
        c.solve()


main()