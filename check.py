def diff_sparse_matrices(lst):
    new_dic = {}
    diction_index = 0
    for dictions in lst:
        for key in dictions:
            if key in new_dic:
                new_dic[key] = new_dic[key] - dictions[key]
            elif not key in new_dic and diction_index > 0:
                new_dic[key] = -1*dictions.get(key, 0)
            else:
                new_dic[key] = dictions.get(key, 0) 
        diction_index += 1
    for dictions in lst:
        for new_key in new_dic.copy():
            if new_dic[new_key] == 0:
                new_dic.pop(new_key)

    return new_dic

print(diff_sparse_matrices([{(1, 3): 2, (2, 7): 1}, {(1, 3): 6}]) == {(1, 3): -4, (2, 7): 1})

print(diff_sparse_matrices([{(1, 3): 2, (2, 7): 1}, {(1, 3): 2}, {(1,3):1}]) == {(1, 3): -1, (2, 7): 1})
