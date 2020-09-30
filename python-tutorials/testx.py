from decimal import Decimal, ROUND_HALF_UP, Context

import yfinance as yf

msft = yf.Ticker("MSFT")
msft.info

print(msft.dividends)

# print(round(2.3, 2))
# print(round(2.45, 1))
# print(round(2.675, 2))
#
# print(Decimal(1.325))
#
# print(Context(prec=3, rounding=ROUND_HALF_UP).create_decimal('2.675'))
