import time 
import numpy as np
def main():

    now = time.time() 

    while True:
        start = time.time()
        num = np.random.randint(0,3)
        if num==1:
            print("Check")
        else:
            print(0)
        end = time.time()
        print(f"loop time taken: {end - start}")
        if now - start > 5:
            break


if __name__ == "__main__":
    main()
