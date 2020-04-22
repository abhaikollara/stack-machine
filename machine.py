from enum import Enum


class OpCode(Enum):
    INC     = 1
    DEC     = 2
    INCI    = 3
    DECI    = 4
    PUSHI   = 5
    POPR    = 6
    ADD     = 7
    SUB     = 8
    MUL     = 9
    DIV     = 10
    DONE    = 11


class StackMachineError(Exception):
    pass


class Machine:

    def __init__(self, instructions=[]):
        self.ip = -1
        self.acc = 0
        self._stack = []
        self.instructions = instructions

    def load_instructions(self, instructions):
        self.instructions = instructions

    def pop(self):
        try:
            return self._stack.pop()
        except:
            raise StackMachineError(f"Attempted to pop from empty stack")

    def push(self, x):
        self._stack.append(x)

    @property
    def top(self):
        return self._stack[-1]

    def run_op(self, op):
        if op == OpCode.INC:
            self.acc += 1
        elif op == OpCode.DEC:
            self.acc -= 1
        elif op == OpCode.INCI:
            self.ip += 1
            i = self.instructions[self.ip]
            self.acc += i
        elif op == OpCode.DECI:
            self.ip += 1
            i = self.instructions[self.ip]
            self.acc -= i
        elif op == OpCode.PUSHI:
            self.ip += 1
            i = self.instructions[self.ip]
            self.push(i)
        elif op == OpCode.POPR:
            self.acc = self.pop()
        elif op == OpCode.ADD:
            arg1 = self.pop()
            arg2 = self.pop()
            self.push(arg1 + arg2)
        elif op == OpCode.SUB:
            arg1 = self.pop()
            arg2 = self.pop()
            self.push(arg1 - arg2)
        elif op == OpCode.MUL:
            arg1 = self.pop()
            arg2 = self.pop()
            self.push(arg1 * arg2)
        elif op == OpCode.DIV:
            arg1 = self.pop()
            arg2 = self.pop()
            if arg2 == 0:
                raise StackMachineError(f"Division by zero")
            self.push(arg1 // arg2)
        else:
            raise StackMachineError(f"Invalid Opcode: {op}")

    def fetch_ins(self):
        try:
            return self.instructions[self.ip]
        except:
            raise StackMachineError(
                f"Instruction pointer out of range. ip: {self.ip} n_instrs: {len(self.instructions)}")

    def execute(self):
        while True:
            self.ip += 1
            ins = self.fetch_ins()
            if ins == OpCode.DONE:
                break

            self.run_op(ins)

        return self.acc
