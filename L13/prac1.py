# check dau dong ngoac cua bieu thuc

def is_valid_parentheses(s:str):
    danhsach_ngoac = {")": "(", "}": "{", "]": "["}
    mongoac = "({["
    stack_luu_mongoac = []
    
    for ch in s:
        #kiem tra mo ngoac
        if ch in mongoac:
            stack_luu_mongoac.append(ch)
        else:
            #kiem tra ngoac dong
            if not stack_luu_mongoac or stack_luu_mongoac[-1] != danhsach_ngoac.get(ch, None):
                return False
            # neu co ngoac dong -> xoa ngoac mo
            stack_luu_mongoac.pop()
            
    # neu danh sach ngoac mo duoc xoa het
    return len(stack_luu_mongoac) == 0
    
if __name__ == "__main__":
    s = input("Chuoi bieu thuc: ").strip()
    print(f"Bieu thuc dung? {is_valid_parentheses(s)}")
