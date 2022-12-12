import requests, openpyxl
from bs4 import BeautifulSoup

#For making a new Excel File and Giving rows names and writing title 
newExcelFile = openpyxl.Workbook()
sheet = newExcelFile.active
sheet.title = 'Top Rated Movies On IDMB 2022'
sheet.append(['Movie Rank','Name','Year of Release','Rating'])

#Code for scraping data of top 250 movies form IDMB website
try:
    url = requests.get("https://www.imdb.com/chart/top/?ref_=nv_mv_250")
    soup = BeautifulSoup(url.text,'html.parser')
    body = soup.find("tbody", class_="lister-list").find_all('tr')

    for movies in body:
        rank = movies.find('td',class_="titleColumn").get_text(strip=True).split('.')[0]
        name = movies.find('td',class_="titleColumn").a.text
        year = movies.find('td',class_="titleColumn").find('span').text
        rating = movies.find('td', class_="ratingColumn imdbRating").strong.text
        print(rank,name,year,rating)
        sheet.append([rank,name,year,rating])
 except Exception as e:
    print(e)

#code to save excel file
newExcelFile.save("IDMB Rating 2022.xlsx")

