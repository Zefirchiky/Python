import telegram as tg
import telegram.ext as tgext
import random
import json
import time
import datetime
import os
from io import BytesIO, BufferedIOBase
from PIL import Image, ImageEnhance
from telegram.ext import CommandHandler, MessageHandler, filters
from handle_response import handle_response, handle_response_all
from rich.traceback import install
from settings import *

install()
os.chdir("C:\AllArtem\Programer\Python\TG_Bots")

TOKEN = "5049453785:AAHpxHcRmXtZZ374iCEcEo8lr40SQzA_ZNw"
BOT_USERNAME = "@IDNKEKBot"
time_from_start = time.time()
message_num = 0

with open("unique_users.json", "r") as f:
    try:
        unique_users = json.load(f)
    except Exception:
        unique_users = {}


class Cache:
    def __init__(self):
        with open("cache.json", "r") as f:
            try:
                self.data_cache = json.load(f)
            except Exception:
                self.data_cache = {
                    "time": time.time()
                }
        self.times = self.data_cache["time"]
        self.sec_diff = time.time() - self.times

    def get_sec_diff(self):
        return self.sec_diff
    
    def get_sec_diff_five(self):
        t = self.get_sec_diff()
        return t/360 if t/360 > 5 else 5

    def get_date_diff(self):
        return datetime.datetime.fromtimestamp(self.get_sec_diff())

    def data_save(self):
        self.data_cache["time"] = time.time()
        with open("cache.json", "w") as f:
            json.dump(self.data_cache, f, indent=4)




'''------------# Base command #------------'''
async def start_command(update: tg.Update, context: tgext.CallbackContext):
    print(f"{YELLOW_TEXT}User ({update.message.chat.id}: {update.message.from_user.username}) in {update.message.chat.type} ({update.message.chat.title}): \"{update.message.text}\"{FORMAT_CLEAR}")
    answ = "Hi there! I`m only test bot."
    await update.message.reply_text(answ)
    print(f"{MAGENTA_TEXT}Bot: {answ}{FORMAT_CLEAR}")

async def help_command(update: tg.Update, context: tgext.CallbackContext):
    print(f"{YELLOW_TEXT}User ({update.message.chat.id}: {update.message.from_user.username}) in {update.message.chat.type} ({update.message.chat.title}): \"{update.message.text}\"{FORMAT_CLEAR}")
    answ = "I`m bot only for testing some staffs. Now i can:\nCount a unique users that wrote messages (/count y/m/w/d/h/m/s).\nReply some messages (for example write 'f/F' or 'f.')"
    await update.message.reply_text(answ)
    print(f"{MAGENTA_TEXT}Bot: {answ}{FORMAT_CLEAR}")


'''------------# Joke commands #------------'''
async def speed_command(update: tg.Update, context: tgext.CallbackContext):
    print(f"{YELLOW_TEXT}User ({update.message.chat.id}: {update.message.from_user.username}) in {update.message.chat.type} ({update.message.chat.title}): \"{update.message.text}\"{FORMAT_CLEAR}")
    answ = random.choice(('yes', 'YES', 'YES!', 'YES! YES! YES!', 'YEEEEEEEEEEEEEEEEEEEEEEEEES!!!', 'no'))
    await update.message.reply_text(answ)
    print(f"{MAGENTA_TEXT}Bot: {answ}{FORMAT_CLEAR}")

async def joke_command(update: tg.Update, context: tgext.CallbackContext):
    print(f"{YELLOW_TEXT}User ({update.message.chat.id}: {update.message.from_user.username}) in {update.message.chat.type} ({update.message.chat.title}): \"{update.message.text}\"{FORMAT_CLEAR}")
    with open("jokes.txt", "r", encoding="utf-8") as f:
        jokes = f.readlines()
    for i, j in enumerate(jokes):
        jokes[i] = j.replace('*/n', '\n')
    answ = random.choice(jokes)
    await update.message.reply_text(answ)
    print(f"{MAGENTA_TEXT}Bot: {answ}{FORMAT_CLEAR}")

async def layka_command(update: tg.Update, context: tgext.CallbackContext):
    print(f"{YELLOW_TEXT}User ({update.message.chat.id}: {update.message.from_user.username}) in {update.message.chat.type} ({update.message.chat.title}): \"{update.message.text}\"{FORMAT_CLEAR}")
    with open("layka.txt", "r", encoding="utf-8") as f:
        layka = f.readlines()
    layka_l = []
    for i, j in enumerate(layka):
        if j != "\n":
            layka_l.append(j.replace('*/n', '\n'))
    answ = random.choice(layka_l)
    await update.message.reply_text(answ)
    print(f"{MAGENTA_TEXT}Bot: {answ}{FORMAT_CLEAR}")

async def spam_command(update: tg.Update, context: tgext.CallbackContext):
    print(f"{YELLOW_TEXT}User ({update.message.chat.id}: {update.message.from_user.username}) in {update.message.chat.type} ({update.message.chat.title}): \"{update.message.text}\"{FORMAT_CLEAR}")
    text = update.message.text.split()
    try:
        n = int(text[1])
        for i in range(n):
            await update.message.chat.send_message(text[2])
            time.sleep(.5)
    except ValueError:
        await update.message.reply_text("Wrong command")
    print(f"{MAGENTA_TEXT}Bot: {' '.join(text[2:])}{FORMAT_CLEAR}")


'''------------# Count commands #------------'''
async def count_command(update: tg.Update, context: tgext.CallbackContext):
    time_us = int(update.message.date.timestamp())
    is_reply = True
    print(f"{YELLOW_TEXT}User ({update.message.from_user.username}: {update.message.from_user.id}) in {update.message.chat.type} ({update.message.chat.title}): \"{update.message.text}\"{FORMAT_CLEAR}")
    text = update.message.text[7:].replace('.', '').replace(' ', '').lower() if len(update.message.text) >= 9 else '1h'
    unique_users_list = []
    match text[-1]:
        case 'y':
            time_us -= int(text[:-1]) * 3600 * 24 * 30 * 12
            print(time_us)
        case 'm':
            time_us -= int(text[:-1]) * 3600 * 24 * 30
            print(time_us)
        case 'w':
            time_us -= int(text[:-1]) * 3600 * 24 * 7
            print(time_us)
        case 'd':
            time_us -= int(text[:-1]) * 3600 * 24
            print(time_us)
        case 'h':
            time_us -= int(text[:-1]) * 3600
            print(time_us)
        case 'm':
            time_us -= int(text[:-1]) * 60
            print(time_us)
        case 's':
            time_us -= int(text[:-1])
            print(time_us)
        case other:
            await update.message.reply_text(f"Please enter correct time!")
            is_reply = False
        
    if update.message.chat.type == 'group' or update.message.chat.type == 'supergroup':
        for user_id, last_time in unique_users[str(update.message.chat.id)].items():
            if last_time >= time_us:
                unique_users_list.append(user_id)
        if is_reply:
            await update.message.reply_text(f"There is {len(unique_users_list)} user in the last {text}.")
    else:
        await update.message.reply_text(f"There is 1 user always -_-")

async def m_num_command(update: tg.Update, context: tgext.CallbackContext):
    print(f"{YELLOW_TEXT}User ({update.message.chat.id}: {update.message.from_user.username}) in {update.message.chat.type} ({update.message.chat.title}): \"{update.message.text}\"{FORMAT_CLEAR}")
    answ = f"There are {message_num} messages since {datetime.datetime.fromtimestamp(int(time.time() - data_cache.get_sec_diff()))}"
    await update.message.reply_text()
    print(f"{MAGENTA_TEXT}Bot: {answ}{FORMAT_CLEAR}")

async def m_all_num_command(update: tg.Update, context: tgext.CallbackContext):
    print(f"{YELLOW_TEXT}User ({update.message.chat.id}: {update.message.from_user.username}) in {update.message.chat.type} ({update.message.chat.title}): \"{update.message.text}\"{FORMAT_CLEAR}")
    answ = f"There are {update.message.message_id} messages for all time"
    await update.message.reply_text(answ)
    print(f"{MAGENTA_TEXT}Bot: {answ}{FORMAT_CLEAR}")

    
'''------------# Other commands #------------'''
async def idea_command(update: tg.Update, context: tgext.CallbackContext):
    text = update.message.text
    chat_type = update.message.chat.type
    chat_name = update.message.chat.title
    if ':' in text or '-' in text:
        await update.message.reply_text("Cool idea!\nI`ll save it...")
        print(f"{YELLOW_TEXT}User ({update.message.from_user.username}: {update.message.from_user.id}) in {chat_type} ({chat_name}): \"{text}\"{FORMAT_CLEAR}")
        
        with open("IDEAS.txt", 'a', encoding="utf-8") as f:
            f.write(f'"{str(text[6:])}"\n')
            
    else:
        print(f'{MAGENTA_TEXT}Bad idea!\nI don` understand it...')
        await update.message.reply_text("Bad idea!\nI don` understand it...")
    

'''------------# Images commands #------------'''
async def anti_command(image, text, update: tg.Update):
    print(f"{YELLOW_TEXT}User ({update.message.chat.id}: {update.message.from_user.username}) in {update.message.chat.type} ({update.message.chat.title}): \"{update.message.text}\"\n \
          {update.message.photo[-1].file_id}{FORMAT_CLEAR}")
    image = await update.message.effective_attachment[-1].get_file()
    await image.download_to_drive("C:\AllArtem\Programer\Python\TG_Bots\image.jpg")
    image = Image.open("image.jpg")

    x = int(text.split()[1]) if len(text.split()) > 6 else -1
    image = ImageEnhance.Contrast(image).enhance(x)
    image.save("C:\AllArtem\Programer\Python\TG_Bots\image.jpg")

    await update.message.reply_photo("C:\AllArtem\Programer\Python\TG_Bots\image.jpg")

async def wtf_command(image, text, update: tg.Update):
    print(f"{YELLOW_TEXT}User ({update.message.chat.id}: {update.message.from_user.username}) in {update.message.chat.type} ({update.message.chat.title}): \"{update.message.text}\"\n \
          {update.message.photo[-1].file_id}{FORMAT_CLEAR}")
    it = await update.message.effective_attachment[-1].get_file()
    await it.download_to_drive("C:\AllArtem\Programer\Python\TG_Bots\image.jpg")
    image = Image.open("image.jpg")

    x = int(text.split()[1]) if len(text.split()) > 1 else False
    image = ImageEnhance.Contrast(image)
    image = image.enhance(x if x else random.randint(-100, 100))
    image = ImageEnhance.Sharpness(image)
    image = image.enhance(x if x else random.randint(-100, 100))
    image = ImageEnhance.Color(image)
    image = image.enhance(x if x else random.randint(-100, 100))
    image = ImageEnhance.Brightness(image)
    image = image.enhance(max(1, x) if x else random.randint(1, 100))
    image.save("C:\AllArtem\Programer\Python\TG_Bots\image.jpg")

    await update.message.reply_photo("C:\AllArtem\Programer\Python\TG_Bots\image.jpg")

        

        
'''------------# All handler #------------'''
async def all_handler(update: tg.Update, context: tgext.CallbackContext):
    '''Check all messages'''
    chat_type = update.message.chat.type
    global message_num
    message_num += 1

    # Group or not | Start with bot username or not
    if chat_type == 'group' or chat_type == 'supergroup':
        try:
            unique_users[str(update.message.chat.id)][str(update.message.from_user.id)] = int(update.message.date.timestamp())
        except KeyError:
            unique_users[str(update.message.chat.id)] = {str(update.message.from_user.id): int(update.message.date.timestamp())}
        with open("unique_users.json", 'w')as f:
            json.dump(unique_users, f, indent=4)   
    else:
        unique_users[str(update.message.chat.id)] = int(update.message.date.timestamp())
        with open("unique_users.json", 'w')as f:
            json.dump(unique_users, f, indent=4)

    data_cache.data_save()

    # await update.message.reply_animation('https://i0.wp.com/www.printmag.com/wp-content/uploads/2021/02/4cbe8d_f1ed2800a49649848102c68fc5a66e53mv2.gif?resize=476%2C280&ssl=1')


'''------------# Text handler #------------'''
async def message_text_handler(update: tg.Update, context: tgext.CallbackContext):
    chat_type = update.message.chat.type
    chat_name = update.message.chat.title
    text = update.message.text
    
    print(f'{GREEN_TEXT}User ({update.message.from_user.username}: {update.message.from_user.id}) in {chat_type} ({chat_name}): "{text}"{FORMAT_CLEAR}')
    
    if chat_type == 'group' or chat_type == 'supergroup':
        if BOT_USERNAME in text:
            if (time.time() - time_from_start) > data_cache.get_sec_diff_five():
                new_text = text.replace(BOT_USERNAME+' ', '')
                response = handle_response(new_text)
            else:
                response = 0
            if not response:
                return   
        else:
            if (time.time() - time_from_start) > data_cache.get_sec_diff_five():
                response = handle_response_all(text, update.message.from_user.username)
            else:
                response = 0
            if not response:
                return   
    else:
        response = handle_response(text)
    print(f'{MAGENTA_TEXT}Bot: "{response}"{FORMAT_CLEAR}')
    if len(response) > 8 and response[-8:] ==  ' */image':
        await update.message.reply_photo(response[:-8])
    elif len(response) > 6 and response[-6:] ==  ' */gif':
        await update.message.reply_animation(response[:-6])
    else:
        await update.message.reply_text(response)
    
    
'''------------# Image handlers #------------'''
async def message_sticker_handler(update: tg.Update, context: tgext.CallbackContext):
    chat_type = update.message.chat.type
    chat_name = update.message.chat.title
    text = update.message.sticker
    
    print(f'{BLUE_TEXT}User ({update.message.from_user.username}: {update.message.from_user.id}) in {chat_type} ({chat_name}) send sticker: "{text.emoji} ({text.set_name}),\n \
          ID: {text.file_id}"){FORMAT_CLEAR}')
    
async def message_photo_handler(update: tg.Update, context: tgext.CallbackContext):
    chat_type = update.message.chat.type
    chat_name = update.message.chat.title
    text = update.message.caption
    image = update.message.photo

    if "/anti" in text:
        await anti_command(image, text, update)
        return
    elif "/wtf" in text:
        await wtf_command(image, text, update)
        return
    
    if text:
    
        print(f'{CYAN_TEXT}User ({update.message.from_user.username}: {update.message.from_user.id}) in {chat_type} ({chat_name}) send photo: "{text}\n \
            ID: {image[-1].file_id}"{FORMAT_CLEAR}')
        
        if chat_type == 'group' or chat_type == 'supergroup':
            if BOT_USERNAME in text:
                if (time.time() - time_from_start) > data_cache.get_sec_diff_five():
                    new_text = text.replace(BOT_USERNAME+' ', '')
                    response = handle_response(new_text)
                else:
                    response = 0
                if not response:
                    return   
            else:
                return   
        else:
            response = handle_response(text)
        print(f'{MAGENTA_TEXT}Bot: "{response}"{FORMAT_CLEAR}')
        await update.message.reply_photo(image[-1].file_id, response)
        
    else:
        print(f'{CYAN_TEXT}User ({update.message.from_user.username}: {update.message.from_user.id}) in {chat_type} ({chat_name}) send photo:\n \
            "ID: {image[-1].file_id}"{FORMAT_CLEAR}')
        if not (chat_type == 'group' or chat_type == 'supergroup'):
            print(f'{MAGENTA_TEXT}Bot: "{image[-1].file_id}"{FORMAT_CLEAR}')
            await update.message.reply_photo(image[-1].file_id)
    

'''------------# Animation handler #------------'''
async def message_animation_handler(update: tg.Update, context: tgext.CallbackContext):
    chat_type = update.message.chat.type
    chat_name = update.message.chat.title
    text = update.message.animation
    
    print(f'{BLUE_TEXT}User ({update.message.from_user.username}: {update.message.from_user.id}) in {chat_type} ({chat_name}) send GIF:\n \
          ID: {text.file_id}{FORMAT_CLEAR}')
    

'''------------# Error handler #------------'''
async def error_handler(update: tg.Update, context: tgext.CallbackContext):
    print(f"{RED_TEXT}Saving data...{FORMAT_CLEAR}")
    # with open("unique_users.json", 'w')as f:
    #     json.dump(unique_users, f, indent=4)
    print(f"{RED_TEXT}Update {update} caused error {context.error}{FORMAT_CLEAR}")


'''------------# Test handler (useless) #------------'''
async def test(update: tg.Update, context: tgext.CallbackContext):
    print(f"edited {update.edited_message.text}")




data_cache = Cache()
def main():
    print("Starting...")
    app = tgext.Application.builder().token(TOKEN).build()
    print(f'Last finish: {datetime.datetime.fromtimestamp(time.time() - data_cache.get_sec_diff())}')
    
    '''------------# Commands handlers #------------'''
    # Base
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    # Jokes
    app.add_handler(CommandHandler("speed", speed_command))
    app.add_handler(CommandHandler("joke", joke_command))
    app.add_handler(CommandHandler("layka", layka_command))
    app.add_handler(CommandHandler("spam", spam_command))
    # Counters
    app.add_handler(CommandHandler("count", count_command))
    app.add_handler(CommandHandler("m_num", m_num_command))
    app.add_handler(CommandHandler("m_all_num", m_all_num_command))
    # Other
    app.add_handler(CommandHandler("idea", idea_command))
    
    '''------------# Message handlers #------------'''
    # All
    app.add_handler(MessageHandler(filters.ALL, all_handler)) 
    # Text
    app.add_handler(MessageHandler(filters.TEXT, message_text_handler), group=1)
    app.add_handler(MessageHandler(filters.UpdateType.EDITED, test), group=1)
    # Image
    app.add_handler(MessageHandler(filters.Sticker.ALL, message_sticker_handler),group=2)
    app.add_handler(MessageHandler(filters.PHOTO, message_photo_handler), group=2)
    # Video / Animation
    app.add_handler(MessageHandler(filters.ANIMATION, message_animation_handler), group=3)
    
    '''------------# Error handler #------------'''
    app.add_error_handler(error_handler)
    
    '''------------# Run #------------'''
    app.run_polling()
    input()
    

if __name__ == "__main__":
    main()
    input()

    