import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException

#Parameters
source_airport = "DUB"
destination_airport = "SXF"
email = "rymatjan@wp.pl"
password = "Qwertyui1"
cardnumber = "11111111111111"
page = "Ryanair"

#Opening browser
driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://www.ryanair.com/ie/en/")

try:
	assert page in driver.title
	print("Welcome on Ryanair page")
except AssertionError:
	print("This is not Ryanair page")
	driver.close()


#Selecting on way flight
inputElement = driver.find_element_by_xpath("//*[@id='flight-search-type-option-one-way']")
inputElement.click()

#Source Airport
field_from_airport = driver.find_element_by_xpath("/html/body/div[2]/main/article/div[2]/smart-search/div/div[2]/div/div/form/div[2]/div/div/div/div[2]/div[2]/div/div/input")
field_from_airport.click()
field_from_airport.send_keys(source_airport)
field_from_airport.send_keys(Keys.ENTER)

#Destination Airport
field_to_airport = driver.find_element_by_xpath("/html/body/div[2]/main/article/div[2]/smart-search/div/div[2]/div/div/form/div[2]/div/div/div[2]/div[2]/div[2]/div/div/input")
field_to_airport.click()
field_to_airport.send_keys(destination_airport)
field_to_airport.send_keys(Keys.ENTER)

#Selecting month
next_month = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, ".//button[@class='arrow right']"))).click()
next_month = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, ".//button[@class='arrow right']"))).click()
next_month = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, ".//button[@class='arrow right']"))).click()
next_month = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, ".//button[@class='arrow right']"))).click()

input_date_from = driver.find_element_by_xpath("//*[@data-id='26-06-2018']").click()


#Passengers
passengers = driver.find_element_by_xpath("//*[@class='dropdown-handle']").click()
adults = driver.find_element_by_xpath("//*[@class='content']//div[@label='Adults']//button[@class='core-btn inc core-btn-wrap']").click()
child = driver.find_element_by_xpath("//*[@class='content']//div[@label='Children']//button[@class='core-btn inc core-btn-wrap']").click()

#continue to next page
lets_go = driver.find_element_by_xpath("//div[@class='col-flight-search-right']//button[@class='core-btn-primary core-btn-block core-btn-big']").click()


page_load = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, ".//*[@class='flight-header__min-price hide-mobile']"))).click()

#Ticket selection
select_ticket = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, ".//*[@class='flights-table-fares__head']"))).click()
accept_ticket = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//div[@class='flight-selector__listing-footer']//button[@id='continue']"))).click()
got_it = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,".//button[@class='core-btn-primary same-seats']"))).click()

#Seats selection

try:
	adult_1 = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[7]/div[2]/div[1]/div/div[3]/dialog-body/seat-map/div[2]/div[1]/div/div[2]/div[14]/div[5]/span/span"))).click()
except TimeoutException:
	print("No seat available")

try:
	child = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[7]/div[2]/div[1]/div/div[3]/dialog-body/seat-map/div[2]/div[1]/div/div[2]/div[14]/div[6]/span/span"))).click()
except TimeoutException:
	print("No seat available")

try:
	adult_2 = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[7]/div[2]/div[1]/div/div[3]/dialog-body/seat-map/div[2]/div[1]/div/div[2]/div[14]/div[7]/span/span"))).click()
except TimeoutException:
	print("No seat available")
	driver.close()



#Confirmation
confirmation = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,".//div[@class='dialog-overlay-footer footer-container']//span[@class='tooltip-disabled-cta-button-wrapper core-btn-phone-full']"))).click()
time.sleep(3)
confirmation_2 = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,".//div[@class='dialog-overlay-footer footer-container']//span[@class='tooltip-disabled-cta-button-wrapper core-btn-phone-full']"))).click()

#closing popup window
no_thanks = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,".//a[@class='priority-boarding-with-bags-popup__close core-link-inline']"))).click()

#Checking out
check_out = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH,".//button[@class='core-btn-primary core-btn-block core-btn-medium btn-text']"))).click()

#closing popup window
close_popup = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH,".//div[@class='popup-msg__close']"))).click()

#login to myRyanair account
login = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,".//button[@class='core-btn-secondary']"))).click()
time.sleep(5)
put_email = driver.find_element_by_xpath(".//*[@class='dialog-body']//div[@class='modal-right signup-home-carousel']//div[@class='modal-form-container']//div[@class='form-field']//input[@type='email']")
put_email.click()
put_email.send_keys(email)
time.sleep(2)
put_password = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH,".//*[@class='dialog-body']//div[@class='modal-right signup-home-carousel']//div[@class='modal-form-container']//div[@class='form-field password']//input[@type='password']")))
put_password.click()
put_password.send_keys(password)
login = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, ".//div[@class='modal-form-group']//button[@type='submit']"))).click()
time.sleep(3)

#scroll page down
botton = driver.find_element_by_tag_name('html')
botton.send_keys(Keys.END)

#enter card number
time.sleep(5)
Card_number = driver.find_element_by_xpath(".//*[@class='main-area']//div[@class='core-card available-step after-pax-validation-step']//div[@class='body']//div[@class='payment-form']//div[@class='details-holder clearfix']//div[@class='clearfix']//payment-method-card[@class='card-method']//input[@name='cardNumber']")
Card_number.click()
Card_number.send_keys(cardnumber)
time.sleep(2)

#blank click
click_blank = driver.find_element_by_xpath("//html").click()
time.sleep(5)

#verification of error message
actual_error = driver.find_element_by_xpath("/html/body/div[2]/main/div[1]/payment/div[2]/div/form/div[1]/div[2]/div[2]/payment-details-form/div/div[2]/div[1]/div[2]/div[1]/payment-method-retrieved-cards/payment-method-card/div[1]/ul/li/span")
expected_error = "Card number is invalid"


try:
	assert expected_error in actual_error.text
	print actual_error.text
except AssertionError:
	print("Card number is to short")
	
driver.close()
