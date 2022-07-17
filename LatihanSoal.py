print('=== LATIHAN KODE PROGRAM LIST DAN SET ===')
print('1. List')
print('2. Set')
list_buah = []
masukan = input('Masukkan angka pilihan Anda = ')

if masukan == '1':
    print('Anda memilih angka %s, yaitu List' %masukan)
    jumlah = int(input('Masukkan berapa kali Anda akan memasukkan buah = '))
    i = 0
    while i < jumlah:
        i += 1
        list_buah.append(input('Masukkan buah ke-%d = ' %i))
    print(list_buah)

    # Menambahkan inputan
    tambah = input('\nIngin menambah jumlah inputan? Ya/Tidak? ')
    if tambah == 'Ya':
        jumlah = int(input('Masukkan berapa kali lagi Anda akan memasukkan buah = '))
        i = 0
        while i < jumlah:
            i += 1
            list_buah.append(input('Masukkan buah ke-%d = ' %i))
        print(list_buah)
    elif tambah == 'Tidak':
        print('Anda tidak ingin menambahkan input buah.')
    else:
        print('Input Anda salah, bye!!')

elif masukan == '2':
    print('Anda memilih angka %s, yaitu Set' %masukan)
    jumlah = int(input('Masukkan berapa kali Anda akan memasukkan buah = '))
    i = 0
    while i < jumlah:
        i += 1
        list_buah.append(input('Masukkan buah ke-%d = ' %i))
    print(set(list_buah))

    # Menambahkan inputan
    tambah = input('\nIngin menambah jumlah inputan? Ya/Tidak? ')
    if tambah == 'Ya':
        jumlah = int(input('Masukkan berapa kali lagi Anda akan memasukkan buah = '))
        i = 0
        while i < jumlah:
            i += 1
            list_buah.append(input('Masukkan buah ke-%d = ' %i))
        print(set(list_buah))
    elif tambah == 'Tidak':
        print('Anda tidak ingin menambahkan input buah.')
    else:
        print('Input Anda salah, bye!!')