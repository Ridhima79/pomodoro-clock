import tkinter as tk

# Global state
timer_seconds = 0
countdown_running = False
is_work_session = True

def start_timer():
    global timer_seconds, countdown_running, is_work_session

    if countdown_running:
        return

    try:
        work_minutes = int(work_entry.get())
        break_minutes = int(break_entry.get())
        task = task_entry.get()

        if is_work_session:
            timer_seconds = work_minutes * 60
            status_label.config(text=f"🎀 Working on: {task}")
        else:
            timer_seconds = break_minutes * 60
            status_label.config(text="💗 Break time!")

        countdown_running = True
        countdown()
    except ValueError:
        status_label.config(text="❌ Please enter valid numbers!")

def countdown():
    global timer_seconds, countdown_running, is_work_session

    if timer_seconds > 0:
        mins = timer_seconds // 60
        secs = timer_seconds % 60
        timer_label.config(text=f"{mins:02d}:{secs:02d}")
        timer_seconds -= 1
        root.after(1000, countdown)
    else:
        countdown_running = False
        timer_label.config(text="🍒 Time's up!")
        root.after(1000, switch_session)

def switch_session():
    global is_work_session
    is_work_session = not is_work_session
    start_timer()

def update_time():
    global timer_seconds

    try:
        new_time_minutes = int(edit_time_entry.get())
        timer_seconds = new_time_minutes * 60
        mins = timer_seconds // 60
        secs = timer_seconds % 60
        timer_label.config(text=f"{mins:02d}:{secs:02d}")
        status_label.config(text="🔄 Time updated 💖")
    except ValueError:
        status_label.config(text="❌ Enter valid minutes!")

# --- UI Setup ---
root = tk.Tk()
root.title("🎀 Sweet Pomodoro")
root.geometry("360x500")
root.configure(bg="#ffd6e8")  # Baby pink background
root.resizable(False, False)

# Card-like Frame
card = tk.Frame(root, bg="#ffd6e8", highlightthickness=0)
card.place(relx=0.5, rely=0.5, anchor="center")

# Title
tk.Label(card, text="🎀 Pomodoro Timer", bg="#ffd6e8",
         font=("Comic Sans MS", 18, "bold"), fg="#c44569").pack(pady=(15, 10))

# Task
tk.Label(card, text="💗 Task Name", bg="#ffd6e8", fg="#c44569", font=("Comic Sans MS", 11)).pack()
task_entry = tk.Entry(card, width=28, font=("Comic Sans MS", 10),
                      bg="#fff6a9", bd=0, justify='center')
task_entry.pack(pady=5)

# Work Time
tk.Label(card, text="🍒 Work Time (mins)", bg="#ffd6e8", fg="#c44569", font=("Comic Sans MS", 11)).pack()
work_entry = tk.Entry(card, width=10, font=("Comic Sans MS", 10),
                      bg="#fff6a9", bd=0, justify='center')
work_entry.insert(0, "25")
work_entry.pack(pady=5)

# Break Time
tk.Label(card, text="🍰 Break Time (mins)", bg="#ffd6e8", fg="#c44569", font=("Comic Sans MS", 11)).pack()
break_entry = tk.Entry(card, width=10, font=("Comic Sans MS", 10),
                       bg="#fff6a9", bd=0, justify='center')
break_entry.insert(0, "5")
break_entry.pack(pady=5)

# Timer Display
timer_label = tk.Label(card, text="00:00", font=("Comic Sans MS", 28, "bold"),
                       fg="#c44569", bg="#ffd6e8")
timer_label.pack(pady=15)

# Start Button
start_button = tk.Button(card, text="▶ Start 🍓", command=start_timer,
                         font=("Comic Sans MS", 11, "bold"),
                         bg="#fff6a9", fg="#c44569", bd=0, width=20)
start_button.pack(pady=8)

# Time Editor
tk.Label(card, text="⏰ Edit Remaining Time (mins)", bg="#ffd6e8", fg="#c44569", font=("Comic Sans MS", 11)).pack()
edit_time_entry = tk.Entry(card, width=10, font=("Comic Sans MS", 10),
                           bg="#fff6a9", bd=0, justify='center')
edit_time_entry.insert(0, "25")
edit_time_entry.pack(pady=5)

update_button = tk.Button(card, text="🔄 Update Time 🍥", command=update_time,
                          font=("Comic Sans MS", 10, "bold"),
                          bg="#fff6a9", fg="#c44569", bd=0, width=20)
update_button.pack(pady=8)

# Status
status_label = tk.Label(card, text="", bg="#ffd6e8", fg="#c44569", font=("Comic Sans MS", 10))
status_label.pack(pady=5)

# Run App
root.mainloop()
