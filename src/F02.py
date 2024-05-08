# nama / nim    : Alfian Hanif FY / 19623281
# judul         : Login
# deskripsi     : Melakukan Login dan melakukan verifikasi login

# KAMUS
id_login = 0 # variabel untuk menyimpan user yang sedang login
# ALGORITMA

data_user = [{'id' : 1,'username' : 'alfian', 'password' : 'tubeskelar', 'role' : 'admin' , 'oc' : 0}]
data_monster = [{'id' : 1,'type' : 'pikachan', 'atk_power' : '150', 'def_power' : '20' , 'hp' : 600}]
data_inventory_item = [{'user_id' : 1,'type' : 'healing','quantity' : 1}]
data_inventory_monster = [{'user_id' : 1,'monster_id' : 1,'level' : 1}]
data_shop_item = [{'type' : 'healing', 'stock' : 99, 'price' : 5}]
data_shop_monster = [{'monster_id' : 1,'stock' : 25, 'price' : 25}]


def search(data:list,param:str,target,target_param:str):
    for element in data:
        if element[param] == target:
            return element[target_param]

def isUsernameInData(username:str,data_user)->bool:
    for user in data_user:
        if user['username'] == username:
            return True
    return False

def isPasswordCorrect(username:str,password:str,data_user:list)->bool:
    for user in data_user:
        if user['username'] == username and user['password'] == password:
            return True
    return False

def isLogin(id_login) -> bool:
    if id_login != 0:
        return True
    return False

def Login(id_login, data_user):
    if not isLogin(id_login):
        username = input("Masukkan username : ")
        password = input("Masukkan password : ")
    
        if not isPasswordCorrect(username,password,data_user) :
            print('Password salah')
        elif not isUsernameInData(username,data_user):
            print("Username tidak terdaftar")
        else:
            id_login = search(data_user,'username',username,'id')
            print(f"Selamat datang, Agent {username}!\nMasukkan command “help” untuk daftar command yang dapat kamu panggil.")
    else:
        username = search
        print(f'Login gagal!\nAnda telah login dengan username {username}, silahkan lakukan “LOGOUT” sebelum melakukan login kembali.')


Login(id_login,data_user)