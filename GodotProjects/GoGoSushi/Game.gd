extends Node2D

onready var ingredient = preload("res://Spawner.tscn")
var node
var countdown = 0


func _process(_delta):
	if countdown <= 0:
		node = ingredient.instance()
		add_child(node)
		countdown = 3000
	countdown -= 1
