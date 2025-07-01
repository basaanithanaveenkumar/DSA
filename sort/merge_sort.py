k=[5,6,3,2,5]

def merge_sort(lst):
    if len(lst)<=1:
        return lst
    mid=len(lst)//2
    left=lst[:mid]
    right=lst[mid:]

    left_lst=merge_sort(left)
    right_lst=merge_sort(right)

    return merge(left_lst,right_lst)
def merge(left_lst,right_lst):
    res=[]
    l_idx,r_idx=0,0
    while l_idx<len(left_lst)and r_idx<len(left_lst):
        if left_lst[l_idx]<right_lst[r_idx]:
            res.append(left_lst[l_idx])
            l_idx+=1
        else:
            res.append(right_lst[r_idx])
            r_idx+=1
        res.extend(left_lst[l_idx:])
        res.extend(right_lst[r_idx:])
    return res
k=merge_sort(k)
print(k)