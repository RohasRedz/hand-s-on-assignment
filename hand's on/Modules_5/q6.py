def triangleType(n1, n2, n3):
    if n1 == n2 == n3:
        return "Equilateral Triangle"
    elif n1 == n2 or n2 == n3 or n1 == n3:
        return "Isoceles Triangle"
    else:
        return "Triangle"

if __name__ == "__main__":
    print(triangleType(5, 5, 5))