print("Christmas comes early with python")

h = 1    # Head
i = 1    # Body
k = 20   # Spacing
s = 1    # Stem
r = 1    # Root

# Head
print(20 * " " + h * "⭐" )

# Body section     
while i < 20 and k > 1:
    print(k * " " + i * "*" + i * "*" )
    i += 1
    k -= 1

# Stem section
if i == 20 and k == 1 :
    while s < 3:
        print(19 * " " + 3 * "*" + 2 * "*")
        s += 1
# Root / Base section
    while r < 3:
        print(12 * " " + 9 * "*" + 10 * "*")
        r += 1
