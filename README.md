# XBT Provider - Fare Value Calculator
Fare Value Calculator keeps track of the value of your crypto certificate holdings.

![example image](https://github.com/wilhelmuggla/fair-value/blob/master/example-image.png)

## Installation
Fare Value Calculator is using [python3](https://www.python.org/download/releases/3.0/), use [pip](https://pip.pypa.io/en/stable/) to install the requrired liberies



1. install [requests](https://requests.readthedocs.io/en/master/)
```bash
pip install requests
```

2. install [colorama](https://pypi.org/project/colorama/)
```bash
pip install colorama
```



## Config

Configure your portfolio in `portfolio.json`:

   ```json
 
    {
        "crypto": "BTC",
        "amount": 0,
        "url": "https://coinshares.com/etps/xbt-provider/bitcoin-tracker-one"
    }
   ```
