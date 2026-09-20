import json
import os

FILE_NAME = "task.json"

def load_task():
    if not os.path.exists(FILE_NAME):
        return []
    
    with open(FILE_NAME, "r") as file:
        return json.load(file)
    
def save_task(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)
        
def main():
    tasks = load_task()
    
    while True:
        print("\n=== CLI TASK MANAGER ===")
        print("1. Lihat semua tugas")
        print("2. Tambah tugas baru")
        print("3. Delete tugas ")
        print("4. Update tugas ")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ")
        
        if pilihan == "1":
            if not tasks:
                print("Belum ada tugas")
            else:
                for t in tasks:
                    print(f"[{t['id']}] {t['tugas']} - ({t['status']})")
        elif pilihan == "2":
            judul = input("Masukan nama tugas: ")
            new_id = len(tasks) + 1
            new_task = {
                "id": new_id,
                "tugas": judul,
                "status": "Belum selesai"
            }
            
            tasks.append(new_task)
            save_task(tasks)
            print("Tugas berhasil disimpan")
            
        elif pilihan == "3":
            if not tasks:
                print("Tidak ada tugas untuk dihapus")
            delete_tugas = int(input("Tugas yang mau dihapus (ID/Urutan): "))
            tasks.pop(delete_tugas - 1)
            save_task(tasks)
            print("\nDaftar Tugas Terbaru:")
            for t in tasks:
                print(f"[{t['id']}] {t['tugas']} - ({t['status']})")
                
        elif pilihan == "4":
            if not tasks:
                print("Tidak ada tugas untuk diubah.")
                continue
            choose_data = int(input("Tugas mana yang mau diganti (ID/Urutan): "))
            change_data = input("Apa yang mau diganti? (Tugas or Status) ").strip().lower()
            if change_data == "tugas":
                task_change = input("Masukan tugas pengganti: ")
                tasks[choose_data - 1]["tugas"] = task_change
            elif change_data == "status":
                tasks[choose_data - 1]["status"] = "(Selesai)"
            
            save_task(tasks)
            print("\nDaftar Tugas Terbaru:")
            for t in tasks:
                print(f"[{t['id']}] {t['tugas']} - ({t['status']})")
        
        elif pilihan == "5":
            print("Terima kasih! Sampai Jumpa.")
            break

if __name__ == "__main__":
    main()