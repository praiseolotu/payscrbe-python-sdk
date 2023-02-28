### Overview
Python API Wrapper for [Payscribe](https://payscribe.ng)

*Status:* ***Active Development***
### Usage
To use the Payscribe class, you need to first create an instance of the class. You can do this by passing in your Payscribe API key, and type to the constructor.


### Instantiate Payscribe

````python
// Using the constructor
from data import Data as dt
from recharge import Recharge as rg
#get_data = dt('ps_test_355', 'sandbox')
get_data = dt(key, type)
result = get_data.dataLookup('network')
print(result)
result = get_data.vendData('plan', 'recepient', 'network')
print(result)
do_recharge = rg(key, type)
result = do_recharge.recharge(qty, amount, 'display_name')
print(result)
````
### DOC & API Reference: <https://documenter.getpostman.com/view/7369921/TW6tLpgz>

> Don't forget to get your API key from [Payscribe](https://payscribe.ng/)

### Available resources

```Python

Airtime
AirtimeToWallet
Data
Electricity
Multichoice
Recharge
Startimes
Transaction
```
