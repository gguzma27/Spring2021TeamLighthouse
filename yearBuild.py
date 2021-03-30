import numpy

def yearBuild():
	i=0
	yearList = []
	year = 1900

	while i<121:
		yearList.append(str(year))
		year += 1
		i += 1
	return yearList

	
if __name__ == "__main__":
	yearBuild()
