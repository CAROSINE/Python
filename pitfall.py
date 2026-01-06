def append_to_list(val, list_=None):
    if list_ is None:
        list_ = []
    list_.append(val)
    return list_

print(append_to_list(1))
print(append_to_list(2, []))
print(append_to_list(3))
