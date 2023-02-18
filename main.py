import kfin
from kfin import *


def main():
    r = kfin.get_exchange_rate(Currency.JPY)
    print(r)


if __name__ == "__main__":
    main()
