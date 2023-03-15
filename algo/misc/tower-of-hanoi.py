def moveDiscs(discs, src, dsn, spare):
    if discs == 1:
        print(f"Move disc from {src} to {dsn}")
        return

    moveDiscs(discs - 1, src, spare, dsn)
    print(f"Move disc from {src} to {dsn}")
    moveDiscs(discs - 1, spare, dsn, src)

def main():
    moveDiscs(3, "A", "C", "B")

if __name__ == "__main__":
    main()
