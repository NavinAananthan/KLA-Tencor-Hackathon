# Mile Stone 6

import math
import numpy as np

def write_file(coordinates):
    with open('E:\KLA Hackathon 2023\Milestone_Input\Milestone 6\output6.txt','a',newline='') as file:
        file.write('boundary \n')
        file.write('layer 1 \n')
        file.write('datatype 0 \n')
        file.write('xy '+ ' '.join([str(elem) for elem in coordinates]) +' \n')
        file.write('endel\n')
        file.close()


def Input_file():
    data=[]
    file=open('E:\KLA Hackathon 2023\Milestone_Input\Milestone 6\Source.txt','r')
    for line in file: 
        word=line.split()
        data.append(word)
    return data


def validattion_file():
    data=[]
    valid_corodinates=[]
    file=open('E:\KLA Hackathon 2023\Milestone_Input\Milestone 6\POI.txt','r')
    for line in file: 
        word=line.split()
        data.append(word)
    
    for i in data:
        if('xy' in i):
            valid_corodinates.append(i)

    return valid_corodinates


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


def perimeter(cord,valid):
    peri1=0
    peri2=0

    for x,y in zip(cord,valid):
        peri1+=x
        peri2+=y
    
    if(peri1==peri2):
        return True
    else:
        return False


def npangle(lst):
    lst=lst[2:]
    lst = [eval(i) for i in lst]
    x=[]
    y=[]
    angle=[]

    for i in range(len(lst)):
        if(i%2==0):
            x.append(lst[i])
        else:
            y.append(lst[i])

    for i in range(len(x)-2):
        ang = math.degrees(math.atan2(y[i+2]-y[i+1], x[i+2]-x[i]) - math.atan2(y[i]-y[i+1], x[i]-x[i+1]))
        angle.append(round(ang + 360) if ang < 0 else round(ang))

    return angle
    


def angle(lst):
    lst=lst[2:]
    lst = [eval(i) for i in lst]
    x=[]
    y=[]
    
    for i in range(len(lst)):
        if(i%2==0):
            x.append(lst[i])
        else:
            y.append(lst[i])

    
    numerator=[]
    denominator=[]
    ratio=[]
    anglerad=[]
    angledeg=[]

    for i in range(len(x)-2):
        numerator.append(y[i+1]*(x[i]-x[i+2])+y[i]*(x[i+2]-x[i+1])+y[i+2]*(x[i+1]-x[i]))
        denominator.append((x[i+1]-x[i])*(x[i]+x[i+2])+(y[i+1]-y[i])*(y[i]+y[i+2]))
        ratio.append(numerator[i]/denominator[i])

        anglerad.append(math.atan(ratio[i]))
        angledeg.append((anglerad[i]*180)/math.pi);

        if(angledeg[i]<0):
            angledeg[i] = 180+angledeg[i]

    return angledeg


def check_angle(angle1,angle2):

    cnt=0

    for i in range(len(angle1)):
        if(angle1[i]==angle2[i]):
            cnt+1

    if(cnt>len(angle1)/2):
        return True
    else:
        return False




def check_polygon(coord,valid_cord):
    result=[]
    
    valangle=npangle(valid_cord)
    valarea=area(valid_cord)
    
    #print(valangle)
    #print(npangle(coord[2]))

    for i in coord:
        iangle=angle(i)
        iarea=area(i)
        if(iarea==valarea):
            result.append(i)
        elif(iangle==valangle):
            result.append(i)
        
    return result
    
        



def main():
    data=Input_file()
    valid_cord=validattion_file()
    coordinates=parse_data(data)
    result=check_polygon(coordinates,valid_cord[0])

    print(len(result))
    for i in result:
        write_file(i[1:])


if __name__=="__main__":
    main()