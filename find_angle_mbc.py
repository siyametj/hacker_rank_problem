# find_angle_mbc.py

if __name__ == "__main__":
    import math

    ab = int(input().strip())
    bc = int(input().strip())

    angle = round(math.degrees(math.atan2(ab, bc)))
    print(f"{angle}{chr(176)}")