extends Node2D

onready var ingredient = preload("res://Ingredient.tscn")
var node
var countdown = 0
var speed = 1

func _process(_delta):
	if countdown <= 0:
		node = ingredient.instance()
		node.speed = 1
		get_parent().add_child(node)
		countdown = 100
		speed += 1
	countdown -= 1
