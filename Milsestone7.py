# Mile Stone 7

import numpy as np
import math


def write_file(coordinates):
    with open('E:\KLA Hackathon 2023\Milestone_Input\Milestone 7\output7.txt','a',newline='') as file:
        file.write('boundary \n')
        file.write('layer 1 \n')
        file.write('datatype 0 \n')
        file.write('xy '+ ' '.join([str(elem) for elem in coordinates]) +' \n')
        file.write('endel\n')
        file.close()


def Input_file():
    data=[]
    file=open('E:\KLA Hackathon 2023\Milestone_Input\Milestone 7\Source.txt','r')
    for line in file: 
        word=line.split()
        data.append(word)
    return data


# These take the validation polygon coordinates
def validattion_file():
    data=[]
    valid_corodinates=[]
    file=open('E:\KLA Hackathon 2023\Milestone_Input\Milestone 7\POI.txt','r')
    for line in file: 
        word=line.split()
        data.append(word)
    
    for i in data:
        if('xy' in i):
            valid_corodinates.append(i)

    return valid_corodinates



def parse_data(data):
    coordinates=[]

    for i in data:
        if('xy' in i):
            coordinates.append(i)

    return coordinates


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


def distance(lst):
    lst=lst[2:]
    lst = [eval(i) for i in lst]
    x=[]
    y=[]
    
    for i in range(len(lst)):
        if(i%2==0):
            x.append(lst[i])
        else:
            y.append(lst[i])

    res=[]

    for i in range(len(x)-1):
        res.append(math.sqrt(((x[i]-y[i])**2)+((x[i+1]-y[i+1])**2)))

    return res

def validate(cord,valid):

    data=[]
    for x,y in zip(cord,valid):
        data.append(x//y)
    
    for i in range(len(data)):
        if(data[i]!=data[i+1]):
            return False
        else:
            return True



def check_polygon(coord,valid_cord1,valid_cord2):
    result=[]

    valid_cord1_area=area(valid_cord1)
    valid_cord2_area=area(valid_cord2)
    
    #coord1_dist=distance(valid_cord1)
    #coord2_dist=distance(valid_cord2)

    
    #validate(coord2_dist,coord1_dist)

    for i in coord:
        #print(i[1])
        if(i[1]==valid_cord1[1]):
            #idist=distance(i)
            ar=area(i)
            if(ar==valid_cord1_area or ar==valid_cord2_area):
                result.append(i)
    
    return result
    
        



def main():
    data=Input_file()
    valid_cord=validattion_file()
    coordinates=parse_data(data)
    result=check_polygon(coordinates,valid_cord[0],valid_cord[1])

    print(len(result))

    for i in result:
        write_file(i[1:])


if __name__=="__main__":
    main()