# -*- coding: utf-8 -*-
"""
Created on Fri May 22 16:36:46 2020

@author: Miguel
"""

import bs4, requests

def getAmazonPrice(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status()
    
    soup = bs4.BeautifulSoup(res.txt, 'html.parser')
    elems = soup.select('document.querySelector("#buyNewSection > h5 > div > div.a-column.a-span8.a-text-right.a-span-last > div > span.a-size-medium.a-color-price.offer-price.a-text-normal")')
    return elems[0].text.sptrip()
    
    
    
    

    
price = getAmazonPrice('https://www.amazon.com/Automate-Boring-Stuff-Python-Programming/dp/1593275994')
print('the price is ' + price)