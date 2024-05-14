# MTG Image Downloader
Download specific MTG card image from [Scryfall](https://scryfall.com/)

And convert it to a one-to-one size to meet the main image requirements of the damn Taobao.

## requirements

`python3 > 3.10.0`

`python-requests`

`python-BeautifulSoup`

[imagemagick](https://imagemagick.org/script/download.php):If you are using Windows, you may need to modify the execution path of convert command.



## 中文

从 [Scryfall](https://scryfall.com/) 下载万智牌卡图，并且将其转为 `1:1` 的比例, 以便适应上架淘宝的要求。

在 MTGCardList 中填写你需要下载的万智牌卡图信息，目前一共有三列值

| 系列代号 | 卡牌编号 | 文字 |
| :------: | :------: | :--: |
|   2x2    |   361    |  z   |
|   lci    |    55    |  j   |

第一列是系列代号，一般在牌的左下角，比如双星大师2(`Double Masters 2022`)的系列代号是 `2x2`，指挥官大师是 `cmm`，当然会有一些特殊画的牌并不是在左下角，比如蚀刻闪的莲花瓣，代号是 `p30m`，兄弟之战老框的牌，系列编号是 `brr` ，这些可以去 **Scryfall** 查询到。

第二列是卡牌本身的编号，比如双星大师2的异画闪电击，可以在左下角看到牌本身的编号是 361，同样的，一些特殊的牌需要去 **Scryfall** 查询

第三列是卡图的文字，`z` 代表简体中文，`j` 代表日文，`d` 代表德文，`f` 代表法文，为空或其他值则是英文，可能存在实体卡图存在某文字，但是 **Scryfall** 没有的情况，如果没有该文字则脚本会自动修改为下载英文
