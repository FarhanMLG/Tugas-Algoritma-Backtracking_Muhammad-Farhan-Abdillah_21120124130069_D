import time
import os

# Representasi Labirin: 
# 0 = Jalan (bisa dilewati)
# 1 = Tembok (constraint)
maze = [
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 0],
    [0, 0, 0, 1, 0, 0],
    [1, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 0]
]

N = len(maze)
# Matrix untuk menyimpan jalur solusi
solusi = [[0 for _ in range(N)] for _ in range(N)]

def print_maze():
    """Fungsi untuk visualisasi labirin di CLI"""
    # Membersihkan layar terminal (support Windows/Linux/Mac)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("--- Visualisasi Rat in a Maze ---")
    for i in range(N):
        baris = ""
        for j in range(N):
            if maze[i][j] == 1:
                baris += "█ " # Tembok
            elif solusi[i][j] == 1:
                baris += "● " # Jalur tikus
            else:
                baris += ". " # Jalan kosong
        print(baris)
    print("---------------------------------")
    time.sleep(0.5) # Memberi jeda waktu agar terlihat seperti animasi

def aman_untuk_maju(x, y):
    """Mengecek apakah koordinat ada di dalam batas labirin dan bukan tembok"""
    if x >= 0 and x < N and y >= 0 and y < N and maze[x][y] == 0:
        return True
    return False

def solve_maze_util(x, y):
    # Base case: Tikus berhasil tiba di pintu keluar (pojok kanan bawah)
    if x == N - 1 and y == N - 1 and maze[x][y] == 0:
        solusi[x][y] = 1
        print_maze()
        return True

    # Mengecek apakah aman untuk meletakkan tikus di maze[x][y]
    if aman_untuk_maju(x, y):
        # Mengecek apakah jalan ini sudah dilewati sebelumnya (menghindari berputar-putar)
        if solusi[x][y] == 1:
            return False
            
        # Tandai sebagai bagian dari jalur solusi
        solusi[x][y] = 1
        print_maze()

        # Ambil salah satu jalan: Coba ke BAWAH
        if solve_maze_util(x + 1, y):
            return True
            
        # Ambil salah satu jalan: Coba ke KANAN
        if solve_maze_util(x, y + 1):
            return True

        # Ambil salah satu jalan: Coba ke ATAS
        if solve_maze_util(x - 1, y):
            return True

        # Ambil salah satu jalan: Coba ke KIRI
        if solve_maze_util(x, y - 1):
            return True

        # BACKTRACKING: Jika semua arah tidak membawa ke tujuan, batalkan rute ini
        solusi[x][y] = 0
        print_maze()
        return False
        
    return False

def jalankan_program():
    print("Mencari solusi...")
    time.sleep(1)
    if solve_maze_util(0, 0) == False:
        print("Solusi tidak ditemukan")
    else:
        print("Tikus berhasil mencapai tujuan!")

# Memulai program
if __name__ == "__main__":
    jalankan_program()