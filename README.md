## English
If you have been investing or trading stocks you must have come across about Japanese Candlestick Pattern.
How effective are them? Can we use them reliably in investing or trading? Let's find out.
<!-- more -->
## Intro
I assume that you already knew the anatomy of a candlestick so I will skip the explanation part.

There are dozens of candlestick pattern out there, be it bullish or bearish ones, what we wanted to know is that can we used them reliably in our investing and trading activities.


## Methodology - Skip this part if you're not into tech
It is possible to handcode a program to identify every pattern but that will be a lot of workload. Fortunately, there is a python library called __[TA-Lib](http://mrjbq7.github.io/ta-lib/)__, which included the identification of candlestick pattern given price data. In this study, **10 years worth** of daily price data (Open, Low, High, Close) was scraped online and saved into a .csv file.

I have written a piece of code that will iterate over the price data to find candlestick pattern. Comment below if you wanted a copy of the code and data.
****
## Results
The performance of each candlestick is measured by how likely it will go up in (1,5,10,30) days. A win rate of 0.7 means that in 7 out of 10 times the price will go up after the pattern appeared.

Here's the entire backtesting results!

![Candlestick pattern and win rate in one table](/candlestick_result_table.png)

Very surprisingly some bullish pattern has very low win rate, my thinking is that when a pattern is too widely known and used, the edge of the pattern diminishes as everyone knows the information making it useless. Besides, the findings also showed very little pattern with winrate more than 50% (I thought I will found my golden formula here :disappointed: ). However there is some relatively high winrate patterns with winrate over 0.45. Perhaps with enough risk management techniques you might be able to construct a consistently profitable strategy.

## Some Afterthoughts
Of course there are something this study misses, for example, some candlestick pattern are only effective while they are on top of the trend etc. Nevertheless this brings me a general view of the effectiveness of candlestick pattern.

I am wondering combined with other technical indicators will the winrate be higher? Also, the low winrate doesn't mean that it is worthless. A 20% winrate indicats there it is 80% likely that the price will drop tomorrow. How about using this as a indicator for shorting of stocks? Well, I leave this to you guys to figure out. Let me know what you think in the comments.

This study is purely for discovery and fun. Please be responsible of your own money and trade at your own risk.

---
## 中文
在股市/汇市有几年经验的朋友相信都知道什么是蜡烛图
可是有没有想过蜡烛图在马股的胜率有多大呢? 到底蜡烛图是不是个可靠的指标?
<!-- more -->
## 介绍
这里就不多加介绍蜡烛图的构造和历史了, 有兴趣的朋友可以上网搜索有关资讯, 而且有关资讯也相当丰富, 也不用我来介绍了.

## 研究方法
小编用了Python编程程序来回测各个蜡烛图形在过去10年马股每一个个股的表现. 不过小编觉得大家应该想直接看结果, 所以编码就不放这里解释了. 如果对编码有兴趣可以留言.

## 结果
程序计算了每个蜡烛图形在马股每一个个股在 (1,5,10,30) 天过后的表现. 0.7的表现就等于在10次出现该蜡烛图形后, 有7次股价是上涨的.

小编整理了一些数据并列出所有的蜡烛图案

![Candlestick pattern and win rate in one table](/candlestick_result_table.png)

神奇的是, 许多牛市信号都有着非常低的赢率, 个人推断是因为当大家都使用同一个信号的时候, 其获利能力将会大大减少. 其实以上的结果是出乎我的意料的, 因为没想到竟然很少指标有超过50%的胜率. 可是值得一提的是有些蜡烛图形有超过0.45的胜率. 如果配合其他的指标和风险管理的话这可能是可以持续性获利的交易指标.

## 想法
这个回测程序也不是100%完美的, 一些弱点比如没有考虑蜡烛形态出现的地方 (有些形态是在低位/高位才比较有效的). 无论如何这次的研究也初步展示了蜡烛图形在马股的有效性和胜率.

或许蜡烛图形必须配合其他技术指标才能达到比较高的胜率. 值得一提的是, 0.2胜率的图形也可以当成反向指标来使用 (0.2的胜率代表图形出现后下跌的概率偏大)

这项研究的出发点是学习和探索用途. 交易自负
