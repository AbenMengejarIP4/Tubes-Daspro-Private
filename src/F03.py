# fungsi logout

def Logut(id_login):
    if id_login == 0:
        print('Logout gagal!\nAnda belum login, silahkan login terlebih dahulu sebelum melakukan logout')
        return id_login
    else:
        print('Logut berhasil')
        id_login = 0
        return id_login
