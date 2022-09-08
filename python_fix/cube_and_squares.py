'''question 2

Write a program which would take an list of integer and return a dictionary as output where
odd numbers would have their cube and even numbers will have squares.
py name: cube_and_squares.py

Ex-

i/p- a = [1,2,3,4,5] o/p- b = {1:1,2:4,3:27,4:16,5:125}

add summary and what code is doing
'''


class list_dict_map:
    def __init__(self):
        self.nums = [1, 2, 3, 4, 5]
        self.mapped_outputs = []

    def mapping_list_dict(self):

        for integer in self.nums:
            if integer % 2 == 0:
                integer ** 3
                print(integer, "and output is ", integer ** 3)
                self.mapped_outputs.append(integer ** 3)
            else:
                integer ** 2
                print(integer, "and output is ", integer ** 2)
                self.mapped_outputs.append(integer ** 2)

def start():
    a = list_dict_map()
    a.mapping_list_dict()
    print(a.mapped_outputs)
    d = dict()
    for i in range(len(a.mapped_outputs)):
        d[i + 1] = a.mapped_outputs[i]
    print(d)

if __name__ == "__main__":
    start()