def getPackets():
    bitString = ""
    for c in open("Day 16 Input.txt").readline().strip():
        bitString += str(bin(int(c, 16)))[2:].zfill(4)

    while "1" in bitString:
        version = int(bitString[0:3],2)
        typeID = int(bitString[3:6],2)
        length = 6
        if typeID == 4:
            group = bitString[length:length+5]
            more = group[0]
            length += 5
            numString = group[1:]
            while more == "1":
                group = bitString[length:length+5]
                more = group[0]
                length += 5
                numString += "".join(group[1:])
            yield version, typeID, length, int(numString,2)
        else:
            lengthID = int(bitString[6])
            length = (18 if lengthID else 22)
            yield version, typeID, length, lengthID, int(bitString[7:length],2)

        bitString = bitString[length:]


def processPacket(packets, depth):
    packet = next(packets)
    indent = "\t" * depth
    output = 0
    typeID, length = packet[1:3]
    if typeID == 4:
        print(indent + "Num: " + str(packet[3]))
        return packet
    else:
        print(indent + "---Operator---")
        sublength = packet[4]
        inputs = []
        while sublength > 0:
            nextPacket = processPacket(packets, depth + 1)
            sublength -= (1 if packet[3] else nextPacket[2])
            length += nextPacket[2]
            inputs.append(nextPacket)
        values = [p[3] for p in inputs]

        if typeID == 0:
            print(indent + "---Sum---")
            output = sum(values)

        elif typeID == 1:
            print(indent + "---Product---")
            output = 1
            for n in values:
                output *= n

        elif typeID == 2:
            print(indent + "---Minimum---")
            output = min(values)

        elif typeID == 3:
            print(indent + "---Maximum---")
            output = max(values)

        elif typeID == 5:
            print(indent + "---Greater Than---")
            output = int(values[0] > values[1])

        elif typeID == 6:
            print(indent + "---Less Than---")
            output = int(values[0] < values[1])

        elif typeID == 7:
            print(indent + "---Equal To---")
            output = int(values[0] == values[1])

    print(indent + "Result: " + str(output))
    print()

    return 0, 4, length, output


processPacket(getPackets(), 0)
