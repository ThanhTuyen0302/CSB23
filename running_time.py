import time
def running_time(func) -> None:
    print("Bat dau chay ham ----------------")
    start_time = time.time() # lay thoi gian hien tai
    result = func() 
    end_time = time.time()
    print(f"ket qua chay ham: {result}")
    print(f"Thoi gian thuc thi: {(end_time - start_time):.6f} giay")
    print("Ket thuc chay ham ----------------")