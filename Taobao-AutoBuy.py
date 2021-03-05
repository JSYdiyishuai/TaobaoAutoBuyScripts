from selenium import webdriver
import datetime
import time

# BUY_TIME = "2021-3-5 17:50:30"
BUY_TIME = input()
MAX_LOGIN_RETRY_TIMES = 6
current_retry_login_times = 0
login_success = False
buy_time_object = datetime.datetime.strptime(BUY_TIME, '%Y-%m-%d %H:%M:%S')

now_time = datetime.datetime.now()
if now_time > buy_time_object:
    print("The time has passed")
    exit(0)

print("open chrome")

option = webdriver.ChromeOptions()
option.add_argument('disable-infobars')
option.add_argument('--blink-settings=imagesEnabled=false')
driver = webdriver.Chrome(chrome_options=option)
driver.maximize_window()
print("chrome has been opened")


def __login_operates():
    driver.get("https://www.taobao.com")
    # noinspection PyBroadException
    try:
        if driver.find_element_by_link_text("login"):
            driver.find_element_by_link_text("login").click()
            time.sleep(10)
    except:
        global login_success
        global current_retry_login_times
        login_success = True
        current_retry_login_times = 0

def login():
    print("login")
    __login_operates()
    global current_retry_login_times
    while current_retry_login_times < MAX_LOGIN_RETRY_TIMES:
        current_retry_login_times = current_retry_login_times + 1
        print("login times:" + str(current_retry_login_times))
        __login_operates()
        if login_success:
            print("successfully")
            break
        else:
            print("wait for login")

    if not login_success:
        exit(0)

    now = datetime.datetime.now()
    print('login success:', now.strftime('%Y-%m-%d %H:%M:%S'))

def __refresh_keep_alive():
    driver.get("https://cart.taobao.com/cart.htm")
    print("refresh")
    time.sleep(60)


def keep_login_and_wait():
    print("long time before the time, start refreshing")
    while True:
        currentTime = datetime.datetime.now()
        if (buy_time_object - currentTime).seconds > 300:
            __refresh_keep_alive()
        else:
            print("stop refreshing")
            break

def buy():
    driver.get("https://cart.taobao.com/cart.htm")
    time.sleep(1)
    while True:
        # noinspection PyBroadException
        try:
        # if driver.find_element_by_id("J_SelectAll2"):
            driver.find_element_by_id("J_SelectAll1").click()
            print("choose all goods")
            break
        except:
            print("No")
    submit_succ = False
    retry_submit_times = 0
    while True:
        now = datetime.datetime.now()
        if now >= buy_time_object:
            start = time.clock()
            print("buy times：" + str(retry_submit_times))
            if submit_succ:
                print("submit order")
                break
            if retry_submit_times > 100:
                print("give up trying")
                break

            retry_submit_times = retry_submit_times + 1

            try:
                if driver.find_element_by_id("J_Go"):
                    driver.find_element_by_id("J_Go").click()
                    click_submit_times = 0
                    while True:
                        # noinspection PyBroadException
                        try:
                            if click_submit_times < 10:
                                driver.find_element_by_link_text('提交订单').click()
                                end = time.clock()
                                print("click submit button")
                                print(end-start)
                                submit_succ = True
                                break
                            else:
                                print("submit failure")
                        except Exception as ee:
                            print(ee)
                            print("retry")
                            click_submit_times = click_submit_times + 1
                            time.sleep(0.1)
            except Exception as e:
                print(e)
                # print("submit failure")

        time.sleep(0.1)


login()
keep_login_and_wait()
buy()
