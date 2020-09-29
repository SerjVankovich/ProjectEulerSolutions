cubes = []

for i in range(346, 10000):
    cube = i ** 3
    str_cube = str(cube)

    cube_array = sorted([int(x) for x in str_cube])
    str_cube = ''
    for x in cube_array:
        str_cube += str(x)
    cubes.append({'cube': cube, 'cube_str': str_cube})

cubes_str = [x['cube_str'] for x in cubes]
for i in range(len(cubes)):
    if cubes_str.count(cubes[i]['cube_str']) == 5:
        print(cubes[i])