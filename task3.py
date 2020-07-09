#findOccurance a function which will take 2 string("string_1" & "string_2") as  input .
#The function will return the number of "string_2"  occur  in  "string_1" .
#Not using any library for this task .


def findOccurance(str1,str2):
    l1 = len(str1)
    l2 = len(str2)
    if(l1<l2):
        return 0

    ans=0
    i=0
    while(i<l1):
        if(str1[i]==str2[0]):
            flag = 1
            for j in range(1,l2):
                if(str1[i+j]!=str2[j]):
                    flag=0
            if flag==1:
                ans=ans+1
                i=i+l2
            else:
                i=i+1
        else:
            i=i+1

    return ans



if __name__ =="__main__":
    string_1  =  "i love muri .ilovemuri. muriislife .without mur i'm nothing . murei is valobasha"
    string_2 = "muri"
    print("Here string_2 occur in string_1 ", findOccurance(string_1,string_2)," times.")

    #output: Here string_2 occur in string_1  3  times.
