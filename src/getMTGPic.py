#!/usr/bin/python
import requests
from bs4 import BeautifulSoup
import os


def download_image(url, filename):
    filename = 'imgs/'+filename
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
        cmdShell = '''convert "'''+filename + \
            '''" -resize '745x745^' -gravity center -extent 1000x1000 "''' + filename+'''"'''
        os.system(cmdShell)
    else:
        print('Download faild:', response.status_code)


def get_image_url(url, cardSet, cardNo):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    cardName = soup.find_all('title')[0].text.split(
        '·')[0].split('//')[0]+cardSet+'_'+cardNo
    image_elements = soup.find_all('img')
    image_url = image_elements[0]['src']
    if image_url.startswith('http'):
        fileName = '_'.join(
            image_elements[0]['alt'].split('(')[0].split()).split('_//')[0]+'-'+cardSet+'-'+cardNo+'.jpg'
        download_image(image_url, fileName)
        print("download from scryfall: ", cardName)
    else:
        print('faild parse url from scryfall,try it again from mtgpics')
        image_url = 'https://www.mtgpics.com/pics/big/'+cardSet+'/'+cardNo+'.jpg'
        fileName = cardSet+'_'+cardNo+'.jpg'
        download_image(image_url, fileName)
        print("download from mtgpics: ", cardName)
    return cardName


def main():
    baseurl = 'https://scryfall.com/card'
    with open("MTGCardList", "r") as f:
        for line in f:
            cardInfo = line.split()
            if len(cardInfo) == 2:
                cardSet, cardNo = cardInfo
                try:
                    url = baseurl+'/'+cardSet+'/'+cardNo+"/zhs"
                    cardName = get_image_url(url, cardSet, cardNo)
                except IndexError:
                    url = baseurl+'/'+cardSet+'/'+cardNo
                    cardName = get_image_url(url, cardSet, cardNo)
                except Exception as e:
                    raise e
                shellCMD = 'echo "'+cardName+'" >> cardList'
                os.system(shellCMD)
            else:
                print("illegal line: ", line)
                continue


if __name__ == '__main__':
    main()
