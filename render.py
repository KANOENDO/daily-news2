from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch()
    pg=b.new_page(viewport={'width':794,'height':1123},device_scale_factor=2)
    pg.goto('file:///home/user/daily-news2/out/news.html')
    for i,h in enumerate(pg.query_selector_all('.page'),1):
        print(i,h.evaluate('e=>[e.scrollHeight,e.clientHeight]'))
        h.screenshot(path=f'/home/user/daily-news2/out/page{i}.png')
    pg.pdf(path='/home/user/daily-news2/out/news.pdf',width='794px',height='1123px',print_background=True)
    b.close()
