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


def get_zhs_cardName(url, cardSet, cardNo):
    response = requests.get(url)
    if response.status_code != 200:
        cardNameZh = ''
        return cardNameZh
    soup = BeautifulSoup(response.content, 'html.parser')
    cardNameZh = soup.find_all('title')[0].text.split(
        '·')[0].split('//')[0]+cardSet+' '+cardNo
    return cardNameZh


def get_image_url(url, cardSet, cardNo):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    image_elements = soup.find_all('img')
    image_url = image_elements[0]['src']
    if image_url.startswith('http'):
        fileName = '_'.join(
            image_elements[0]['alt'].split('(')[0].split()).split('_//')[0]+'-'+cardSet+'-'+cardNo+'.jpg'
        download_image(image_url, fileName)
        cardNameEn = fileName.strip('.jpg').replace('-', ' ').replace('_', ' ')
        #  print("download: ", cardNameEn)
    else:
        cardNameEn = "default "+cardSet+' '+cardNo
        print('faild parse url from scryfall: ', cardNameEn)
        #  image_url = 'https://www.mtgpics.com/pics/big/'+cardSet+'/'+cardNo+'.jpg'
        #  download_image(image_url, fileName)
        #  print("download from mtgpics: ")
    return cardNameEn


def main():
    baseurl = 'https://scryfall.com/card'
    with open("MTGCardList", "r") as f:
        for line in f:
            cardInfo = line.split()
            if len(cardInfo) == 3:
                cardSet, cardNo, cardLang = cardInfo
            elif len(cardInfo) == 2:
                cardSet, cardNo = cardInfo
                cardLang = ''
            else:
                print("illegal line: ", line)
                continue
            match cardLang:
                case 'z':
                    cardUrlLang = "/zhs"
                case 'f':
                    cardUrlLang = "/fr"
                case 'd':
                    cardUrlLang = "/de"
                case 'j':
                    cardUrlLang = "/ja"
                case _:
                    cardUrlLang = ""

            try:
                url = baseurl+'/'+cardSet+'/'+cardNo+cardUrlLang
                cardNameEn = get_image_url(url, cardSet, cardNo)
            except IndexError:
                url = baseurl+'/'+cardSet+'/'+cardNo
                cardNameEn = get_image_url(url, cardSet, cardNo)
            except Exception as e:
                raise e
            zhsUrl = baseurl+'/'+cardSet+'/'+cardNo+'/zhs'
            cardName = get_zhs_cardName(zhsUrl, cardSet, cardNo)
            if cardName == "":
                cardName = cardNameEn
            print("download: ", cardName)
            shellCMD = 'echo "'+cardName+'" >> cardList'
            os.system(shellCMD)


if __name__ == '__main__':
    main()
