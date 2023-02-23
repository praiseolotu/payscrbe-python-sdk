
from data import Data as dt
from recharge import Recharge as rg
# sample usage
rg1 = rg('ps_live_355', 'sandbox')
dt1 = dt('ps_live_355', 'sandbox')
print(dt1.dataLookup('mtn'))
print(dt1.vendData('monthly', '07083023292', 'airtel'))
print(rg1.getCardPins('1467gf6'))
