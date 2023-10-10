def binary(arr:list,target)->int:
    begin_index=0
    end_index=len(arr)
    while begin_index<end_index:
        midpoint=(begin_index+end_index)//2
        midpoint_value=arr[midpoint]
        
            
        if midpoint_value<=target:
            begin_index=midpoint+1
        else:
            begin_index=midpoint-1
    return begin_index

print(binary([2,3,4,5],4))