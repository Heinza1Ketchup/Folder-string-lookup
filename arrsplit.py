my_file = open("file2.txt", "r")

data = """(L)64GB 2Rx4 PC5-4800B-RA0-1010-XT(S)80CE01223803A7EFA4(P)M321R8GA0BB0-CQKDS(M)W08C130
(L)64GB 2Rx4 PC5-4800B-RA0-1010-XT(S)80CE01223803A76912(P)M321R8GA0BB0-CQKMS(M)W06H130
(L)64GB 2Rx4 PC5-4800B-RA0-1010-XT(S)80CE01223803A771A0(P)M321R8GA0BB0-CQKDS(M)W06E120
(L)64GB 2Rx4 PC5-4800B-RA0-1010-XT(S)80CE01223803AA05E6(P)M321R8GA0BB0-CQKDS(M)W09O120
"""
data_into_list = data.split('\n')
print(len(data_into_list))

my_file.close()

# string parse for serial no.
for x in range(0, len(data_into_list)):
    arr1 = data_into_list[x]
    serialstr = arr1.split("(S)")
    batchstr = arr1.split("(M)")
    pnostr = arr1.split("(P)")
    arr2 = serialstr[1][0:18]
    arr3 = pnostr[1][0:18]
    arr4 = batchstr[1][0:7]
    print(arr3)
