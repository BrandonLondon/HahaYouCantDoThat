from time import sleep

def brr():
    print("r", end = '')
    sleep(0.05)
    brr()

def noYouCantNotDoThat():
    print("Haha Terminal go brr", end = '')
    brr()

def main():
    noYouCantNotDoThat()
    return 1

if __name__ == "__main__":
    main()