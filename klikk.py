import area.dream_zan
import loadGame
import logs
import memory.main
import reset
import targetPathing
import vars
import xbox

game_vars = vars.vars_handle()
game_vars.set_start_vars()

memory.main.start()
# Plug in controller
FFXC = xbox.controller_handle()

area.dream_zan.new_game("Klikk testing")
loadGame.load_save_num(101)
memory.main.await_control()
while memory.main.user_control():
    targetPathing.set_movement([0, 0])
    if memory.main.get_coords()[0] > -40:
        xbox.tap_b()
area.baaj.Klikk_fight()

reset.mid_run_reset(land_run=False, start_time=logs.time_stamp())
