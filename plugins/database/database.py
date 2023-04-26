from typing import List, Dict
import pymongo
import config
import json

myclient = pymongo.MongoClient(config.db_url)
mydb = myclient[config.db_name]

mycol = mydb['user']


class Database():
    def __init__(self, user_id: int):
        self.user_id = user_id

    async def tambah_databot(self):
        data = {
            "_id": self.user_id,
            "menfess": 0,
            "bot_status": True,
            "talent": {},
            "daddy_sugar": {},
            "moansboy": {},
            "moansgirl": {},
            "gfrent": {},
            "bfrent": {},
            "member": {},
            "ban": {},
            "admin": [],
            "kirimchannel": {
                "photo": True,
                "video": False,
                "voice": False
            }
        }
        await self.tambah_pelanggan(data)

    async def cek_user_didatabase(self):
        found = mycol.find_one({'_id': self.user_id})
        if found:
            return True
        else:
            return False

    async def tambah_pelanggan(self, data):
        mycol.insert_one(data)
    
    async def hapus_pelanggan(self, user_id: int):
        mycol.delete_one({'_id': user_id})
        return

    async def update_menfess(self, coin: int, menfess: int, all_menfess: int):
        user = self.get_data_pelanggan()
        last_coin = user.coin
        last_menfess = user.menfess
        last_all_menfess = user.all_menfess
        mycol.update_one(
            {"coin": f"{last_coin}_{str(user.id)}", "menfess": last_menfess, "all_menfess": last_all_menfess},
            {"$set": {
                "coin": f"{coin}_{str(user.id)}",
                "menfess": (menfess + 1),
                "all_menfess": (all_menfess + 1)}
            }
        )
    async def update_status(self, coin: int):
        user = self.get_data_pelanggan()
        last_coin = user.coin
        mycol.update_one(
            {"coin": f"{last_coin}_{str(user.id)}"},
            {"$set": {
                "coin": f"{coin}_{str(user.id)}"}
            }
        )
    async def update_coinmember(self, coin: int):
        user = self.get_data_pelanggan()
        last_coin = user.coin
        mycol.update_one(
            {"coin": f"{last_coin}_{str(user.id)}"},
            {"$set": {
                "coin": f"{coin}_{str(user.id)}"}
            }
        )
    async def reset_menfess(self):
        last = {"menfess" : {"$regex": "^[0-9]"}}
        new = { "$set": { "menfess": 0 } }
        x = mycol.update_many({}, new)
        return x.modified_count
        
    async def transfer_coin(self, ditranfer: int, diterima: int, coin_awal_target_full: int, id_target: int):
        coin_awal_user = self.get_data_pelanggan().coin_full
        a = mycol.update_one(
            {"coin": coin_awal_user},
            {"$set": {
                "coin": f"{ditranfer}_{self.user_id}"
            }}
        )
        b = mycol.update_one(
            {"coin": coin_awal_target_full},
            {"$set": {
                "coin": f"{diterima}_{id_target}"
            }}
        )
    async def update_admin(self, id_admin: int, id_bot: int):
        last_data = {
            "admin": self.get_data_bot(id_bot).admin
        }
        data = self.get_data_bot(id_bot).admin
        data.append(id_admin)

        last_status = self.get_data_pelanggan().status_full
        coin_awal = self.get_data_pelanggan().coin
        mycol.update_one(
            {"status": last_status, "coin": f"{coin_awal}_{str(id_admin)}"},
            {"$set": {
                "status": f"admin_{str(id_admin)}",
                "coin": f"{(coin_awal + 1000)}_{str(id_admin)}"
            }
            })
        mycol.update_one(last_data, {"$set": {"admin": data}})

    async def hapus_admin(self, id_admin: int, id_bot: int):
        last_data = {
            "admin": self.get_data_bot(id_bot).admin
        }
        data = self.get_data_bot(id_bot).admin
        data.remove(id_admin)

        last_status = self.get_data_pelanggan().status_full
        mycol.update_one(
            {"status": last_status},
            {"$set": {
                "status": f"member_{str(id_admin)}"
            }
            })
        mycol.update_one(last_data, {"$set": {"admin": data}})

    
    async def update_member(self, id_member: int, id_bot: int):
        last_status = self.get_data_pelanggan().status_full
        mycol.update_one(
            {"status": last_status},
            {"$set": {
                "status": f"member_{str(id_member)}"
            }
            })

    async def hapus_member(self, id_member: int, id_bot: int):
        last_status = self.get_data_pelanggan().status_full
        mycol.update_one(
            {"status": last_status},
            {"$set": {
                "status": f"non member_{str(id_member)}"
            }
            })
    async def banned_user(self, id_banned: int, id_bot: int, alasan: str):
        last_data = {
            "ban": self.get_data_bot(id_bot).ban
        }
        new_data = self.get_data_bot(id_bot).ban
        new_data[str(id_banned)] = str(alasan)
        last_status = self.get_data_pelanggan().status_full
        mycol.update_one(
            {"status": last_status},
            {"$set": {"status": f"banned_{str(id_banned)}"}
             })
        mycol.update_one(last_data, {"$set": {"ban": new_data}})
    
    async def unban_user(self, id_banned: int, id_bot: int):
        last_data = {
            "ban": self.get_data_bot(id_bot).ban
        }
        new_data = self.get_data_bot(id_bot).ban
        del new_data[str(id_banned)]
        last_status = self.get_data_pelanggan().status_full
        mycol.update_one(
            {"status": last_status},
            {"$set": {"status": f"non member_{str(id_banned)}"}}
        )
        mycol.update_one(last_data, {"$set": {"ban": new_data}})

    async def tambah_jakartans(self, id_talent: int, id_bot: int, nama: str):
        last_status = self.get_data_pelanggan().status_full
        mycol.update_one(
            {"status": last_status},
            {"$set": {
                "status": f"jakartans_{str(id_talent)}"
            }
            })

    async def tambah_baby_girl(self, id_talent: int, id_bot: int, nama: str):
        last_status = self.get_data_pelanggan().status_full
        mycol.update_one(
            {"status": last_status},
            {"$set": {
                "status": f"baby girl_{str(id_talent)}"
            }
            })
   
    async def tambah_sad_girl(self, id_talent: int, id_bot: int, nama: str):
        last_status = self.get_data_pelanggan().status_full
        mycol.update_one(
            {"status": last_status},
            {"$set": {
                "status": f"sad girl_{str(id_talent)}"
            }
            })

    async def tambah_melayu(self, id_talent: int, id_bot: int, nama: str):
        last_status = self.get_data_pelanggan().status_full
        mycol.update_one(
            {"status": last_status},
            {"$set": {
                "status": f"melayu_{str(id_talent)}"
            }
            })

    async def tambah_body_goals(self, id_talent: int, id_bot: int, nama: str):
        last_status = self.get_data_pelanggan().status_full
        mycol.update_one(
            {"status": last_status},
            {"$set": {
                "status": f"body goals_{str(id_talent)}"
            }
            })    
    
    async def tambah_pick_me(self, id_talent: int, id_bot: int, nama: str):
        last_status = self.get_data_pelanggan().status_full
        mycol.update_one(
            {"status": last_status},
            {"$set": {
                "status": f"pick me_{str(id_talent)}"
            }
            })

    async def tambah_wong_jowo(self, id_talent: int, id_bot: int, nama: str):
        last_status = self.get_data_pelanggan().status_full
        mycol.update_one(
            {"status": last_status},
            {"$set": {
                "status": f"wong jowo_{str(id_talent)}"
            }
            })

    async def tambah_balinese(self, id_talent: int, id_bot: int, nama: str):
        last_status = self.get_data_pelanggan().status_full
        mycol.update_one(
            {"status": last_status},
            {"$set": {
                "status": f"balinese_{str(id_talent)}"
            }
            })

    async def tambah_abg(self, id_talent: int, id_bot: int, nama: str):
        last_status = self.get_data_pelanggan().status_full
        mycol.update_one(
            {"status": last_status},
            {"$set": {
                "status": f"abg_{str(id_talent)}"
            }
            })

    async def tambah_borneo(self, id_talent: int, id_bot: int, nama: str):
        last_status = self.get_data_pelanggan().status_full
        mycol.update_one(
            {"status": last_status},
            {"$set": {
                "status": f"borneoensis_{str(id_talent)}"
            }
            })

    async def tambah_talent(self, id_talent: int, id_bot: int, nama: str):
        last_data = {
            "talent": self.get_data_bot(id_bot).talent
        }
        new_data = self.get_data_bot(id_bot).talent
        new_data[str(id_talent)] = {
            "nama": nama,
            "username": f"<a href='tg://openmessage?user_id={str(id_talent)}'>{nama}</a>",
            "rate": 0
        }
        last_status = self.get_data_pelanggan().status_full
        mycol.update_one(
            {"status": last_status},
            {"$set": {"status": f"talent_{str(id_talent)}"}
             })
        mycol.update_one(last_data, {"$set": {"talent": new_data}})

    async def hapus_talent(self, id_talent: int, id_bot: int):
        last_data = {
            "talent": self.get_data_bot(id_bot).talent
        }
        new_data = self.get_data_bot(id_bot).talent
        del new_data[str(id_talent)]
        last_status = self.get_data_pelanggan().status_full
        mycol.update_one(
            {"status": last_status},
            {"$set": {"status": f"member_{str(id_talent)}"}}
        )
        mycol.update_one(last_data, {"$set": {"talent": new_data}})

    async def rate_talent(self, id_talent: str, id_bot: int, coin: int):
        last_data = {
            "talent": self.get_data_bot(id_bot).talent
        }
        new_data = self.get_data_bot(id_bot).talent
        new_data[id_talent].update({"rate": new_data[id_talent]['rate'] + 1})

        last_coin = self.get_data_pelanggan().coin
        mycol.update_one(
            {"coin": f"{last_coin}_{self.user_id}"},
            {"$set": {"coin": f"{coin}_{self.user_id}"}}
        )
        mycol.update_one(last_data, {"$set": {"talent": new_data}})

    async def tambah_sugar_daddy(self, id_talent: int, id_bot: int, nama: str):
        last_data = {
            "daddy_sugar": self.get_data_bot(id_bot).daddy_sugar
        }
        new_data = self.get_data_bot(id_bot).daddy_sugar
        new_data[str(id_talent)] = {
            "nama": nama,
            "username": f"<a href='tg://openmessage?user_id={str(id_talent)}'>{nama}</a>",
            "rate": 0
        }
        last_status = self.get_data_pelanggan().status_full
        mycol.update_one(
            {"status": last_status},
            {"$set": {"status": f"daddy sugar_{str(id_talent)}"}
             })
        mycol.update_one(last_data, {"$set": {"daddy_sugar": new_data}})

    async def hapus_sugar_daddy(self, id_talent: int, id_bot: int):
        last_data = {
            "daddy_sugar": self.get_data_bot(id_bot).daddy_sugar
        }
        new_data = self.get_data_bot(id_bot).daddy_sugar
        del new_data[str(id_talent)]
        last_status = self.get_data_pelanggan().status_full
        mycol.update_one(
            {"status": last_status},
            {"$set": {"status": f"member_{str(id_talent)}"}}
        )
        mycol.update_one(last_data, {"$set": {"daddy_sugar": new_data}})

    async def rate_sugar_daddy(self, id_talent: str, id_bot: int, coin: int):
        last_data = {
            "daddy_sugar": self.get_data_bot(id_bot).daddy_sugar
        }
        new_data = self.get_data_bot(id_bot).daddy_sugar
        new_data[id_talent].update({"rate": new_data[id_talent]['rate'] + 1})

        last_coin = self.get_data_pelanggan().coin
        mycol.update_one(
            {"coin": f"{last_coin}_{self.user_id}"},
            {"$set": {"coin": f"{coin}_{self.user_id}"}}
        )
        mycol.update_one(last_data, {"$set": {"daddy_sugar": new_data}})

    async def tambah_pro_player(self, id_talent: int, id_bot: int, nama: str):
        last_data = {
            "proplayer": self.get_data_bot(id_bot).proplayer
        }
        new_data = self.get_data_bot(id_bot).proplayer
        new_data[str(id_talent)] = {
            "nama": nama,
            "username": f"<a href='tg://openmessage?user_id={str(id_talent)}'>{nama}</a>",
            "rate": 0
        }
        last_status = self.get_data_pelanggan().status_full
        mycol.update_one(
            {"status": last_status},
            {"$set": {"status": f"proplayer_{str(id_talent)}"}
             })
        mycol.update_one(last_data, {"$set": {"proplayer": new_data}})

    async def hapus_pro_player(self, id_talent: int, id_bot: int):
        last_data = {
            "proplayer": self.get_data_bot(id_bot).proplayer
        }
        new_data = self.get_data_bot(id_bot).proplayer
        del new_data[str(id_talent)]
        last_status = self.get_data_pelanggan().status_full
        mycol.update_one(
            {"status": last_status},
            {"$set": {"status": f"member_{str(id_talent)}"}}
        )
        mycol.update_one(last_data, {"$set": {"proplayer": new_data}})

    async def rate_pro_player(self, id_talent: str, id_bot: int, coin: int):
        last_data = {
            "proplayer": self.get_data_bot(id_bot).proplayer
        }
        new_data = self.get_data_bot(id_bot).proplayer
        new_data[id_talent].update({"rate": new_data[id_talent]['rate'] + 1})

        last_coin = self.get_data_pelanggan().coin
        mycol.update_one(
            {"coin": f"{last_coin}_{self.user_id}"},
            {"$set": {"coin": f"{coin}_{self.user_id}"}}
        )
        mycol.update_one(last_data, {"$set": {"proplayer": new_data}})
    
    async def tambah_teman_curhat(self, id_talent: int, id_bot: int, nama: str):
        last_data = {
            "temancurhat": self.get_data_bot(id_bot).temancurhat
        }
        new_data = self.get_data_bot(id_bot).temancurhat
        new_data[str(id_talent)] = {
            "nama": nama,
            "username": f"<a href='tg://openmessage?user_id={str(id_talent)}'>{nama}</a>",
            "rate": 0
        }
        last_status = self.get_data_pelanggan().status_full
        mycol.update_one(
            {"status": last_status},
            {"$set": {"status": f"teman curhat_{str(id_talent)}"}
             })
        mycol.update_one(last_data, {"$set": {"temancurhat": new_data}})
    
    async def hapus_teman_curhat(self, id_talent: int, id_bot: int):
        last_data = {
            "temancurhat": self.get_data_bot(id_bot).temancurhat
        }
        new_data = self.get_data_bot(id_bot).temancurhat
        del new_data[str(id_talent)]
        last_status = self.get_data_pelanggan().status_full
        mycol.update_one(
            {"status": last_status},
            {"$set": {"status": f"member_{str(id_talent)}"}}
        )
        mycol.update_one(last_data, {"$set": {"temancurhat": new_data}})

    async def rate_teman_curhat(self, id_talent: str, id_bot: int, coin: int):
        last_data = {
            "temancurhat": self.get_data_bot(id_bot).temancurhat
        }
        new_data = self.get_data_bot(id_bot).temancurhat
        new_data[id_talent].update({"rate": new_data[id_talent]['rate'] + 1})

        last_coin = self.get_data_pelanggan().coin
        mycol.update_one(
            {"coin": f"{last_coin}_{self.user_id}"},
            {"$set": {"coin": f"{coin}_{self.user_id}"}}
        )
        mycol.update_one(last_data, {"$set": {"temancurhat": new_data}})

    async def tambah_gf_rent(self, id_talent: int, id_bot: int, nama: str):
        last_data = {
            "gfrent": self.get_data_bot(id_bot).gfrent
        }
        new_data = self.get_data_bot(id_bot).gfrent
        new_data[str(id_talent)] = {
            "nama": nama,
            "username": f"<a href='tg://openmessage?user_id={str(id_talent)}'>{nama}</a>",
            "rate": 0
        }
        last_status = self.get_data_pelanggan().status_full
        mycol.update_one(
            {"status": last_status},
            {"$set": {"status": f"girlfriend rent_{str(id_talent)}"}
             })
        mycol.update_one(last_data, {"$set": {"gfrent": new_data}})
    
    async def hapus_gf_rent(self, id_talent: int, id_bot: int):
        last_data = {
            "gfrent": self.get_data_bot(id_bot).gfrent
        }
        new_data = self.get_data_bot(id_bot).gfrent
        del new_data[str(id_talent)]
        last_status = self.get_data_pelanggan().status_full
        mycol.update_one(
            {"status": last_status},
            {"$set": {"status": f"member_{str(id_talent)}"}}
        )
        mycol.update_one(last_data, {"$set": {"gfrent": new_data}})
    
    async def rate_gf_rent(self, id_talent: str, id_bot: int, coin: int):
        last_data = {
            "gfrent": self.get_data_bot(id_bot).gfrent
        }
        new_data = self.get_data_bot(id_bot).gfrent
        new_data[id_talent].update({"rate": new_data[id_talent]['rate'] + 1})

        last_coin = self.get_data_pelanggan().coin
        mycol.update_one(
            {"coin": f"{last_coin}_{self.user_id}"},
            {"$set": {"coin": f"{coin}_{self.user_id}"}}
        )
        mycol.update_one(last_data, {"$set": {"gfrent": new_data}})
    
    async def tambah_bf_rent(self, id_talent: int, id_bot: int, nama: str):
        last_data = {
            "bfrent": self.get_data_bot(id_bot).bfrent
        }
        new_data = self.get_data_bot(id_bot).bfrent
        new_data[str(id_talent)] = {
            "nama": nama,
            "username": f"<a href='tg://openmessage?user_id={str(id_talent)}'>{nama}</a>",
            "rate": 0
        }
        last_status = self.get_data_pelanggan().status_full
        mycol.update_one(
            {"status": last_status},
            {"$set": {"status": f"boyfriend rent_{str(id_talent)}"}
             })
        mycol.update_one(last_data, {"$set": {"bfrent": new_data}})

    async def hapus_bf_rent(self, id_talent: int, id_bot: int):
        last_data = {
            "bfrent": self.get_data_bot(id_bot).bfrent
        }
        new_data = self.get_data_bot(id_bot).bfrent
        del new_data[str(id_talent)]
        last_status = self.get_data_pelanggan().status_full
        mycol.update_one(
            {"status": last_status},
            {"$set": {"status": f"member_{str(id_talent)}"}}
        )
        mycol.update_one(last_data, {"$set": {"bfrent": new_data}})

    async def rate_bf_rent(self, id_talent: str, id_bot: int, coin: int):
        last_data = {
            "bfrent": self.get_data_bot(id_bot).bfrent
        }
        new_data = self.get_data_bot(id_bot).bfrent
        new_data[id_talent].update({"rate": new_data[id_talent]['rate'] + 1})

        last_coin = self.get_data_pelanggan().coin
        mycol.update_one(
            {"coin": f"{last_coin}_{self.user_id}"},
            {"$set": {"coin": f"{coin}_{self.user_id}"}}
        )
        mycol.update_one(last_data, {"$set": {"bfrent": new_data}})
    
    async def bot_handler(self, status: str):
        if status == 'on' or status == '<on>':
            bot_status = True
            last_data = {"bot_status": False}
        else:
            bot_status = False
            last_data = {"bot_status": True}

        mycol.update_one(last_data, {"$set": {"bot_status": bot_status}})

    async def photo_handler(self, status: str, id_bot: int):
        data_bot = self.get_data_bot(id_bot).kirimchannel
        last_data = {"kirimchannel": {"photo": data_bot.photo, "video": data_bot.video, "voice": data_bot.voice }}
        if status == '✅':
            photo_status = {
                "$set": {"kirimchannel": {
                    "photo": False,
                    "video": data_bot.video,
                    "voice": data_bot.voice
                    }
                }
            }
        else:
            photo_status = {
                "$set": {"kirimchannel": {
                    "photo": True,
                    "video": data_bot.video,
                    "voice": data_bot.voice
                    }
                }
            }
        mycol.update_one(last_data, photo_status)

    async def video_handler(self, status: str, id_bot: int):
        data_bot = self.get_data_bot(id_bot).kirimchannel
        last_data = {"kirimchannel": {"photo": data_bot.photo, "video": data_bot.video, "voice": data_bot.voice }}
        if status == '✅':
            photo_status = {
                "$set": {"kirimchannel": {
                    "photo": data_bot.photo,
                    "video": False,
                    "voice": data_bot.voice
                    }
                }
            }
        else:
            photo_status = {
                "$set": {"kirimchannel": {
                    "photo": data_bot.photo,
                    "video": True,
                    "voice": data_bot.voice
                    }
                }
            }
        mycol.update_one(last_data, photo_status)

    async def voice_handler(self, status: str, id_bot: int):
        data_bot = self.get_data_bot(id_bot).kirimchannel
        last_data = {"kirimchannel": {"photo": data_bot.photo, "video": data_bot.video, "voice": data_bot.voice }}
        if status == '✅':
            photo_status = {
                "$set": {"kirimchannel": {
                    "photo": data_bot.photo,
                    "video": data_bot.video,
                    "voice": False
                    }
                }
            }
        else:
            photo_status = {
                "$set": {"kirimchannel": {
                    "photo": data_bot.photo,
                    "video": data_bot.video,
                    "voice": True
                    }
                }
            }
        mycol.update_one(last_data, photo_status)

    def get_pelanggan(self):
        user_id = []
        for doc in mycol.find():
            user_id.append(doc['_id'])
        
        return get_pelanggan(user_id)

    def get_data_pelanggan(self):
        found = mycol.find_one({'_id': self.user_id})
        return data_pelanggan(found)

    def get_data_bot(self, id_bot):
        found = mycol.find_one({'_id': id_bot})
        return data_bot(found)

class get_pelanggan():
    def __init__(self, args: list):
        args.remove(args[0])
        self.total_pelanggan = len(args)
        self.id_pelanggan = args
        self.json = { "total_pelanggan": len(args), "id_pelanggan": args }

    def get_data_pelanggan(self, index: int = 0):
        found = mycol.find_one({'_id': self.id_pelanggan[index]})
        if found:
            return data_pelanggan(found)
        else:
            return 'ID tidak ditemukan'
    def __str__(self) -> str:
        return str(json.dumps(self.json, indent=3))

class data_pelanggan():
    def __init__(self, args):
        self.id = args['_id']
        self.nama = str(args['nama'])
        self.mention = f'<a href="tg://user?id={self.id}">{self.nama}</a>'
        self.coin = int(args['coin'].split('_')[0])
        self.coin_full = str(args['coin'])
        self.status = str(args['status'].split('_')[0])
        self.status_full = str(args['status'])
        self.menfess = int(args['menfess'])
        self.all_menfess = int(args['all_menfess'])
        self.json = args

    def __str__(self) -> str:
        return str(json.dumps(self.json, indent=3))


class data_bot():
    def __init__(self, args):
        super().__init__()
        self.id = args['_id']
        self.bot_status = args['bot_status']
        self.talent = dict(args['talent'])
        self.daddy_sugar = dict(args['daddy_sugar'])
        self.proplayer = dict(args['moansgirl'])
        self.temancurhat = dict(args['moansboy'])
        self.gfrent = dict(args['gfrent'])
        self.bfrent = dict(args['bfrent'])
        self.ban = dict(args['ban'])
        self.admin = list(args['admin'])
        self.kirimchannel = kirim_channel(dict(args['kirimchannel']))
        # del args['menfess']
        self.json = args

    def __str__(self) -> str:
        return str(json.dumps(self.json, indent=3))

class kirim_channel():
    def __init__(self, args):
        self.photo = args['photo']
        self.video = args['video']
        self.voice = args['voice']
        self.json = args
    def __str__(self) -> str:
        return str(json.dumps(self.json, indent=3))
