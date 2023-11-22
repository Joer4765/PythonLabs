import Vector


def main():

    vector = Vector.Vector

    """ Float Vector """

    v1 = vector(3, 1.0)
    v2 = vector(4, 2.0)

    # Testing methods

    print("v1:", end=" ")
    v1.print_elements()

    print("v2:", end=" ")
    v2.print_elements()

    v1.set_value(3.0)
    print("v1 after setting value to 3.0:", end=" ")
    v1.print_elements()

    print("Number of vectors:", vector.get_num_vectors())

    # Testing attributes

    print("Size of v1:", v1.size)
    print("Size of v2:", v2.size)

    print("CodeError of v1:", v1.code_error)
    print("CodeError of v2:", v2.code_error)

    # Testing indexation

    print("v1[0]:", v1[0])
    print("v1[3]:", v1[3])
    print("CodeError of v1 after accessing out-of-bounds index:", v1.code_error)

    # Testing unary operations

    print("v1 is True:", end=" ")
    print(not v1)

    # Testing binary operations

    print("v1 + v2:", end=" ")
    (v1 + v2).print_elements()

    print("v1 - v2:", end=" ")
    (v1 - v2).print_elements()

    print("v1 * v2:", end=" ")
    (v1 * v2).print_elements()

    print("v1 / v2:", end=" ")
    (v1 / v2).print_elements()

    print("v1 % v2:", end=" ")
    (v1 % v2).print_elements()

    print("v1 == v2:", end=" ")
    print(v1 == v2)

    print("v1 != v2:", end=" ")
    print(v1 != v2)

    print("v1 > v2:", end=" ")
    print(v1 > v2)

    print("v1 >= v2:", end=" ")
    print(v1 >= v2)

    print("v1 < v2:", end=" ")
    print(v1 < v2)

    print("v1 <= v2:", end=" ")
    print(v1 <= v2)


if __name__ == "__main__":
    main()
