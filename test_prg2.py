from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys
import pytest

@pytest.fixture
def setUp():
    global driver,email,password,mobile,address,pincode
    email=input("Enter Email :")
    password=input("Password :")
    address=input("Address :")
    pincode=input("Pincode :")
    mobile=input("Mobile :")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield
    time.sleep(5)
    driver.close()
    print("Tested Successfully")

def test_program02(setUp):
    driver.get("https://iprimedtraining.herokuapp.com/training.php")
    time.sleep(1)
    driver.find_element_by_name("loginEmail").send_keys(email)
    time.sleep(1)
    driver.find_element_by_name("loginpass").send_keys(password)
    time.sleep(1)
    driver.find_element_by_name("loginbtn").click()
    time.sleep(2)
    driver.find_element_by_name("name").send_keys("Pradeep Kumar A")
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[2]/td[2]/input[1]").click()
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[3]/td[2]/select/option[1]").click()
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[4]/td[2]/input").send_keys("5/7/2001")
    time.sleep(1)
    driver.find_element_by_name("Address").send_keys(address)
    time.sleep(1)
    driver.find_element_by_name("Pincode").send_keys(pincode)
    time.sleep(1)
    driver.find_element_by_name("Mobile").send_keys(mobile)
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[8]/td[2]/input").send_keys(email)
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[9]/td[2]/input").send_keys(password)
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[10]/td[2]/input").send_keys(password)
    time.sleep(1)
    button=driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[12]/td[2]")
    driver.execute_script("arguments[0].click();",button)
    time.sleep(10)
    driver.execute_script("window.scrollTo(0,window.scrollY+1000)")
    time.sleep(3)