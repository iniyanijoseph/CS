extends Node2D

var score = 0
onready var scoreboard = get_node("Text")

func _process(_delta):
	score = str(score)
	scoreboard.text = score
