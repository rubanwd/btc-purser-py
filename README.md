# btc-purser-py

It's purser price of BTC. The price gets from https://coinmarketcap.com/ and show the price each 10 minutes using linux notifications.

# crontab
*/10 * * * * export DISPLAY=:0 && cd /home/serjdev/dev/btc_purser && ./btc_purser.py
