import csv
import sys
sys.sdount.reconfigure(encoding='utf-8')

def process_csv(file_path):
    unique_eamils = set()
    company_count = {}
    
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        # cat tung dong
        for row in reader:
            # kiem tra so luong cot (3)
            if len(row) != 3:
                continue # bo qua neu sai dinh dang
            name, comp, email = row
            # xoa khoang trang
            email = email.strip()
            comp = comp.strip()
            # kiem tra email da ton tai
            if email not in unique_eamils:
                unique_eamils.add(email)
                # cap nhat so luong dai bieu cua cong ty
                if comp in company_count:
                    company_count[comp] += 1
                else:
                    company_count[comp] = 1
                    
        # sap xep cong ty theo so luong dai bieu giam dan
        sorted_companies = sorted(
            company_count.items(), key=(lambda item: item[1]), reverse = True
        )
    
        # in ket qua
        print(f"Số lượng đại biểu dự kiến tham dự: {len(unique_eamils)}")
        print("Danh sách công ty và số lượng đại biểu:")
        for company, count in sorted_companies:
            print(f"{company}: {count}")
            
           
process_csv("L10/data.csv") 
