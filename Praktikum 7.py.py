# Initialize an empty list to store student data
students = []

def display_data():
    if not students:
        print("============================================")
        print("| NO | NIM    | NAMA       | TUGAS | UTS | UAS | AKHIR |")
        print("============================================")
        print("|                 TIDAK ADA DATA            |")
        print("============================================")
    else:
        print("============================================")
        print("| NO | NIM    | NAMA       | TUGAS | UTS | UAS | AKHIR |")
        print("============================================")
        for i, student in enumerate(students):
            print(f"| {i+1:<2} | {student['nim']:<6} | {student['nama']:<10} | {student['tugas']:<5} | {student['uts']:<3} | {student['uas']:<3} | {student['akhir']:<5} |")
        print("============================================")

def add_data():
    nim = input("Masukkan NIM: ")
    nama = input("Masukkan Nama: ")
    tugas = float(input("Masukkan Nilai Tugas: "))
    uts = float(input("Masukkan Nilai UTS: "))
    uas = float(input("Masukkan Nilai UAS: "))
    akhir = (tugas * 0.3) + (uts * 0.35) + (uas * 0.35)
    students.append({"nim": nim, "nama": nama, "tugas": tugas, "uts": uts, "uas": uas, "akhir": akhir})
    print("Data berhasil ditambahkan!")

def update_data():
    display_data()
    if students:
        no = int(input("Masukkan nomor data yang akan diubah: ")) - 1
        if 0 <= no < len(students):
            print("Masukkan data baru:")
            students[no]['nim'] = input("Masukkan NIM: ")
            students[no]['nama'] = input("Masukkan Nama: ")
            students[no]['tugas'] = float(input("Masukkan Nilai Tugas: "))
            students[no]['uts'] = float(input("Masukkan Nilai UTS: "))
            students[no]['uas'] = float(input("Masukkan Nilai UAS: "))
            students[no]['akhir'] = (students[no]['tugas'] * 0.3) + (students[no]['uts'] * 0.35) + (students[no]['uas'] * 0.35)
            print("Data berhasil diperbarui!")
        else:
            print("Nomor data tidak valid!")

def delete_data():
    display_data()
    if students:
        no = int(input("Masukkan nomor data yang akan dihapus: ")) - 1
        if 0 <= no < len(students):
            students.pop(no)
            print("Data berhasil dihapus!")
        else:
            print("Nomor data tidak valid!")

def search_data():
    nim = input("Masukkan NIM yang dicari: ")
    found = False
    print("============================================")
    print("| NO | NIM    | NAMA       | TUGAS | UTS | UAS | AKHIR |")
    print("============================================")
    for i, student in enumerate(students):
        if student['nim'] == nim:
            print(f"| {i+1:<2} | {student['nim']:<6} | {student['nama']:<10} | {student['tugas']:<5} | {student['uts']:<3} | {student['uas']:<3} | {student['akhir']:<5} |")
            found = True
    if not found:
        print("|            DATA TIDAK DITEMUKAN           |")
    print("============================================")

while True:
    print("\nProgram Input Nilai")
    print("====================")
    print("(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar")
    choice = input("Pilih menu: ").lower()

    if choice == 'l':
        display_data()
    elif choice == 't':
        add_data()
    elif choice == 'u':
        update_data()
    elif choice == 'h':
        delete_data()
    elif choice == 'c':
        search_data()
    elif choice == 'k':
        print("Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi!")
