import tkinter
from tkinter import messagebox 

# Warna (Hex codes diambil dari logo Python)
color_blue = "#45A4B6"
color_yellow = "#FFDE57"
color_gray = "#343434"
color_light_gray = "#646464"

# Pemain
playerX = "X"
playerO = "O"
curr_player = playerX

# Papan (Awalnya diisi None)
board = [[None, None, None],
         [None, None, None],
         [None, None, None]]

# Status Game
turns = 0
game_over = False

def new_game():
    """Mengatur ulang game ke kondisi awal untuk babak baru."""
    global turns, game_over, curr_player
    
    # Reset status game
    turns = 0
    game_over = False
    
    # Update Label (Diterjemahkan)
    # Pemain saat ini (curr_player) akan menjadi pemain yang memulai babak baru
    label.config(text="Giliran " + curr_player, foreground="white") 
    
    # Reset semua tombol pada papan
    for row in range(3):
        for column in range(3):
            # Reset text, warna, dan status tombol
            board[row][column].config(text="", 
                                      foreground=color_blue, 
                                      background=color_gray,
                                      state=tkinter.NORMAL) 

def check_winner():
    """Memeriksa semua kondisi menang (Horizontal, Vertikal, Diagonal) dan Seri."""
    global turns, game_over
    turns += 1

    # Logika untuk menampilkan pemenang (Diterjemahkan)
    def handle_winner(winner_tile, row_indices, col_indices):
        global game_over
        label.config(text="Pemenangnya adalah " + winner_tile + "!", foreground=color_yellow)
        
        # Mengubah warna tombol yang menang
        for r, c in zip(row_indices, col_indices):
            board[r][c].config(foreground=color_yellow, background=color_light_gray)
            
        game_over = True
        return True
    
    # --- Cek Baris Horizontal ---
    for row in range(3):
        first_tile = board[row][0]["text"]
        if (first_tile == board[row][1]["text"] and 
            first_tile == board[row][2]["text"] and 
            first_tile != ""): 
            
            return handle_winner(first_tile, [row, row, row], [0, 1, 2])
    
    # --- Cek Kolom Vertikal ---
    for column in range(3):
        first_tile = board[0][column]["text"]
        if (first_tile == board[1][column]["text"] and 
            first_tile == board[2][column]["text"] and 
            first_tile != ""):
            
            return handle_winner(first_tile, [0, 1, 2], [column, column, column])


    # --- Cek Diagonal Kiri Atas ke Kanan Bawah ---
    first_tile = board[0][0]["text"]
    if (first_tile == board[1][1]["text"] and 
        first_tile == board[2][2]["text"] and 
        first_tile != ""):
        
        return handle_winner(first_tile, [0, 1, 2], [0, 1, 2])

    # --- Cek Diagonal Kanan Atas ke Kiri Bawah ---
    first_tile = board[0][2]["text"]
    if (first_tile == board[1][1]["text"] and 
        first_tile == board[2][0]["text"] and 
        first_tile != ""):
        
        return handle_winner(first_tile, [0, 1, 2], [2, 1, 0])

    # --- Cek Seri (Tie) ---
    if turns == 9:
        label.config(text="Hasilnya Seri!", foreground=color_yellow) # Diterjemahkan
        game_over = True
        return True

    return False


def set_tile(row, column):
    """Menangani klik tombol dan menempatkan simbol pemain."""
    global curr_player, game_over
    
    # Cek jika ubin sudah terisi atau game sudah berakhir
    if board[row][column]["text"] != "" or game_over:
        return
        
    # Isi ubin dengan simbol pemain saat ini
    board[row][column].config(text=curr_player) 
    
    # Cek pemenang setelah giliran selesai
    check_winner()

    # Ganti pemain (hanya jika game belum berakhir)
    if not game_over:
        if curr_player == playerO:
            curr_player = playerX
        else:
            curr_player = playerO
        
        # Update Label (Diterjemahkan)
        label.config(text="Giliran " + curr_player)

# Jendela Utama
window = tkinter.Tk()
window.title("Tic Tac Toe") # Judul jendela tetap dalam Bahasa Inggris, ini umum.
window.resizable(False, False) 

# Frame (Wadah untuk komponen)
frame = tkinter.Frame(window) 

# Label Status (Menampilkan giliran pemain atau hasil) (Diterjemahkan)
label = tkinter.Label(frame, 
                      text="Giliran " + curr_player, 
                      font=("Consolas", 20), 
                      background=color_gray, 
                      foreground="white") 

label.grid(row=0, column=0, columnspan=3, sticky="we") 

# Loop untuk membuat 9 tombol papan
for row in range(3):
    for column in range(3):
        btn = tkinter.Button(frame, 
                             text="", 
                             font=("Consolas", 50, "bold"),
                             background=color_gray, 
                             foreground=color_blue, 
                             width=4, 
                             height=1, 
                             command=lambda row=row, column=column: set_tile(row, column)) 
        
        # Menyimpan referensi tombol ke dalam list 'board'
        board[row][column] = btn 
        
        # Menempatkan tombol di grid
        # row+1 karena row 0 sudah dipakai label
        board[row][column].grid(row=row+1, column=column) 

# Tombol Restart (Diterjemahkan)
button = tkinter.Button(frame, 
                        text="MULAI ULANG", # Diterjemahkan
                        font=("Consolas", 20), 
                        background=color_gray, 
                        foreground="white", 
                        command=new_game) 

button.grid(row=4, column=0, columnspan=3, sticky="we") 

frame.pack()

window.update() 
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight() 

window_x = int(screen_width / 2 - window_width / 2)
window_y = int(screen_height / 2 - window_height / 2)

# Mengatur posisi jendela (widthxheight+x+y)
window.geometry(f'{window_width}x{window_height}+{window_x}+{window_y}')

# Memulai Loop Utama Tkinter
window.mainloop()