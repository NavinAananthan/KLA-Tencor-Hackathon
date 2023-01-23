# Mile Stone 3

import math
import numpy as np

def write_file(coordinates):
    with open('E:\KLA Hackathon 2023\Milestone_Input\Milestone 3\output3.txt','a',newline='') as file:
        file.write('boundary \n')
        file.write('layer 1 \n')
        file.write('datatype 0 \n')
        file.write('xy '+ ' '.join([str(elem) for elem in coordinates]) +' \n')
        file.write('endel\n')
        file.close()


def Input_file():
    data=[]
    file=open('E:\KLA Hackathon 2023\Milestone_Input\Milestone 3\Source.txt','r')
    for line in file: 
        word=line.split()
        data.append(word)
    return data


def validattion_file():
    data=[]
    valid_corodinates=[]
    file=open('E:\KLA Hackathon 2023\Milestone_Input\Milestone 3\POI.txt','r')
    for line in file: 
        word=line.split()
        data.append(word)
    
    for i in data:
        if('xy' in i):
            valid_corodinates.append(i)

    return valid_corodinates


def parse_data(data,valid_cord):
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

    return coordinates,layers,datatype


def area(lst):
    lst=lst[2:]
    lst = [eval(i) for i in lst]
    x=[]
    y=[]
    
    for i in range(len(lst)):
        if(i%2==0):
            x.append(lst[i])
        else:
            y.append(lst[i])

    area=0.5*(np.abs(np.dot(x,np.roll(y,1))-np.dot(y,np.roll(x,1))))

    return area






def check_polygon(coord,valid_cord,vertices):
    result=[]
    
    for i in coord:
        if(area(i)==area(valid_cord)):
            result.append(i)

    return result
    
        



def main():
    data=Input_file()
    valid_cord=validattion_file()
    coordinates,layers,datatype=parse_data(data,valid_cord[0])
    result=check_polygon(coordinates,valid_cord[0],valid_cord[0][1])

    for i in result:
        write_file(i[1:])


if __name__=="__main__":
    main()