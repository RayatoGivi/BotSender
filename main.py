import discord
import asyncio

# Создаем бота
intents = discord.Intents.default()
client = discord.Client(intents=intents)

async def send_message():
    channel = client.get_channel(CHANNEL_ID)  # Замените CHANNEL_ID на ID канала, куда хотите отправлять сообщения
    while True:
        await channel.send("|| @everyone @here || \n**:triangular_flag_on_post: - Доброго времени суток, уважаемые пользователи ZANE CRMP, хочу напомнить о том, что открыты заявки на пост Модерации нашего Discord-сервера. \n――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― \nКритерии для поступление на пост Модератора \n:beaver:  — Адекватность, грамотность, умение разговаривать с людьми \n:beaver:  — Иметь хороший микрофон и поставленный голос \n:beaver:  — Знать правила Discord сервера \n:beaver:  — Возраст 13+ (возможны исключения) \n――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― \nКарьерный рост в виде повышений. \nХороший и общительный состав. \n――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― \n:alarm_clock: На этом все, приятной игры на ZANE CRMP! \nТут вы можете подать заявку на модератора: \nhttps://forum.zane-rp.ru/threads/z-rp-Заявление-на-пост-Модератора-discord.121/ \nГруппа сервера: [ВК](https://forum.zane-rp.ru/link-forums/%D0%9D%D0%B0%D1%88%D0%B0-%D0%B3%D1%80%D1%83%D0%BF%D0%BF%D0%B0-%D0%B2%D0%BE-%D0%92%D0%9A%D0%BE%D0%BD%D1%82%D0%B0%D0%BA%D1%82%D0%B5.59/)")
        await asyncio.sleep(3 * 60 * 60)  # Пауза на 3 часа

@client.event
async def on_ready():
    print('Бот успешно запущен!')
    await send_message()

client.run('TOKEN') # Токен вашего бота
