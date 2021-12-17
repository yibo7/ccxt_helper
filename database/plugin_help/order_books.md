# 交易委托账本
交易所会提供敞口委托单的买入/卖出价格、交易量以及其他数据。 通常对每一个特定的市场都会有一个单独的访问短接点来查询交易委托账本的状态。 交易委托账本经常被称为市场深度。委托账本信息可以用于交易决策过程。
## 一.调用方法
获取指定符号的交易委托账本的方法是fetchOrderBook或fetch_order_book。 
该方法的参数是交易符号以及一个可选的参数字典（如果该交易所支持的话）

    import ccxt
    # return up to ten bidasks on each side of the order book stack
    limit = 10
    ccxt.cex().fetch_order_book('BTC/USD', limit)

###市场深度说明：

委托账本聚合的层级或详情通常是数字标注的，就像L1、L2、L3...
- L1：
    较少的详情，用于快速获取非常基本的信息，也就是仅市场价格。看起来就像在委托账本中仅包含一个委托单。
- L2：
    最常用的聚合层级，委托单交易量按价格分组。如果两个委托单有相同的价格，那么他们会合并为一项，其总量 为这两个委托单的交易量的和。这个聚合层级可能适合大部分的应用目的。
- L3：
    最详细的层级，包含所有的订单，没有聚合。这一层级自然包含了输出中的重复内容。因此，如果两个订单 有相同的价格，它们也不会合并在一起，这两个订单的优先级则取决于交易所的撮合引擎。你不一定真的需要 L3详情来进行交易。实际上，大多数情况下你根本不需要这么详细的信息。因此有些交易所不支持这个级别的数据， 总是返回聚合后的委托账本。
    如果你想获取L2委托账本，可以使用统一API中的fetchL2OrderBook(symbol, limit, params) 或 fetch_l2_order_book(symbol, limit, params)方法。
## 二.返回结果
ccxt返回的委托账本结构如下：

    {
        'bids': [
            [ price, amount ], // [ float, float ]
            [ price, amount ],
            ...
        ],
        'asks': [
            [ price, amount ],
            [ price, amount ],
            ...
        ],
        'timestamp': 1499280391811, // Unix Timestamp in milliseconds (seconds * 1000)
        'datetime': '2017-07-05T18:47:14.692Z', // ISO8601 datetime string with milliseconds
    }

如果查询的交易所在其API响应中没有提供时间戳和日期值，那么在返回的结果 中时间戳和日期的值可能也会缺失（undefined/None/null）。

Price和amount都是浮点数。
### bids:
>数组按价格降序排列，最高的买入价格排在第一个，最低的 买入价格排在最后一个。

### asks:
> 数组按价格升序排列，最低的卖出价格排在第一个，最高的卖出 价格排在最后一个。

### bids/asks:
> 数组可以是空的，表示交易所的委托账本中没有相应 的委托单。

交易所可能返回用于分析的不同层级的委托单，结果中要么包含每个订单的详情，要么 已经按照价格和交易量进行了分组聚合因而其中的详情信息要少一些。越多的详情信息 就需要越多的带宽，因此总体上会更慢一些，但是好处在于有更高的精度。
较少的详情 信息通常会快一些，但是可能在某些特定情况下不够用。

### orderbook['timestamp']:
是交易所生成这个响应的时间，可能会缺失（undefined/None/null）。 
如果交易所有定义的话，那么它是一个UTC时间戳，以毫秒为单位，记录子1970年1月1日零点 以来的毫秒数。

## 三.获取最佳市场价格
为了获取当前的最好价格（查询市场价格）并且计算买入卖出的价差， 可以使用如下代码。

    orderbook = exchange.fetch_order_book (exchange.symbols[0])
    bid = orderbook['bids'][0][0] if len (orderbook['bids']) > 0 else None
    ask = orderbook['asks'][0][0] if len (orderbook['asks']) > 0 else None
    spread = (ask - bid) if (bid and ask) else None
    print (exchange.id, 'market price', { 'bid': bid, 'ask': ask, 'spread': spread })
