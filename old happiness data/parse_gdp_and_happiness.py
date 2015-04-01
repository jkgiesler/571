##super hacky script to combine GDP text file with Happiness text file

file_in = open('happiness_by_country.txt','rt')
file_out = open('parsed_countries.txt','wt')
gdps_in = open('gdp_2000_2004.txt','rt')

country_names = list()
country_happiness = list()
country_gdp = list()
count = 1

gdp_dict = dict()

#add all gps to a dictionary
for line in gdps_in:
	line = line.rstrip()
	seper = line.split('\t')
	gdp_dict[seper[0]]=seper[1:]

for line in file_in:
	line = line.rstrip()
	line.replace(" ","") #get rid of weird spacing in original document
	if(count%2 != 0):
		country_names.append(line)
		try:
			country_gdp.append(gdp_dict[line])
		except:
			#don't have data on this country so insert a blank so data matches up
			country_gdp.append("")
	else:
		country_happiness.append(line)

	count +=1

for i in range(len(country_names)): #spit it all out into a nicely formatted text file
	print(country_names[i]+'\t'+country_happiness[i]+'\t'+"\t".join(country_gdp[i]),file = file_out)

file_out.close()
file_in.close()
gdps_in.close()