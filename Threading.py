import concurrent.futures.thread
import time
import requests

start = time.perf_counter()
img_urls = [
    'https://image.shutterstock.com/image-photo/barcelona-feb-23-lionel-messi-260nw-1900547713.jpg',
    'https://interesnyefakty.org/wp-content/uploads/Foto-Messi-2.jpg',
    'https://metaratings.ru/upload/iblock/63e/63ef19031e47ec85e5c2383ff0617794.jpg',
    'https://i.trbna.com/preset/wysiwyg/f/d3/8f91a99f211ebb97ee7bc846a68b2.jpeg',
    'https://billionnews.ru/uploads/posts/2021-04/1618316425_1.jpg',
    'https://metaratings.ru/upload/iblock/e2e/e2e7fff01929d3fe5e55084c6d52ebb3.jpg',
    'https://www.thesun.co.uk/wp-content/uploads/2020/02/NINTCHDBPICT000561582860-e1581328800320.jpg',
    'http://almode.ru/uploads/posts/2020-11/1604548983_11-p-lionel-messi-27.jpg',
    'https://images7.alphacoders.com/929/929970.jpg',
]
def download(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[3]
    img_name = f'{img_name}.jpg'
    with open(img_name,'wb') as img_files:
        img_files.write(img_bytes)
        print(f"{img_name}img was downloaded")

with concurrent.futures.ThreadPoolExecutor() as executor:
    f = executor.map(download,img_urls)

finish = time.perf_counter()
print(round(finish - start,2))
