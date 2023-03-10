from arc.arc_api import ARC
from nlp.sentiment_analysis import SentimentAnalysis
from napi.news_api import NewsApi
from graph.graph import Graph
from ai.random_forest import RandomForest
from sapi.stock_api import StockApi
import json
import logging
import asyncio

logging.basicConfig(level=logging.INFO)


async def main():
    config = {
        'nlp': {
            'field': 'N/A'
        }
    }
    SNT = SentimentAnalysis(config)
    NAPI = NewsApi()
    G = Graph(config)
    RF = RandomForest(config)
    SAPI = StockApi(config)

    arc = ARC(config, SNT, NAPI, G, RF, SAPI)
    #await arc.generate_graph(-1, 'Aaron Rogers', '2023-02-14', '2023-03-14')
    await arc.generate_next_stock(-1, 'Microsoft', 'MSFT', '2023-02-14', '2023-03-14')

    # await arc.get_and_store_articles(30, 'Microsoft', '2023-02-13', '2023-03-12')
    # article_store = await arc.get_article_store()
    # await arc.analyze_and_store_scores(article_store)
    # sentiment_store = await arc.get_sentiment_store()
    # await arc.get_and_store_stock('MSFT', '2023-02-13', '2023-03-12')
    # stock_store = await arc.get_stock_store()
    # await arc.sync_sentiment_stock(sentiment_store, stock_store, '2023-02-13', '2023-03-12')



async def run():
    await main()

if __name__ == '__main__':
    asyncio.run(run())
