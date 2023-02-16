import kfin

def main():
    r = kfin.get_exchange_rate("USD")
    print(r)

if __name__ == "__main__":
    main()
