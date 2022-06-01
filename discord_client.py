import os
from money import Money

from src.robinhood_client import RobinhoodClient
from discord.ext import tasks

from dotenv import load_dotenv
import discord
from typing import Dict, Optional


load_dotenv()


def format_stock_to_message(stock_data: Optional[Dict]):
    price = stock_data.get("price")
    quantity = stock_data.get("quantity")
    percent_change = stock_data.get("percent_change")
    current_portfolio_value = float(quantity) * float(price)
    message = f"Price: {price}, QTY: {quantity}, Current Value: {current_portfolio_value}, Change: {percent_change}"
    return message


def total_portfolio(stock_data):
    """Total portfolio"""
    total_value = 0.0
    for stock, data in stock_data.items():
        quantity = data.get("quantity")
        price = data.get("price")
        current_portfolio_value = float(quantity) * float(price)
        total_value += current_portfolio_value
    return str(Money(amount=total_value, currency="USD"))


class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.my_background_task.start()

    async def on_ready(self):
        print("Logged in as")
        print(self.user.name)
        print(self.user.id)
        print("------")

    @tasks.loop(seconds=14400)  # task runs every 4 hours
    async def my_background_task(self):
        try:
            channel = self.get_channel(
                int(os.environ.get("DISCORD_STOCK_CHANNEL_ID"))
            )  # channel ID goes here
            robinhood_client = RobinhoodClient()
            stocks_data = robinhood_client.get_stock_data()
            stock_message = ["--=--=--=--=--=--=--=--=--"]
            for stock, data in stocks_data.items():
                stock_message.append(f"{stock}: {format_stock_to_message(data)}")
            stock_message.append(f"Total Portfolio: {total_portfolio(stocks_data)}")
            stock_message.append("--=--=--=--=--=--=--=--=--")
            sent_message = await channel.send("\n".join(stock_message))
            print(f"Sent message with id: {sent_message.id}")
        except Exception as ex:
            raise ex

    @my_background_task.before_loop
    async def before_my_task(self):
        await self.wait_until_ready()  # wait until the bot logs in


if __name__ == "__main__":
    client = MyClient()
    client.run(os.environ.get("DISCORD_BOT_TOKEN"))
