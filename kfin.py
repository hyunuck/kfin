import httpx
import os
import json
import koreaexim.exchange_rate


def get_get_exchange_rates():
    uri = "https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={0}&data={1}".format(
        os.environ["KOREAEXIM_KEY"], "AP01")
    response = httpx.get(uri)
    items = json.loads(response.text, object_hook=koreaexim.exchange_rate.ExchangeRate.from_dict)
    return items

def get_get_exchange_rate(cur_unit):
    for item in get_get_exchange_rates():
        if item.cur_unit == cur_unit:
            return item