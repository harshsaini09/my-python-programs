def read_line(filename,n):
	f = open(filename,"r")
	lines = f.readlines()
	if (len(lines) <= n-1):
		print("None")
	else:
		print(lines[n])