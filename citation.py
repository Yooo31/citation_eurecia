from requests_html import HTMLSession

session = HTMLSession()
htmlContent = session.get('http://evene.lefigaro.fr/citations/mot.php?mot=jour')

def getElement(css) :
  result = htmlContent.html.find(css, first=True).text

  return result

def getCitation() :
  citation = getElement('.figsco__quote__text')
  author = getElement('.figsco__quote__from')
  finalSentence = citation + ' ' + author

  return finalSentence