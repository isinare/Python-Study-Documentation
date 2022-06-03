#import main
#print(main.added)

import Shopping.Shopping_cart
print(Shopping.Shopping_cart.buy("Shampoo"))

from Shopping.Shopping_cart import buy
print(buy('Food'))