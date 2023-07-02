disk_length = 21
disk_length_s = 21
# Format: ('length_n_program')
programs_length = [4,5,6,1,2,3,4,3]
programs_length_s = [4,5,6,1,2,3,4,3]
array_programs = []
# programs_length ordered from smallest to largest
programs_length.sort()
programs_length_s.sort()
print(programs_length)

def insert_programs(array_programs, disk_length):
    if disk_length == 0:        
        return array_programs
    n_program = len(array_programs)    
    if programs_length_s[n_program] > disk_length_s:
        return array_programs
    else:
        sum_programs = sum(array_programs)
        if sum_programs + programs_length_s[n_program] <= disk_length_s:
            array_programs.append(programs_length_s[n_program])
            programs_length.remove(programs_length_s[n_program])
            programs_length.sort()
            sum_programs = sum(array_programs)
        else:
            difference = disk_length_s - sum_programs
            found = search_disk(difference,array_programs,len(array_programs))
            return array_programs        
        if sum_programs == disk_length_s:
            return array_programs
        elif sum_programs < disk_length_s:            
            return insert_programs(array_programs, disk_length-programs_length_s[n_program])
                   
        return insert_programs(array_programs, disk_length-programs_length_s[n_program])
   
def search_disk(difference, elements, i):    
    if i < 0:
        return i
    n_search = difference + elements[i-1]    
    if n_search in programs_length:
        array_programs.append(n_search)
        programs_length.remove(n_search)
        array_programs.remove(elements[i-1])
        programs_length.append(elements[i-1])
        programs_length.sort()
        return i
    else:
        return search_disk(difference, elements, i - 1)

#RECURSIVE
insert_programs(array_programs, disk_length)
print(array_programs)
print("##############")



def max_programs(disk, programs):
    n_programs = len(programs)    
    matrix = [[0] * (disk+1) for _ in range(n_programs+1)]
    for i in range(1, n_programs+1):
        for j in range(1, disk+1):            
            if programs[i-1] > j:
                matrix[i][j] = matrix[i-1][j]
            else:                
                matrix[i][j] = max(matrix[i-1][j], 1 + matrix[i-1][j - programs[i-1]])    
    return matrix[n_programs][disk]


# ITERATIVE
programs = [4,5,6,1,2,3,4,3]
disk = 21
print(max_programs(disk,programs))




