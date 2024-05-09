from src import F00,F01,F02,F03,utilities as util

def main():

    # inisiasi variabel untuk menyimpan data csv dan lainnya
    data_user = [{'id' : 1,'username' : 'alfian', 'password' : 'tubeskelar', 'role' : 'admin' , 'oc' : 0}]
    data_monster = [{'id' : 1,'type' : 'pikachan', 'atk_power' : '150', 'def_power' : '20' , 'hp' : 600}]
    data_inventory_item = [{'user_id' : 1,'type' : 'healing','quantity' : 1}]
    data_inventory_monster = [{'user_id' : 1,'monster_id' : 1,'level' : 1}]
    data_shop_item = [{'type' : 'healing', 'stock' : 99, 'price' : 5}]
    data_shop_monster = [{'monster_id' : 1,'stock' : 25, 'price' : 25}]
    id_login = 1
    util.div()
    print('selamat datang di OWCA')
    util.div()
    while True:

        user_input = input('>> ')
        util.div()

        if user_input == 'REGISTER':
            F01.register(data_user,data_monster,data_inventory_monster,id_login)
            util.div()
        
        elif user_input == 'LOGIN':
            F02.login(id_login,data_user)
            util.div()

        elif user_input == 'LOGOUT':
            F03.logout(id_login)
            util.div()

        elif user_input == 'EXIT':
            break

        else:
            print('ketik "HELP" untuk melihat menu yang tersedia !')
            util.div()

        # menu admin



        # menu agent

if __name__ == '__main__':
    main()



