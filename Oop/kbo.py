import requests

from bs4 import BeautifulSoup

req = requests.get("https://www.koreabaseball.com/TeamRank/TeamRank.aspx")

# html코드 불러오기
html = req.text

#print(html)


# html 코드를 메모리 상에 올려 텍스트 객체화 >> BS

soup = BeautifulSoup(html, 'html.parser')



trs = soup.select('#cphContents_cphContents_cphContents_udpRecord table tbody tr')   #=id

#print(target)

for line in trs:
    #print(line)
    tds = line.select('td')
    print(tds[0].text, tds[1].text)
    print("-------------------------------------------------------------")