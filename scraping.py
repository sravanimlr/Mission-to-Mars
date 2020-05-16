
# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import datetime as dt

def scrape_all():
    # Initiate headless driver for deployment
    browser = Browser("chrome", executable_path="chromedriver", headless=True)
    # Set the executable path and initialize the chrome browser in splinter
    #executable_path = {'executable_path': 'chromedriver'}
    #browser = Browser('chrome', **executable_path)

    news_title, news_paragraph = mars_news(browser)
    # Run all scraping functions and store results in dictionary
    data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image(browser),
        "facts": mars_facts(),
        "last_modified": dt.datetime.now()
    }

    browser.quit  
    return data 

def mars_news(browser):

    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    # Optional delay for loading the page
    browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)

    html = browser.html
    news_soup = BeautifulSoup(html, 'html.parser')

# Add try/except for error handling
    try:
        slide_elem = news_soup.select_one('ul.item_list li.slide')
        slide_elem.find("div", class_='content_title')

        # Use the parent element to find the first `a` tag and save it as `news_title`
        news_title = slide_elem.find("div", class_='content_title').get_text()

        # Use the parent element to find the paragraph text
        news_p = slide_elem.find('div', class_="article_teaser_body").get_text()
    except AttributeError:
        return None, None

    return news_title, news_p


def featured_image(browser):
    # Visit URL
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)

    # Find and click the full image button
    full_image_elem = browser.find_by_id('full_image')
    full_image_elem.click()

    # Find the more info button and click that
    browser.is_element_present_by_text('more info', wait_time=1)
    more_info_elem = browser.find_link_by_partial_text('more info')
    more_info_elem.click()

    # Parse the resulting html with soup
    html = browser.html
    img_soup = BeautifulSoup(html, 'html.parser')
    try:
        # Find the relative image url
        img_url_rel = img_soup.select_one('figure.lede a img').get("src")

    except AttributeError:
        img_url_rel = ""

    img_url = f'https://www.jpl.nasa.gov{img_url_rel}'  
    return img_url

#Hemisphere 1
def hemi_one(browser):
    #visit the URL
    url_hemi_one = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'
    browser.visit(url_hemi_one)

    full_image_hemi_one = browser.find_by_text('Sample')
    full_image_hemi_one.click()

    html = browser.html
    img_hemi_one = BeautifulSoup(html, 'html.parser')

    try:
        #find the relative image URL
        img_url_rel_hemi_one = img_soup.select_one('body.overflowingVertical img').get("src")
        
    except AttributeError:
        img_url_rel_hemi_one = ""
        
    img_url_hemi_one = f'https://astrogeology.usgs.gov{img_url_rel_hemi_one}'
    return img_url_hemi_one

#Hemishphere 1 title
def hemi_title_one(browser):

    hemi_one_title_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'
    browser.visit(hemi_one_title_url)
    html = browser.html
    title_soup = BeautifulSoup(html, 'html.parser')
    try:
        hemi_title_one = title_soup.select_one('title')

    except AttributeError:
        return None

    return hemi_title_one

#Hemisphere 2
def hemi_two(browser):
    #visit the URLS
    url_hemi_two = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'
    browser.visit(url_hemi_two)

    full_image_hemi_two = browser.find_by_text('Sample')
    full_image_hemi_two.click()

    html = browser.html
    img_hemi_two = BeautifulSoup(html, 'html.parser')

    try:
        #find relative image URL
        img_url_rel_hemi_two = img_soup.select_one('body.overflowingVertical img').get("src")

    except AttributeError:
        img_url_rel_hemi_two = ""

    img_url_hemi_two = f'https://astrogeology.usgs.gov{img_url_rel_hemi_two}'
    return img_url_hemi_two

#Hemishphere 2 title
def hemi_tltle_two(broswer):
    hemi_two_title_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'
    browser.visit(hemi_two_title_url)
    html = browser.html
    title_soup = BeautifulSoup(html, 'html.parser')
    try:
        hemi_title_two = title_soup.select_one('title')
    
    except AttributeError:
        return None

    return hemi_title_two

#Hemisphere 3
def hemi_three(browser):
    #visit the URLS
    url_hemi_three = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'
    browser.visit(url_hemi_three)

    full_image_hemi_three = browser.find_by_text('Sample')
    full_image_hemi_three.click()

    html = browser.html
    img_hemi_three = BeautifulSoup(html, 'html.parser')

    try:
        #find relative image URL
        img_url_rel_hemi_three = img_soup.select_one('body.overflowingVertical img').get("src")

    except AttributeError:
        img_url_rel_hemi_three = ""

    img_url_hemi_three = f'https://astrogeology.usgs.gov{img_url_rel_hemi_three}'
    return img_url_hemi_three

#Hemishphere 3 title
def hemi_title_three(browser):
    hemi_three_title_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'
    browser.visit(hemi_three_title_url)
    html = browser.html
    title_soup = BeautifulSoup(html, 'html.parser')
    try:
        hemi_title_three = title_soup.select_one('title')
    except AttributeError:
        return None

    return hemi_title_three

#Hemisphere 4
def hemi_four(browser):
    #visit the URLS
    url_hemi_four = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'
    browser.visit(url_hemi_four)

    full_image_hemi_four = browser.find_by_text('Sample')
    full_image_hemi_four.click()

    html = browser.html
    img_hemi_four = BeautifulSoup(html, 'html.parser')

    try:
        #find relative image URL
        img_url_rel_hemi_four = img_soup.select_one('body.overflowingVertical img').get("src")

    except AttributeError:
        img_url_rel_hemi_four = ""

    img_url_hemi_four = f'https://astrogeology.usgs.gov{img_url_rel_hemi_four}'
    
    return img_url_hemi_four

#Hemishphere 4 title
def hemi_title_four(browser):
    hemi_four_title_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'
    browser.visit(hemi_four_title_url)
    html = browser.html
    title_soup = BeautifulSoup(html, 'html.parser')
    try:
        hemi_title_four = title_soup.select_one('title')
    except AttributeError:
        return None

    return hemi_title_four
 
def mars_facts():
    try:
        df = pd.read_html('http://space-facts.com/mars/')[0]

    except BaseException:
        return None

    df.columns=['description', 'value']
    df.set_index('description', inplace=True)
    
    return df.to_html()

if __name__ == "__main__":
    # If running as script, print scraped data
    print(scrape_all())



