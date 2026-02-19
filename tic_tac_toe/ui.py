import tkinter as tk
from game import check_winner
from ai import easy_ai, medium_ai, hard_ai

# UI Constants
BG_COLOR = "#1e293b"
BTN_COLOR = "#334155"
ACCENT = "#38bdf8"
TEXT = "#f1f5f9"
WIN_COLOR = "#22c55e" # Green for win highlight

class TicTacToeUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        self.root.geometry("500x700") # Slightly taller for better spacing
        self.root.configure(bg=BG_COLOR)

        self.player_score = 0
        self.bot_score = 0
        self.mode = "AI"
        self.level = "Easy"
        self.game_active = False # Flag to prevent moves after end game

        self.show_home()

    def clear(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def modern_button(self, text, command, parent=None, pack=True):
        target = parent if parent else self.root
        btn = tk.Button(target, text=text, command=command,
                        font=("Arial", 14, "bold"), bg=BTN_COLOR, fg=TEXT,
                        activebackground=ACCENT, activeforeground=BG_COLOR,
                        width=20, height=2, bd=0, cursor="hand2")
        if pack:
            btn.pack(pady=10)
        return btn

    # ---------------- SCREENS ----------------

    def show_home(self):
        self.clear()
        tk.Label(self.root, text="Tic Tac Toe", font=("Arial", 32, "bold"),
                 bg=BG_COLOR, fg=ACCENT).pack(pady=60)

        self.modern_button("Play Solo (AI)", self.show_difficulty)
        self.modern_button("Play With Friend", self.start_friend_game)
        self.modern_button("Exit", self.root.quit)

    def show_difficulty(self):
        self.clear()
        tk.Label(self.root, text="Select Difficulty", font=("Arial", 22),
                 bg=BG_COLOR, fg=TEXT).pack(pady=40)

        for lvl in ["Easy", "Medium", "Hard"]:
            self.modern_button(lvl, lambda l=lvl: self.start_ai_game(l))

        tk.Label(self.root, text="", bg=BG_COLOR).pack(pady=10) # Spacer
        self.modern_button("Back", self.show_home)

    # ---------------- GAME LOGIC ----------------

    def start_ai_game(self, level):
        self.mode = "AI"
        self.level = level
        self.start_game()

    def start_friend_game(self):
        self.mode = "Friend"
        self.start_game()

    def start_game(self):
        self.clear()
        self.board = [""] * 9
        self.current_player = "X"
        self.game_active = True
        self.buttons = []

        # Scoreboard Header
        score_frame = tk.Frame(self.root, bg=BG_COLOR)
        score_frame.pack(pady=20)
        
        self.p_label = tk.Label(score_frame, text=f"Player (X): {self.player_score}",
                                bg=BG_COLOR, fg=ACCENT, font=("Arial", 14, "bold"))
        self.p_label.pack(side="left", padx=30)

        self.b_label = tk.Label(score_frame, text=f"Opponent (O): {self.bot_score}",
                                bg=BG_COLOR, fg="orange", font=("Arial", 14, "bold"))
        self.b_label.pack(side="left", padx=30)

        self.turn_label = tk.Label(self.root, text="X's Turn", bg=BG_COLOR,
                                   fg=TEXT, font=("Arial", 18))
        self.turn_label.pack(pady=10)

        # Game Grid
        grid = tk.Frame(self.root, bg=BG_COLOR)
        grid.pack(pady=10)

        for i in range(9):
            btn = tk.Button(grid, text="", width=6, height=2,
                            font=("Arial", 28, "bold"), bg=BTN_COLOR, fg=TEXT,
                            activebackground=BTN_COLOR, bd=2, relief="flat",
                            command=lambda i=i: self.handle_click(i))
            btn.grid(row=i//3, column=i%3, padx=5, pady=5)
            self.buttons.append(btn)

        # Bottom Controls
        btn_frame = tk.Frame(self.root, bg=BG_COLOR)
        btn_frame.pack(pady=20)
        self.modern_button("Reset Board", self.start_game, parent=btn_frame)
        self.modern_button("Main Menu", self.show_home, parent=btn_frame)

    def handle_click(self, i):
        # Only allow click if game is active, spot is empty, and it's not AI's turn
        if self.game_active and self.board[i] == "":
            self.make_move(i, self.current_player)
            
            if not self.game_active: return

            if self.mode == "AI":
                self.current_player = "O"
                self.turn_label.config(text="Bot is thinking...")
                self.root.after(500, self.ai_move)
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.turn_label.config(text=f"{self.current_player}'s Turn")

    def make_move(self, i, player):
        self.board[i] = player
        self.buttons[i].config(text=player, fg=ACCENT if player == "X" else "orange")
        
        winner = check_winner(self.board)
        if winner:
            self.end_game(winner)

    def ai_move(self):
        if not self.game_active: return
        
        if self.level == "Easy":
            move = easy_ai(self.board)
        elif self.level == "Medium":
            move = medium_ai(self.board, "X", "O")
        else:
            move = hard_ai(self.board, "X", "O")

        if move is not None:
            self.make_move(move, "O")
            if self.game_active:
                self.current_player = "X"
                self.turn_label.config(text="Your Turn (X)")

    def end_game(self, winner):
        self.game_active = False
        if winner == "X":
            self.player_score += 1
            self.turn_label.config(text="Player X Wins!", fg=WIN_COLOR)
        elif winner == "O":
            self.bot_score += 1
            self.turn_label.config(text="Player O Wins!", fg="orange")
        else:
            self.turn_label.config(text="It's a Draw!", fg=TEXT)

        # Update Scoreboard Labels immediately
        self.p_label.config(text=f"Player (X): {self.player_score}")
        self.b_label.config(text=f"Opponent (O): {self.bot_score}")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = TicTacToeUI()
    game.run()