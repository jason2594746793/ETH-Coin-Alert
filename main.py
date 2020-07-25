from egsapi_transform import api_to_GasPrice
import time

user_low = input("Price for low:")
if not user_low:
    user_low = 0
else:
    try:
        user_low = float(user_low)
    except ValueError:
        print("ValueError")
        exit(1)



# user_medium = input("Price for standard:")
# if not user_medium:
#     user_medium = None

# user_high = input("Price for fast:")
# if not user_high:
#     user_high = None
def price_compare(target, current):
    if target < current:
        print("No")
    else:
        print("Yes")

while True:
    time.sleep(15)
    current_price = api_to_GasPrice()
    print("current price:" + str(current_price))
    print("User price:" + str(user_low))
    price_compare(user_low, current_price.low)


        
