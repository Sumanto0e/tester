import config

from pyrogram import Client, types, enums
from plugins import Helper, Database
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

async def start_handler(client: Client, msg: types.Message):
    helper = Helper(client, msg)
    first = msg.from_user.first_name
    last = msg.from_user.last_name
    fullname = first if not last else first + ' ' + last
    username = '@leoopttt' if not msg.from_user.username else '@' + msg.from_user.username
    mention = msg.from_user.mention
    markup = InlineKeyboardMarkup([
            [InlineKeyboardButton('Rules', url='https://t.me/onsbase/5378')]
        ])
    await msg.reply_text(
        text = config.start_msg.format(
            id = msg.from_user.id,
            mention = mention,
            username = username,
            first_name = await helper.escapeHTML(first),
            last_name = await helper.escapeHTML(last),
            fullname = await helper.escapeHTML(fullname),
            ),
        reply_markup=markup,
        disable_web_page_preview = True,
        quote = True
    )

async def status_handler(client: Client, msg: types.Message):
    helper = Helper(client, msg)
    db = Database(msg.from_user.id).get_data_pelanggan()
    pesan = f'🆔 <b>ID</b>                  : <code>{db.id}</code>\n\n'
    pesan += f'👮 <b>User</b>              : {db.mention}\n\n'
    pesan += f'👑 <b>Status</b>          : {db.status}\n\n'
    pesan += f'💸 <b>Coin</b>              : {helper.formatrupiah(db.coin)} ONS\n\n'
    pesan += f'📆 <b>Daily Send</b>  : {db.menfess}/{config.batas_kirim}\n\n'
    pesan += f'/help untuk melihat command yang tersedia untuk anda'
    markup = InlineKeyboardMarkup([
            [InlineKeyboardButton('Rules', url='https://t.me/onsbase/5378'), InlineKeyboardButton('Top up Coin', url='https://trakteer.id/nazhak-tv-dfbf2/tip?open=true')]
        ])
    await msg.reply(pesan, True, enums.ParseMode.HTML, reply_markup=markup)

async def topup_handler(client: Client, msg: types.Message):
    pesan = 'Format untuk pembelian Coin ONS ini <b>ID</b> dan <b>USERNAME</b> anda dikolom <b>pesan dukungan</b>.\n\n'
    pesan += 'Cost ⦂ 1000 ONS = Rp.1000\n\n'
    pesan += 'Kami akan mengirimkan coin sesuai dengan jumlah unit yang anda berikan.\n\n'
    pesan += '<b>NOTE</b>: bila <b>ID</b> dan <b>USERNAME</b> tidak dicantumkan dikolom <b>pesan dukungan</b> maka kami anggap sebagai <b>DONASI</b>\n\n'
    pesan += '           ⬇️ Klik link dibawah ⬇️\n'
    pesan += 'https://trakteer.id/nazhak-tv-dfbf2/tip\n\n'
    pesan += 'Atau beli coin secara manual ke @Leoopttt'
    await msg.reply(pesan, True, enums.ParseMode.HTML)

async def rubahstatus_handler(client: Client, msg: types.Message):
    pesan = 'Check pick status yang tersedia di @statusonsbase'
    pesan += '<b>COMMAND STATUS YANG TERSEDIA</b>\n'
    pesan += '/member — penguna dijadikan member'
    pesan += '/addborneo — menambahkan status borneoensis\n'
    pesan += '/addjakartans — menambahkan status jakartans\n'
    pesan += '/addbalinese — menambahkan status balinese\n'
    pesan += '/addpickme — menambahkan status pick me\n'
    pesan += '/addsadgirl — menambahkan status sad girl\n'
    pesan += '/addbabygirl — menambahkan status baby girl\n'
    pesan += '/addabg — menambahkan status abg\n'
    pesan += '/addmelayu — menambahkan status melayu\n'
    pesan += '/addwongjowo — menambahkan status wong jowo\n'
    pesan += '/addbodygoals — menambahkan status bodygoals\n'
    await msg.reply(pesan, True, enums.ParseMode.HTML)

async def statistik_handler(client: Helper, id_bot: int):
    db = Database(client.user_id)
    bot = db.get_data_bot(id_bot)
    db_user = db.get_data_pelanggan()
    pesan = "<b>📊 STATISTIK BOT\n\n"
    pesan += f"▪️Pelanggan: {db.get_pelanggan().total_pelanggan}\n"
    pesan += f"▪️Admin: {len(bot.admin)}\n"
    pesan += f"▪️Talent: {len(bot.talent)}\n"
    pesan += f"▪️Daddy sugar: {len(bot.daddy_sugar)}\n"
    pesan += f"▪️Proplayer: {len(bot.proplayer)}\n"
    pesan += f"▪️Teman Curhat: {len(bot.temancurhat)}\n"
    pesan += f"▪️Girlfriend rent: {len(bot.gfrent)}\n"
    pesan += f"▪️Boyfriend rent: {len(bot.bfrent)}\n"
    pesan += f"▪️Banned: {len(bot.ban)}\n\n"
    pesan += f"🔰Status bot: {'AKTIF' if bot.bot_status else 'TIDAK AKTIF'}</b>"
    await client.message.reply_text(pesan, True, enums.ParseMode.HTML)

async def list_admin_handler(helper: Helper, id_bot: int):
    db = Database(helper.user_id).get_data_bot(id_bot)
    pesan = "<b>Owner bot</b>\n"
    pesan += "• ID: " + str(config.id_admin) + " | <a href='tg://user?id=" + str(config.id_admin) + "'>Owner bot</a>\n\n"
    if len(db.admin) > 0:
        pesan += "<b>Daftar Admin bot</b>\n"
        ind = 1
        for i in db.admin:
            pesan += "• ID: " + str(i) + " | <a href='tg://user?id=" + str(i) + "'>Admin " + str(ind) + "</a>\n"
            ind += 1
    await helper.message.reply_text(pesan, True, enums.ParseMode.HTML)

async def list_ban_handler(helper: Helper, id_bot: int):
    db = Database(helper.user_id).get_data_bot(id_bot)
    if len(db.ban) == 0:
        return await helper.message.reply_text('<i>Tidak ada user dibanned saat ini</i>', True, enums.ParseMode.HTML)
    else:
        pesan = "<b>Daftar banned</b>\n"
        ind = 1
        for i in db.ban:
            pesan += "• ID: " + str(i) + " | <a href='tg://openmessage?user_id=" + str(i) + "'>( " + str(ind) + " )</a>\n"
            ind += 1
    await helper.message.reply_text(pesan, True, enums.ParseMode.HTML)

async def gagal_kirim_handler(client: Client, msg: types.Message):
    anu = Helper(client, msg)
    first_name = msg.from_user.first_name
    last_name = msg.from_user.last_name
    fullname = first_name if not last_name else first_name + ' ' + last_name
    username = '@leoopttt' if not msg.from_user.username else '@' + msg.from_user.username
    mention = msg.from_user.mention
    return await msg.reply(config.gagalkirim_msg.format(
        id = msg.from_user.id,
        mention = mention,
        username = username,
        first_name = await anu.escapeHTML(first_name),
        last_name = await anu.escapeHTML(last_name),
        fullname = await anu.escapeHTML(fullname)
    ), True, enums.ParseMode.HTML, disable_web_page_preview=True)

async def help_handler(client, msg):
    db = Database(msg.from_user.id)
    member = db.get_data_pelanggan()
    pesan = "Supported commands\n"
    pesan += '/status — melihat status\n'
    pesan += '/topup — top up coin\n'
    pesan += '/tf_coin — transfer coin\n'
    pesan += '/rubahstatus — merubah status\n'
    if member.status == 'admin':
        pesan += '\nHanya Admin\n'
        pesan += '/tf_coin — transfer coin\n'
        pesan += '/settings — melihat settingan bot\n'
        pesan += '/list_admin — melihat list admin\n'
        pesan += '/list_ban — melihat list banned\n\n'
        pesan += 'Perintah banned\n'
        pesan += '/ban — ban user\n'
        pesan += '/unban — unban user\n'
    if member.status == 'owner':
        pesan += '\n=====OWNER COMMAND=====\n'
        pesan += '/tf_coin — transfer coin\n'
        pesan += '/settings — melihat settingan bot\n'
        pesan += '/list_admin — melihat list admin\n'
        pesan += '/list_ban — melihat list banned\n'
        pesan += '/stats — melihat statistik bot\n'
        pesan += '/bot — setbot (on|off)\n'
        pesan += '\n=====FITUR TALENT=====\n'
        pesan += '/addtalent — menambahkan talent baru\n'
        pesan += '/addsugar — menambahkan talent daddy sugar\n'
        pesan += '/addproplayer — menambahkan talent proplayer\n'
        pesan += '/addtemancurhat — menambahkan talent teman curhat\n'
        pesan += '/addgf — menambahkan talent girlfriend rent\n'
        pesan += '/addbf — menambahkan talent boyfriend rent\n'
        pesan += '/addborneo — menambahkan status borneoensis\n'
        pesan += '/addjakartans — menambahkan status jakartans\n'
        pesan += '/addbalinese — menambahkan status balinese\n'
        pesan += '/addpickme — menambahkan status pick me\n'
        pesan += '/addsadgirl — menambahkan status sad girl\n'
        pesan += '/addbabygirl — menambahkan status baby girl\n'
        pesan += '/addabg — menambahkan status abg\n'
        pesan += '/addmelayu — menambahkan status melayu\n'
        pesan += '/addwongjowo — menambahkan status wong jowo\n'
        pesan += '/addbodygoals — menambahkan status bodygoals\n'
        pesan += '/hapus — menghapus talent\n'
        pesan += '\n=====BROADCAST OWNER=====\n'
        pesan += '/broadcast — mengirim pesan broadcast kesemua user\n'
        pesan += '/admin — menambahkan admin baru\n'
        pesan += '/unadmin — menghapus admin\n'
        pesan += '/member — penguna dijadikan member\n'
        pesan += '/unmember — penguna dijadikan unmember\n'
        pesan += '/list_ban — melihat list banned\n'
        pesan += '\n=====BANNED COMMAND=====\n'
        pesan += '/ban — ban user\n'
        pesan += '/unban — unban user\n'
    await msg.reply(pesan, True)
