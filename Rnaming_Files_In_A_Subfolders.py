import os
path= os.chdir("D:\\CCT Saares Project\\cct\\cct")
SubF_name= os.listdir(path)

for sub in SubF_name :
    i=0
    new_path= os.chdir("D:\\CCT Saares Project\\cct\\cct\\" + sub)
    for file in os.listdir(new_path):
        new_file_name = "{a}_{b}.jpg".format(a=sub, b=i)
        os.rename(file,new_file_name)
        i=i+1
        
    