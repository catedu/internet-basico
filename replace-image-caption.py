import re, os

mds = []
pattern = r'\[.*\]\('

for root, dirs, files in os.walk(os.getcwd()):
	for file in files:
		if file.endswith('.md'):
			mds.append(file)
	
mds.sort()

for file in mds:
	tmp_file = str(file) + '1'
	file_name = str(file)
	with open(file, 'r') as infile, open(tmp_file, 'w') as outfile:
		for line in infile:
			if 'Fig. ' in line:
				line = line.replace('.', '-')
				line = re.sub(pattern, '', line)
				line = line.replace(')', '')
			outfile.write(line)
	os.remove(file)
	os.rename(tmp_file, file_name)

