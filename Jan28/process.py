"""Program to process data"""

def find_days(filename = "downloaded_issues.txt"):
	with open(filename) as f:
		before = 1419.34251881
		for i,line in enumerate(f):
			if i%100 == 0 and i != 0:
				print i*100,(before -  float(line.split()[3]))
				before = float(line.split()[3])



def find_cumdays(filename = "downloaded_issues.txt"):
	with open(filename) as f:
		before = 1419.34251881
		for i,line in enumerate(f):
			if i%100 == 0 and i != 0:
				print int(before - float(line.split()[3]))

if __name__ == '__main__': 
	find_cumdays()
	find_days()