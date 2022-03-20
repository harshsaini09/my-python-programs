new_l = []
def get_max_line(filename):
    f = open(filename,"r")
    for i in f:
    	new_l.append(i)
    print(new_l.index(max(new_l))+1)
    print(max(new_l))
get_max_line("test.txt")