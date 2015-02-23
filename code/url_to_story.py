from newspaper import Article
import os
file_in = open('filtered_links.txt','rt')
filename = 1
# newspaper http://newspaper.readthedocs.org/en/latest/
'''given a url grab important text and title and generate a textfile for each article
- this will be passed for sentiment analysis'''
os.chdir("/Users/jgiesler/Desktop/PythonTwitter/data/forsentimate")

for line in file_in:
	#make file for output
	art_file = open(str(filename)+".txt",'wt')
	
	#parse url
	line = line.rstrip()
	url = line
	print("Extracting:" + url)
	
	#newspaper queries
	try:
		a = Article(url)
		a.download()
		a.parse()


		##output text,filenumber,url and data
		print(a.title, file = art_file)
		print(str(filename), file = art_file)
		print(url, file = art_file)
		print("",file = art_file)
		print(a.text, file = art_file)
	except:
		pass
	art_file.close()
	filename += 1

file_in.close()
print("\a")

