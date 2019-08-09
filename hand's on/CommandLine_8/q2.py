import sys, samplepack.mathmod
fname = sys.argv[1]
x = int(sys.argv[2])
y = int(sys.argv[3])

method = getattr(samplepack.mathmod, fname)
print(method(x, y))
