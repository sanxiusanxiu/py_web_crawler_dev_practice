import requests
import logging
import time

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

url = 'https://www.httpbin.org/delay/5'
total_number = 100

start_time = time.time()
for i in range(1, total_number + 1):
    logging.info(f'Scraping %s... {url}')
    response = requests.get(url)
end_time = time.time()
# 2025-01-16 09:23:43,910 - INFO - Total time: 622.6026341915131 seconds
logging.info(f'Total time: {end_time - start_time} seconds')
