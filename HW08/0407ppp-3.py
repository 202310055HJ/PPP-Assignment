def f2c(tf):
    temp_c = (tf - 32)/1.8
    return temp_c

def c2f(tc):
    return tc * 1.8 + 32

def main():
    print(f2c(80))
    print(c2f(26.67))

if __name__=="__main__":
    main()
