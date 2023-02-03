from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

linkedin_url = 'https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0'
s = Service("C:\development\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get(linkedin_url)
time.sleep(4)
url22='https://www.linkedin.com/login?emailAddress=&fromSignIn=&trk=public_jobs_conversion-modal-signin&session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fjobs%2Fsearch%2F%3Ff_LF%3Df_AL%26geoId%3D102257491%26keywords%3Dpython%2520developer%26location%3DLondon%252C%2520England%252C%2520United%2520Kingdom%26redirect%3Dfalse%26position%3D1%26pageNum%3D0'


#driver.find_element_by_id("submit").click()
login_button=driver.find_element(By.LINK_TEXT,value='Sign in').click()
input_key=driver.find_element(By.NAME,value='session_key')
input_password=driver.find_element(By.NAME,value='session_password')
driver.implicitly_wait(4)
input_key.send_keys('shlomo.mica@outlook.co.il')
input_password.send_keys('cccc')
time.sleep(1)
signin_button=driver.find_element(By.TAG_NAME,value='button').click()


#driver.implicitly_wait(8)
# <a class="cta-modal__primary-btn btn-md btn-primary inline-block !text-[20px] w-full mt-3 py-1.5 px-0.5 leading-[25px]" href="https://www.linkedin.com/login?emailAddress=&amp;fromSignIn=&amp;trk=public_jobs_conversion-modal-signin&amp;session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fjobs%2Fsearch%2F%3Ff_LF%3Df_AL%26geoId%3D102257491%26keywords%3Dpython%2520developer%26location%3DLondon%252C%2520England%252C%2520United%2520Kingdom%26redirect%3Dfalse%26position%3D1%26pageNum%3D0" data-tracking-control-name="public_jobs_conversion-modal-signin" data-tracking-will-navigate="">
#         Sign in
#       </a>
#<button class="btn__primary--large from__button--floating"
# data-litms-control-urn="login-submit"
# type="submit" aria-label="Sign in">Sign in</button>
