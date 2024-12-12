import fsl

f = open("../tests/example.fsl", "r")

structure = fsl.parse(f.read())