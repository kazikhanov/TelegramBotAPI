from config import API_KEY
import asyncio
import aiohttp

async def main(city):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'http://api.weatherapi.com/v1/current.json?key={API_KEY}',
                               params={'q':f'{city}', 'days':'1', 'lang':'ru'}) as resp:

            response = await resp.json()



            out = (f"Погода в {response['location']['name']}:\n"
                   f"\nВ {response['location']['name']} сейчас {response['current']['condition']['text'].lower()}.\n"
                   f"Температура {response['current']['temp_c']}°C.\n"
                   f"Температура ощушается как {response['current']['feelslike_c']}°C.\n"
                   f"Скорость ветра {response['current']['wind_kph']} km/h\n"
                   f"Влажность {response['current']['humidity']}%\n"
                   f"Облачность {response['current']['cloud']}%")


            localtime = (f"Дата: {response['location']['localtime'].split()[0]}\n"
                         f"Время: {response['location']['localtime'].split()[1]}")

            return f"{out}\n{localtime}"


async def temp(city):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'http://api.weatherapi.com/v1/current.json?key={API_KEY}',
                               params={'q':f'{city}', 'days':'1', 'lang':'ru'}) as resp:
            response = await resp.json()

            out = (f"Температура в {response['location']['name']} {response['current']['temp_c']}°C")
            print()
            return out

print(asyncio.run(temp('48.8567,2.3508')))
