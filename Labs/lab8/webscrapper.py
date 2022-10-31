from selenium import webdriver

url = 'https://www.youtube.com/watch?v=CHUxmVVH2AQ'
browser = webdriver.Chrome()
browser.get(url) 
browser.find_element_by_xpath('//*[@id="movie_player"]/div[1]/video').click()