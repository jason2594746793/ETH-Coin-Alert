from gas_price import GasPrice
from egsapi_access import get_low, get_medium, get_high

def api_to_GasPrice():
    current_gas_price = GasPrice(get_low(), get_medium(), get_high())
    return current_gas_price

