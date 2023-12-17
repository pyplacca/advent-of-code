from utils import get_bounds

gondola = open("./sample.txt", "r").read().splitlines()

part_numbers = 0
i = 0

while i < len(gondola):
    row = gondola[i]
    row_length = len(row)
    j = 0
    num = ""

    while j < row_length:
        cell = row[j]

        if str.isdigit(cell):
            num += cell
            k = j + 1

            while k < row_length:
                if str.isdigit(row[k]):
                    num += row[k]
                else:
                    k -= 1
                    break
                k += 1

            if num:
                bounding_elements = get_bounds(gondola, i, j, k)["elements"]
                # print(f"{i=}, {j=}, {k=}", num, bounding_elements)
                if len(bounding_elements.replace(".", "")):
                    part_numbers += int(num)

            j = k
            num = ""
        j += 1
    i += 1

print(f"Part 1: {part_numbers=}")
