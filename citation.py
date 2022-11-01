from requests_html import HTMLSession

session = HTMLSession()
htmlContent = session.get('http://evene.lefigaro.fr/citations/mot.php?mot=jour')

citationBalise = htmlContent.html.find('.figsco__quote__text', first=True)

citation = citationBalise.text