# 价格行情

## 一.调用方法
获取行情数据的方法如下：

fetchTicker (symbol[, params = {}]), symbol必须，params可选
fetchTickers ([symbols = undefined[, params = {}]]), 两个参数都是可选的
    
    if (exchange.has['fetchTicker']):
        print(exchange.fetch_ticker('LTC/ZEC')) # ticker for LTC/ZEC
    
    if (exchange.has['fetchTickers']): 
        print(exchange.fetch_tickers(['ETH/BTC', 'LTC/BTC'])) # listed tickers indexed by their symbols

价格行情包含了最近一段时间内特定交易市场的统计信息，通常使用24小时进行统计。 查询价格行情的方法如下
检查交易所的
exchange.has['fetchTicker']
exchange.has['fetchTickers']属性 来决定所查询的交易所是否支持这些方法。

## 二.实时行情数据结构
```
{
    'symbol':        string 市场的字符串符号（'btc / usd'，'eth / btc'，......）
    'info':        { 来自交易所原始数据 },
    'timestamp':     int (时间戳)
    'datetime':      ISO8601 DateTime字符串，带毫秒
    'high':          float, // 最高价格
    'low':           float, // 价格最低
    'bid':           float, // 当前最佳出价（买）价格 current best bid (buy) price
    'bidVolume':     float, // 当前最佳出价（买入）金额（可能缺失或未确定）current best bid (buy) amount (may be missing or undefined)
    'ask':           float, // 当前最好的询问（卖）价格 current best ask (sell) price
    'askVolume':     float, // 当前最佳询问（卖）金额（可能缺失或未确定）current best ask (sell) amount (may be missing or undefined)
    'vwap':          float, // 卷的平均价格 volume weighed average price
    'open':          float, // 开盘价 opening price
    'close':         float, // 上次贸易价格（当前期间的收盘价） price of last trade (closing price for current period)
    'last':          float, // 与`关闭，为方便起见重复 same as `close`, duplicated for convenience
    'previousClose': float, // 上一段时间的闭钱价格 closing price for the previous period
    'change':        float, // /绝对变化（last - open），absolute change, `last - open`
    'percentage':    float, // 相对变化((change/open) * 100) relative change, `(change/open) * 100`
    'average':       float, // 平均价格，`(last + open) / 2` average price, `(last + open) / 2`
    'baseVolume':    float, // 持续24小时的基础货币数量 volume of base currency traded for last 24 hours
    'quoteVolume':   float, // 报价货币数量过去24小时交易 volume of quote currency traded for last 24 hours
}
```

### 注意：
行情结构中的所有价格都是以报价货币计量，其中某些字段可能是undefined / None / null。

- bidVolume指的是委托账本中当前的最优买入价委托单的总量
- askVolume指的是委托账本中当前的最优卖出价委托单的总量
- baseVolume指的是过去24小时内基准货币的交易量（买入或卖出）
- quoteVolume指的是过去24小时内报价货币的交易量（买入或卖出）

时间戳和日期都是以毫秒为单位的UTC时间值：

### ticker['timestamp'] 
是交易所生成响应的时间，有的交易所可能没有这个值，因此在结果中会缺失
### exchange.last_response_headers['Date'] 
是收到的最后一个HTTP响应的日期-时间字符串。
Date解析器 应当考虑时区问题。日期-时间的精度是1秒、1000毫秒。
这个日期应当由交易所服务器参考以下标准设置：
https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.18
https://tools.ietf.org/html/rfc1123#section-5.2.14
https://tools.ietf.org/html/rfc822#section-5

## 三. 注意事项：
虽然有些交易所在其行情数据中混入了委托账本的最高买入/最低卖出价格，
你不应当将行情数据视为fetchOrderBook的替代方法。
行情数据的主要目的是提供统计数据，
可以将其视为活跃的24小时OHLCV数据。
已知的是，交易所不鼓励频繁地调用fetchTicker。 
如果你需要一个统一的方法去访问bids和asks，你应当使用fetchL[123]OrderBook系列的方法。
要获取历史价格和数量，使用统一API中的fetchOHLCV方法。

