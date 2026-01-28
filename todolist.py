#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json, os
from datetime import datetime

FILE = 'data_tugas.json'

def load(): 
    return json.load(open(FILE)) if os.path.exists(FILE) else []

def save(data): 
    json.dump(data, open(FILE, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

def get_id(tasks): 
    return max(t['id'] for t in tasks) + 1 if tasks else 1

def add(tasks):
    judul = input("Judul: ").strip()
    if not judul: return print("❌ Judul tidak boleh kosong!")
    
    deskripsi = input("Deskripsi (opsional): ").strip()
    
    print("Prioritas: 1=TINGGI, 2=SEDANG, 3=RENDAH")
    prio = {'1': 'TINGGI', '2': 'SEDANG', '3': 'RENDAH'}.get(input("Pilih: ").strip(), 'SEDANG')
    
    while True:
        deadline = input("Deadline (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(deadline, '%Y-%m-%d')
            break
        except: print("❌ Format tidak valid!")
    
    task = {
        'id': get_id(tasks),
        'judul': judul,
        'deskripsi': deskripsi,
        'prioritas': prio,
        'deadline': deadline,
        'selesai': False
    }
    tasks.append(task)
    save(tasks)
    print(f"✅ Tugas ditambahkan! (ID: {task['id']})")

def view(tasks):
    if not tasks: return print("📭 Tidak ada tugas!")
    print("\n" + "="*60)
    print("📋 DAFTAR TUGAS")
    print("="*60)
    
    prio_order = {'TINGGI': 1, 'SEDANG': 2, 'RENDAH': 3}
    for t in sorted(tasks, key=lambda x: (prio_order.get(x['prioritas'], 4), x['deadline'])):
        status = "✅" if t['selesai'] else "⏳"
        print(f"\n[{t['id']}] {status} {t['judul']}")
        print(f"    {t['prioritas']} | {t['deadline']}")
        if t['deskripsi']: print(f"    {t['deskripsi']}")

def view_pending(tasks):
    pending = [t for t in tasks if not t['selesai']]
    if not pending: return print("✅ Semua selesai!")
    
    print("\n" + "="*60)
    print("⏳ TUGAS BELUM SELESAI")
    print("="*60)
    
    icons = {'TINGGI': '🔴', 'SEDANG': '🟡', 'RENDAH': '🟢'}
    for prio in ['TINGGI', 'SEDANG', 'RENDAH']:
        group = [t for t in pending if t['prioritas'] == prio]
        if group:
            print(f"\n{icons.get(prio, '')} {prio}")
            for t in sorted(group, key=lambda x: x['deadline']):
                print(f"  [{t['id']}] {t['judul']} - {t['deadline']}")

def complete(tasks):
    view(tasks)
    try:
        id = int(input("\nID tugas: "))
        for t in tasks:
            if t['id'] == id:
                t['selesai'] = True
                save(tasks)
                print(f"✅ Selesai!")
                return
        print("❌ Tidak ditemukan!")
    except: print("❌ Input invalid!")

def delete(tasks):
    view(tasks)
    try:
        id = int(input("\nID tugas: "))
        for i, t in enumerate(tasks):
            if t['id'] == id:
                if input("Yakin? (y/n): ").lower() == 'y':
                    tasks.pop(i)
                    save(tasks)
                    print("✅ Dihapus!")
                return
        print("❌ Tidak ditemukan!")
    except: print("❌ Input invalid!")

def filter_prio(tasks):
    print("Prioritas: 1=TINGGI, 2=SEDANG, 3=RENDAH")
    prio = {'1': 'TINGGI', '2': 'SEDANG', '3': 'RENDAH'}.get(input("Pilih: ").strip())
    if not prio: return print("❌ Invalid!")
    
    filtered = [t for t in tasks if t['prioritas'] == prio]
    if not filtered: return print(f"❌ Tidak ada tugas {prio}!")
    
    print(f"\n🔴 Prioritas {prio}")
    for t in sorted(filtered, key=lambda x: x['deadline']):
        status = "✅" if t['selesai'] else "⏳"
        print(f"  {status} [{t['id']}] {t['judul']} - {t['deadline']}")

def stats(tasks):
    if not tasks: return print("📭 Tidak ada tugas!")
    
    total = len(tasks)
    done = len([t for t in tasks if t['selesai']])
    pending = total - done
    
    print("\n" + "="*60)
    print("📊 STATISTIK")
    print("="*60)
    print(f"Total: {total} | ✅ Selesai: {done} | ⏳ Belum: {pending}")
    print(f"📈 Progres: {done/total*100:.1f}%")

def main():
    print("🎉 APLIKASI TO-DO LIST 🎉\n")
    
    while True:
        print("\n" + "="*60)
        print("1. ➕ Tambah  2. 📋 Lihat  3. ⏳ Belum  4. 🔍 Filter")
        print("5. ✅ Selesai  6. 🗑️ Hapus  7. 📊 Statistik  8. ❌ Keluar")
        print("="*60)
        
        tasks = load()
        pilihan = input("Pilih (1-8): ").strip()
        
        if pilihan == '1': add(tasks)
        elif pilihan == '2': view(tasks)
        elif pilihan == '3': view_pending(tasks)
        elif pilihan == '4': filter_prio(tasks)
        elif pilihan == '5': complete(tasks)
        elif pilihan == '6': delete(tasks)
        elif pilihan == '7': stats(tasks)
        elif pilihan == '8':
            print("\n👋 Terima kasih! Data tersimpan di data_tugas.json\n")
            break
        else: print("❌ Pilihan tidak valid!")

if __name__ == '__main__':
    main()
