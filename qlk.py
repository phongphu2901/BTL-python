import os

# Tên file lưu trữ
FILE_NAME = 'kho_hang.txt'

kho_hang = {}

# CÁC HÀM TIỆN ÍCH (NHẬP/XUẤT & KIỂM TRA DỮ LIỆU)

def nhap_chuoi(prompt, bat_buoc=True):
    while True:
        val = input(prompt).strip()
        if not val and bat_buoc:
            print("Lỗi: Thông tin này không được bỏ trống!")
        else:
            return val

def nhap_so(prompt, kieu='int', cho_phep_am=False):
    while True:
        val = input(prompt).strip()
        if not val:
            print("Lỗi: Không được bỏ trống!")
            continue
        try:
            if kieu == 'int':
                num = int(val)
            else:
                num = float(val)
                
            if not cho_phep_am and num < 0:
                print("Lỗi: Giá trị phải lớn hơn hoặc bằng 0!")
            else:
                return num
        except ValueError:
            print(f"Lỗi: Vui lòng nhập đúng định dạng số {'nguyên' if kieu == 'int' else 'thực'}!")

def hien_thi_1_sp(ma_sp, sp):
    print(f"| {ma_sp:<8} | {sp['ten']:<20} | {sp['nhom']:<15} | {sp['sl_ton']:<8} | {sp['muc_min']:<8} | {sp['gia_nhap']:<12.0f} | {sp['gia_ban']:<12.0f} | {sp['trang_thai']:<12} |")

def in_tieu_de_bang():
    print("-" * 115)
    print(f"| {'Mã SP':<8} | {'Tên sản phẩm':<20} | {'Nhóm SP':<15} | {'SL Tồn':<8} | {'Mức Min':<8} | {'Giá Nhập':<12} | {'Giá Bán':<12} | {'Trạng thái':<12} |")
    print("-" * 115)

# CÁC HÀM CHỨC NĂNG CHÍNH 

def them_san_pham():
    print("\n--- THÊM SẢN PHẨM MỚI ---")
    ma_sp = nhap_chuoi("Nhập mã sản phẩm: ")
    if ma_sp in kho_hang:
        print("Lỗi: Mã sản phẩm đã tồn tại!")
        return

    ten = nhap_chuoi("Nhập tên sản phẩm: ")
    nhom = nhap_chuoi("Nhập nhóm sản phẩm: ")
    don_vi = nhap_chuoi("Nhập đơn vị tính: ")
    ncc = nhap_chuoi("Nhập nhà cung cấp: ")
    gia_nhap = nhap_so("Nhập giá nhập: ", kieu='float')
    gia_ban = nhap_so("Nhập giá bán: ", kieu='float')
    sl_ton = nhap_so("Nhập số lượng tồn: ", kieu='int')
    muc_min = nhap_so("Nhập mức tồn tối thiểu: ", kieu='int')
    trang_thai = nhap_chuoi("Nhập trạng thái (Còn hàng/Hết hàng/Ngừng KD): ")

    kho_hang[ma_sp] = {
        'ten': ten, 'nhom': nhom, 'don_vi': don_vi, 'ncc': ncc,
        'gia_nhap': gia_nhap, 'gia_ban': gia_ban, 
        'sl_ton': sl_ton, 'muc_min': muc_min, 'trang_thai': trang_thai
    }
    print("Thêm sản phẩm thành công!")

def hien_thi_danh_sach():
    print("\n--- DANH SÁCH SẢN PHẨM TRONG KHO ---")
    if not kho_hang:
        print("Kho hàng đang trống!")
        return
    in_tieu_de_bang()
    for ma_sp, sp in kho_hang.items():
        hien_thi_1_sp(ma_sp, sp)
    print("-" * 115)

def cap_nhat_san_pham():
    print("\n--- CẬP NHẬT THÔNG TIN SẢN PHẨM ---")
    ma_sp = nhap_chuoi("Nhập mã sản phẩm cần cập nhật: ")
    if ma_sp not in kho_hang:
        print("Lỗi: Không tìm thấy sản phẩm này!")
        return

    print("Nhập thông tin mới (Nhấn Enter để giữ nguyên giá trị cũ):")
    sp = kho_hang[ma_sp]
    
    ten = input(f"Tên SP [{sp['ten']}]: ").strip()
    if ten: sp['ten'] = ten
        
    nhom = input(f"Nhóm SP [{sp['nhom']}]: ").strip()
    if nhom: sp['nhom'] = nhom
        
    sl_ton_str = input(f"Số lượng tồn [{sp['sl_ton']}]: ").strip()
    if sl_ton_str: 
        try: 
            val = int(sl_ton_str)
            if val >= 0: sp['sl_ton'] = val
            else: print("Giá trị không hợp lệ, giữ nguyên cũ.")
        except: print("Lỗi định dạng, giữ nguyên cũ.")

    print("Cập nhật thành công!")

def xoa_san_pham():
    print("\n--- XÓA SẢN PHẨM ---")
    ma_sp = nhap_chuoi("Nhập mã sản phẩm cần xóa: ")
    if ma_sp not in kho_hang:
        print("Lỗi: Không tìm thấy sản phẩm này!")
        return
        
    xac_nhan = nhap_chuoi(f"Bạn có chắc chắn muốn xóa SP '{kho_hang[ma_sp]['ten']}'? (Y/N): ").upper()
    if xac_nhan == 'Y':
        
        print("Đã xóa sản phẩm thành công!")
    else:
        print("Đã hủy thao tác xóa.")

def tim_kiem():
    print("\n--- TÌM KIẾM SẢN PHẨM ---")
    print("1. Theo mã sản phẩm")
    print("2. Theo tên sản phẩm")
    print("3. Theo nhóm sản phẩm")
    chon = nhap_chuoi("Chọn tiêu chí tìm kiếm (1-3): ")
    
    tu_khoa = nhap_chuoi("Nhập từ khóa tìm kiếm: ").lower()
    ket_qua = {}
    
    for ma, sp in kho_hang.items():
        if chon == '1' and tu_khoa in ma.lower():
            ket_qua[ma] = sp
        elif chon == '2' and tu_khoa in sp['ten'].lower():
            ket_qua[ma] = sp
        elif chon == '3' and tu_khoa in sp['nhom'].lower():
            ket_qua[ma] = sp

    if not ket_qua:
        print("Không tìm thấy sản phẩm nào phù hợp!")
    else:
        in_tieu_de_bang()
        for ma, sp in ket_qua.items():
            hien_thi_1_sp(ma, sp)
        print("-" * 115)

def sap_xep():
    print("\n--- SẮP XẾP SẢN PHẨM ---")
    print("1. Theo tên sản phẩm")
    print("2. Theo số lượng tồn")
    tieu_chi = nhap_chuoi("Chọn tiêu chí (1-2): ")
    thu_tu = nhap_chuoi("Sắp xếp tăng dần (T) hay giảm dần (G)? ").upper()
    
    reverse_sort = True if thu_tu == 'G' else False
    
    if tieu_chi == '1':
        sorted_items = sorted(kho_hang.items(), key=lambda x: x[1]['ten'].lower(), reverse=reverse_sort)
    elif tieu_chi == '2':
        sorted_items = sorted(kho_hang.items(), key=lambda x: x[1]['sl_ton'], reverse=reverse_sort)
    else:
        print("Lựa chọn không hợp lệ!")
        return

    in_tieu_de_bang()
    for ma, sp in sorted_items:
        hien_thi_1_sp(ma, sp)
    print("-" * 115)

def thong_ke_va_giao_dich():
    print("\n--- TÍNH TOÁN & THỐNG KÊ ---")
    print("1. Nhập thêm hàng")
    print("2. Xuất hàng")
    print("3. Báo cáo thống kê kho")
    chon = nhap_chuoi("Chọn thao tác (1-3): ")
    
    if chon == '1' or chon == '2':
        ma_sp = nhap_chuoi("Nhập mã sản phẩm: ")
        if ma_sp not in kho_hang:
            print("Lỗi: Sản phẩm không tồn tại!")
            return
            
        sl = nhap_so("Nhập số lượng giao dịch: ", kieu='int')
        if chon == '1':
            kho_hang[ma_sp]['sl_ton'] += sl
            print(f"Nhập hàng thành công! Tồn kho mới: {kho_hang[ma_sp]['sl_ton']}")
        else:
            if kho_hang[ma_sp]['sl_ton'] < sl:
                print(f"Lỗi: Số lượng tồn không đủ! (Chỉ còn {kho_hang[ma_sp]['sl_ton']})")
            else:
                kho_hang[ma_sp]['sl_ton'] -= sl
                print(f"Xuất hàng thành công! Tồn kho mới: {kho_hang[ma_sp]['sl_ton']}")
                
    elif chon == '3':
        tong_sl = 0
        tong_gia_tri = 0
        duoi_muc_min = []
        
        for ma, sp in kho_hang.items():
            tong_sl += sp['sl_ton']
            tong_gia_tri += (sp['sl_ton'] * sp['gia_nhap'])
            if sp['sl_ton'] < sp['muc_min']:
                duoi_muc_min.append((ma, sp))
                
        print(f"\nTổng số lượng sản phẩm trong kho: {tong_sl}")
        print(f"Tổng giá trị tồn kho: {tong_gia_tri:,.0f} VNĐ")
        
        print("\nDANH SÁCH SẢN PHẨM DƯỚI MỨC TỒN TỐI THIỂU CẦN NHẬP THÊM:")
        if not duoi_muc_min:
            print("Không có sản phẩm nào thiếu hụt.")
        else:
            in_tieu_de_bang()
            for ma, sp in duoi_muc_min:
                hien_thi_1_sp(ma, sp)
            print("-" * 115)

def luu_file():
    try:
        with open(FILE_NAME, 'w', encoding='utf-8') as f:
            for ma, sp in kho_hang.items():
                line = f"{ma}|{sp['ten']}|{sp['nhom']}|{sp['don_vi']}|{sp['ncc']}|{sp['gia_nhap']}|{sp['gia_ban']}|{sp['sl_ton']}|{sp['muc_min']}|{sp['trang_thai']}\n"
                f.write(line)
        print("Lưu dữ liệu xuống file thành công!")
    except Exception as e:
        print(f"Lỗi khi ghi file: {e}")

def doc_file():
    if not os.path.exists(FILE_NAME):
        print("Thông báo: Không tìm thấy file dữ liệu hoặc file chưa được tạo.")
        return
        
    try:
        kho_hang.clear()
        with open(FILE_NAME, 'r', encoding='utf-8') as f:
            for line in f:
                parts = line.strip().split('|')
                if len(parts) == 10:
                    ma_sp, ten, nhom, don_vi, ncc, gn, gb, sl, mmin, tt = parts
                    kho_hang[ma_sp] = {
                        'ten': ten, 'nhom': nhom, 'don_vi': don_vi, 'ncc': ncc,
                        'gia_nhap': float(gn), 'gia_ban': float(gb), 
                        'sl_ton': int(sl), 'muc_min': int(mmin), 'trang_thai': tt
                    }
        print("Đọc dữ liệu từ file thành công!")
    except Exception as e:
        print(f"Lỗi khi đọc file (Sai định dạng dữ liệu): {e}")

#HÀM ĐIỀU KHIỂN CHÍNH 

def main():
    # Khởi động đọc dữ liệu ngay lập tức
    doc_file()

    while True:
        print("\n" + "="*40)
        print(" CHƯƠNG TRÌNH QUẢN LÝ NHẬP XUẤT TỒN KHO")
        print("="*40)
        print("1. Thêm bản ghi mới")
        print("2. Hiển thị danh sách")
        print("3. Cập nhật thông tin")
        print("4. Xóa bản ghi")
        print("5. Tìm kiếm")
        print("6. Sắp xếp")
        print("7. Tính toán / Thống kê / Nhập Xuất")
        print("8. Lưu dữ liệu")
        print("9. Đọc dữ liệu")
        print("0. Thoát")
        print("="*40)
        
        chon = input("Nhập lựa chọn của bạn: ").strip()
        
        if chon == '1': them_san_pham()
        elif chon == '2': hien_thi_danh_sach()
        elif chon == '3': cap_nhat_san_pham()
        elif chon == '4': xoa_san_pham()
        elif chon == '5': tim_kiem()
        elif chon == '6': sap_xep()
        elif chon == '7': thong_ke_va_giao_dich()
        elif chon == '8': luu_file()
        elif chon == '9': doc_file()
        elif chon == '0':
            print("Cảm ơn bạn đã sử dụng chương trình!")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng nhập từ 0-9!")

if __name__ == "__main__":
    main()