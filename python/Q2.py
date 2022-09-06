'''question 2

Write a program which would take an list of integer and return a dictionary as output where odd numbers would have their cube and even numbers will have squares.

Ex-

i/p- a = [1,2,3,4,5] o/p- b = {1:1,2:4,3:27,4:16,5:125}'''


class list_dict_map:
    def __init__(self):
        self.list_nums = [1, 2, 3, 4, 5]
        self.list_mappedOP = []
    def mapping_list_dict(self):
    '''t=performs square on odd and cube on even numbers while iterating through list of integers'''
        for integer in self.list_nums:
            if integer % 2 == 0:
                integer ** 3
                print(integer, "and output is ", integer ** 3)
                self.list_mappedOP.append(integer ** 3)
            else:
                integer ** 2
                print(integer, "and output is ", integer ** 2)
                self.list_mappedOP.append(integer ** 2)

a = list_dict_map()
a.mapping_list_dict()
print(a.list_mappedOP)
d=dict()
'creating a dictionary to store while iterating through the mappped output and used for printing concise result'
for i in range(len(a.list_mappedOP)):
    d[i+1] = a.list_mappedOP[i]
print(d)