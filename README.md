# kfin

## Prerequisites

###  API KEY

####  Realtime currency exchange rate
* Set environment variable *KOREAEXIM_KEY*
* Request URL : https://www.koreaexim.go.kr/ir/HPHKIR020M01?apino=2&viewtype=O#tab1

## Install
```
pip install kfin
```

## Usage

```python
import kfin
from kfin import *

# Get KRW to USD exchange rate
kfin.get_exchange_rate(Currency.USD)
```