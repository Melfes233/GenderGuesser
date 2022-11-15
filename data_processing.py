import sys
import os
from tqdm import tqdm
import csv

def getkey(elem):
    return elem[2]

if __name__=='__main__':
    file_path=os.path.join(sys.path[0],'givenname.csv')
    with open(file_path,'r',encoding='utf-8') as f:
        reader=csv.reader(f)
        labels=next(reader)
        data=[]
        for line in tqdm(reader):
            data.append([line[0],int(line[3]),int(line[4])])
    
    # output_path=os.path.join(sys.path[0],'charfreq.csv')
    # if os.path.exists(output_path):
    #     os.remove(output_path)
    # with open(output_path,'w',encoding='utf-8',newline='') as f:
    #     writer=csv.writer(f)
    #     headers=['char','male','female']
    #     writer.writerow(headers)
    #     writer.writerows(data)
    
    data.sort(key=getkey,reverse=True)
    output_path=os.path.join(sys.path[0],'charfreq_sorted_female.csv')
    if os.path.exists(output_path):
        os.remove(output_path)
    with open(output_path,'w',encoding='utf-8',newline='') as f:
        writer=csv.writer(f)
        headers=['char','male','female']
        writer.writerow(headers)
        writer.writerows(data)
    
    