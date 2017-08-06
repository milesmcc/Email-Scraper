# Email Scraper
This is exactly what you think it is. A quick and hacked-together email scraping script meant to cause as few headaches as possible. It's not perfect—for example, it'll match text like `illustration-fork@2x-79b491de4c9951a68bc6187a0e04afcedd01df430a371e744f3559a47fa57321.png` as an email, but otherwise it works quite well and is sure to satisfy your email scraping needs.

### Why?
Firstly, I'll mention that it's very early in the morning but I wanted to push something to GitHub. Secondly, it's very important that people understand the ease in scraping the internet for email addresses. I made this script so anyone can do it.

**Please don't use this tool to build your own super-evil email list.** Just use it as a proof-of-concept tool.

### How It Works
This tool is extremely simple. It's operation can be described (with a few details omitted) in five bullet points:
* Pick a random url from the queue
* Go to the URL and get the contents
* Look for all the links and add them back into the queue
* Look for all the email addresses and add them into a text file at `./addresses.txt`
* (repeat)

### How to Use
Simply run the script `./scrape.py` and provide the necessary arguments, and then let it go! Arguments are specified by the script, so if you're confused, you can just run the script with no arguments and read the error message it gives you.

## License
This code is licensed under GPLv3. See the `LICENSE` fill for more details.
