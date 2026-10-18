import re
t=open('template.html').read()
pages=open('pages.html').read()
open('out/news.html','w').write(t.replace('<!--PAGES-->',pages))
