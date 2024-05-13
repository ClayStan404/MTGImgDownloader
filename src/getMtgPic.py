#!/usr/bin/python
import requests
from bs4 import BeautifulSoup
import os


def download_image(url, filename):
    filename='imgs/'+filename
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
        cmdShell = '''convert "'''+filename + \
            '''" -resize '745x745^' -gravity center -extent 1000x1000 "''' + filename+'''"'''
        os.system(cmdShell)
    else:
        print('Download faild:', response.status_code)


def get_image_url(cardSet, cardNo):
    baseurl = 'https://scryfall.com/card'
    #  url = baseurl+'/'+cardSet+'/'+cardNo+"/zhs"
    url = baseurl+'/'+cardSet+'/'+cardNo

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    cardName = soup.find_all('title')[0].text.split('·')[0]+cardSet+'_'+cardNo
    fileName = cardName+'.jpg'
    #  fileName = "default-"+cardSet+cardNo+'.jpg'
    #  fileName = '_'.join(image_elements[0]['alt'].split('(')[0].split())+'.jpg'
    image_elements = soup.find_all('img')
    image_url = image_elements[0]['src']
    if image_url.startswith('http'):
        fileName = '_'.join(
            image_elements[0]['alt'].split('(')[0].split())+cardSet+'_'+cardNo+'.jpg'
        fileName = fileName.replace('_//', '')
        download_image(image_url, fileName)
        print("download from scryfall: ", cardName)
    else:
        print('faild parse url from scryfall,try it again from mtgpics')
        image_url = 'https://www.mtgpics.com/pics/big/'+cardSet+'/'+cardNo+'.jpg'
        download_image(image_url, fileName)
        print("download from mtgpics: ", cardName)


def main():
    with open("MTGCardList", "r") as f:
        for line in f:
            values = line.split()  # Split the line by whitespace
            if len(values) == 2:  # Check if there are exactly two values
                cardSet, cardNo = values  # Extract the key and value
                get_image_url(cardSet, cardNo)


if __name__ == '__main__':
    main()
