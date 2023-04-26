import config
import re

from pyrogram import Client, types, enums
from plugins import Database, Helper
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Update



async def send_with_pic_handler(client: Client, msg: types.Message, key: str, hastag: list):
    db = Database(msg.from_user.id)
    helper = Helper(client, msg)
    user = db.get_data_pelanggan()
    if msg.text or msg.photo or msg.video or msg.voice:
        menfess = user.menfess
        all_menfess = user.all_menfess
        coin = user.coin
        if menfess >= config.batas_kirim:
            if user.status == 'member' or user.status == 'talent' or user.status == 'non member' or user.status == 'girlfriend rent' or user.status == 'proplayer' or user.status == 'teman curhat' or user.status == 'daddy sugar' or user.status == 'boyfriend rent' or user.status == 'sad girl' or user.status == 'melayu' or user.status == 'balinese' or user.status == 'jakartans' or user.status == 'pick me' or user.status == 'borneoensis' or user.status == 'body goals' or user.status == 'abg' or user.status == 'baby girl' or user.status == 'wong jowo':
                if coin >= config.biaya_kirim:
                    coin = user.coin - config.biaya_kirim
                else:
                    return await msg.reply(f'🙅🏻‍♀️ <b>Pesan Gagal Terkirim</b> karena <b>Daily send</b> kamu telah habis serta <b>coin</b> mu kurang dari <b>100 ONS</b> untuk mengirim menfess, segera cek /status kamu.\n\n <b>Daily send</b> direset setiap jam 1 pagi', quote=True)

        if key == hastag[0]:
            picture = config.pic_girl
        if key == hastag[1]:
            picture = config.pic_boy
        if key == hastag[1] or key == hastag[0]:
            if user.status == 'talent':
                picture = config.pic_talent
        if key == hastag[1] or key == hastag[0]:
            if user.status == 'gf rent':
                picture = config.pic_gfrent
        if key == hastag[1] or key == hastag[0]:
            if user.status == 'proplayer':
                picture = config.pic_proplayer
        if key == hastag[1] or key == hastag[0]:
            if user.status == 'teman curhat':
                picture = config.pic_temancurhat
        if key == hastag[1] or key == hastag[0]:
            if user.status == 'jakartans':
                picture = config.pic_jakartans
        if key == hastag[1] or key == hastag[0]:
            if user.status == 'balinese':
                picture = config.pic_balinese
        if key == hastag[1] or key == hastag[0]:
            if user.status == 'borneoensis':
                picture = config.pic_borneo
        if key == hastag[1] or key == hastag[0]:
            if user.status == 'melayu':
                picture = config.pic_melayu
        if key == hastag[1] or key == hastag[0]:
            if user.status == 'sad girl':
                picture = config.pic_sadgirl
        if key == hastag[1] or key == hastag[0]:
            if user.status == 'body goals':
                picture = config.pic_bodygoals
        if key == hastag[1] or key == hastag[0]:
            if user.status == 'wong jowo':
                picture = config.pic_wongjowo
        if key == hastag[1] or key == hastag[0]:
            if user.status == 'abg':
                picture = config.pic_abg
        if key == hastag[1] or key == hastag[0]:
            if user.status == 'baby girl':
                picture = config.pic_babygirl
        if key == hastag[1] or key == hastag[0]:
            if user.status == 'pick me':
                picture = config.pic_pickme        
        if key == hastag[1] or key == hastag[0]:
            if user.status == 'bf rent':
                picture = config.pic_bfrent
        if key == hastag[1] or key == hastag[0]:
            if user.status == 'daddy sugar':
                picture = config.pic_daddysugar

        link = await get_link()
        caption = msg.text or msg.caption
        entities = msg.entities or msg.caption_entities


        kirim = await client.send_photo(config.channel_1, picture, caption, caption_entities=entities)
        await helper.send_to_channel_log(type="log_channel", link=link + str(kirim.id))
        await db.update_menfess(coin, menfess, all_menfess)
        await helper.send_to_user_id(type="send_user", link=link + str(kirim.id))
    else:
        await msg.reply('media yang didukung photo, video dan voice')

async def send_menfess_handler(client: Client, msg: types.Message):
    helper = Helper(client, msg)
    db = Database(msg.from_user.id)
    db_user = db.get_data_pelanggan()
    db_bot = db.get_data_bot(client.id_bot).kirimchannel
    if msg.text or msg.photo or msg.video or msg.voice:
        if msg.photo and not db_bot.photo:
            if db_user.status == 'member' or db_user.status == 'talent' or db_user.status == 'non member' or db_user.status == 'daddy sugar' or db_user.status == 'daddy sugar':
                return await msg.reply('Tidak bisa mengirim photo, karena sedang dinonaktifkan oleh admin', True)
        elif msg.video and not db_bot.video:
            if db_user.status == 'member' or db_user.status == 'talent':
                return await msg.reply('Tidak bisa mengirim video, karena sedang dinonaktifkan oleh admin', True)
        elif msg.voice and not db_bot.voice:
            if db_user.status == 'member' or db_user.status == 'talent':
                return await msg.reply('Tidak bisa mengirim voice, karena sedang dinonaktifkan oleh admin', True)

        menfess = db_user.menfess
        all_menfess = db_user.all_menfess
        coin = db_user.coin
        if menfess >= config.batas_kirim:
            if db_user.status == 'member' or db_user.status == 'talent' or db_user.status == 'non member' or db_user.status == 'girlfriend rent' or db_user.status == 'proplayer' or db_user.status == 'teman curhat' or db_user.status == 'daddy sugar' or db_user.status == 'boyfriend rent' or db_user.status == 'sad girl' or db_user.status == 'melayu' or db_user.status == 'balinese' or db_user.status == 'jakartans' or db_user.status == 'pick me' or db_user.status == 'borneoensis' or db_user.status == 'body goals' or db_user.status == 'abg' or db_user.status == 'baby girl' or db_user.status == 'wong jowo':
                if coin >= config.biaya_kirim:
                    coin = db_user.coin - config.biaya_kirim
                else:
                    return await msg.reply(f'🙅🏻‍♀️ <b>Pesan Gagal Terkirim</b> karena <b>Daily send</b> kamu telah habis serta <b>coin</b> mu kurang dari <b>100 ONS</b> untuk mengirim menfess, segera cek /status kamu.\n\n <b>Daily send</b> direset setiap jam 1 pagi', quote=True)

        link = await get_link()
        kirim = await client.copy_message(config.channel_1, msg.from_user.id, msg.id)
        await helper.send_to_channel_log(type="log_channel", link=link + str(kirim.id))
        await db.update_menfess(coin, menfess, all_menfess)
        await helper.send_to_user_id(type="send_user", link=link + str(kirim.id))
    else:
        await msg.reply('media yang didukung photo, video dan voice')

async def get_link():
    anu = str(config.channel_1).split('-100')[1]
    return f"https://t.me/c/{anu}/"

async def transfer_coin_handler(client: Client, msg: types.Message):
    if re.search(r"^[\/]tf_coin(\s|\n)*$", msg.text or msg.caption):
        err = "<i>perintah salah /tf_coin [jmlh_coin]</i>" if msg.reply_to_message else "<i>perintah salah /tf_coin [id_user] [jmlh_coin]</i>"
        return await msg.reply(err, True)
    helper = Helper(client, msg)
    if re.search(r"^[\/]tf_coin\s(\d+)(\s(\d+))?", msg.text or msg.caption):
        x = re.search(r"^[\/]tf_coin\s(\d+)(\s(\d+))$", msg.text or msg.caption)
        if x:
            target = x.group(1)
            coin = x.group(3)
        y = re.search(r"^[\/]tf_coin\s(\d+)$", msg.text or msg.caption)
        if y:
            if msg.reply_to_message:
                if msg.reply_to_message.from_user.is_bot == True:
                    return await msg.reply('🤖Bot tidak dapat ditranfer coin', True)
                elif msg.reply_to_message.sender_chat:
                    return await msg.reply('channel tidak dapat ditranfer coin', True)
                else:
                    target = msg.reply_to_message.from_user.id
                    coin = y.group(1)
            else:
                return await msg.reply('sambil mereply sebuah pesan', True)
        
        if msg.from_user.id == int(target):
            return await msg.reply('<i>Tidak dapat transfer coin untuk diri sendiri</i>', True)

        user_db = Database(msg.from_user.id)
        anu = user_db.get_data_pelanggan()
        my_coin = anu.coin
        if my_coin >= int(coin):
            db_target = Database(int(target))
            if await db_target.cek_user_didatabase():
                target_db = db_target.get_data_pelanggan()
                ditransfer = my_coin - int(coin)
                diterima = target_db.coin + int(coin)
                nama = "Admin" if anu.status == 'owner' or anu.status == 'admin' else msg.from_user.first_name
                nama = await helper.escapeHTML(nama)
                try:
                    await client.send_message(target, f"Coin berhasil ditambahkan senilai {coin} coin, cek /status\n└Oleh <a href='tg://user?id={msg.from_user.id}'>{nama}</a>")
                    await user_db.transfer_coin(ditransfer, diterima, target_db.coin_full, int(target))
                    await msg.reply(f'<i>berhasil transfer coin sebesar {coin} coin💰</i>', True)
                except Exception as e:
                    return await msg.reply_text(
                        text=f"❌<i>Terjadi kesalahan, sepertinya user memblokir bot</i>\n\n{e}", quote=True,
                        parse_mode=enums.ParseMode.HTML
                    )
            else:
                return await msg.reply_text(
                    text=f"<i><a href='tg://user?id={str(target)}'>user</a> tidak terdaftar didatabase</i>", quote=True,
                    parse_mode=enums.ParseMode.HTML
                )
        else:
            return await msg.reply(f'<i>coin kamu ({my_coin}) tidak dapat transfer coin.</i>', True)
