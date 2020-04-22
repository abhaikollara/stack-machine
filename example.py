from machine import Machine
from machine import OpCode as Op


# 1 + 2 * 3

instructions = [
    Op.PUSHI, 1,
    Op.PUSHI, 2,
    Op.PUSHI, 3,
    Op.MUL,
    Op.ADD,
    Op.POPR,
    Op.DONE]

m = Machine()
m.load_instructions(instructions)
m.execute()

print(m.acc)
