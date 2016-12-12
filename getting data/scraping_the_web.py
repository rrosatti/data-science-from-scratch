from bs4 import BeautifulSoup
import requests
from time import sleep
import re
import matplotlib.pyplot as plt
from collections import Counter

url = "http://shop.oreilly.com/category/browse-subjects/data.do?sortby=publicationDate&page=1"

books = []

NUM_PAGES = 5

'''
# find all the td thumbtext tag elements
tds = soup('td', 'thumbtext')
print len(tds)
'''

def is_video(td):
	# it's a video if it has exactly one pricelabel, and if the stirpped text inside that pricelabel starts with 'Video'
	pricelabels = td('span', 'pricelabel')
	return (len(pricelabels) == 1 and pricelabels[0].text.strip().startswith('Video'))

def book_info(td):
	# the book title is inside the <a> tag inside the <div class="thumbheader">
	title = td.find('div', 'thumbheader').a.text

	# the author(s) are in the text of AuthorName <div>. Here we will get rid of the 'By' and the commas
	author_name = td.find('div', 'AuthorName').text
	authors = [x.strip for x in re.sub('^By ', '', author_name).split(',')]

	# the ISBN is contained in the link inside the <div>
	isbn_link = td.find('div', 'thumbheader').a.get('href')
	# re.match captures the part of the regex in parentheses
	isbn = re.match('/product/(.*)\.do', isbn_link).group(1)

	# the date is the content of the <span class="directorydate">
	date = td.find('span', 'directorydate').text.strip()	

	return {
		'title': title,
		'authors': authors,
		'isbn': isbn,
		'date': date
	}

def get_year(book):
	# the result of book['date'] is 'November 2014', so we need to split on the space and then take the second piece
	return int(book['date'].split()[1])

for page_num in range(1, NUM_PAGES + 1):
	print 'souping page', page_num, ',', len(books), ' found so far'
	url = url + str(page_num)
	soup = BeautifulSoup(requests.get(url).text, 'html5lib')

	for td in soup('td', 'thumbtext'):
		if not is_video(td):
			books.append(book_info(td))

	# respecting the terms of the O'really site and waiting 30 seconds before another request
	sleep(30)	

# ploting the number of books published each year
year_counts = Counter(get_year(book) for book in books if get_year(book) <= 2016)

years = sorted(year_counts)
book_counts = [year_counts[year] for year in years]
plt.plot(years, book_counts)
plt.ylabel('# of data books')
plt.title('Scraping the Web!')
plt.show()
