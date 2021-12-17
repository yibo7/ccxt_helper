from ccxt import Exchange


def ccxt_exchange(exchange_t: Exchange) -> Exchange:
    exchange = exchange_t()
    exchange.proxies = {
        'http': 'http://127.0.0.1:41081',  # these proxies won't work for you, they are here for example
        'https': 'http://127.0.0.1:41081',
    }
    return exchange