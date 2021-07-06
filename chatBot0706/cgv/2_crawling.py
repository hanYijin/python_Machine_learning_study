# 2_crawling.py
# 현재 상영정보를 받아오는 함수를 포함한 코드

import requests
from bs4 import BeautifulSoup
import datetime

def crawl_schedule(areaCode, theaterCode):
	# 오늘자 지정된 지역과 영화관의 데이터 크롤링
	date = datetime.datetime.now().strftime("%Y%m%d")
	URL = f'http://www.cgv.co.kr/reserve/show-times/?areacode={areaCode}&theaterCode={theaterCode}&date={date}'
	req = requests.get(URL)
	html = req.text
	soup = BeautifulSoup(html, 'html.parser')
	soup = soup.select('body > div > div')
	print(soup)
	movies = soup[0].find_all("div", {"class" : "sect-showtimes"})
	print(movies)
	obj = {}
	for movie in movies:
		title = movie.select_one('div > div.info-movie > a > strong').get_text().strip()
		timetable = get_timetable(movie)
		obj[title] = timetable
	return obj

def get_timetable(movie):
	tuples = []
	timetables = movie.select('div > div.type_hall > div.info_timetable > ul > li')
	for timetable in timetables:
		time = timetable.select_one('a > em').get_text()
		seat = timetable.select_one('a > span').get_text()
		tup = (time, set)
		tuples.append(tup)
	return tuples

if __name__== "__main__":
	test = crawl_schedule('01', '0030')