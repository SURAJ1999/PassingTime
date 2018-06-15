# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 19:35:41 2018

@author: SURAJ S
"""
#input is a single column of pandas dataframe or array
def CategoricalEncoder(w):#CATEGORICAL ENCODER function similar to CategoricalEncoder of Sklearn
    q=w.tolist()
    list1=[]    #initializing a list
    for i in q:
        if (i in list1)==True:
            continue
        else:
            list1.append(i)
    cat_matrix=[]
    for j in range(0,len(list1),1):
        list2=[]
        for k in range(0,len(list1),1):
            list2.append(int(0))
        list2[j]=int(1)
        cat_matrix.append(list2)
    
    for l in range(0,len(q),1):
        for m in range(0,len(list1),1):
            if q[l]==list1[m]:
                q[l]=cat_matrix[m]
                break
            else:
                continue
    return (q)#Retuns an encoded list inside a list