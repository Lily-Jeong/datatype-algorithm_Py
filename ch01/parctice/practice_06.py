def printReverse(msg, len):
    # 구현할 부분.
    if len > 0:
        print(msg[len-1])
        printReverse(msg, len-1)


instr = "자료구조"
printReverse(instr, len(instr))