from selenium import webdriver
from flask import Flask, request
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

app = False(__name__)

def download():
    opt = webdriver.ChromeOptions()
    opt.add_argument("--headless")
    opt.add_argument("--no-sandbox")
    opt.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=opt)
    driver.get("https://google.com")
    title = driver.title
    data = {"title":title}
    return data

@app.route('/', methods=["GET","POST"])
def home():
    if request.method == "GET":
        return download()


if __name__ == "__main__":
    app.run(debug=True, port=3000)