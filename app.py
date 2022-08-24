from selenium import webdriver
from bs4 import BeautifulSoup
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def myProfile():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(executable_path=r'./chromedriver/chromedriver.exe', options=options)
    driver.get(url='https://www.op.gg/summoners/kr/hide%20on%20bush')

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    tear = soup.select_one('#content-container > div:nth-child(1) > div.css-er3yn6.e1x14w4w1 > div.content > div.info > div.tier')
    lp = soup.select_one('#content-container > div:nth-child(1) > div.css-er3yn6.e1x14w4w1 > div.content > div.info > div.lp')
    win_lose = soup.select_one('#content-container > div:nth-child(1) > div.css-er3yn6.e1x14w4w1 > div.content > div.win-lose')
    driver.close()

    return render_template('index.html', tear=tear, lp=lp, win_lose=win_lose)


if __name__ == '__main__':
    app.run()
