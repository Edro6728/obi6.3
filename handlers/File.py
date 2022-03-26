import config
import datetime


from telethon import Button,TelegramClient
from pydownloader.tltdownloader import TLTDownloader

import infos

from utils import get_file_size,sizeof_fmt,nice_time

import shutil

async def progress_download(downloader, filename, currentBits, totalBits, speed , time, args, stop=False):
    try:
        bot = args[0]
        message = args[1]
        id = args[2]
        text = '<b>'
        text += '📡 Descargando Archivo....\n'
        text += text_progres(currentBits,totalBits)+'\n'
        text += '➤ Porcentaje: '+str(porcent(currentBits,totalBits))+'%\n\n'
        text += '➤ Total: '+sizeof_fmt(totalBits)+'\n\n'
        text += '➤ Descargado: '+sizeof_fmt(currentBits)+'\n\n'
        text += '➤ Velocidad: '+sizeof_fmt(speed)+'/s\n\n'
        text += '➤ Tiempo de Descarga: '+str(datetime.timedelta(seconds=int(time)))+'s\n'
        text += '</b>'
        await message.edit(text,parse_mode='HTML',
                           buttons=[[Button.inline('💢Cancelar💢','cancel_download '+str(id))]])
    except Exception as ex:
        print(str(ex))
    pass


async def handle(ev,bot,jdb,message_edited=None):

    message = await bot.send_message(ev.sender_id,'⏳Procesando...')

    await message.edit('📡Descargando Archivo...')

    filename = await bot.download_media(ev.message)

    filesize = get_file_size(filename)

    shutil.move(filename,'root/'+filename)

    text = '📡 Subiendo Archivo(s)....\n\n'
    text += text_progres(currentBits,totalBits)+'\n'
        text += '➤ Porcentaje: '+str(porcent(currentBits,totalBits))+'%\n\n'
        text += '➤ Total: '+sizeof_fmt(totalBits)+'\n\n'
        text += '➤ Descargado: '+sizeof_fmt(currentBits)+'\n\n'
        text += '➤ Velocidad: '+sizeof_fmt(speed)+'/s\n\n'
        text += '➤ Tiempo de Descarga: '+str(datetime.timedelta(seconds=int(time)))+'s\n'
        text += '</b>'
    buttons = []
    buttons.append([Button.inline('🗂Abrir Carpeta🗂','open_root')])

    await message.edit(text=text,buttons=buttons)

    pass

