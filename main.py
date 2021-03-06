from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import json

f = open('config.json', encoding="utf8")
data = json.load(f)
username = data["username"]
password = data["password"]
url = data["url"]
delayLogin = data["delayLogin"]
Test = data["Test"]
f.close()

browser = webdriver.Chrome('chromedriver')

browser.get('https://shopee.co.th/buyer/login')
sleep(1)
# ปุ่มเลือกภาษา
browser.find_element_by_class_name('shopee-button-outline.shopee-button-outline--primary-reverse').click()
usernamebox = browser.find_element_by_name('loginKey')
usernamebox.send_keys(username)
passwdbox = browser.find_element_by_name('password')
passwdbox.send_keys(password)
sleep(1)
# ปุ่มกดล็อคอิน
Btnlogin = browser.find_element_by_class_name('_1ruZ5a._3Nrkgj._3kANJY._1IRuK_.hh2rFL._3_offS').click()
# ดีเลย์ใส่ OTP (20 วิเปลื่อนได้ แต่ถ้าไม่มี OTP ก็ปิดเลย ใส่ # หน้าบรรทัด)
sleep(delayLogin)

browser.get(url)
sleep(0.5)

def Stage7onpagePay():#กดจ่ายเงิน
    Stage7 = False
    while not Stage7:
        try:
            BtnPay = browser.find_element_by_class_name('stardust-button.stardust-button--primary.stardust-button--large._1qSlAe')
            Stage7 = True
            if Test == 'False':
                BtnPay.click()
                print("Pay Success (Stage7)")
                break
            elif Test == 'True':
                print("[TEST CASE]Pay Success (Stage7)")
                break
            else:
                print('Config Test Error')
                break
        except NoSuchElementException:
            print("NoSuchElementException (Stage7)")

def Stage6onpagePay():#กดเลือกบัตร
    Stage6 = False
    while not Stage6:
        try:
            browser.find_element_by_class_name('credit-card-info-view').click()
            print("Success (Stage6)")
            Stage6 = True
            Stage7onpagePay()
        except NoSuchElementException:
            print("NoSuchElementException (Stage6)")

def Stage5onpagePay():#เลือกเป็นจ่ายผ่านบัตร
    Stage5 = False
    while not Stage5:
        try:
            browser.find_element_by_xpath('//*[@id="main"]/div/div[3]/div[2]/div[4]/div[1]/div/div[1]/div[2]/span[3]/button').click()
            print("Success (Stage5)")
            Stage5 = True
            Stage6onpagePay()
        except NoSuchElementException:
            print("NoSuchElementException (Stage5)")

def Stage4onpagePay():#กดปุ่มเปลี่ยนวิธีชำระ
    Stage4 = False
    while not Stage4:
        try:
            sleep(0.5)
            browser.find_element_by_class_name('_1n5Ut6').click()
            # browser.find_element_by_xpath('//*[@id="main"]/div/div[3]/div[2]/div[4]/div[1]/div/div[3]').click()
            print("Success (Stage4)")
            Stage4 = True
            Stage5onpagePay()
        except NoSuchElementException:
            print("NoSuchElementException (Stage4)")

def Stage3onpagePay():#กดปุ่มยืนยันเวลาส่ง
    Stage3 = False
    while not Stage3:
        try:
            sleep(0.5)
            browser.find_element_by_xpath('//*[@id="modal"]/div[2]/div[1]/div[2]/div/button[2]').click()
            print("Success (Stage3)")
            sleep(0.5)
            browser.refresh()
            Stage3 = True
            Stage4onpagePay()
        except NoSuchElementException:
            print("NoSuchElementException (Stage3)")

def Stage2onpagePay():#กดปุ่มเลือกเวลา
    Stage2 = False
    while not Stage2:
        try:
            # ดีเลย์ 0.5 วิ ถ้าเน็ตมืงไวมืงตั้ง 0.1 เลยก็ได้ ตั้งดีๆ นะไม่งั้น error นะจ๊ะ
            sleep(0.5)
            browser.find_element_by_class_name('_1uYE59').click()
            print("Success (Stage2)")
            Stage2 = True
            Stage3onpagePay()
        except NoSuchElementException:
            print("NoSuchElementException (Stage2)")

def Stage1onpagePay():# กดเปลี่ยนเวลาจัดส่ง
    Stage1 = False
    while not Stage1:
        try:
            # ดีเลย์ 0.5 วิ ถ้าเน็ตมืงไวมืงตั้ง 0.1 เลยก็ได้ ตั้งดีๆ นะไม่งั้น error นะจ๊ะ
            sleep(0.5)
            browser.find_element_by_xpath('//*[@id="main"]/div/div[3]/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[3]').click()
            Stage1 = True
            print("Success (Stage1)")
            Stage2onpagePay()
        except NoSuchElementException:
            print("NoSuchElementException (Stage1)")

def pageCart():
    onclickbtnpageCart = False
    while not onclickbtnpageCart:
        try:
            # ดีเลย์ 0.5 วิ ถ้าเน็ตมืงไวมืงตั้ง 0.1 เลยก็ได้ ตั้งดีๆ นะไม่งั้น error นะจ๊ะ
            sleep(0.5)
            browser.find_element_by_tag_name('body').click()
            browser.find_element_by_class_name('shopee-button-solid.shopee-button-solid--primary').click()
            print('Open Pay Page')
            onclickbtnpageCart = True
            Stage1onpagePay()
        except NoSuchElementException:
            print("NoSuchElementException")

def pageProduct():
    onclickbtnpageProduct = False
    while not onclickbtnpageProduct:
        try:
            try:
                browser.find_element_by_class_name('btn.btn-solid-primary.btn--l.btn-solid-primary--disabled._3Kiuzg')
                print('Btn Close')
                browser.refresh()
            except:
                browser.find_element_by_class_name('btn.btn-solid-primary.btn--l._3Kiuzg').click()
                print('Btn Open')
                onclickbtnpageProduct = True
                pageCart()
        except NoSuchElementException:
            print("NoSuchElementException")

pageProduct()