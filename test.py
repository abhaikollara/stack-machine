from machine import Machine
from machine import OpCode as Op


instructions = [
    Op.PUSHI, 1,
    Op.PUSHI, 2,
    Op.PUSHI, 3,
    Op.ADD,
    Op.SUB,
    Op.POPR,
    Op.DONE]

m = Machine(instructions)
m.execute()

print(m.acc)
