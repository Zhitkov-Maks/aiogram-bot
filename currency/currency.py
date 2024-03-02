import asyncio
import aiohttp
from aiohttp import ClientSession

URL = "https://www.cbr-xml-daily.ru/daily_json.js"


async def get_valute() -> tuple:
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as response:
            data = await response.json(content_type='application/javascript')
            return (
                (data.get('Valute').get("USD").get("Value"), data.get('Valute').get("USD").get("Name")),
                (data.get('Valute').get("EUR").get("Value"), data.get('Valute').get("EUR").get("Name")),
                (data.get('Valute').get("BYN").get("Value"), data.get('Valute').get("BYN").get("Name")),
                (data.get('Valute').get("CNY").get("Value"), data.get('Valute').get("CNY").get("Name")),
                (data.get('Valute').get("AZN").get("Value"), data.get('Valute').get("AZN").get("Name")),
                (data.get('Valute').get("AMD").get("Value"), data.get('Valute').get("AMD").get("Name")),
                (data.get('Valute').get("GEL").get("Value"), data.get('Valute').get("GEL").get("Name")),
                (data.get('Valute').get("INR").get("Value"), data.get('Valute').get("INR").get("Name")),
                (data.get('Valute').get("TRY").get("Value"), data.get('Valute').get("TRY").get("Name")),
                (data.get('Valute').get("KZT").get("Value"), data.get('Valute').get("KZT").get("Name")),
            )

