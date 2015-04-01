import os


#make a dictionary of dictionaries so the outer dictionary will be all years
#the inner dictionary is then all countries. a query to the dictionary is
#formed like gdp_dict['2006']['Korea']
#this will return korea's gdp in 2006
gdp_dict = dict()
gdps = open('gdps.txt','rt')
header = gdps.readline()
header = header.rstrip()
header_list = header.split('\t')
for line in gdps:
	line = line.rstrip()
	row = line.split('\t')
	for i in range(len(row)-1):	
		if header_list[i+1] in gdp_dict.keys():
			#if the year exists use the existing inner dictionary
			gdp_dict[header_list[i+1]][row[0]]=row[i+1]
		else:
			#if the year doesnt exist make an inner dictionary and use that.
			gdp_dict[header_list[i+1]]=dict()
			gdp_dict[header_list[i+1]][row[0]]=row[i+1]
gdps.close()

#now we just have to go through and append the gdp to each country for each year
#easy peasy.
for filename in os.listdir(os.getcwd()):
	year = filename[:filename.find('.')]#get just year for dictionary lookup
	#thankfully all of our data is in the 2000's so we can filter files like this
	#we also want to ignore combined files if they have been made
	if '2' in filename and 'combined' not in filename:
		file_in = open(filename,'rt')
		header = file_in.readline()
		header = header.rstrip()
		file_out = open('combined_'+year+'.txt','wt')
		print(header+'\t'+'GDP',file=file_out) #print out header with GDP added
		for line in file_in:
			line = line.rstrip()
			rows = line.split('\t')
			try:
				rows.append(gdp_dict[year][rows[0]])#gets GDP from dict and tacks it on the last column
			except:
				rows.append('NA')#we don't have data on this country

			print('\t'.join(rows),file=file_out)#print all rows to combined file.
		file_out.close()
		file_in.close()
