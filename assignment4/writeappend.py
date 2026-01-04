with open("output.txt", 'wt') as fh:
    line1=str(input("enter text to write to file: "))
    fh.write(line1+"\n")

print("data successfully written to output.txt")

with open("output.txt", 'at') as fh:
    line2=str(input("enter additional text to append: "))
    fh.write(line2+"\n")

print("data appended successfully to output.txt")
print("final content of output.txt:\n")

with open("output.txt", 'rt') as fh:
    for line in fh:
        print(line.strip())
