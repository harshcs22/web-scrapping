(a) How you have implemented the scraper, what challenges you faced, and how did you solve them?

Library used: 
bs4-BeautifulSoup for web scraping and html parsing.
request- for accessing URL.
pandas- for storing data and exporting 

Created a search function that searched tag and class name of html for specific string. I faced an issue while accessing URL, as it asked for captcha verification. So I redirected the url to a link that displays all the reviews for the particular product and was able to extract data for the same.

(b) What else you could do to improve your scraper?

I can put all the search commands under one loop so that multiple iterations can be stopped and time complexity decreases

(c) How would you design it to make it work on other retailers as well?

By creating a list of keywords(tags,className) that are needed and iterating them, we can scrap data from any type of retail website, just URL has to be added.