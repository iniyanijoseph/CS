extends Sprite

onready var player = get_parent().get_node("Hero")
onready var firebar = get_node("FireProgress")
onready var meleebar = get_node("MeleeProgress")

func _process(_delta):
	firebar.value = 100*player.attacklist[0][1] / player.attacklist[0][2]
	meleebar.value = 100*player.attacklist[1][1] / player.attacklist[1][2]
