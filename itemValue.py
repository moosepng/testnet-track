import requests
import re
from bs4 import BeautifulSoup

def puppyscan(item):
    url = "https://puppyscan.shib.io/"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        if item == 5:
            #5-daily transactions
            daily_tr_span_soup = soup.find('span', {'data-selector': f'tx_per_day'}).text
            item_value = re.sub(r'\s+', '', daily_tr_span_soup)
        else:    
            #1-avg block, 2-total transactions, 3-total blocks, 4-wallet addresses
            avg_blk_div_soup = soup.find('div', {'class': f'dashboard-banner-network-stats-item dashboard-banner-network-stats-item-{item}'})
            avg_blk_span_soup = avg_blk_div_soup.find('span', {'class' : 'dashboard-banner-network-stats-value'}).text
            item_value = re.sub(r'\s+', '', avg_blk_span_soup)
        
        if item == 1:
            item_value = re.sub(r"^(\d+\.\d+)([a-zA-Z]).*", r"\1\2", item_value)
        
        return item_value
    else:
        print(f"Request failed with status code: {response.status_code}")
        return " "