import re

from pyrogram import Client, filters
from pyrogram.types import Message, CallbackQuery

from plugins import Database, Helper
from plugins.command import *
from bot import Bot


@Bot.on_message()
async def on_message(client: Client, msg: Message):
    if msg.chat.type == enums.ChatType.PRIVATE:
        if msg.from_user != None:
            uid = msg.from_user.id
        else:
            return

        helper = Helper(client, msg)
        database = Database(uid)

        # cek apakah user sudah bergabung digrup chat
        if not await helper.cek_langganan_channel(uid):
            return await helper.pesan_langganan() # jika belum akan menampilkan pesan bergabung

        if not await database.cek_user_didatabase():  # cek apakah user sudah ditambahkan didatabase
            await helper.daftar_pelanggan()  # jika belum akan ditambahkan data user ke database
            await helper.send_to_channel_log(type="log_daftar")

        # Pesan jika bot sedang dalam kondisi tidak aktif
        if not database.get_data_bot(client.id_bot).bot_status:
            status = [
                'member', 'banned', 'talent', 'daddy sugar', 'teman curhat',
                'proplayer', 'girlfriend rent', 'boyfriend rent'
            ]
            member = database.get_data_pelanggan()
            if member.status in status:
                return await client.send_message(uid, "<i>Saat ini bot sedang dinonaktifkan</i>", enums.ParseMode.HTML)

        # anu = msg.caption if not msg.text else msg.text
        # print(f"-> {anu}")

        command = msg.text or msg.caption
        if command != None:
            if command == '/start':  # menampilkan perintah start
                return await start_handler(client, msg)
            
            elif command == '/help':
                return await help_handler(client, msg)
            
            elif command == '/topup':
                return await topup_handler(client, msg)

            elif command == '/rubahstatus':
                return await rubahstatus_handler(client, msg)

            elif command == '/status':  # menampilkan perintah status
                return await status_handler(client, msg)

            elif command == '/list_admin':  # menampilkan perintah list admin
                return await list_admin_handler(helper, client.id_bot)

            elif command == '/list_ban':  # menampilkan perintah list banned
                return await list_ban_handler(helper, client.id_bot)

            elif command == '/talent':
                return await talent_handler(client, msg)
            
            elif command == '/daddysugar':
                return await daddy_sugar_handler(client, msg)

            elif command == '/temancurhat':
                return await teman_curhat_handler(client, msg)
            
            elif command == '/proplayer':
                return await pro_player_handler(client, msg)

            elif command == '/gfrent':
                return await gf_rent_handler(client, msg)

            elif command == '/bfrent':
                return await bf_rent_handler(client, msg)

            elif command == '/stats':  # menampilkan perintah statistik
                if uid == config.id_admin:
                    return await statistik_handler(helper, client.id_bot)

            elif command == '/broadcast':
                if uid == config.id_admin:
                    return await broadcast_handler(client, msg)

            elif command == '/settings' or command == '/setting':  # menampilkan perintah settings
                member = database.get_data_pelanggan()
                if member.status == 'admin' or member.status == 'owner':
                    return await setting_handler(client, msg)

            elif re.search(r"^[\/]rate", command):
                return await rate_talent_handler(client, msg)
            
            elif re.search(r"^[\/]tf_coin", command):
                return await transfer_coin_handler(client, msg)

            elif re.search(r"^[\/]bot", command): # menonaktifkan dan mengaktifkan bot
                if uid == config.id_admin:
                    return await bot_handler(client, msg)

            elif re.search(r"^[\/]admin", command):  # menambahkan admin baru
                if uid == config.id_admin:
                    return await tambah_admin_handler(client, msg)

            # menghapus admin yang telah diangkat
            elif re.search(r"^[\/]unadmin", command):
                if uid == config.id_admin:
                    return await hapus_admin_handler(client, msg)

            elif re.search(r"^[\/]member", command):  # menambahkan member baru
                    return await tambah_member_handler(client, msg)

            # menghapus member yang telah diangkat
            elif re.search(r"^[\/]unmember", command):
                if uid == config.id_admin:
                    return await hapus_member_handler(client, msg)

            elif re.search(r"^[\/]addjakartans", command):  # menambahkan status jakartans baru
                return await tambah_jakartans_handler(client, msg)
                    
            elif re.search(r"^[\/]addbabygirl", command):  # menambahkan status baby girl baru
                return await tambah_babygirl_handler(client, msg)

            elif re.search(r"^[\/]addwongjowo", command):  # menambahkan status wong jowo baru
                return await tambah_wong_jowo_handler(client, msg)
            
            elif re.search(r"^[\/]addmelayu", command):  # menambahkan status melayu baru
                return await tambah_melayu_handler(client, msg)

            elif re.search(r"^[\/]addbalinese", command):  # menambahkan status balinese baru
                return await tambah_balinese_handler(client, msg)

            elif re.search(r"^[\/]addabg", command):  # menambahkan status abg baru
                return await tambah_abg_handler(client, msg)

            elif re.search(r"^[\/]addpickme", command):  # menambahkan status pick me baru
                return await tambah_pick_me_handler(client, msg)

            elif re.search(r"^[\/]addbodygoals", command):  # menambahkan status body goals baru
                return await tambah_body_goals_handler(client, msg)

            elif re.search(r"^[\/]addsadgirl", command):  # menambahkan status sad girl baru
                return await tambah_sad_girl_handler(client, msg)
            
            elif re.search(r"^[\/]addborneo", command):  # menambahkan status borneo baru
                return await tambah_borneo_handler(client, msg)

            elif re.search(r"^[\/]addtalent", command):  # menambahkan talent baru
                if uid == config.id_admin:
                    return await tambah_talent_handler(client, msg)
            
            elif re.search(r"^[\/]addsugar", command):  # menambahkan daddy sugar baru
                if uid == config.id_admin:
                    return await tambah_sugar_daddy_handler(client, msg)
            
            elif re.search(r"^[\/]addproplayer", command):  # menambahkan proplayer baru
                if uid == config.id_admin:
                    return await tambah_pro_player_handler(client, msg)
            
            elif re.search(r"^[\/]addtemancurhat", command):  # menambahkan temancurhat baru
                if uid == config.id_admin:
                    return await tambah_teman_curhat_handler(client, msg)

            elif re.search(r"^[\/]addgf", command):  # menambahkan gf rent baru
                if uid == config.id_admin:
                    return await tambah_gf_rent_handler(client, msg)

            elif re.search(r"^[\/]addbf", command):  # menambahkan bf rent baru
                if uid == config.id_admin:
                    return await tambah_bf_rent_handler(client, msg)

            elif re.search(r"^[\/]hapus", command):  # menambahkan mengapus talent
                if uid == config.id_admin:
                    return await hapus_talent_handler(client, msg)

            elif re.search(r"^[\/]ban", command):  # membanned user
                member = database.get_data_pelanggan()
                if member.status == 'admin' or member.status == 'owner':
                    return await ban_handler(client, msg)

            elif re.search(r"^[\/]unban", command):  # membuka kembali banned kepada user
                member = database.get_data_pelanggan()
                if member.status == 'admin' or member.status == 'owner':
                    return await unban_handler(client, msg)

            x = re.search(fr"(?:^|\s)({config.hastag})", command.lower())
            if x:
                print('kaa')
                y = re.search(r"(?:^|\s)(@[-a-zA-Z0-9@:%._\+~#=]{1,256})", command.lower())
                if y:
                    try:
                        tipe = await client.get_chat(y.group(1))
                        if tipe.type == enums.ChatType.BOT:
                            return await msg.reply('Terdeteksi username bot tidak dapat mengirim menfess')
                        elif tipe.type == enums.ChatType.CHANNEL:
                            return await msg.reply('Terdeteksi username channel/grup/orang lain tidak dapat mengirim menfess')
                        elif tipe.type == enums.ChatType.SUPERGROUP:
                            return await msg.reply('Terdeteksi username channel/grup/orang lain tidak dapat mengirim menfess')
                        elif tipe.type == enums.ChatType.GROUP:
                            return await msg.reply('Terdeteksi username channel/grup/orang lain tidak dapat mengirim menfess')
                        elif tipe.type != message.from_user.username:
                            return await msg.reply('Terdeteksi username orang lain tidak dapat mengirim menfess')
                    except:
                        pass
                z = re.search(r"(?:^|\s)(t\.me|telegram\.me)\/([-a-zA-Z0-9@:%._\+~#=]{1,256})", command.lower())
                if z:
                    try:
                        tipe = await client.get_chat(z.group(2))
                        if tipe.type == enums.ChatType.BOT:
                            return await msg.reply('Terdeteksi username bot tidak dapat mengirim menfess')
                        elif tipe.type == enums.ChatType.CHANNEL:
                            return await msg.reply('Terdeteksi username channel/grup tidak dapat mengirim menfess')
                        elif tipe.type == enums.ChatType.SUPERGROUP:
                            return await msg.reply('Terdeteksi username channel/grup tidak dapat mengirim menfess')
                        elif tipe.type == enums.ChatType.GROUP:
                            return await msg.reply('Terdeteksi username channel/grup tidak dapat mengirim menfess')
                    except:
                        return await msg.reply('Terdeteksi link channel/grup/tautan tidak dapat mengirim menfess')
                u = re.search(r"(?:^|\s)https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b\/([-a-zA-Z0-9()!@:%_\+.~#?&\/\/=]*)", command.lower())
                if u:
                    try:
                        tipe = await client.get_chat(u.group(2))
                        if tipe.type == enums.ChatType.BOT:
                            return await msg.reply('Terdeteksi link bot tidak dapat mengirim menfess')
                        elif tipe.type == enums.ChatType.CHANNEL:
                            return await msg.reply('Terdeteksi link channel/grup tidak dapat mengirim menfess')
                        elif tipe.type == enums.ChatType.SUPERGROUP:
                            return await msg.reply('Terdeteksi link channel/grup tidak dapat mengirim menfess')
                        elif tipe.type == enums.ChatType.GROUP:
                            return await msg.reply('Terdeteksi link channel/grup tidak dapat mengirim menfess')
                    except:
                        return await msg.reply('Terdeteksi link channel/grup/tautan tidak dapat mengirim menfess')
                member = database.get_data_pelanggan()
                t = re.search(fr"(?:^|\s)({config.kata_terlarang})", command.lower())
                if t:
                    try:
                        return await msg.reply('<b>Pesan Gagal Terkirim</b> karena <b>pesan</b> anda mengandung <b>kata terlarang</b>', quote=True)
                    except:
                        pass
                
                d = re.search(fr"(?:^|\s)({config.nonmember})", command.lower())
                if d:
                    try:
                        if member.status == 'non member':
                            return await msg.reply('<b>Pesan Gagal Terkirim</b> karena status anda <b>non member</b>, /rubahstatus jika ingin menjadi member', quote=True)
                    except:
                        pass
                key = x.group(1)
                hastag = config.hastag.split('|')
                kata_terlarang = config.kata_terlarang.split('|')
                if member.status == 'banned':
                    return await msg.reply(f'Kamu telah <b>di banned</b>\n\n<u>Alasan:</u> {database.get_data_bot(client.id_bot).ban[str(uid)]}\nsilahkan kontak admin @leoopttt untuk unbanned', True, enums.ParseMode.HTML)
                if key in [hastag[0], hastag [1]]:
                    if key == command.lower() or len(command.split(' ')) < 3:
                        return await msg.reply('🙅🏻‍♀️  post gagal terkirim, <b>mengirim pesan wajib lebih dari 3 kata.</b>', True, enums.ParseMode.HTML)
                    else:
                        return await send_with_pic_handler(client, msg, key, hastag)
                elif key in hastag:
                    if key == command.lower() or len(command.split(' ')) < 3:
                        return await msg.reply('🙅🏻‍♀️  post gagal terkirim, <b>mengirim pesan wajib lebih dari 3 kata.</b>', True, enums.ParseMode.HTML)
                    else:
                        return await send_menfess_handler(client, msg)
                else:
                    await gagal_kirim_handler(client, msg)
            else:
                await gagal_kirim_handler(client, msg)      
        else:
            await gagal_kirim_handler(client, msg)
    
    # perintah yang bisa diakses di group
    elif msg.chat.type == enums.ChatType.SUPERGROUP:
        command = msg.text or msg.caption
        if msg.from_user != None:
            uid = msg.from_user.id
        else:
            if msg.sender_chat.id == config.channel_1:
                x = re.search(fr"(?:^|\s)({config.hastag})", command.lower())
                if x:
                    hastag = config.hastag.split('|')
                    if x.group(1) in [hastag[0], hastag [1]]:
                        try:
                            await client.delete_messages(msg.chat.id, msg.id)
                        except:
                            pass
            else:
                return
        
        if command != None:
            return



@Bot.on_callback_query()
async def on_callback_query(client: Client, query: CallbackQuery):
    try:
        if query.data == 'photo':
            await photo_handler_inline(client, query)
        elif query.data == 'video':
            await video_handler_inline(client, query)
        elif query.data == 'voice':
            await voice_handler_inline(client, query)
        elif query.data == 'status_bot':
            if query.message.chat.id == config.id_admin:
                await status_handler_inline(client, query)
            else:
                await query.answer('Ditolak, kamu tidak ada akses', True)
        elif query.data == 'ya_confirm':
            await broadcast_ya(client, query)
        elif query.data == 'tidak_confirm':
            await close_cbb(client, query)
    except:
        pass
