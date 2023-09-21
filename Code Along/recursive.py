def main():
    print("Start of main")
    func_a()
    print("End of main")

def func_a():
    print("Start of func_a")
    func_b()
    print("End of func_a")

def func_b():
    print("Start of func_b")
    print("End of func_b")

main()