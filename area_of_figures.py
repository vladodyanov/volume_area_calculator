type_of_the_figure = input(
        "Please select type of the figure: square [S], rectangle [R], circle [C], triangle [T] or exit [E]: ")
while type_of_the_figure != 'E':
    import math
    perimeter_or_area = input("Please select area [A] or perimeter [P]: ")
    perimeter = 0
    area = 0
    if perimeter_or_area == 'A':
        if type_of_the_figure == "S":
            a = float(input('Please enter the side [cm] of the square: '))
            area = a * a
        elif type_of_the_figure == "C":
            radius = float(input('Please enter the radius [cm] of the circle: '))
            area = math.pi * radius * radius
        elif type_of_the_figure == "R":
            a = float(input('Please enter  side "a" [cm] of the rectangular: '))
            b = float(input('Please enter  side "b" [cm] of the rectangular: '))
            area = a * b
        elif type_of_the_figure == "T":
            a = float(input('Please enter the side [cm] of the triangle: '))
            ha = float(input('Please enter the height to the side [cm] of the triangle: '))
            area = a * ha / 2
        else:
            print('Please enter valid figure !')

        print (f'The area of the selected figure is {area:.3f}cm2')

    elif perimeter_or_area == 'P':
        if type_of_the_figure == "S":
            a = float(input('Please enter the side [cm] of the square: '))
            perimeter = 4 * a
        elif type_of_the_figure == "C":
            radius = float(input('Please enter the radius [cm] of the circle: '))
            perimeter = 2 * math.pi * radius
        elif type_of_the_figure == "R":
            a = float(input('Please enter  side "a" [cm] of the rectangular: '))
            b = float(input('Please enter  side "b" [cm] of the rectangular: '))
            perimeter = 2*a + 2*b
        elif type_of_the_figure == "T":
            a = float(input('Please enter the side "a" [cm] of the triangle: '))
            b = float(input('Please enter the side "b" [cm] of the triangle: '))
            c = float(input('Please enter the side "c" [cm] of the triangle: '))
            perimeter = a + b + c
        else:
            print('Please enter valid figure !')
            continue


        print(f'The perimeter of the selected figure is {perimeter:.3f}cm')
    else:
        print('Please select valid operation !')
        break

    type_of_the_figure = input(
        "Please select type of the figure: square [S], rectangle [R], circle [C], triangle [T] or exit [E]: ")

print('Thanks for using my Volume and Area for figures calculator !')




