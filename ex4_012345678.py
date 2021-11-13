''' Exercise #4. Python for Engineers.'''

"""
#########################################
# Question 1 - do not delete this comment
#########################################
def most_popular_characters(my_string):
    char_count = {}
    sorted_chars = {}
    for char in my_string:
        char_count[char] = char_count.get(char, 0) + 1
    sorted_chars = sorted(char_count, key=char_count.get, reverse=True)
    i=1
    temp=sorted_chars[i-1]
    while i<len(sorted_chars) and char_count[sorted_chars[i]]==char_count[sorted_chars[i-1]]:
        temp=temp+sorted_chars[i]
        i+=1
    return(''.join(sorted(temp)))
    

#########################################
# Question 2 - do not delete this comment
#########################################
def diff_sparse_matrices(lst):
    diff_sparse={}
    diff=0
    used_keys={}
    for dic in lst:
        for key in dic :
            used_keys.update({key})
            if key in diff_sparse:
                temp=diff_sparse[key]-dic[key]
                if temp!=0:
                    diff_sparse[key]=temp
                else:
                    del diff_sparse[key]
            elif key not in used_keys:
                diff_sparse[key]=dic.get(key)
            else:
                diff_sparse[key]=(-1)*dic[key]
            
    
    print(diff_sparse)
    return diff_sparse 

"""


#########################################
# Question 3 - do not delete this comment
#########################################
def find_substring_locations(s, k):
    new_dict={}
    for i in range(0,len(s)-k+1):
        comb=s[i:i+k]
        if comb in new_dict:
            new_dict[comb].append(i)
        else:
            new_dict[comb]=[i]
    return new_dict
    


#########################################
# Question 4 - do not delete this comment
#########################################
def courses_per_student(tuples_lst):
    new_dict = {}
    for tup in tuples_lst:
        if tup[0].lower() not in new_dict:
            new_dict[tup[0].lower()]=[tup[1].lower()]
        else:
            new_dict[tup[0].lower()].append(tup[1].lower())

    return new_dict


def num_courses_per_student(stud_dict):
    for stud in stud_dict:
        stud_dict[stud]=len(stud_dict[stud])
        


#########################
# main code - do not delete this comment
# Tests have been added for your convenience.
# You can add more tests below.
#########################

if __name__ == '__main__': #Do not delete this line!
	# Q1
	#print(most_popular_characters('aabbAA') == 'Aab')

	# Q2
	#print(diff_sparse_matrices([{(1, 3): 2, (2, 7): 1}, {(1, 3): 6, (2, 7): 1, (3, 3): 3}, {(2, 7): 1}]) == {(1, 3): -4, (3, 3): 3,(2, 7): -1})
		
	# Q3
	print(find_substring_locations('', 3))
	print(find_substring_locations('TTAATTAGGGGCGC', 2) == {'TT': [0, 4], 'TA': [1, 5], 'AA': [2], 'AT': [3], 'AG': [6], 'GG': [7, 8, 9], 'GC': [10, 12], 'CG': [11]})
        
        
	# Q4
	stud_dict = courses_per_student([('Tom', 'Math'), ('Oxana', 'Chemistry'), ('Scoobydoo', 'python'), ('tom', 'pYthon'), ('Oxana', 'biology')])
		
	print(stud_dict == {'tom': ['math', 'python'], 'oxana': ['chemistry', 'biology'], 'scoobydoo': ['python']})
		
	num_courses_per_student(stud_dict)
	print(stud_dict == {'tom': 2, 'oxana': 2, 'scoobydoo': 1})


# ============================== END OF FILE =================================

