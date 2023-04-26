import config
import re

from pyrogram import Client, enums, types
from plugins import Database, Helper

async def pro_player_handler(client: Client, msg: types.Message):
    db = Database(msg.from_user.id)
    pro_player = db.get_data_bot(client.id_bot).proplayer
    top_rate = [] # total rate pro_player
    top_id = [] # id pro_player
    if len(pro_player) == 0:
        return await msg.reply('<b>Saat ini tidak ada Proplayer yang tersedia.</b>', True, enums.ParseMode.HTML)
    else:
        for uid in pro_player:
            rate = pro_player[str(uid)]['rate']
            if rate >= 0:
                top_rate.append(rate)
                top_id.append(uid)
        top_rate.sort(reverse=True)
        pesan = "<b>Daftar Proplayer trusted</b>\n\n"
        pesan += "No — Proplayer — Rating\n"
        index = 1
        for i in top_rate:
            if index > config.batas_proplayer:
                break
            for j in top_id:
                if pro_player[j]['rate'] == i:
                    pesan += f"<b> {str(index)}.</b> {pro_player[j]['username']} ➜ {str(pro_player[j]['rate'])} 🍬\n"
                    top_id.remove(j)
                    index += 1
        pesan += f"\nmenampilkan Real talent Proplayer ONS"
        await msg.reply(pesan, True, enums.ParseMode.HTML)

async def tambah_pro_player_handler(client: Client, msg: types.Message):
    helper = Helper(client, msg)
    if re.search(r"^[\/]addproplayer(\s|\n)*$", msg.text or msg.caption):
        return await msg.reply_text(
            text="<b>Cara penggunaan tambah Proplayer</b>\n\n<code>/addproplayer id_user</code>\n\nContoh :\n<code>/addproplayer 121212021</code>", quote=True,
            parse_mode=enums.ParseMode.HTML
        )
    y = re.search(r"^[\/]addproplayer(\s|\n)*(\d+)$", msg.text or msg.caption)
    if y:
        target = y.group(2)
        db = Database(int(target))
        if target in db.get_data_bot(client.id_bot).ban:
            return await msg.reply_text(
                text=f"<i><a href='tg://user?id={str(target)}'>User</a> sedang dalam kondisi banned</i>\n└Tidak dapat menjadikan Proplayer", quote=True,
                parse_mode=enums.ParseMode.HTML
            )
        if await db.cek_user_didatabase():
            status = [
                'admin', 'owner', 'talent', 'daddy sugar', 'proplayer',
                'teman curhat', 'girlfriend rent', 'boyfriend rent'
            ]
            member = db.get_data_pelanggan()
            if member.status in status:
                return await msg.reply_text(
                    text=f"❌<i>Terjadi kesalahan, <a href='tg://user?id={str(target)}'>user</a> adalah seorang {member.status.upper()} tidak dapat ditambahkan menjadi Proplayer</i>", quote=True,
                    parse_mode=enums.ParseMode.HTML
                )
            try:
                a = await client.get_chat(target)
                nama = await helper.escapeHTML(a.first_name if not a.last_name else a.first_name + ' ' + a.last_name)
                await client.send_message(
                    int(target),
                    text=f"<i>Kamu telah menjadi Proplayer</i>\n└Diangkat oleh : <a href='tg://openmessage?user_id={str(config.id_admin)}'>Admin</a>",
                    parse_mode=enums.ParseMode.HTML
                )
                await db.tambah_pro_player(int(target), client.id_bot, nama)
                return await msg.reply_text(
                    text=f"<a href='tg://openmessage?user_id={str(target)}'>User</a> <i>berhasil menjadi Proplayer</i>\n└Diangkat oleh : <a href='tg://openmessage?user_id={str(config.id_admin)}'>Admin</a>", quote=True,
                    parse_mode=enums.ParseMode.HTML
                )
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
        return await msg.reply_text(
            text="<b>Cara penggunaan tambah Proplayer</b>\n\n<code>/addproplayer id_user</code>\n\nContoh :\n<code>/addproplayer 121212021</code>", quote=True,
            parse_mode=enums.ParseMode.HTML
        )