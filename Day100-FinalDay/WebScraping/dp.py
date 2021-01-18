import bs4 as bs
import urllib.request

source = urllib.request.urlopen('*******************URL*******************').read()
soup = bs.BeautifulSoup(source,'html.parser')
table = soup.find('table', attrs={'id' : 'ctl00_ContentPlaceHolder1_gvst'})
res = []
table_rows = table.find_all('tr')
for tr in table_rows:
  td = tr.find_all('td')
  row = [tr.text for tr in td if tr.text]
  if row:
    print(row)
    res.append(row)
