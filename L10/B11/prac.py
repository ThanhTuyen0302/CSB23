# De: tao chuc nang forward, backward cho web browser
# su dung 2 stack de luu
# Lop Browser: visit_page, back, forward

class Browser:
    def __init__(self):
        self.current_page = "home"
        self.back_history = []
        self.forward_history = []
        
    def visit_page(self, page_name):
        #luu trang hien tai vao back
        self.back_history.append(self.current_page)
        # thay doi trang hien tai
        self.current_page = page_name
        # xoa trang trong forward
        self.forward_history.clear()
        return f"Visited {self.current_page}"
        
    def back(self):
        if len(self.back_history) == 0: return "No back history"
        # luu trang hien tai vao forward
        self.forward_history.append(self.current_page)
        # quay lai trang truoc
        self.current_page = self.back_history.pop()
        print(f"Back to {self.current_page}")
        
    def forward(self):
        if len(self.forward_history) == 0: return "No forward history"
        # luu trang hien tai vao back
        self.back_history.append(self.current_page)
        # di toi trang tiep theo
        self.current_page = self.forward_history.pop()
        return(f"Forward to {self.current_page}")
         
 
def testdrive():
    # tao obj browser
    browser = Browser()
    functions_table = """ Use number 1,2,3 for functions:
        1. visit_page -> input page name
        2. <- back
        3. -> forward
        4. exit
    """
    request = ""
    while request != "4":
        # hien thi bang chuc nang
        print(functions_table)
        # cho nguoi dung nhap yeu cau
        request = input("Enter your choice: ")
        match request:
            case "1":
                page_name = input("Enter page name: ").strip() # xoa khoang trang
                # khong dien trang
                if not page_name:
                    print("Page name cannot be empty")
                    continue
                # page name dung yeu cau
                print(browser.visit_page(page_name))
            case "2":
                print(browser.back())
            case "3":
                print(browser.forward())
            case "4":
                print("Exiting the program. Goodbye!")
                break
            case _:
                print("Invalid choice, please try again")
                
        # xoa request cu
        request = ""
        
testdrive()
                