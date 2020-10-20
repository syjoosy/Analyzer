#Fortress analyzer by syjoosy
from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def wheel_element(element, deltaY = 120, offsetX = 0, offsetY = 0): #ФУНКЦИЯ ЭМУЛЯЦИИ ПРОКРУТКИ
  error = element._parent.execute_script("""
    var element = arguments[0];
    var deltaY = arguments[1];
    var box = element.getBoundingClientRect();
    var clientX = box.left + (arguments[2] || box.width / 2);
    var clientY = box.top + (arguments[3] || box.height / 2);
    var target = element.ownerDocument.elementFromPoint(clientX, clientY);

    for (var e = target; e; e = e.parentElement) {
      if (e === element) {
        target.dispatchEvent(new MouseEvent('mouseover', {view: window, bubbles: true, cancelable: true, clientX: clientX, clientY: clientY}));
        target.dispatchEvent(new MouseEvent('mousemove', {view: window, bubbles: true, cancelable: true, clientX: clientX, clientY: clientY}));
        target.dispatchEvent(new WheelEvent('wheel',     {view: window, bubbles: true, cancelable: true, clientX: clientX, clientY: clientY, deltaY: deltaY}));
        return;
      }
    }    
    return "Element is not interactable";
    """, element, deltaY, offsetX, offsetY)
  if error:
    raise WebDriverException(error)

# CHUNKBASE_ROOT_URL = "https://www.chunkbase.com/apps/nether-fortress-finder"
driver = webdriver.Firefox()
driver.get("https://www.chunkbase.com/apps/nether-fortress-finder")
x = driver.find_element_by_id('map-goto-x')
z = driver.find_element_by_id('map-goto-z')
x.send_keys("0")
z.send_keys("0")
sleep(1)
go = driver.find_element_by_id('map-goto-go')
move = ActionChains(driver)
go.click()
print("Слайдер")
source = driver.find_element_by_xpath('//*[@id="map-zoom-slider"]/a')
print("Нашел слайдер")

# target = driver.find_element_by_xpath('//*[@id="box103"]')
action = ActionChains(driver)
# action.drag_and_drop(source, target).perform()
xOffset = 100
yOffset = 100
print("Перед перемещением")
action.drag_and_drop_by_offset(source, xOffset, yOffset)
# move.click_and_hold(source).move_by_offset(-200, 0).release().perform()
print("Выполнилось")
