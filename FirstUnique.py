def solution(A):
    freq={}
    for num in A:
        if num in freq:
            freq[num]+=1  
        else:
            freq[num]=1
            
            
    result=[]
    for i in A:        
        if freq[i]==1:
            result.append(i)

    final=[]        
    if len(result)>0:
        final.append(result[0])
    else:
        final.append(-1)

    res=int(final[0])

    return res

