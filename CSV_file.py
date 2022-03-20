def get_dic(filename):
	f = open(filename,"r")
	line = f.readlines()
	for i in range(1,len(line)):
		s = ":".join(line[i].split(","))
		print(s,end="")
get_dic("Student.csv")