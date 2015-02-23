
##get rid of shitty utf-8 characters. who really needs them???
import codecs
file_out = open("outfile.txt",'wt')
f = codecs.open("sentiment.txt","r","UTF-8")
for line in f:
	try:
		print(line,file = file_out)
	except:
		pass

f.close()
file_out.close()



#now that we have a clean file - extract the numbers and move to R!
file_in = open("outfile.txt",'rt')
file_out = open("output_for_R.txt",'wt')
for line in file_in:
	line = line.rstrip()

	if 'Sentiment(p' in line:
		polarity = line[line.find('polarity=')+9:line.find(',')]
		subjectivity = line[line.find('subjectivity=')+13:line.find(')')]
		print(polarity + '\t' + subjectivity, file = file_out)

file_in.close()
file_out.close()


