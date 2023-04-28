def get_coordinate(s):
    v = int(input(s))
    if 1 <= v <= 8:
        return v
    exit()


print('White Bishop 1: ')
wb1X = get_coordinate(f'{"Row: ":>7}')
wb1Y = get_coordinate(f'{"Col: ":>7}')

print('White Bishop 2: ')
wb2X = get_coordinate(f'{"Row: ":>7}')
wb2Y = get_coordinate(f'{"Col: ":>7}')

print('Black Bishop 1: ')
bb1X = get_coordinate(f'{"Row: ":>7}')
bb1Y = get_coordinate(f'{"Col: ":>7}')

print('Black Bishop 2: ')
bb2X = get_coordinate(f'{"Row: ":>7}')
bb2Y = get_coordinate(f'{"Col: ":>7}')

# White Bishops
if abs(wb1X - wb2X) == abs(wb1Y - wb2Y):
    print("White Bishops are defending each other")


# Black Bishops
if abs(bb1X - bb2X) == abs(bb1Y - bb2Y):
    print("Black Bishops are defending each other")

# White Bishop 1 and Black Bishop 1
if abs(wb1X - bb1X) == abs(wb1Y - bb1Y):
    print("White Bishop 1 and Black Bishop 1 are attacking each other")


# White Bishop 1 and Black Bishop 2
if abs(wb1X - bb2X) == abs(wb1Y - bb2Y):
    print("White Bishop 1 and Black Bishop 2 are attacking each other")


# White Bishop 2 and Black Bishop 1
if abs(wb2X - bb1X) == abs(wb2Y - bb1Y):
    print("White Bishop 2 and Black Bishop 1 are attacking each other")


# White Bishop 2 and Black Bishop 2
if abs(wb2X - bb2X) == abs(wb2Y - bb2Y):
    print("White Bishop 2 and Black Bishop 2 are attacking each other")
