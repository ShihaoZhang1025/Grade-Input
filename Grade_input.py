
# coding: utf-8

# In[ ]:

# Guilde line:
# Environment: Python 2.7
# 1, write only uni if the person' score=10 (e.g. "sz2531")
# 2, write "sz2531 9.5" or "sz2531 9" if the person's score<10
# 3, write "quit" to quit the process

import pandas as pd
import numpy as np

grade=pd.read_csv("/Users/ShihaoZhang/Desktop/Ada_Gradebook.csv", index_col = None, header = 0)

hw_number=raw_input("Please specify which HW you are grading")
hw_number=int(hw_number)+1
count=0
uni_score='NULL'

while(True):
    uni_score=raw_input("Enter the student's uni and score:")
    if(uni_score=='quit'):
        break
    uni=uni_score[:6]
    
    if(len(uni_score)==6):
        score=10
    elif(len(uni_score)>=8):
        score=float(uni_score[6:len(uni_score)])
        if(score>10):
            print("Error. The score is more than 10.")
            continue
    else:
        print("Error, please check your input")
        continue

    verify=grade['Student ID'].str.match(uni, case=True, as_indexer=True)
    verify=np.array(verify)

    if(sum(verify==1)):
        grade.ix[verify,hw_number]=score
        count=count+1
        print(grade.iloc[verify, [0,1,3]])
    elif(sum(verify)>1):
        print('There more than one student with this uni')
        print(grade.iloc[verify, [0,1,3]])
    elif(sum(verify==0)):
        print('Student not found')

print("The total number of the input is: %d", %count)
grade.to_csv("/Users/ShihaoZhang/Desktop/Ada_Gradebook.csv", index=False)
