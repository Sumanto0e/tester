import config
import re

from pyrogram import Client, enums, types
from plugins import Database


async def tambah_admin_handler(client: Client, msg: types.Message):
    if re.search(r"^[\/]admin(\s|\n)*$", msg.text):
        return await msg.reply_text(
            text="<b>Cara penggunaan tambah admin</b>\n\n<code>/admin id_user</code>\n\nContoh :\n<code>/admin 121212021</code>", quote=True,
            parse_mode=enums.ParseMode.HTML
        )
    y = re.search(r"^[\/]admin(\s|\n)*(\d+)$", msg.text)
    if y:
        target = y.group(2)
        db = Database(int(target))
        if target in db.get_data_bot(client.id_bot).ban:
            return await msg.reply_text(
                text=f"<i><a href='tg://user?id={str(target)}'>User</a> sedang dalam kondisi banned</i>\n└Tidak dapat menjadikan user admin", quote=True,
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
                    text=f"❌<i>Terjadi kesalahan, <a href='tg://user?id={str(target)}'>user</a> adalah seorang {member.status.upper()}</i>", quote=True,
                    parse_mode=enums.ParseMode.HTML
                )
            try:
                await client.send_message(
                    int(target),
                    text=f"<i>Kamu telah menjadi admin bot</i>\n└Diangkat oleh : <a href='tg://openmessage?user_id={str(config.id_admin)}'>Admin</a>",
                    parse_mode=enums.ParseMode.HTML
                )
                await db.update_admin(int(target), client.id_bot)
                return await msg.reply_text(
                    text=f"<a href='tg://openmessage?user_id={str(target)}'>User</a> <i>berhasil menjadi admin bot</i>\n└Diangkat oleh : <a href='tg://openmessage?user_id={str(config.id_admin)}'>Admin</a>", quote=True,
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
            text="<b>Cara penggunaan tambah admin</b>\n\n<code>/admin id_user</code>\n\nContoh :\n<code>/admin 121212021</code>", quote=True,
            parse_mode=enums.ParseMode.HTML
        )


async def hapus_admin_handler(client: Client, msg: types.Message):
    if re.search(r"^[\/]unadmin(\s|\n)*$", msg.text):
        return await msg.reply_text(
            text="<b>Cara penggunaan mencabut status admin</b>\n\n<code>/unadmin id_user</code>\n\nContoh :\n<code>/unadmin 121212021</code>", quote=True,
            parse_mode=enums.ParseMode.HTML
        )
    y = re.search(r"^[\/]unadmin(\s|\n)*(\d+)$", msg.text)
    if y:
        target = y.group(2)
        db = Database(int(target))
        if await db.cek_user_didatabase():
            status = [
                'owner', 'talent', 'daddy sugar', 'proplayer',
                'teman curhat', 'girlfriend rent', 'boyfriend rent'
            ]
            member = db.get_data_pelanggan()
            if member.status in status:
                return await msg.reply_text(
                    text=f"❌<i>Terjadi kesalahan, <a href='tg://user?id={str(target)}'>user</a> adalah seorang {member.status.upper()}</i>", quote=True,
                    parse_mode=enums.ParseMode.HTML
                )
            if member.status == 'admin':
                try:
                    await client.send_message(
                        int(target),
                        text=f"<i>Sayangnya owner telah mencabut jabatanmu sebagai admin</i>\n└Diturunkan oleh : <a href='tg://openmessage?user_id={str(config.id_admin)}'>Admin</a>",
                        parse_mode=enums.ParseMode.HTML
                    )
                    await db.hapus_admin(int(target), client.id_bot)
                    return await msg.reply_text(
                        text=f"<a href='tg://openmessage?user_id={str(target)}'>User</a> <i>berhasil diturunkan menjadi member</i>\n└Diturunkan oleh : <a href='tg://openmessage?user_id={str(config.id_admin)}'>Admin</a>", quote=True,
                        parse_mode=enums.ParseMode.HTML
                    )
                except Exception as e:
                    return await msg.reply_text(
                        text=f"❌<i>Terjadi kesalahan, sepertinya user memblokir bot</i>\n\n{e}", quote=True,
                        parse_mode=enums.ParseMode.HTML
                    )
            else:
                return await msg.reply_text(
                    text=f"<i><a href='tg://openmessage?user_id={str(target)}'>User</a> bukan seorang admin</i>", quote=True,
                    parse_mode=enums.ParseMode.HTML
                )
        else:
            return await msg.reply_text(
                text=f"<i><a href='tg://user?id={str(target)}'>user</a> tidak terdaftar didatabase</i>", quote=True,
                parse_mode=enums.ParseMode.HTML
            )
    else:
        await msg.reply_text(
            text="<b>Cara penggunaan mencabut status admin</b>\n\n<code>/unadmin id_user</code>\n\nContoh :\n<code>/unadmin 121212021</code>", quote=True,
            parse_mode=enums.ParseMode.HTML
        )

async def tambah_member_handler(client: Client, msg: types.Message):
    if re.search(r"^[\/]member(\s|\n)*$", msg.text):
        return await msg.reply_text(
            text="<b>Cara penggunaan tambah member</b>\n\n<code>/member id_user</code>\n\nContoh :\n<code>/member 121212021</code>", quote=True,
            parse_mode=enums.ParseMode.HTML
        )
    y = re.search(r"^[\/]member(\s|\n)*(\d+)$", msg.text)
    if y:
        target = y.group(2)
        db = Database(int(target))
        db_user = db.get_data_pelanggan()
        coin = db_user.coin
        if target in db.get_data_bot(client.id_bot).ban:
            return await msg.reply_text(
                text=f"<i><a href='tg://user?id={str(target)}'>User</a> sedang dalam kondisi banned</i>\n└Tidak dapat menjadikan user member", quote=True,
                parse_mode=enums.ParseMode.HTML
            )
        if coin >= config.biaya_member:
            coin = db_user.coin - config.biaya_member
            await db.update_coinmember(coin)
            if await db.cek_user_didatabase():
                status = [
                    'admin', 'owner'
                ]
                member = db.get_data_pelanggan()
                if member.status in status:
                    return await msg.reply_text(
                        text=f"❌<i>Terjadi kesalahan, <a href='tg://user?id={str(target)}'>user</a> adalah seorang {member.status.upper()}</i>", quote=True,
                        parse_mode=enums.ParseMode.HTML
                    )
                try:
                    await client.send_message(
                        int(target),
                        text=f"<i>Kamu telah menjadi member bot</i>\n└Diangkat oleh : <a href='tg://openmessage?user_id={str(config.id_admin)}'>Admin</a>",
                        parse_mode=enums.ParseMode.HTML
                    )
                    await db.update_member(int(target), client.id_bot)
                    return await msg.reply_text(
                        text=f"<a href='tg://openmessage?user_id={str(target)}'>User</a> <i>berhasil menjadi member bot</i>\n└Diangkat oleh : <a href='tg://openmessage?user_id={str(config.id_admin)}'>Admin</a>", quote=True,
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
            return await msg.reply(f'<i>coin kamu hanya {coin} ONS, biaya untuk menjadi member sebesar 2000 ONS.</i>', True)
    else:
        return await msg.reply_text(
            text="<b>Cara penggunaan tambah member</b>\n\n<code>/member id_user</code>\n\nContoh :\n<code>/member 121212021</code>", quote=True,
            parse_mode=enums.ParseMode.HTML
        )


async def hapus_member_handler(client: Client, msg: types.Message):
    if re.search(r"^[\/]unmember(\s|\n)*$", msg.text):
        return await msg.reply_text(
            text="<b>Cara penggunaan mencabut status member</b>\n\n<code>/unmember id_user</code>\n\nContoh :\n<code>/unmember 121212021</code>", quote=True,
            parse_mode=enums.ParseMode.HTML
        )
    y = re.search(r"^[\/]unmember(\s|\n)*(\d+)$", msg.text)
    if y:
        target = y.group(2)
        db = Database(int(target))
        if await db.cek_user_didatabase():
            status = [
                'admin', 'owner', 'talent', 'daddy sugar', 'proplayer',
                'teman curhat', 'girlfriend rent', 'boyfriend rent'
            ]
            member = db.get_data_pelanggan()
            if member.status in status:
                return await msg.reply_text(
                    text=f"❌<i>Terjadi kesalahan, <a href='tg://user?id={str(target)}'>user</a> adalah seorang {member.status.upper()}</i>", quote=True,
                    parse_mode=enums.ParseMode.HTML
                )
            if member.status == 'member':
                try:
                    await client.send_message(
                        int(target),
                        text=f"<i>Sayangnya owner telah mencabut statusmu sebagai member</i>\n└Diturunkan oleh : <a href='tg://openmessage?user_id={str(config.id_admin)}'>Admin</a>",
                        parse_mode=enums.ParseMode.HTML
                    )
                    await db.hapus_member(int(target), client.id_bot)
                    return await msg.reply_text(
                        text=f"<a href='tg://openmessage?user_id={str(target)}'>User</a> <i>berhasil diturunkan menjadi member</i>\n└Diturunkan oleh : <a href='tg://openmessage?user_id={str(config.id_admin)}'>Admin</a>", quote=True,
                        parse_mode=enums.ParseMode.HTML
                    )
                except Exception as e:
                    return await msg.reply_text(
                        text=f"❌<i>Terjadi kesalahan, sepertinya user memblokir bot</i>\n\n{e}", quote=True,
                        parse_mode=enums.ParseMode.HTML
                    )
            else:
                return await msg.reply_text(
                    text=f"<i><a href='tg://openmessage?user_id={str(target)}'>User</a> bukan seorang member</i>", quote=True,
                    parse_mode=enums.ParseMode.HTML
                )
        else:
            return await msg.reply_text(
                text=f"<i><a href='tg://user?id={str(target)}'>user</a> tidak terdaftar didatabase</i>", quote=True,
                parse_mode=enums.ParseMode.HTML
            )
    else:
        await msg.reply_text(
            text="<b>Cara penggunaan mencabut status member</b>\n\n<code>/unmember id_user</code>\n\nContoh :\n<code>/unmember 121212021</code>", quote=True,
            parse_mode=enums.ParseMode.HTML
        )
