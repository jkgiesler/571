import requests

def read_in_statuses(filename):
	'''read in raw list of tweets and cleanup hashtags, urls, and add each word to a dict with its count'''
	file_in = open(filename,'rt')
	words_used = dict()
	for line in file_in:
		line = line.rstrip()
		line_list = line.split(' ')
		for i in line_list:
			#cleaning up hashtags
			if '#' in i:
				i = i[i.find("#"):]
				if("\\" in i):
					i = i[:i.find("\\")]
			if "\\" in i:
				pass
			else:
				if i in words_used:
					words_used[i] += 1
				else:
					words_used[i] = 1
	file_in.close()
	return words_used

def extract_real_urls(list_of_words):
	'''given twitters short urls generate real length urls and make a conversion dictionary'''
	url_dictionary = dict()
	for i in list_of_words:
		if "http://t.co" in i:
			try:
				start_idx =	i.find("http://")
				end_idx = start_idx + 22
				short_url = i[start_idx:end_idx]
				long_url = requests.get(short_url,stream = True).url
				url_dictionary[i] = long_url
				print(short_url + "||" + long_url)
			except:
				pass
	return url_dictionary

def parse_statuses(filename):
	'''uses other functions to print raw tweet list to 3 files (words,hashtags,urls [hopefully full] ) 
	with their frequencies'''
	temp_dict = read_in_statuses(filename)
	real_urls = extract_real_urls(list(temp_dict.keys()))
	words = open('words_stream31.txt','wt')
	hashtags = open('hashtags_stream31.txt','wt')
	links = open('links_stream31.txt','wt')
	for i in temp_dict.keys():
		if "#" in i:
			print(i + "\t" + str(temp_dict[i]),file = hashtags)
		elif "http" in i:
			try:
				print(real_urls[i] + "\t" + str(temp_dict[i]), file = links)
			except:
				print(i + "\t" + str(temp_dict[i]), file = links)
		else:
			print(i + "\t" + str(temp_dict[i]), file = words)
	words.close()
	hashtags.close()
	links.close()

parse_statuses("raw_stream31.txt")
print("\a")
