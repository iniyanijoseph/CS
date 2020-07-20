extends Node2D

onready var ingredient = preload("res://Ingredient.tscn")
var node
var countdown = 0


func _process(_delta):
	if countdown <= 0:
		node = ingredient.instance()
		get_parent().add_child(node)
		countdown = 100
	countdown -= 1
