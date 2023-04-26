import config
import re

from pyrogram import Client, enums, types
from plugins import Database, Helper

async def teman_curhat_handler(client: Client, msg: types.Message):
    db = Database(msg.from_user.id)
    teman_curhat = db.get_data_bot(client.id_bot).temancurhat
    top_rate = [] # total rate teman_curhat
    top_id = [] # id teman_curhat
    if len(teman_curhat) == 0:
        return await msg.reply('<b>Saat ini tidak ada Teman curhat yang tersedia.</b>', True, enums.ParseMode.HTML)
    else:
        for uid in teman_curhat:
            rate = teman_curhat[str(uid)]['rate']
            if rate >= 0:
                top_rate.append(rate)
                top_id.append(uid)
        top_rate.sort(reverse=True)
        pesan = "<b>Daftar Teman curhat trusted</b>\n\n"
        pesan += "No — Teman curhat — Rating\n"
        index = 1
        for i in top_rate:
            if index > config.batas_temancurhat:
                break
            for j in top_id:
                if teman_curhat[j]['rate'] == i:
                    pesan += f"<b> {str(index)}.</b> {teman_curhat[j]['username']} ➜ {str(teman_curhat[j]['rate'])} 🍥\n"
                    top_id.remove(j)
                    index += 1
        pesan += f"\nmenampilkan Real talent Teman curhat ONS"
        await msg.reply(pesan, True, enums.ParseMode.HTML)

async def tambah_teman_curhat_handler(client: Client, msg: types.Message):
    helper = Helper(client, msg)
    if re.search(r"^[\/]addtemancurhat(\s|\n)*$", msg.text or msg.caption):
        return await msg.reply_text(
            text="<b>Cara penggunaan tambah Teman curhat</b>\n\n<code>/addtemancurhat id_user</code>\n\nContoh :\n<code>/addtemancurhat 121212021</code>", quote=True,
            parse_mode=enums.ParseMode.HTML
        )
    y = re.search(r"^[\/]addtemancurhat(\s|\n)*(\d+)$", msg.text or msg.caption)
    if y:
        target = y.group(2)
        db = Database(int(target))
        if target in db.get_data_bot(client.id_bot).ban:
            return await msg.reply_text(
                text=f"<i><a href='tg://user?id={str(target)}'>User</a> sedang dalam kondisi banned</i>\n└Tidak dapat menjadikan Teman curhat", quote=True,
                parse_mode=enums.ParseMode.HTML
            )
        if await db.cek_user_didatabase():
            status = [
                'admin', 'owner', 'talent', 'daddy sugar', 'teman curhat',
                'teman curhat', 'girlfriend rent', 'boyfriend rent'
            ]
            member = db.get_data_pelanggan()
            if member.status in status:
                return await msg.reply_text(
                    text=f"❌<i>Terjadi kesalahan, <a href='tg://user?id={str(target)}'>user</a> adalah seorang {member.status.upper()} tidak dapat ditambahkan menjadi Teman curhat</i>", quote=True,
                    parse_mode=enums.ParseMode.HTML
                )
            try:
                a = await client.get_chat(target)
                nama = await helper.escapeHTML(a.first_name if not a.last_name else a.first_name + ' ' + a.last_name)
                await client.send_message(
                    int(target),
                    text=f"<i>Kamu telah menjadi Teman curhat</i>\n└Diangkat oleh : <a href='tg://openmessage?user_id={str(config.id_admin)}'>Admin</a>",
                    parse_mode=enums.ParseMode.HTML
                )
                await db.tambah_teman_curhat(int(target), client.id_bot, nama)
                return await msg.reply_text(
                    text=f"<a href='tg://openmessage?user_id={str(target)}'>User</a> <i>berhasil menjadi Teman curhat</i>\n└Diangkat oleh : <a href='tg://openmessage?user_id={str(config.id_admin)}'>Admin</a>", quote=True,
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
            text="<b>Cara penggunaan tambah Teman Curhat</b>\n\n<code>/addtemancurhat id_user</code>\n\nContoh :\n<code>/addtemancurhat 121212021</code>", quote=True,
            parse_mode=enums.ParseMode.HTML
        )