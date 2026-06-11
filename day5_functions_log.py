import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# # Bài 1 – Viết hàm chào

# def chao_ten(name):
#     print(f"Xin chào {name} ! Chào mừng đến với Python SOC.")

# my_name = input("Nhập tên của tôi: ")

# chao_ten(my_name)

# # Bài 2 – Hàm xử lý log đơn giản

# def xu_ly_log(ip, critical):
#     if critical:
#         print(f"IP: {ip} - Mức độ: Nguy hiểm")
#     else:
#         print(f"IP: {ip} - Mức độ: An toàn")

# xu_ly_log("10.0.0.1", True)
# xu_ly_log("192.168.1.1", False)

# # Bài 3 – Hàm có return

# def phan_loai_alert(code):
#     if code >= 500:
#         return("Cảnh báo nghiêm trọng")
#     elif code >= 400:
#         return("Cảnh báo trung bình")
#     else:
#         return("Cảnh báo nhẹ")

# print(phan_loai_alert(501))  # ➜ Cảnh báo nghiêm trọng
# print(phan_loai_alert(403))  # ➜ Cảnh báo trung bình
# print(phan_loai_alert(200))  # ➜ Cảnh báo nhẹ

# Bonus – Phân loại danh sách log theo alert code

def phan_loai_alert(code):
    if code >= 500:
        return("Cảnh báo nghiêm trọng")
    elif code >= 400:
        return("Cảnh báo trung bình")
    else:
        return("Cảnh báo nhẹ")

logs = [
    {"ip": "192.168.1.1", "alert": 501},
    {"ip": "10.0.0.5", "alert": 403},
    {"ip": "8.8.8.8", "alert": 200}
]

for log in logs:
    print(f'IP: {log["ip"]} | Mã cảnh báo: {log["alert"]} | Phân loại: {phan_loai_alert(log["alert"])}')