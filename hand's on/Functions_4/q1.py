import math

def trig():
    n = float(input("Enter any float input (this will be in radians): "))
    print("Sine of {} is {}".format(n, math.sin(n)))
    print("Cosine of {} is {}".format(n, math.cos(n)))
    print("Tangent of {} is {}".format(n, math.tan(n)))
    print("HyperbolicSine of {} is {}".format(n, math.sinh(n)))
    print("HyperbolicCosine of {} is {}".format(n, math.cosh(n)))
    print("HyperbolicTangent of {} is {}".format(n, math.tanh(n)))

if __name__ == "__main__":
    trig()
