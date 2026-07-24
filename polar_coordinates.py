# polar_coordinates.py

import cmath

if __name__ == "__main__":
    # input of z
    z = complex(input().strip())

    # modulas
    print(abs(z))

    print(cmath.phase(z))

