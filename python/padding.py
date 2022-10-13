# -----general syntax-----

# ----------left-padding----------
#  string.ljust(width, char)

# ----------right-padding----------
#  string.rjust(width, char)

# ----------center-padding----------
#  string.center(width, char)

left = "left padding"
print(left.ljust(20, '-'))

right = "right padding"
print(right.rjust(20, '*'))

center = "center padding"
print(center.center(20, '#'))