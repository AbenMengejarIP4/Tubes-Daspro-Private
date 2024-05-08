# =================== DONE =======================

# nama / nim    : Alfian Hanif FY / 19623281
# judul         : Register
# deskripsi     : Mendaftarkan akun baru kedalam database dan melakukan verifikasi

# KAMUS

# ALGORITMA

data_user = [{'id' : 1,'username' : 'alfian', 'password' : 'tubeskelar', 'role' : 'admin' , 'oc' : 0}]
data_monster = [{'id' : 1,'type' : 'pikachan', 'atk_power' : '150', 'def_power' : '20' , 'hp' : 600}]
data_inventory_item = [{'user_id' : 1,'type' : 'healing','quantity' : 1}]
data_inventory_monster = [{'user_id' : 1,'monster_id' : 1,'level' : 1}]
data_shop_item = [{'type' : 'healing', 'stock' : 99, 'price' : 5}]
data_shop_monster = [{'monster_id' : 1,'stock' : 25, 'price' : 25}]



def isUsernameValid(username :str,data_user:list) -> int:
    for char in username:
        if 48 <= ord(char) <= 57 or 65 <= ord(char) <= 90 or 97 <= ord(char) <= 122 or ord(char) == 45 or ord(char) == 95:
            pass
        else:
            return 0 # case tidak valid 1
    for user in data_user:
        if user['username'] == username:
            return -1 # case tidak valid 2
    return 1 # case valid

def search(data:list,param:str,target,target_param:str):
    for element in data:
        if element[param] == target:
            return element[target_param]

def showMonsterName(data_monster:list):
    for monster in data_monster:
        print(f'{monster["id"]}. {monster["type"]}')

def generateId(data_user:list) -> int:
    id = len(data_user) + 1
    return id

def register(data_user:list,data_monster:list,data_inventory_monster:list):
    # belum handle login
    username = input('Masukkan username : ')
    password = input('Masukkan password : ')

    if isUsernameValid(username,data_user) == 1:
        # input data diri kedalam user.csv
        user_id = generateId(data_user)

        print('\nSilahkan pilih salah satu monster sebagai monster awalmu.')
        showMonsterName(data_monster)
        
        monster_id = int(input('\nMonster pilihanmu : '))
        monster = {
            'user_id' : user_id,
            'monster_id' : monster_id,
            'level' : 1
        }
        user = {
            'id' : user_id,
            'username' : username,
            'password' : password,
            'role' : 'agent',
            'oc' : 0
        }
        data_inventory_monster.append(monster)
        data_user.append(user)


        print(f'\nSelamat datang Agent {username}. Mari kita mengalahkan Dr. Asep Spakbor dengan {search(data_monster,"id",monster_id,"type")} !')


    else:
        if isUsernameValid(username,data_user) == 0:
            print("Username hanya boleh berisi alfabet, angka, underscore, dan strip!")
        else:
            print(f'Username {username} sudah terpakai, silahkan gunakan username lain')

register(data_user,data_monster,data_inventory_monster)