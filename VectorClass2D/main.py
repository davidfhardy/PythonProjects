from Vector2D import Vector2D

vector1 = Vector2D(1,2)
vector2 = Vector2D(3,4)

print("Vector 1 = {}".format(vector1.components()))
print("Vector 2 = {}".format(vector2.components()))
print("Vector 1 Normalized = {}".format(vector1.normalize().components()))
print("Vector 1 Magnitude = {}".format(vector1.magnitude()))
print("Vector 1 Argument = {} deg.".format(vector1.argument()))
print("Vector 1 in Polar = {}".format(vector1.polar()))
print("Vector 1 Negated = {}".format(vector1.negation().components()))
print("Vector 1 + Vector 2 = {}".format(vector1.add(vector2).components()))
print("Vector 1 - Vector 2 = {}".format(vector1.subtract(vector2).components()))
print("Vector 1 . Vector 2 = {}".format(vector1.dot(vector2)))
print("Projection of Vector 1 on 2 = {}".format(vector1.project(vector2).components()))
print("Projection of Vector 2 on 1 = {}".format(vector2.project(vector1).components()))