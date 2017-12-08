"""
Day 8: I Heard You Like Registers
"""


def is_condition_valid(registers, cond_reg, cond, cond_val):
    reg_value = registers[cond_reg] if cond_reg in registers else 0
    cond_val = int(cond_val)
    if cond == '>':
        return reg_value > cond_val
    elif cond == '<':
        return reg_value < cond_val
    elif cond == '>=':
        return reg_value >= cond_val
    elif cond == '<=':
        return reg_value <= cond_val
    elif cond == '==':
        return reg_value == cond_val
    elif cond == '!=':
        return reg_value != cond_val
    return False


def main():
    data = open('input.txt', 'r').readlines()
    registers = {}
    max_reg = 0

    for line in data:
        info = line.split()
        reg = info[0]
        inc = info[1] == 'inc'
        inc_val = int(info[2])
        cond_reg = info[4]
        cond = info[5]
        cond_val = int(info[6])

        if is_condition_valid(registers, cond_reg, cond, cond_val):
            prev_val = registers[reg] if reg in registers else 0
            prev_val = prev_val + inc_val if inc else prev_val - inc_val
            registers[reg] = prev_val

        max_reg = max(list(registers.values()) + [max_reg])
    print("max register: ", max_reg)


if __name__ == '__main__':
    main()
