import config
import re

from pyrogram import Client, enums, types
from plugins import Database, Helper

async def tambah_jakartans_handler(client: Client, msg: types.Message):
    helper = Helper(client, msg)
    if re.search(r"^[\/]addjakartans(\s|\n)*$", msg.text or msg.caption):
        return await msg.reply_text(
            text="<b>Cara penggunaan tambah jakartans</b>\n\n<code>/addjakartans id_user</code>\n\nContoh :\n<code>/addjakartans 121212021</code>", quote=True,
            parse_mode=enums.ParseMode.HTML
        )
    y = re.search(r"^[\/]addjakartans(\s|\n)*(\d+)$", msg.text or msg.caption)
    if y:
        target = y.group(2)
        db = Database(int(target))
        db_user = db.get_data_pelanggan()
        coin = db_user.coin

        if target in db.get_data_bot(client.id_bot).ban:
            return await msg.reply_text(
                text=f"<i><a href='tg://user?id={str(target)}'>User</a> sedang dalam kondisi banned</i>\n└Tidak dapat menjadikan jakartans", quote=True,
                parse_mode=enums.ParseMode.HTML
            )
        if coin >= config.biaya_status:
            coin = db_user.coin - config.biaya_status
            await db.update_status(coin)
            if await db.cek_user_didatabase():
                status = [
                    'admin', 'owner', 'talent', 'daddy sugar', 'prolpayer',
                    'teman curhat', 'girlfriend rent', 'boyfriend rent'
                ]
                member = db.get_data_pelanggan()
                if member.status in status:
                    return await msg.reply_text(
                        text=f"❌<i>Terjadi kesalahan, <a href='tg://user?id={str(target)}'>user</a> adalah seorang {member.status.upper()} tidak dapat ditambahkan menjadi jakartans</i>", quote=True,
                        parse_mode=enums.ParseMode.HTML
                    )
                try:
                    a = await client.get_chat(target)
                    nama = await helper.escapeHTML(a.first_name if not a.last_name else a.first_name + ' ' + a.last_name)
                    await client.send_message(
                        int(target),
                        text=f"<i>Status kamu telah menjadi Jakartans</i>\n└Diangkat oleh : <a href='tg://openmessage?user_id={str(config.id_admin)}'>Admin</a>",
                        parse_mode=enums.ParseMode.HTML
                    )
                    await db.tambah_jakartans(int(target), client.id_bot, nama)
                    return await msg.reply_text(
                        text=f"<a href='tg://openmessage?user_id={str(target)}'>User</a> <i>berhasil menjadi Jakartans</i>\n└Diangkat oleh : <a href='tg://openmessage?user_id={str(config.id_admin)}'>Admin</a>", quote=True,
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
            return await msg.reply(f'<i>coin kamu hanya {coin} ONS, biaya untuk menjadi jakartans sebesar 5000 ONS.</i>', True)
    else:
        return await msg.reply_text(
            text="<b>Cara penggunaan tambah jakartans</b>\n\n<code>/addjakartans id_user</code>\n\nContoh :\n<code>/addjakartans 121212021</code>", quote=True,
            parse_mode=enums.ParseMode.HTML
        )

async def tambah_body_goals_handler(client: Client, msg: types.Message):
    helper = Helper(client, msg)
    if re.search(r"^[\/]addbodygoals(\s|\n)*$", msg.text or msg.caption):
        return await msg.reply_text(
            text="<b>Cara penggunaan tambah body goals</b>\n\n<code>/addbodygoals id_user</code>\n\nContoh :\n<code>/bodygoals 121212021</code>", quote=True,
            parse_mode=enums.ParseMode.HTML
        )
    y = re.search(r"^[\/]addbodygoals(\s|\n)*(\d+)$", msg.text or msg.caption)
    if y:
        target = y.group(2)
        db = Database(int(target))
        db_user = db.get_data_pelanggan()
        coin = db_user.coin
        if target in db.get_data_bot(client.id_bot).ban:
            return await msg.reply_text(
                text=f"<i><a href='tg://user?id={str(target)}'>User</a> sedang dalam kondisi banned</i>\n└Tidak dapat menjadikan body goals", quote=True,
                parse_mode=enums.ParseMode.HTML
            )
        if coin >= config.biaya_status:
            coin = db_user.coin - config.biaya_status
            await db.update_status(coin)   
            if await db.cek_user_didatabase():
                status = [
                    'admin', 'owner', 'talent', 'daddy sugar', 'prolpayer',
                    'teman curhat', 'girlfriend rent', 'boyfriend rent'
                ]
                member = db.get_data_pelanggan()
                if member.status in status:
                    return await msg.reply_text(
                        text=f"❌<i>Terjadi kesalahan, <a href='tg://user?id={str(target)}'>user</a> adalah seorang {member.status.upper()} tidak dapat ditambahkan menjadi body goals</i>", quote=True,
                        parse_mode=enums.ParseMode.HTML
                    )
                try:
                    a = await client.get_chat(target)
                    nama = await helper.escapeHTML(a.first_name if not a.last_name else a.first_name + ' ' + a.last_name)
                    await client.send_message(
                        int(target),
                        text=f"<i>Status kamu telah menjadi bodygoals</i>\n└Diangkat oleh : <a href='tg://openmessage?user_id={str(config.id_admin)}'>Admin</a>",
                        parse_mode=enums.ParseMode.HTML
                        )
                    await db.tambah_body_goals(int(target), client.id_bot, nama)
                    return await msg.reply_text(
                    text=f"<a href='tg://openmessage?user_id={str(target)}'>User</a> <i>berhasil menjadi body goals</i>\n└Diangkat oleh : <a href='tg://openmessage?user_id={str(config.id_admin)}'>Admin</a>", quote=True,
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
            return await msg.reply(f'<i>coin kamu hanya {coin} ONS, biaya untuk menjadi body goals sebesar 5000 ONS.</i>', True)
    else:
        return await msg.reply_text(
            text="<b>Cara penggunaan tambah body goals</b>\n\n<code>/addbodygoals id_user</code>\n\nContoh :\n<code>/addbodygoals 121212021</code>", quote=True,
            parse_mode=enums.ParseMode.HTML
            )

async def tambah_abg_handler(client: Client, msg: types.Message):
    helper = Helper(client, msg)
    if re.search(r"^[\/]addabg(\s|\n)*$", msg.text or msg.caption):
        return await msg.reply_text(
            text="<b>Cara penggunaan tambah abg</b>\n\n<code>/addabg id_user</code>\n\nContoh :\n<code>/addabg 121212021</code>", quote=True,
            parse_mode=enums.ParseMode.HTML
        )
    y = re.search(r"^[\/]addabg(\s|\n)*(\d+)$", msg.text or msg.caption)
    if y:
        target = y.group(2)
        db = Database(int(target))
        db_user = db.get_data_pelanggan()
        coin = db_user.coin
        if target in db.get_data_bot(client.id_bot).ban:
            return await msg.reply_text(
                text=f"<i><a href='tg://user?id={str(target)}'>User</a> sedang dalam kondisi banned</i>\n└Tidak dapat menjadikan abg", quote=True,
                parse_mode=enums.ParseMode.HTML
            )
        if coin >= config.biaya_status:
            coin = db_user.coin - config.biaya_status
            await db.update_status(coin)
            if await db.cek_user_didatabase():
                status = [
                    'admin', 'owner', 'talent', 'daddy sugar', 'prolpayer',
                    'teman curhat', 'girlfriend rent', 'boyfriend rent'
                ]
                member = db.get_data_pelanggan()
                if member.status in status:
                    return await msg.reply_text(
                        text=f"❌<i>Terjadi kesalahan, <a href='tg://user?id={str(target)}'>user</a> adalah seorang {member.status.upper()} tidak dapat ditambahkan menjadi abg</i>", quote=True,
                        parse_mode=enums.ParseMode.HTML
                    )
                try:
                    a = await client.get_chat(target)
                    nama = await helper.escapeHTML(a.first_name if not a.last_name else a.first_name + ' ' + a.last_name)
                    await client.send_message(
                        int(target),
                     text=f"<i>Status kamu telah menjadi abg</i>\n└Diangkat oleh : <a href='tg://openmessage?user_id={str(config.id_admin)}'>Admin</a>",
                        parse_mode=enums.ParseMode.HTML
                    )
                    coin - 5000
                    await db.tambah_abg(int(target), client.id_bot, nama)
                    return await msg.reply_text(
                        text=f"<a href='tg://openmessage?user_id={str(target)}'>User</a> <i>berhasil menjadi abg</i>\n└Diangkat oleh : <a href='tg://openmessage?user_id={str(config.id_admin)}'>Admin</a>", quote=True,
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
            return await msg.reply(f'<i>coin kamu hanya {coin} ONS, biaya untuk menjadi ABG sebesar 5000 ONS.</i>', True)

    else:
        return await msg.reply_text(
            text="<b>Cara penggunaan tambah abg</b>\n\n<code>/addabg id_user</code>\n\nContoh :\n<code>/addabg 121212021</code>", quote=True,
            parse_mode=enums.ParseMode.HTML
        )

async def tambah_babygirl_handler(client: Client, msg: types.Message):
    helper = Helper(client, msg)
    if re.search(r"^[\/]addbabygirl(\s|\n)*$", msg.text or msg.caption):
        return await msg.reply_text(
            text="<b>Cara penggunaan tambah babygirl</b>\n\n<code>/addbabygirl id_user</code>\n\nContoh :\n<code>/addbabygirl 121212021</code>", quote=True,
            parse_mode=enums.ParseMode.HTML
        )
    y = re.search(r"^[\/]addbabygirl(\s|\n)*(\d+)$", msg.text or msg.caption)
    if y:
        target = y.group(2)
        db = Database(int(target))
        db_user = db.get_data_pelanggan()
        coin = db_user.coin
        if target in db.get_data_bot(client.id_bot).ban:
            return await msg.reply_text(
                text=f"<i><a href='tg://user?id={str(target)}'>User</a> sedang dalam kondisi banned</i>\n└Tidak dapat menjadikan baby girl", quote=True,
                parse_mode=enums.ParseMode.HTML
            )
        if coin >= config.biaya_status:
            coin = db_user.coin - config.biaya_status
            await db.update_status(coin)
            if await db.cek_user_didatabase():
                status = [
                    'admin', 'owner', 'talent', 'daddy sugar', 'prolpayer',
                    'teman curhat', 'girlfriend rent', 'boyfriend rent'
                ]
                member = db.get_data_pelanggan()
                if member.status in status:
                    return await msg.reply_text(
                        text=f"❌<i>Terjadi kesalahan, <a href='tg://user?id={str(target)}'>user</a> adalah seorang {member.status.upper()} tidak dapat ditambahkan menjadi baby girl</i>", quote=True,
                        parse_mode=enums.ParseMode.HTML
                    )
                try:
                    a = await client.get_chat(target)
                    nama = await helper.escapeHTML(a.first_name if not a.last_name else a.first_name + ' ' + a.last_name)
                    await client.send_message(
                        int(target),
                        text=f"<i>Status kamu telah menjadi baby girl</i>\n└Diangkat oleh : <a href='tg://openmessage?user_id={str(config.id_admin)}'>Admin</a>",
                        parse_mode=enums.ParseMode.HTML
                    )
                    await db.tambah_baby_girl(int(target), client.id_bot, nama)
                    return await msg.reply_text(
                        text=f"<a href='tg://openmessage?user_id={str(target)}'>User</a> <i>berhasil menjadi baby girl</i>\n└Diangkat oleh : <a href='tg://openmessage?user_id={str(config.id_admin)}'>Admin</a>", quote=True,
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
            return await msg.reply(f'<i>coin kamu hanya {coin} ONS, biaya untuk menjadi baby girl sebesar 5000 ONS.</i>', True)
    else:
        return await msg.reply_text(
            text="<b>Cara penggunaan tambah baby girl</b>\n\n<code>/addbabygirl id_user</code>\n\nContoh :\n<code>/addbabygirl 121212021</code>", quote=True,
            parse_mode=enums.ParseMode.HTML
        )

async def tambah_pick_me_handler(client: Client, msg: types.Message):
    helper = Helper(client, msg)
    if re.search(r"^[\/]addpickme(\s|\n)*$", msg.text or msg.caption):
        return await msg.reply_text(
            text="<b>Cara penggunaan tambah pick me</b>\n\n<code>/addpickme id_user</code>\n\nContoh :\n<code>/addpickme 121212021</code>", quote=True,
            parse_mode=enums.ParseMode.HTML
        )
    y = re.search(r"^[\/]addpickme(\s|\n)*(\d+)$", msg.text or msg.caption)
    if y:
        target = y.group(2)
        db = Database(int(target))
        db_user = db.get_data_pelanggan()
        coin = db_user.coin
        if target in db.get_data_bot(client.id_bot).ban:
            return await msg.reply_text(
                text=f"<i><a href='tg://user?id={str(target)}'>User</a> sedang dalam kondisi banned</i>\n└Tidak dapat menjadikan pick me", quote=True,
                parse_mode=enums.ParseMode.HTML
            )
        if coin >= config.biaya_status:
            coin = db_user.coin - config.biaya_status
            await db.update_status(coin)
            if await db.cek_user_didatabase():
                status = [
                    'admin', 'owner', 'talent', 'daddy sugar', 'prolpayer',
                    'teman curhat', 'girlfriend rent', 'boyfriend rent'
                ]
                member = db.get_data_pelanggan()
                if member.status in status:
                    return await msg.reply_text(
                        text=f"❌<i>Terjadi kesalahan, <a href='tg://user?id={str(target)}'>user</a> adalah seorang {member.status.upper()} tidak dapat ditambahkan menjadi pick me</i>", quote=True,
                        parse_mode=enums.ParseMode.HTML
                    )
                try:
                    a = await client.get_chat(target)
                    nama = await helper.escapeHTML(a.first_name if not a.last_name else a.first_name + ' ' + a.last_name)
                    await client.send_message(
                        int(target),
                        text=f"<i>Status kamu telah menjadi pick me</i>\n└Diangkat oleh : <a href='tg://openmessage?user_id={str(config.id_admin)}'>Admin</a>",
                        parse_mode=enums.ParseMode.HTML
                    )
                    await db.tambah_pick_me(int(target), client.id_bot, nama)
                    return await msg.reply_text(
                        text=f"<a href='tg://openmessage?user_id={str(target)}'>User</a> <i>berhasil menjadi pick me</i>\n└Diangkat oleh : <a href='tg://openmessage?user_id={str(config.id_admin)}'>Admin</a>", quote=True,
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
            return await msg.reply(f'<i>coin kamu hanya {coin} ONS, biaya untuk menjadi pick me sebesar 5000 ONS.</i>', True)    
    else:
        return await msg.reply_text(
            text="<b>Cara penggunaan tambah pick me</b>\n\n<code>/addpickme id_user</code>\n\nContoh :\n<code>/addpickme 121212021</code>", quote=True,
            parse_mode=enums.ParseMode.HTML
        )

async def tambah_melayu_handler(client: Client, msg: types.Message):
    helper = Helper(client, msg)
    if re.search(r"^[\/]addmelayu(\s|\n)*$", msg.text or msg.caption):
        return await msg.reply_text(
            text="<b>Cara penggunaan tambah melayu</b>\n\n<code>/addmelayu id_user</code>\n\nContoh :\n<code>/addmelayu 121212021</code>", quote=True,
            parse_mode=enums.ParseMode.HTML
        )
    y = re.search(r"^[\/]addmelayu(\s|\n)*(\d+)$", msg.text or msg.caption)
    if y:
        target = y.group(2)
        db = Database(int(target))
        db_user = db.get_data_pelanggan()
        coin = db_user.coin
        if target in db.get_data_bot(client.id_bot).ban:
            return await msg.reply_text(
                text=f"<i><a href='tg://user?id={str(target)}'>User</a> sedang dalam kondisi banned</i>\n└Tidak dapat menjadikan melayu", quote=True,
                parse_mode=enums.ParseMode.HTML
            )
        if coin >= config.biaya_status:
            coin = db_user.coin - config.biaya_status
            await db.update_status(coin)
            if await db.cek_user_didatabase():
                status = [
                    'admin', 'owner', 'talent', 'daddy sugar', 'prolpayer',
                    'teman curhat', 'girlfriend rent', 'boyfriend rent'
                ]
                member = db.get_data_pelanggan()
                if member.status in status:
                    return await msg.reply_text(
                        text=f"❌<i>Terjadi kesalahan, <a href='tg://user?id={str(target)}'>user</a> adalah seorang {member.status.upper()} tidak dapat ditambahkan menjadi melayu</i>", quote=True,
                        parse_mode=enums.ParseMode.HTML
                    )
                try:
                    a = await client.get_chat(target)
                    nama = await helper.escapeHTML(a.first_name if not a.last_name else a.first_name + ' ' + a.last_name)
                    await client.send_message(
                        int(target),
                        text=f"<i>Status kamu telah menjadi melayu</i>\n└Diangkat oleh : <a href='tg://openmessage?user_id={str(config.id_admin)}'>Admin</a>",
                        parse_mode=enums.ParseMode.HTML
                    )
                    await db.tambah_melayu(int(target), client.id_bot, nama)
                    return await msg.reply_text(
                        text=f"<a href='tg://openmessage?user_id={str(target)}'>User</a> <i>berhasil menjadi melayu</i>\n└Diangkat oleh : <a href='tg://openmessage?user_id={str(config.id_admin)}'>Admin</a>", quote=True,
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
            return await msg.reply(f'<i>coin kamu hanya {coin} ONS, biaya untuk menjadi melayu sebesar 5000 ONS.</i>', True)
    else:
        return await msg.reply_text(
            text="<b>Cara penggunaan tambah melayu</b>\n\n<code>/addmelayu id_user</code>\n\nContoh :\n<code>/addmelayu 121212021</code>", quote=True,
            parse_mode=enums.ParseMode.HTML
        )

async def tambah_wong_jowo_handler(client: Client, msg: types.Message):
    helper = Helper(client, msg)
    if re.search(r"^[\/]addwongjowo(\s|\n)*$", msg.text or msg.caption):
        return await msg.reply_text(
            text="<b>Cara penggunaan tambah wong jowo</b>\n\n<code>/addwongjowo id_user</code>\n\nContoh :\n<code>/addwong jowo 121212021</code>", quote=True,
            parse_mode=enums.ParseMode.HTML
        )
    y = re.search(r"^[\/]addwongjowo(\s|\n)*(\d+)$", msg.text or msg.caption)
    if y:
        target = y.group(2)
        db = Database(int(target))
        db_user = db.get_data_pelanggan()
        coin = db_user.coin
        if target in db.get_data_bot(client.id_bot).ban:
            return await msg.reply_text(
                text=f"<i><a href='tg://user?id={str(target)}'>User</a> sedang dalam kondisi banned</i>\n└Tidak dapat menjadikan wong jowo", quote=True,
                parse_mode=enums.ParseMode.HTML
            )
        if coin >= config.biaya_status:
            coin = db_user.coin - config.biaya_status
            await db.update_status(coin)
            if await db.cek_user_didatabase():
                status = [
                    'owner', 'talent', 'daddy sugar', 'prolpayer',
                    'teman curhat', 'girlfriend rent', 'boyfriend rent'
                ]
                member = db.get_data_pelanggan()
                if member.status in status:
                    return await msg.reply_text(
                        text=f"❌<i>Terjadi kesalahan, <a href='tg://user?id={str(target)}'>user</a> adalah seorang {member.status.upper()} tidak dapat ditambahkan menjadi wong jowo</i>", quote=True,
                        parse_mode=enums.ParseMode.HTML
                    )
                try:
                    a = await client.get_chat(target)
                    nama = await helper.escapeHTML(a.first_name if not a.last_name else a.first_name + ' ' + a.last_name)
                    await client.send_message(
                        int(target),
                        text=f"<i>Status kamu telah menjadi wong jowo</i>\n└Diangkat oleh : <a href='tg://openmessage?user_id={str(config.id_admin)}'>Admin</a>",
                        parse_mode=enums.ParseMode.HTML
                    )
                    await db.tambah_wong_jowo(int(target), client.id_bot, nama)
                    return await msg.reply_text(
                        text=f"<a href='tg://openmessage?user_id={str(target)}'>User</a> <i>berhasil menjadi wong jowo</i>\n└Diangkat oleh : <a href='tg://openmessage?user_id={str(config.id_admin)}'>Admin</a>", quote=True,
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
            return await msg.reply(f'<i>coin kamu hanya {coin} ONS, biaya untuk menjadi wong jowo sebesar 5000 ONS.</i>', True)
    else:
        return await msg.reply_text(
            text="<b>Cara penggunaan tambah wong jowo</b>\n\n<code>/addwong jowo id_user</code>\n\nContoh :\n<code>/addwongjowo 121212021</code>", quote=True,
            parse_mode=enums.ParseMode.HTML
        )

async def tambah_balinese_handler(client: Client, msg: types.Message):
    helper = Helper(client, msg)
    if re.search(r"^[\/]addbalinese(\s|\n)*$", msg.text or msg.caption):
        return await msg.reply_text(
            text="<b>Cara penggunaan tambah balinese</b>\n\n<code>/addbalinese id_user</code>\n\nContoh :\n<code>/addbalinese 121212021</code>", quote=True,
            parse_mode=enums.ParseMode.HTML
        )
    y = re.search(r"^[\/]addbalinese(\s|\n)*(\d+)$", msg.text or msg.caption)
    if y:
        target = y.group(2)
        db = Database(int(target))
        db_user = db.get_data_pelanggan()
        coin = db_user.coin
        if target in db.get_data_bot(client.id_bot).ban:
            return await msg.reply_text(
                text=f"<i><a href='tg://user?id={str(target)}'>User</a> sedang dalam kondisi banned</i>\n└Tidak dapat menjadikan balinese", quote=True,
                parse_mode=enums.ParseMode.HTML
            )
        if coin >= config.biaya_status:
            coin = db_user.coin - config.biaya_status
            await db.update_status(coin)
            if await db.cek_user_didatabase():
                status = [
                    'owner', 'talent', 'daddy sugar', 'prolpayer',
                    'teman curhat', 'girlfriend rent', 'boyfriend rent'
                ]
                member = db.get_data_pelanggan()
                if member.status in status:
                    return await msg.reply_text(
                        text=f"❌<i>Terjadi kesalahan, <a href='tg://user?id={str(target)}'>user</a> adalah seorang {member.status.upper()} tidak dapat ditambahkan menjadi balinese</i>", quote=True,
                        parse_mode=enums.ParseMode.HTML
                    )
                try:
                    a = await client.get_chat(target)
                    nama = await helper.escapeHTML(a.first_name if not a.last_name else a.first_name + ' ' + a.last_name)
                    await client.send_message(
                        int(target),
                        text=f"<i>Status kamu telah menjadi balinese</i>\n└Diangkat oleh : <a href='tg://openmessage?user_id={str(config.id_admin)}'>Admin</a>",
                        parse_mode=enums.ParseMode.HTML
                    )
                    await db.tambah_balinese(int(target), client.id_bot, nama)
                    return await msg.reply_text(
                        text=f"<a href='tg://openmessage?user_id={str(target)}'>User</a> <i>berhasil menjadi balinese</i>\n└Diangkat oleh : <a href='tg://openmessage?user_id={str(config.id_admin)}'>Admin</a>", quote=True,
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
            return await msg.reply(f'<i>coin kamu hanya {coin} ONS, biaya untuk menjadi balinese sebesar 5000 ONS.</i>', True)
    else:
        return await msg.reply_text(
            text="<b>Cara penggunaan tambah balinese</b>\n\n<code>/addbalinese id_user</code>\n\nContoh :\n<code>/addbalinese 121212021</code>", quote=True,
            parse_mode=enums.ParseMode.HTML
        )

async def tambah_sad_girl_handler(client: Client, msg: types.Message):
    helper = Helper(client, msg)
    if re.search(r"^[\/]addsadgirl(\s|\n)*$", msg.text or msg.caption):
        return await msg.reply_text(
            text="<b>Cara penggunaan tambah sad girl</b>\n\n<code>/addsadgirl id_user</code>\n\nContoh :\n<code>/addsadgirl 121212021</code>", quote=True,
            parse_mode=enums.ParseMode.HTML
        )
    y = re.search(r"^[\/]addsadgirl(\s|\n)*(\d+)$", msg.text or msg.caption)
    if y:
        target = y.group(2)
        db = Database(int(target))
        db_user = db.get_data_pelanggan()
        coin = db_user.coin
        if target in db.get_data_bot(client.id_bot).ban:
            return await msg.reply_text(
                text=f"<i><a href='tg://user?id={str(target)}'>User</a> sedang dalam kondisi banned</i>\n└Tidak dapat menjadikan sad girl", quote=True,
                parse_mode=enums.ParseMode.HTML
            )
        if coin >= config.biaya_status:
            coin = db_user.coin - config.biaya_status
            await db.update_status(coin)
            if await db.cek_user_didatabase():
                status = [
                    'admin', 'owner', 'talent', 'daddy sugar', 'prolpayer',
                    'teman curhat', 'girlfriend rent', 'boyfriend rent'
                ]
                member = db.get_data_pelanggan()
                if member.status in status:
                    return await msg.reply_text(
                        text=f"❌<i>Terjadi kesalahan, <a href='tg://user?id={str(target)}'>user</a> adalah seorang {member.status.upper()} tidak dapat ditambahkan menjadi sad girl</i>", quote=True,
                        parse_mode=enums.ParseMode.HTML
                    )
                try:
                    a = await client.get_chat(target)
                    nama = await helper.escapeHTML(a.first_name if not a.last_name else a.first_name + ' ' + a.last_name)
                    await client.send_message(
                        int(target),
                        text=f"<i>Status kamu telah menjadi sad girl</i>\n└Diangkat oleh : <a href='tg://openmessage?user_id={str(config.id_admin)}'>Admin</a>",
                        parse_mode=enums.ParseMode.HTML
                    )
                    await db.tambah_sad_girl(int(target), client.id_bot, nama)
                    return await msg.reply_text(
                        text=f"<a href='tg://openmessage?user_id={str(target)}'>User</a> <i>berhasil menjadi sad girl</i>\n└Diangkat oleh : <a href='tg://openmessage?user_id={str(config.id_admin)}'>Admin</a>", quote=True,
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
            return await msg.reply(f'<i>coin kamu hanya {coin} ONS, biaya untuk menjadi sad girl sebesar 5000 ONS.</i>', True)
    else:
        return await msg.reply_text(
            text="<b>Cara penggunaan tambah sad girl</b>\n\n<code>/addsadgirl id_user</code>\n\nContoh :\n<code>/addsadgirl 121212021</code>", quote=True,
            parse_mode=enums.ParseMode.HTML
        )

async def tambah_borneo_handler(client: Client, msg: types.Message):
    helper = Helper(client, msg)
    if re.search(r"^[\/]addborneo(\s|\n)*$", msg.text or msg.caption):
        return await msg.reply_text(
            text="<b>Cara penggunaan tambah borneoensis</b>\n\n<code>/addborneo id_user</code>\n\nContoh :\n<code>/addborneo 121212021</code>", quote=True,
            parse_mode=enums.ParseMode.HTML
        )
    y = re.search(r"^[\/]addborneo(\s|\n)*(\d+)$", msg.text or msg.caption)
    if y:
        target = y.group(2)
        db = Database(int(target))
        db_user = db.get_data_pelanggan()
        coin = db_user.coin

        if target in db.get_data_bot(client.id_bot).ban:
            return await msg.reply_text(
                text=f"<i><a href='tg://user?id={str(target)}'>User</a> sedang dalam kondisi banned</i>\n└Tidak dapat menjadikan borneoensis", quote=True,
                parse_mode=enums.ParseMode.HTML
            )
        if coin >= config.biaya_status:
            coin = db_user.coin - config.biaya_status
            await db.update_status(coin)
            if await db.cek_user_didatabase():
                    status = [
                        'admin', 'owner', 'talent', 'daddy sugar', 'prolpayer',
                        'teman curhat', 'girlfriend rent', 'boyfriend rent'
                    ]
                    member = db.get_data_pelanggan()

            if member.status in status:
                return await msg.reply_text(
                    text=f"❌<i>Terjadi kesalahan, <a href='tg://user?id={str(target)}'>user</a> adalah seorang {member.status.upper()} tidak dapat ditambahkan menjadi borneoensis</i>", quote=True,
                    parse_mode=enums.ParseMode.HTML
                )
                try:
                    a = await client.get_chat(target)
                    nama = await helper.escapeHTML(a.first_name if not a.last_name else a.first_name + ' ' + a.last_name)
                    await client.send_message(
                        int(target),
                        text=f"<i>Status kamu telah menjadi Borneoensis</i>\n└Diangkat oleh : <a href='tg://openmessage?user_id={str(config.id_admin)}'>Admin</a>",
                        parse_mode=enums.ParseMode.HTML
                        )
                    await db.tambah_borneo(int(target), client.id_bot, nama)
                    return await msg.reply_text(
                        text=f"<a href='tg://openmessage?user_id={str(target)}'>User</a> <i>berhasil menjadi Borneoensis</i>\n└Diangkat oleh : <a href='tg://openmessage?user_id={str(config.id_admin)}'>Admin</a>", quote=True,
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
            return await msg.reply(f'<i>coin kamu hanya {coin} ONS, biaya untuk menjadi borneo sebesar 5000 ONS.</i>', True)
    else:
        return await msg.reply_text(
            text="<b>Cara penggunaan tambah sad girl</b>\n\n<code>/addsadgirl id_user</code>\n\nContoh :\n<code>/addsadgirl 121212021</code>", quote=True,
            parse_mode=enums.ParseMode.HTML
        )
