# Phân tích và giải pháp 
# Khởi tạo đầu chương trình , có thể truy cập từ bất kỳ đâu nhưng từ khóa là global khi muốn chinh sửa giá trị ở bên trong hàm 
# inventory_stock (Kiểu int): Lưu số lượng hàng hiện tại trong kho
# total_revenue (Kiểu float) : Lưu tổng doanh thu tích lũy của cửa hàng 

# Biến cục bộ (local Variables)
# Chỉ tồn tại bên trong hàm được khai báo
# add_stock(amount): amount tham số 
# calculate_final_price(quantity, price): quantity, price (tham số); subtotal, discount, tax, final_total

inventory_stock = 100
total_revenue = 0.0

def add_stock(amount: int) -> None: 
    """ Cộng thêm số lượng hàng vào kho .

    Args:
        amount (int): Số lượng sản phẩm muốn nhập thêm vào kho hàng .
    """ 
    global inventory_stock 
    inventory_stock += amount
    print(f"Đã nhập thành công {amount} sản phẩm.")
    print(f"Tồn kho hiện tại : {inventory_stock}")
    
def process_sale(quantity: int) -> bool:
    """ Kiểm tra xem số lượng hàng trong khi có đủ để bán hay không .

    Args:
        quantity (int): Số lượng sản phẩm khách hàng muốn mua .

    Returns:
        bool: True nếu đủ hàng , False nếu không đủ hàng .
    """
    global inventory_stock
    if quantity > inventory_stock:
        print(f"Lỗi : Không đủ hàng trong kho. Tồn kho hiện tại chỉ còn {inventory_stock}")        
        return False 
    return True 

def calculate_final_price(quantity: int, price: float):
    """ Tính toán hóa đơn chi tiết bao gồm chiết khấu và thuế VAT.

    Args:
        quantity (int): Số lượng mua (phải >=0)
        price (float): Đơn giá của một sản phẩm (phải>0)
        
    Returns:
        tuple : Trả về một tuple chứa (subtotal,discount,tax,final_total)
    """   
    subtotal = quantity * price
    
    # Tính chiết khấu 
    if subtotal >= 1000:
        discount = subtotal * 0.10 
    else:
        discount = 0.0
        
    # Tính thuế VAT 8% trên giá trị sau chiết khấu 
    tax = (subtotal - discount) * 0.08
    
    # Tổng thanh toán cuối cùng (Đã thụt lề vào trong hàm)
    final_total = subtotal - discount + tax
    
    # Lệnh return phải nằm trong hàm (Đã thụt lề vào trong hàm)
    return subtotal, discount, tax, final_total

def print_report() -> None:
    """In ra báo cáo tổng quan về tình hình kinh doanh của cửa hàng.

    Hàm này truy cập vào hai biến toàn cục 'inventory_stock' và 'total_revenue'
    để hiển thị lượng tồn kho hiện tại cùng tổng doanh thu tích lũy.
    """
    print("--- BÁO CÁO KINH DOANH ---")
    print(f"Tồn kho hiện tại: {inventory_stock} sản phẩm")
    print(f"Tổng doanh thu: ${total_revenue:.1f}")

def main():
    global inventory_stock, total_revenue
    
    # Toàn bộ khối lệnh bên dưới main phải thụt lề vào 1 cấp
    while True:
        print("\n========== TECHSTORE MANAGEMENT SYSTEM ==========")
        print("1. Nhập thêm hàng vào kho")
        print("2. Bán hàng (Tính toán hóa đơn)")
        print("3. Xem báo cáo tổng quan")
        print("4. Thoát chương trình")
        print("=================================================")
        
        choice = input("Chọn chức năng (1-4): ").strip()
        
        if choice == "1":
            print("--- NHẬP HÀNG ---")
            try:
                amount = int(input("Nhập số lượng sản phẩm muốn thêm: "))
                # Bẫy số âm hoặc bằng 0
                if amount <= 0:
                    print("Dữ liệu nhập vào phải lớn hơn 0.")
                    continue
                
                # Gọi hàm xử lý nhập kho
                add_stock(amount)
                
            except ValueError:
                print("Lỗi: Vui lòng nhập vào một số nguyên hợp lệ.")
                
        elif choice == "2":
            print("--- BÁN HÀNG ---")
            try:
                quantity = int(input("Nhập số lượng mua: "))
                if quantity <= 0:
                    print("Dữ liệu nhập vào phải lớn hơn 0.")
                    continue
                
                # Bước 1: Kiểm tra kho hàng
                if not process_sale(quantity):
                    continue  # Quay lại menu chính nếu không đủ hàng
                
                # Nhập đơn giá sau khi đã qua bước kiểm tra kho thành công
                price = float(input("Nhập đơn giá ($): "))
                if price <= 0:
                    print("Dữ liệu nhập vào phải lớn hơn 0.")
                    continue
                
                # Bước 2: Tính toán hóa đơn
                subtotal, discount, tax, final_total = calculate_final_price(quantity, price)
                
                # Bước 3: Hoàn tất giao dịch (Cập nhật biến toàn cục)
                inventory_stock -= quantity
                total_revenue += final_total
                
                # In hóa đơn chi tiết
                print("-> Hóa đơn chi tiết:")
                print(f"Số lượng: {quantity} | Đơn giá: ${price:.1f}")
                print(f"Tạm tính: ${subtotal:.1f}")
                print(f"Giảm giá (10%): ${discount:.1f}")
                print(f"Thuế VAT (8%): ${tax:.1f}")
                print(f"Tổng thanh toán: ${final_total:.1f}")
                print("Đã bán thành công!")
                
            except ValueError:
                print("Lỗi: Nhập sai kiểu dữ liệu. Số lượng phải là số nguyên và đơn giá phải là số.")
                
        elif choice == "3":
            print_report()
            
        elif choice == "4":
            print("Cảm ơn bạn đã sử dụng TechStore Inventory. Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ! Vui lòng chọn từ 1 đến 4.")

# Điểm khởi chạy chương trình
if __name__ == "__main__":
    main()
    
