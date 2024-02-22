import tkinter, random, math

class RPSGame:
    def __init__(self):
        self.player_choice = None
        self.computer_choice = None
        self.scoreboard = {"player": 0, "computer": 0, "ties": 0}
        self.options_list = ["Rock", "Paper", "Scissors", "L", "W"]

    def check_winner(self, player1choice, player2choice) -> int:
        # it's a tie
        if player1choice - player2choice == 0:
            return 2
        # player 1 wins
        elif player1choice - player2choice in [1, -2]:
            return 0
        # player 2 wins
        else:
            return 1

    def player_choose(self, choice: int):
        global timer_displayed
        global bot_made_choice
        global player_choice_shown
        global bot_time
        player_choice_shown = True
        global_timers["player_input_timerB"] = 100
        global_timers["player_input_timerC"] = 150

        timer_displayed = False
        bot_made_choice = 1
        self.player_choice = choice
        bot_time = random.randint(100,200)
        global_timers["bot_timer"] = bot_time
        create_buttons(False)

    def update_score(self, scorer: int):
        if scorer == 0:
            self.scoreboard["player"] += 1
        elif scorer == 2:
            self.scoreboard["ties"] += 1
        else:
            self.scoreboard["computer"] += 1

def sine_between(min, max, percent):
    return max + 0.5 * (1-math.cos(percent*math.pi)) * (min - max)

def create_buttons(enabled: bool):
    main_canvas.delete("rockbutton","paperbutton","scissorsbutton","timertext")
    if enabled:
        main_canvas.create_rectangle(5, 695, 155, 545, fill="#cc0000", activefill="#ff0000", width=5, outline="black", activewidth=7, tags="rockbutton")
        main_canvas.create_rectangle(175, 695, 325, 545, fill="#00cc00", activefill="#00ff00", width=5, outline="black", activewidth=7, tags="paperbutton")
        main_canvas.create_rectangle(345, 695, 495, 545, fill="#0000cc", activefill="#0000ff", width=5, outline="black", activewidth=7, tags="scissorsbutton")
        main_canvas.tag_bind("rockbutton", "<Button-1>", lambda event: rps_game.player_choose(0))
        main_canvas.tag_bind("paperbutton", "<Button-1>", lambda event: rps_game.player_choose(1))
        main_canvas.tag_bind("scissorsbutton", "<Button-1>", lambda event: rps_game.player_choose(2))
        main_canvas.create_text(80, 620, text="Rock", fill="white", font=("", 20), tags="rockbutton", activefill="#aaaaaa")
        main_canvas.create_text(250, 620, text="Paper", fill="black", font=("", 20), tags="paperbutton", activefill="#666666")
        main_canvas.create_text(420, 620, text="Scissors", fill="white", font=("", 20), tags="scissorsbutton", activefill="#bbbbbb")
        main_canvas.create_text(250, 200, text="Choose one!", font=("", 70), tags="timertext", fill="black")
        main_canvas.create_text(250, 335, text="Your time drains\never faster...", justify="center", fill="black", font=("", 25), tags="timertext")
    else:
        main_canvas.create_rectangle(5, 695, 155, 545, fill="#aaaaaa", width=5, outline="black", activewidth=7, tags="rockbutton")
        main_canvas.create_rectangle(175, 695, 325, 545, fill="#dddddd", width=5, outline="black", activewidth=7, tags="paperbutton")
        main_canvas.create_rectangle(345, 695, 495, 545, fill="#777777", width=5, outline="black", activewidth=7, tags="scissorsbutton")
        main_canvas.tag_bind("rockbutton", "<Button-1>", lambda event: do_nothing())
        main_canvas.tag_bind("paperbutton", "<Button-1>", lambda event: reset_for_next_round())
        main_canvas.tag_bind("scissorsbutton", "<Button-1>", lambda event: do_nothing())
        main_canvas.create_text(250, 620, text="Next", fill="black", font=("", 20), tags="paperbutton", activefill="#555555")

sliding_state: int = -1
def display_score(setPositionTo: int):
    global sliding_state
    main_canvas.delete("scoreboard")

    if setPositionTo == 0:
        # bring down
        main_canvas.create_rectangle(5, sine_between(-145, 5, global_timers["scoreboard_sliding_timer"] / 100), 494, sine_between(0, 150, global_timers["scoreboard_sliding_timer"] / 100), width=3, fill="white", tags="scoreboard", outline="black")
        main_canvas.create_text(15, sine_between(-135, 15, global_timers["scoreboard_sliding_timer"] / 100), text="Your Score:", font=("", 15), fill="black", tags="scoreboard", anchor="nw")
        main_canvas.create_text(15, sine_between(-120, 30, global_timers["scoreboard_sliding_timer"] / 100), text=f"{rps_game.scoreboard['player']}", font=("", 100), fill="black", tags="scoreboard", anchor="nw")
        main_canvas.create_text(485, sine_between(-135, 15, global_timers["scoreboard_sliding_timer"] / 100), text="Bot Score:", font=("", 15), fill="black", tags="scoreboard", anchor="ne")
        main_canvas.create_text(485, sine_between(-120, 30, global_timers["scoreboard_sliding_timer"] / 100), text=f"{rps_game.scoreboard['computer']}", font=("", 100), fill="black", tags="scoreboard", anchor="ne")
    if setPositionTo == 1:
        # send up
        main_canvas.create_rectangle(5, sine_between(5, -145, global_timers["scoreboard_sliding_timer"] / 100), 494, sine_between(150, 0, global_timers["scoreboard_sliding_timer"] / 100), width=3, fill="white", tags="scoreboard", outline="black")
        main_canvas.create_text(15, sine_between(15, -135, global_timers["scoreboard_sliding_timer"] / 100), text="Your Score:", font=("", 15), fill="black", tags="scoreboard", anchor="nw")
        main_canvas.create_text(15, sine_between(30, -120, global_timers["scoreboard_sliding_timer"] / 100), text=f"{rps_game.scoreboard['player']}", font=("", 100), fill="black", tags="scoreboard", anchor="nw")
        main_canvas.create_text(485, sine_between(15, -135, global_timers["scoreboard_sliding_timer"] / 100), text="Bot Score:", font=("", 15), fill="black", tags="scoreboard", anchor="ne")
        main_canvas.create_text(485, sine_between(30, -120, global_timers["scoreboard_sliding_timer"] / 100), text=f"{rps_game.scoreboard['computer']}", font=("", 100), fill="black", tags="scoreboard", anchor="ne")
        # score at the top left
    #main_canvas.create_text(15, 15, anchor="nw", text=f"Current Score: {rps_game.scoreboard['player']} (You) - {rps_game.scoreboard['computer']} (Computer) - {rps_game.scoreboard['ties']} Ties")

player_choice_shown: bool = False
def display_results(enabled: bool):
    main_canvas.delete("resultstext")
    if enabled:
        # you and bot chose...
        main_canvas.create_text(sine_between(-195, 5, global_timers["player_input_timerB"] / 100), 460, anchor="nw", text=" You chose: ", tags="resultstext", fill="black", font=("", 15))
        main_canvas.create_text(sine_between(-195, 5, global_timers["player_input_timerB"] / 100), 475, anchor="nw", text=rps_game.options_list[rps_game.player_choice], tags="resultstext", fill="black", font=("", 50))
        main_canvas.create_text(sine_between(645, 495, global_timers["player_input_timerB"] / 150), 460, anchor="ne", text="The bot chose: ", tags="resultstext", fill="black", font=("", 15))
        if bot_made_choice in range(3,7):
            main_canvas.create_text(sine_between(695, 495, global_timers["player_input_timerC"] / 100), 475, anchor="ne", text=rps_game.options_list[rps_game.computer_choice], tags="resultstext", fill="black", font=("", 50))

            # win / lose / tie text
            main_canvas.create_text(250, sine_between(-40, 360, global_timers["results_timer"] / 100), anchor="s", text=game_result_text, tags="resultstext", fill="black" if game_result == 2 else "#005500" if game_result == 0 else "#550000", font=("", 80))
            main_canvas.create_text(250, sine_between(-30, 370, global_timers["results_timer"] / 100), anchor="center", text="Press a button to start the next round.", tags="resultstext", fill=("#%02x%02x%02x" % (round(sine_between(153, 0, global_timers["scoreboard_sliding_timer"] / 100)),round(sine_between(153, 0, global_timers["scoreboard_sliding_timer"] / 100)),round(sine_between(153, 0, global_timers["scoreboard_sliding_timer"] / 100)))) if bot_made_choice in [5,6] else "#999999", font=("", 20))

def do_nothing() -> None:
    return None

timer_displayed: bool = False
def display_input_timer(enabled: bool = True):
    global max_player_time
    main_canvas.delete("timerboxes")
    if enabled:
        main_canvas.create_rectangle(10, 10, 490, 30, fill="#333333", outline="black", width=3, tags="timerboxes")
        main_canvas.create_rectangle(491,31,460,55, fill="#222222",outline="black", width=2, tags="timerboxes")
        main_canvas.create_text(475,36,anchor="n", text=f"{round((global_timers['player_input_timerA'] + 50)/100)}", tags="timerboxes")
        if global_timers["player_input_timerA"] > 0:
            main_canvas.create_rectangle(10, 10, 10 + ((global_timers['player_input_timerA'] / max_player_time) * 480), 30, fill="#00ff00", outline="black", width=3, tags="timerboxes")

max_player_time: int = 1000
global_timers = {"player_input_timerA": 1000, "player_input_timerB": 0, "player_input_timerC": 0, "scoreboard_sliding_timer": 0, "bot_timer": 0, "results_timer": 0}
def tick_down_timers():
    global global_timers
    timers = [timer for timer in global_timers]
    countdown_values = [2, 2, 2, 1, 1, 1]
    for index in range(0,len(timers)):
        global_timers[timers[index]] -= countdown_values[index]
        if global_timers[timers[index]] < 0:
            global_timers[timers[index]] = 0

bot_made_choice: int = -1
game_result: int = -1
game_result_text: str = ""
def computer_chooses():
    global bot_made_choice
    global global_timers
    global game_result
    global game_result_text
    global sliding_state
    # bot_made_choice; 0 = in between, 1 = choosing, 2 = choice made, 3 = displaying win/loss text, 4 = display scoreboard, 5 = update scoreboard, 6 = after everything
    if bot_made_choice == 1:
        if global_timers["bot_timer"] == 0:
            if not timed_out:
                rps_game.computer_choice = random.randint(0,2)
                game_result = rps_game.check_winner(rps_game.player_choice, rps_game.computer_choice)
            bot_made_choice = 2
            game_result_text = "You Win!" if game_result == 0 else "You Lose!" if game_result == 1 else "It's a Tie!" if game_result == 2 else "You Took\nToo Long!"
            global_timers["player_input_timerC"] = 100
    if bot_made_choice in range(2,7):
        if bot_made_choice == 2:
            global_timers["results_timer"] = 100
            bot_made_choice = 3
        elif global_timers["results_timer"] == 0 and bot_made_choice < 5:
            bot_made_choice = 4
        if bot_made_choice == 4:
            global_timers["scoreboard_sliding_timer"] = 100
            sliding_state = 0
            bot_made_choice = 5
        elif bot_made_choice == 5 and global_timers["scoreboard_sliding_timer"] < 1:
            rps_game.update_score(game_result)
            bot_made_choice = 6

def reset_for_next_round():
    global timer_displayed
    global sliding_state
    global player_choice_shown
    global global_timers
    global bot_made_choice
    global timed_out
    global max_player_time
    if bot_made_choice in [-1,0,6]:
        main_canvas.delete("startingtext")
        timed_out = False
        create_buttons(enabled=True)
        timer_displayed = True
        print(max_player_time)
        sliding_state = 1
        player_choice_shown = False
        bot_made_choice = 0
        max_player_time = round(max_player_time * 0.9)
        global_timers["player_input_timerA"] = max_player_time

timed_out: bool = False
def on_time_runs_out():
    global game_result
    global bot_made_choice
    global rps_game
    global timer_displayed
    global bot_made_choice
    global player_choice_shown
    global bot_time
    global timed_out

    if global_timers["player_input_timerA"] == 0 and bot_made_choice == 0:
        timed_out = True
        bot_made_choice = 1
        game_result = 3
        rps_game.player_choice = 3
        rps_game.computer_choice = 4
        player_choice_shown = True
        global_timers["player_input_timerB"] = 100
        global_timers["player_input_timerC"] = 150
        timer_displayed = False
        global_timers["bot_timer"] = 100
        create_buttons(False)

# runs every frame, which is 10 ms for ease of use
def tick():
    tick_down_timers()
    display_input_timer(timer_displayed)
    display_score(sliding_state)
    computer_chooses()
    display_results(player_choice_shown)
    on_time_runs_out()

    main_window.after(10,tick)

if __name__ == "__main__":
    rps_game = RPSGame()

    # Create Tkinter window
    main_window = tkinter.Tk()
    main_window.title("RPS Deluxe")
    main_window.geometry("500x700")
    main_canvas = tkinter.Canvas(main_window, width=500, height=700, bg="#999999")
    main_canvas.pack()

    #create buttons and bind them
    create_buttons(enabled=False)
    #display starting text
    main_canvas.create_text(250, 200, text="Welcome to\nRPS Deluxe!", font=("",70), tags="startingtext", fill="black")
    main_canvas.create_text(250, 335, text="Press \"Next\" below to start playing!",justify="center", fill="black", font=("",25), tags="startingtext")
    tick()

    main_window.mainloop()
