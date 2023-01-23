# Mile Stone 1

def write_file(layer,coordinates,datatype):
    with open('E:\KLA Hackathon 2023\Milestone_Input\Milestone 1\output.txt','a',newline='') as file:
        file.write('boundary \n')
        file.write('layer '+layer+' \n')
        file.write('datatype '+datatype+' \n')
        file.write('xy '+ ' '.join([str(elem) for elem in coordinates]) +' \n')
        file.write('endel\n')
        file.close()


def parse_file():
    data=[]
    file=open('E:\KLA Hackathon 2023\Milestone_Input\Milestone 1\Format_Source.txt','r')
    for line in file: 
        word=line.split()
        data.append(word)

    return data


def parse_data(data):
    coordinates=[]
    layers=[]
    datatype=[]
    for i in data:
        if('xy' in i):
            coordinates.append(i)
        if('layer' in i):
            layers.append(i)
        if('datatype' in i):
            datatype.append(i)
    crd1=coordinates[0][1:]
    crd2=coordinates[1][1:]
    dtp1=datatype[0][1]
    dtp2=datatype[1][1]
    layer1=layers[0][1]
    layer2=layers[1][1]

    #print(crd2)

    return crd1,crd2,dtp1,dtp2,layer1,layer2

         
def main():

    data=parse_file()
    crd1,crd2,dtp1,dtp2,layer1,layer2=parse_data(data)

    write_file(layer1,crd1,dtp1)
    write_file(layer2,crd2,dtp2)
    


if __name__=="__main__":
    main()