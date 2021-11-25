import time

def compare_two(a:tuple,b:tuple):
    return 1 in [len(set(i)) for i in list(zip(a,b))]

def get_indices(data:list) -> list:
    '''
    time complexity: O(n^2)
    space complexity: O(n)
    '''
    start = time.time()
    if not isinstance(data, list):
        raise TypeError('input data is not a list.')
    m = len(data) # sample size
    n = max([len(row) for row in data if isinstance(row,tuple)]) # column size

    for i,value in enumerate(data):
        if isinstance(value,tuple):              
            if len(value) != n:
                print('Warning: Row %d may have %d missing value'%(i,n-len(value)))
        else:
            raise TypeError('Row %d is not a tuple'%i) 

        
    group = [] # target output 
    values = [] # ravelled data: all values in group
    for i in range(m-1):
        for j in range(i+1,m):
            # print('round: ', i,j)
            if compare_two(data[i],data[j]): # compare i and j(j>i) 
                # print('group: ', i,j)
                # if i never appeared in any subgroup before, we add a new subgroup [i,j]
                if i not in values:               
                    group.append([i,j])
                    values.extend([i,j])
                    # if i pairs with any j(j>1), we stop the loop to avoid duplicate computation so as to speed up
                    break 
                else:
                    # if i is in value, i must be in a subgroup in the previous loop
                    # So we find the index of the existed group, and add a new member to this group
                    idx = [idx for idx, x in enumerate(group) if i in x][0]
                    group[idx].append(j)
                    values.append(j)
                    
    # we add rows that does not belong to any group here
    res =  group+([[x] for x in list(range(m)) if x not in values])
    end = time.time()
    print('function costs: ', end - start, ' seconds')
    return res


