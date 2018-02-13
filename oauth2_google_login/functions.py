from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from os import listdir
from os.path import isfile, join
from requests_oauthlib import OAuth2Session
import json


def __get_client_secret_file__(filename):
    json_data = open(filename)
    d = json.load(json_data)["web"]
    json_data.close()
    return d


def get_access_token(username, password, client_id = "", client_secret = "", scope= [], driver = None):

    if driver == None:
        driver = webdriver.Chrome()

    auth_uri = "https://accounts.google.com/o/oauth2/auth",
    token_uri = "https://accounts.google.com/o/oauth2/token"
    authorization_base_url = "https://accounts.google.com/o/oauth2/v2/auth"
    redirect_uri = 'https://localhost:8080/'

    google = OAuth2Session(client_id, redirect_uri=redirect_uri, scope=scope)

    authorization_url, state = google.authorization_url(authorization_base_url, access_type="offline", prompt="select_account")

    driver.get(authorization_url)

    username_elem = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, 'identifierId')))
    username_elem.send_keys(username)
    driver.find_element_by_id("identifierNext").click()

    password_elem = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.NAME, 'password')))
    password_elem.send_keys(password)
    driver.find_element_by_id("passwordNext").click()

    if len(WebDriverWait(driver, 3).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="view_container"]/form/div[2]/div/div/div/ul/li[1]/div')))) != 0:
        driver.find_element_by_xpath('//*[@id="view_container"]/form/div[2]/div/div/div/ul/li[1]/div').click()


    next_btn = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, 'submit_approve_access')))
    next_btn.click()

    wait = WebDriverWait(driver, 10)
    wait.until(lambda driver: redirect_uri in driver.current_url)

    redirect_response = driver.current_url

    google.fetch_token(token_uri, client_secret=client_secret, authorization_response=redirect_response)

    driver.close()

    return google
