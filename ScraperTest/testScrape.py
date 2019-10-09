from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait

from ScraperTest.DBHandler import addURLTable


def init_driver():
    driver = webdriver.Chrome()
    driver.set_page_load_timeout(100)
    return driver


def format_scraped_recipe(scraped_recipe):
    name_start_index = scraped_recipe.find("\"name\":") + 8
    name_stop_index = scraped_recipe.find("\",", name_start_index)
    name = scraped_recipe[name_start_index:name_stop_index]

    recpie_ingredients_start_index = scraped_recipe.find("\"recipeIngredient\":[\"") + 20
    recpie_ingredients_end_index = scraped_recipe.find("],", recpie_ingredients_start_index)
    recpie_ingredients = scraped_recipe[recpie_ingredients_start_index:recpie_ingredients_end_index]
    print("Name: " + name + "\nIngredients: " + recpie_ingredients)


def click(driver, element):
    driver.execute_script("arguments[0].click();", element)
    print("Clicking: " + element.text)


# Scrapes the urls for recipes in the food page and adds them to the database
# Last used from 200 to 1000
def scrape_recipe_urls(start_index, stop_index):
    driver = init_driver
    base_url = "https://www.food.com/recipe?ref=nav&pn="

    for page in range(start_index, stop_index):
        driver.get(base_url + str(page))
        elements_list = driver.find_elements_by_class_name("fd-recipe")
        print(len(elements_list))
        for e in elements_list:
            url = e.get_attribute("data-url")
            addURLTable(url)
            print("added: " + url)
        time.sleep(2)

    driver.close()


def scrape_recipe_info(recipe_url):
    driver = init_driver()
    driver.get(recipe_url)
    elements_list = driver.find_elements_by_tag_name("script")

    for element in elements_list:
        element_type = element.get_attribute("type")
        if element_type is not None and element_type == "application/ld+json":
            scraped_recpie = element.get_attribute("innerHTML")

    print(scraped_recpie)
    format_scraped_recipe(scraped_recpie)


#scrape_recipe_info("https://www.food.com/recipe/pizza-scrolls-229227")

