# Design an algorithm to encode a list of strings to a string.
# The encoded string is then sent over the network and
# is decoded back to the original list of strings.

def encode(strs: list[str]) -> str:
    safe = ""
    for str in strs:
        safe += f"{len(str)}#{str}"
    return safe

def decode(safe: str) -> list[str]:
    strs, i = [], 0
    while i < len(safe):
        j = i
        while safe[j] != "#":
            j += 1
        n = int(safe[i:j])
        strs.append(safe[j + 1 : j + n + 1])
        i = n + j + 1
    return strs

print(encode(["Python", "is", "ultrasonicoliio", "aesthetic"]))
print(decode("6#Python2#is15#ultrasonicoliio9#aesthetic"))
