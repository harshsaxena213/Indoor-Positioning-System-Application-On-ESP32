# finding "A" and "N" with taking sample of 50 rssi values for 4 different distance
# mathmatical realtion between rssi and distance is 
# RSSI=A−10Nlog10​(d)
# where "A" is mean of 50 values of rssi taken at distance of 1m   
# "N" is   environment-specific path-loss exponent




import raw_data as rd
import numpy as np


average_rssai=[]
raw_values=[rd.one_meter,rd.two_meter,rd.three_meter,rd.four_meter]
temp=0

#Taking Average Or Mean Of Raw RSSI Values
for key in raw_values:
    temp=sum(key)/len(key)
    average_rssai.append(temp)


print("The Average RSSI Found To Be:- ",average_rssai)  

temp_list=average_rssai

average_rssai=[
    (1,temp_list[0]),   #One Meter
    (2,temp_list[1]),   #Two Meter
    (3,temp_list[2]),   #Three Meter
    (4,temp_list[3])    #Four Meter
]


distance = np.array([x[0] for x in average_rssai])
mean_rssai = np.array([x[1] for x in average_rssai])

#matrix M with first column as 1 and second column as 10log(d) where log is base to 10 
M=np.column_stack((
    np.ones(len(distance)),
    10*np.log10(distance)
    
))

#least square method
MT=M.T
MTM=MT @ M
MTy=MT @ mean_rssai

x = np.linalg.solve(MTM, MTy)

A = x[0]
n = -x[1]

print("A =", A)
print("n =", n)
