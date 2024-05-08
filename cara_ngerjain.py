# ========== semoga paham ============

'''

jadi gini ges buat data-data itu kita simpen kayak gini...
bentuknya array isinya dictionary...

'''

data_user = [{'id' : 1,'username' : 'alfian', 'password' : 'tubeskelar', 'role' : 'admin' , 'oc' : 0}]
data_monster = [{'id' : 1,'type' : 'pikachan', 'atk_power' : '150', 'def_power' : '20' , 'hp' : 600}]
data_inventory_item = [{'user_id' : 1,'type' : 'healing','quantity' : 1}]
data_inventory_monster = [{'user_id' : 1,'monster_id' : 1,'level' : 1}]
data_shop_item = [{'type' : 'healing', 'stock' : 99, 'price' : 5}]
data_shop_monster = [{'monster_id' : 1,'stock' : 25, 'price' : 25}]

'''
data diatas tuh ngewakilin csv yang ada di spesifikasi...
jadi kalian ga perlu mikirin caranya ngambil data dari csv, itu urusannya aben :)
kalian copy aja variabel diatas buat nge tes fungsi kalian
'''

'''
terus gimana cara makenya????
simpelnya gini, misal w butuh data user... kan w harus akses data2 di user.csv padahal w ga tau caranya...
jadi w ga perlu direct access si csv nya, w cuman perlu manggil variabel dari array diatas...

contoh nya...
w kebagian tugas buat bikin fungsi nampilin semua nama user yang terdaftar,
otomatis w perlu akses ke data di user.csv kan?
buat akses data itu, w cuman perlu masukin parameter 'data_user' ke fungsi w
kayak yang dibawah
'''

def showUser(data_user:list):
    for user in data_user:
        print(f"{user['username']}")

'''
w ga perlu read csv yang entah dimana keberadaannya, 
w ga peduli isi csv nya apa, 
yang penting w tau kalo 'data_user' itu ngewakilin isi dari 'user.csv'
dan bisa w akses sesuai struktur yang ada di spesifikasi

oiya strukturnya itu sesuai spesifikasi dibagian 'struktur data file' yaa...
'''

'''
buat yang mau update data atau nambahin data ke array juga bisa ya...

gini contohnya:
misal w dapet tugas menu admin buat nambahin monster ke database...
karena w perlu akses 'monster.csv' maka w bakal masukin 'data_monster' ke parameter fungsi w...
kayak fungsi dibwah

'''

def addMonster(data_monster):
    id = int(input('masukkan id : '))       # harusnya bagian id ga di input manual tapi otomatis (increasing)
    type = input('masukkan type : ')
    atk_power = int(input('masukkan atk_power : '))
    def_power = int(input('masukkan def_power : '))
    hp = int(input('masukkan hp :'))

    # terus kita buat dictionary nya !
    # pastikan dictionary yang dibuat sesuai struktur !

    monster = {
        'id' : id,
        'type' : type,
        'atk_power' : atk_power,
        'def_power' : def_power,
        'hp' : hp
    }

    # lalu kita masukkin variabel dictionary kita ke array data_monster
    data_monster.append(monster)

'''
nah nanti bakalan nambah 1 data baru di data_monster kalo kita panggil fungsi diatas

semoga paham ya ges :)
'''