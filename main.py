import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import os
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')


def getHtml(href):
    """
    获取页面内容
    :param href:页面地址
    :return:string
    """
    browser = webdriver.Chrome(options=options)
    browser.get(href)

    content = WebDriverWait(browser, 10).until(
        lambda x: x.find_element(By.XPATH, '//*[@id="main"]/div/div[3]/div[2]/div/div[2]/div'))
    """:type: selenium.webdriver.remote.webelement.WebElement"""
    ret = content.get_attribute("outerHTML")
    browser.close()
    return ret


def getMenu(url):
    """
    获取菜单
    :param url: 需要获取菜单的连接
    :return: array
    """
    browser = webdriver.Chrome(options=options)
    browser.get(url)
    button = WebDriverWait(browser, 10).until(
        lambda x: x.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[3]/div[1]/div/div[2]/div[4]/a"))
    """:type: selenium.webdriver.remote.webelement.WebElement"""
    button.click()
    hrefs = WebDriverWait(browser, 10).until(
        lambda x: x.find_elements(By.XPATH, '//*[@id="main"]/div/div[3]/div[1]/div[2]/div/ul/li/ul/li/a'))
    """:type: list[selenium.webdriver.remote.webelement.WebElement]"""
    ret = []
    for href in hrefs:
        ret.append({"title": href.get_attribute("innerHTML"), "href": href.get_attribute("href")})
    browser.close()
    return ret


if __name__ == '__main__':
    url = "https://www.kancloud.cn/manual/thinkphp6_0"
    dir = "thinkphp6"
    # 创建文件目录
    if not os.path.exists(dir):
        os.mkdir(dir)
    with open("template.html", "r", encoding="utf-8") as f:
        html = f.read()
        f.close()
        menu = getMenu(url)
        indexes = "["
        for item in menu:
            if indexes == "[":
                indexes += '{"t": "' + item["title"] + '", "p": "' + item["title"] + '.html","d":"' + item["href"] + '"}'
            else:
                indexes += ',{"t": "' + item["title"] + '", "p": "' + item["title"] + '.html","d":"' + item["href"] + '"}'
            htmlTemp = html.replace("{{title}}", item["title"])
            htmlTemp = htmlTemp.replace("{{content}}", getHtml(item["href"]))
            htmlTemp = htmlTemp.replace('<span class="ಠcopy-code-button">复制</span>', "")
            # 保存html文件
            with open(dir + "\\" + item["title"] + ".html", "w", encoding="utf-8") as w:
                w.write(htmlTemp)
                w.close()
            time.sleep(0.1)

    with open(dir + "\\indexes.json", "w", encoding="utf-8") as w:
        w.write(indexes + "]")
        w.close()
