uniqueness = set()
count = 0
# unicode = 17 planes of 2**16 symbols
for codepoint in range(17 * 2 ** 16):
    ch = chr(codepoint)
    if ch.isalpha():
        count += 1
print(count)
