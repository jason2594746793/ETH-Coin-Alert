from egsapi_transform import api_to_GasPrice
from win10toast import ToastNotifier
import time

toast = ToastNotifier()

user_low = input("Price for low: ")
if not user_low:
    user_low = 9999
else:
    try:
        user_low = float(user_low)
    except ValueError:
        print("ValueError")
        exit(1)

user_medium = input("Price for standard: ")
if not user_medium:
    user_medium = 9999
else:
    try:
        user_medium = float(user_medium)
    except ValueError:
        print("ValueError")
        exit(1)

user_high = input("Price for fast: ")
if not user_high:
    user_high = 9999
else:
    try:
        user_high = float(user_high)
    except ValueError:
        print("ValueError")
        exit(1)


def price_compare(target, current):
    for x in range(3):
        if target[x] > current[x]:
            return True

def Notification_head(target, current, reminder):
    reminder = [False, False, False]
    for x in range(3):
        if target[x] > current[x]:
            reminder[x] = True
    print(reminder)
    return reminder       

def notificationer(target, current, reminder):
    toast.show_toast("Your Target is reached ", "Low option " + str(reminder[0]) + "  Medium option " + str(reminder[1]) + "  High option " + str(reminder[2]) + "       Current price is " + str(current) + " Your target price is " + str(target) ,duration=1000, icon_path="coin.ico")


while True:
    current_price = api_to_GasPrice()
    show_current_price = str(current_price)
    show_target_price = "low: " + str(user_low) + "  medium: " + str(user_medium) + "  high: "  + str(user_high)
    print("current price:" + show_current_price)
    print("User price:   " + show_target_price)
    target_list = [user_low, user_medium, user_high]
    current_list = [current_price.low, current_price.medium, current_price.high]
    if price_compare(target_list, current_list):
        reminder = []
        reminder = Notification_head(target_list, current_list, reminder)
        notificationer(show_target_price, show_current_price, reminder)
    time.sleep(15)


        
