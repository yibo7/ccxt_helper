# 市场数据结构
交易所是用来交易有价物品的场所。优势它们被冠以各种不同的 术语，例如工具、符号、交易对、货币、股票、商品、合同等， 但是指的都是一个东西 - 交易对、符号或金融工具。

在ccxt库中，每个交易所都提供了多个市场。
不同交易所提供的 交易市场各有不同，因而也提供了跨交易所的套利机会。
一个市场 通常指的是一对可交易的数字货币或法币。
## 一.在CCXT中，市场模型的数据结构如下：

    {
        'id':     ' btcusd',  // string literal for referencing within an exchange
        'symbol':  'BTC/USD', // uppercase string literal of a pair of currencies
        'base':    'BTC',     // uppercase string, unified base currency code, 3 or more letters
        'quote':   'USD',     // uppercase string, unified quote currency code, 3 or more letters
        'baseId':  'btc',     // any string, exchange-specific base currency id
        'quoteId': 'usd',     // any string, exchange-specific quote currency id
        'active': true,       // boolean, market status
        'precision': {        // number of decimal digits "after the dot"
            'price': 8,       // integer or float for TICK_SIZE roundingMode, might be missing if not supplied by the exchange
            'amount': 8,      // integer, might be missing if not supplied by the exchange
            'cost': 8,        // integer, very few exchanges actually have it
        },
        'limits': {           // value limits when placing orders on this market
            'amount': {
                'min': 0.01,  // order amount should be > min
                'max': 1000,  // order amount should be < max
            },
            'price': { ... }, // same min/max limits for the price of the order
            'cost':  { ... }, // same limits for order cost = price * amount
        },
        'info':      { ... }, // the original unparsed market info from the exchange
    }

## 二.每个市场都是一个关联数组（或称为字典），包含以下键：

### id：
> 市场ID，用来在交易所内区分不同市场的字符串或数字ID。

### symbol：
> 市场符号，用来表示交易对的大写的字符串代码。通常记作：基础货币/报价货币，例如： BTC/USD, LTC/CNY 或 ETH/EUR等等。在ccxt库中使用市场符号来引用不同的市场。
### base：
> 基础货币代码，表示基础法币或加密货币的统一的大写字符串代码，代码是标准化的，在 CCXT中以及CCXT统一API中，使用货币代码来引用不同的货币。
### quote：
> 报价货币代码，用来表示报价法币或数字货币的统一的大写字符串代码。
### baseId：
> 基础货币ID，是交易所特定的表示基础货币的ID，不是统一的代码，理论上可以是任何 字符串。
### quoteId：
> 报价货币ID，是交易所特定的表示报价货币的ID，也不是统一的代码，每个交易所自行维护。
### active：
> 是否激活，布尔值，表示这个市场是否可交易。通常如果一个市场未激活，那么所有相关的 行情、委托账本以及其他访问端结点都返回空响应、全零、无数据或过时数据。调用者需要检查市场 是否激活并且定期刷新市场缓存。
### info：
> 一个用于记录非共性市场属性的关联数组，包括手续费、费率、限制以及其他一般性市场信息。 内部的info数组对每个特定的市场都是不同的，其内容依赖于交易所。
### precision：
> 在委托单中金额相关字段（例如价格、数量、成本等）支持的最大小数位数。
### limits：
> 限值，价格、数量和成本等的最高和最低限值，其中：成本 = 价格 * 数量。