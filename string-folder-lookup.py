import os

#change directory to path
os.chdir("N:\Application ENG\PST\DDR5")
os.chdir("2023_Logs\December 2022-Feburary2023")
print(os.getcwd())

#get folder names
directory_file_names = []
for filename in os.listdir(os.getcwd()):
    directory_file_names.append(filename)

#string for folder look up
dirstr = """WI2B150005
WI2B140100
WI2B150004
WI2B252623
WI2B130023
WI2B140101
WI2B252629
WI31092517
WI31092525
WI31092515"""
#splint string by end space
data_into_list1 = dirstr.split('\n')
print(len(data_into_list1))

#get file path name
data_into_list = []
for x in range(0, len(data_into_list1)):
    for y in range(0, len(directory_file_names)):
        if data_into_list1[x] in directory_file_names[y]:
            data_into_list.append(directory_file_names[y])
print(len(data_into_list))

#Search through folders
notfound = []
for x in range(0, len(data_into_list)):
    try:
        os.chdir(data_into_list[x])
        print(os.getcwd())
        #serach through files within folder
        for filename in os.listdir(os.getcwd()):
            with open(os.path.join(os.getcwd(), filename), 'r') as f:  # open in readonly mode
                # print(filename)
                file1 = open(filename, "r")
                data = file1.read()
                dlist = data.split('\n')
                # print(dlist)
                listex = []
                #search for containing string
                for y in range(0, len(dlist)):
                    arr1 = dlist[y]
                    if "[ODECC_ENABLE]" in arr1:
                        snstr = arr1.split('S/N:')
                        serialstring = snstr[1][1:14]
                        if serialstring not in listex:
                            listex.append(serialstring)

                        # print(filename)
                if len(listex) > 0:
                    print(listex)

        os.chdir("N:\Application ENG\PST\DDR5")
        os.chdir("2023_Logs\December 2022-Feburary2023")
    except:
        notfound.append(data_into_list[x])
        continue

print("not found: ", notfound)
#for filename in os.listdir(os.getcwd()):
#   with open(os.path.join(os.getcwd(), filename), 'r') as f: # open in readonly mode
#       print(filename)
