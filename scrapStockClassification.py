import requests
import csv
from BeautifulSoup import BeautifulSoup

def getStockClassification(stockCode):
  url = 'https://www.msn.com/en-in/money/stockdetails/company/fi-138.1.' + stockCode + '.NSE'
  response = requests.get(url)
  html = response.content
  soup = BeautifulSoup(html)
  classification = soup.find('div', attrs={'class':'caption-pair caption-style'})
  classification = classification.find('p', attrs={'class':'captionData'})
  return classification.text

def getAllStockClassification(stocks):
  allClassification = {}
  for stockCode in stocks:
    classification = ''
    try:
      classification = getStockClassification('INFY')
    except Exception, e:
      print str(e)
      classification = 'Error'
    finally:
      allClassification[stockCode] = classification
  print 'classification data fetch complete'
  return allClassification

def writeToCsv(source):
  with open('stockClassification.csv', 'wb') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in source.items():
       writer.writerow([key, value])
  return

stocks = ['test1','test2','test3']
writeToCsv(getAllStockClassification(stocks))
