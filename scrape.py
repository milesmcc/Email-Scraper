# Email Scraper: a script for scraping the internet for email addresses.
#     Copyright (C) 2017 Miles McCain
#
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <http://www.gnu.org/licenses/>.

import requests
import sys
import random
from bs4 import BeautifulSoup
import re
from urlparse import urljoin

mini_dedup = [] # for local deduplication

# write a new email address to the file
def write_new_address(address):
    if address.strip() not in mini_dedup: # I could assign address.strip() to a variable but I won't
        with open("addresses.txt", "a+") as outfile:
            outfile.write(address.strip() + "\n")
            mini_dedup.append(address.strip())

# scrape scrape scrape
def crawl(max_queue_size, seeds):
    email_regex = re.compile(r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)")
    # max queue size for performance reasons, mostly
    urlpool = [seed for seed in seeds] # reiterate for shallow clone
    while len(urlpool) is not 0:
        print("Queue size: " + str(len(urlpool)))
        try:
            random.shuffle(urlpool) # it's not the most efficient way, but it's the most pythonic
            url = urlpool.pop()
            content = requests.get(url, timeout=2).content
            soup = BeautifulSoup(content, "lxml")
            urls = []
            for a in soup.find_all("a"):
                try:
                    urls.append(urljoin(url, a.attrs['href']))
                except:
                    pass # nothing can go wrong
            if len(urlpool) < max_queue_size:
                urlpool.extend(urls)
                # IT'S NOT PERFECT, IT ALLOWS FOR THE QUEUE TO GO PAST MAX SIZE SLIGHTLY,
                # BUT IT'S OK.
            emails_found = email_regex.findall(soup.prettify().replace("mailto:", " "))
            for email in emails_found:
                print("Found email: " + email)
                write_new_address(email)
        except Exception as e:
            print("error'ed, but moving on.")
            print(e)

if len(sys.argv) is not 3:
    print("Usage: <comma separated seed urls> <max queue size>")
    print(sys.argv)
else:
    seeds = sys.argv[1].split(",")
    max_size = int(sys.argv[2])
    print("Crawling...")
    crawl(max_size, seeds)
