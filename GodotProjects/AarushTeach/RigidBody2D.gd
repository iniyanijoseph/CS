extends RigidBody2D

func _ready():
	apply_central_impulse(Vector2(1000, 1000))
