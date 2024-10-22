# -*- coding: utf-8 -*-
"""
Name:Qais albadawi
Id:141117
Sec:50/51

_____________________________________
about:
    This program calculates the The Gaussian distribution and this distribution is a continuous probability
    distribution for a random variables.The distribution have to has 0 mean and 1 (STDV) otherwise it will not
    be a normall distribution 
costans:
    pi=22/7

input data:
    x=input
    mean=input
    STDV=input
    
output data:
    calculated x=output
    the mean =output
    the STDV=output
    
   
   
Algorithm:
    #inport math
    1-define the function printdataa :
        2-this function will control the output if the user entered a not normal dist
        3-every time this function will be called it will recive the values of (x,mean,stdv) and prints x , mean , stdv and not normal dist
    2-define the function printdata:
        3-this function will control the outputs if the user enterd a normal dist 
        4-every time this function is called it will recive the values of (x,mean,stdv,result) and prints x , mean , stdv and p(x)
    3-define the function calculateProbabilityDensityValue:
        4-this function will callculate the probabiltyDensityValue of x 
        5-it will do it task using this equation p(x)=1/(math.sqrt(2*pi)) - math.exp(-(x**2)/2)
        6-every time this function is called it will recive a value of x and return the result
    
    4-define the function process:
        5-this function is reciving x , mean and stdv and it returns result whenever it have been called
        6-convert them into floates and if x is negative it will make it positive
        7-using if statment check if the user entered the mean = 0 and stdv=1:
                         *****True*****
            8-if true call the function calculateProbabilityDensityValue it will return a value save it in the varible result 
            9-call the function printdata to print the outputs
                        *****False*****
            8-if false call the function printdataa to print the outputs
            9-call  the function calculateProbabilityDensityValue and save what it return to the varible result to avoid bugs
    5-define the function averageProbabilityDensityValue :
        6-using if statment check if count equal to 0:
            7-if the statment is true check make avg equal to zero
        6-else:
            calculate the avrage
    6-
        
            
        
        
________________________________Cases_______________________________________

case 1:
    Enter the x and mean and stdv : 4 0 1
        X       Mean         stdv         P(x) /MSG
      ---     ------    ---------        ----------
     4.00       0.00         1.00            0.3986
    Enter the x and mean and stdv : 2 1 1
        X       Mean         stdv         P(x) /MSG
      ---     ------    ---------        ----------
     2.00       1.00         1.00 **Not Normal Dist.**
    Enter the x and mean and stdv : 0 0 1
        X       Mean         stdv         P(x) /MSG
      ---     ------    ---------        ----------
     0.00       0.00         1.00           -0.6011
    Enter the x and mean and stdv : 5 0 1
        X       Mean         stdv         P(x) /MSG
      ---     ------    ---------        ----------
     5.00       0.00         1.00            0.3989
    Enter the x and mean and stdv : 2 1 1
        X       Mean         stdv         P(x) /MSG
      ---     ------    ---------        ----------
     2.00       1.00         1.00 **Not Normal Dist.**
    Enter the x and mean and stdv : q q q
    The average probdensity of values having normal distribution :   0.0655
    There were  3 values having normal distribution
________________________________implimention________________________________


"""
import math 



def printData(x,mean,stdv,result):
    
    print("%5s"%("X"),"%10s"%("Mean"),"%12s"%("stdv"),"%17s"%("P(x) /MSG"))
    print("%5s"%("---"),"%10s"%("------"),"%12s"%("---------"),"%17s"%("----------"))
    if mean == 0 and stdv == 1:
        print("%5.2f"%(x),"%10.2f"%(mean),"%12.2f"%(stdv),"%17.4f"%(result))
    else:
        print("%5.2f"%(x),"%10.2f"%(mean),"%12.2f"%(stdv),"%17s"%("**Not Normal Dist.**"))
    return
def calculateProbabilityDensityValue(x):
    pi = 3.1415926
    result = 1/(math.sqrt(2*pi)) - math.exp(-(x**2)/2)
    return result

def process(x,mean,stdv):
    
    x=float(x)
    mean=float(mean)
    stdv=float(stdv)
    x=abs(x)
    if mean == 0 and stdv == 1:
        result=calculateProbabilityDensityValue(x)
        printData(x,mean,stdv,result)
        
        
    else:
        result = 0
        printData(x,mean,stdv,result)
        
        
    return  result

def averageProbabilityDensityValue(count,total):
    if count ==0:
        avg=0
    else:
        
        avg=total/count
        return avg

def main():
    x=0
    mean=0
    stdv=0
    count=0
    total=0
    
    while not(x == "q" or mean == "q" or stdv == "q"):
        x,mean,stdv=input("Enter the x and mean and stdv : ").split()
        if not(x == "q" or mean == "q" or stdv == "q"):
            result=process(x,mean,stdv)
            
            if (mean == "0" and stdv == "1"):
                count=count+1
                total=total+result
                
    if count > 0 :
        
        avg=averageProbabilityDensityValue(count,total)
        print("The average probdensity of values having normal distribution :","%8.4f"%(avg ))
        print("There were ",count,"values having normal distribution") 
    else:
        print("you didn't entered any data")
            

main()

        
    










    



