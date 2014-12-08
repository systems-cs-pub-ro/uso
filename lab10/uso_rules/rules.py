import urllib2
from BeautifulSoup import BeautifulSoup

# Cerem pagina HTML de la adresa dorita
response = urllib2.urlopen('http://ocw.cs.pub.ro/courses/uso/punctaj')
html = response.read()

# Translatam continutul fisierului intr-un obiect
parsed_html = BeautifulSoup(html)

# Extragem informatia care ne intereseaza (liniile 8 - 15)
rules = parsed_html.body.findAll('div', attrs={'class':'li'})[8:15]

# Afisam fiecare linie din rezultat
print 'PUNCTAJ USO:'
for rule in rules:
    print rule.text
