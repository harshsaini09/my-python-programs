new_l = []
def get_max_line(filename):
    f = open(filename,"r")
    for i in f:
    	new_l.append(int(i))
    print(new_l.index(max(new_l))+1)
get_max_line("test.txt")