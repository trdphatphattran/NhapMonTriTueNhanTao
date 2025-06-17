# LAB 2: ARTIFICIAL INTELLIGENCE  
## THỰC HÀNH 6: BÀI TOÁN 4-QUEENS
## Mục tiêu:  
1. Hiểu rõ và mô tả bài toán 4-Queens.
2. Xác định số lượng lời giải hợp lệ.
## Mô tả bài toán:  
Bài toán 4-Queens là phiên bản đơn giản của bài toán N-Queens trong trí tuệ nhân tạo. Mục tiêu là đặt 4 quân hậu (Queens) lên bàn cờ 4x4 sao cho không có 2 quân hậu nào tấn công lẫn nhau.  
Các quân hậu có thể tấn công theo:
- Cùng hàng (ngang)
- Cùng cột (dọc)
- Đường chéo
## Bài tập minh họa:  
![image](https://github.com/user-attachments/assets/ded83901-26fa-4950-b2df-202eae6d7cae)  
Hàm kiểm tra xem trạng thái hiện tại đã chứa đủ số quân hậu hay chưa, nếu đúng thì hợp lệ.  
![image](https://github.com/user-attachments/assets/277cbbdf-12a6-4d5b-ac50-23fb8ede93ae)  
Nếu chưa có quân hậu nào đang đứng sẵn thì mọi cột đều hợp lệ  
![image](https://github.com/user-attachments/assets/66ddb5cd-c404-4d23-86be-3e1f446b93d6)  
position là hàng đang xét, candidates chứa tất cả các cột có thể đặt thử quân hậu.  
![image](https://github.com/user-attachments/assets/c9da02a7-f449-45f2-a31d-d39274639c6d)  
Loại bỏ các cột trùng cột hay đường chéo với con hậu đã đặt trước đó.  
![image](https://github.com/user-attachments/assets/0102fedb-be37-4f66-a15a-f2b399a877c5)  
Khi tìm ra giải pháp thì thêm vào solutions và in ra.  
![image](https://github.com/user-attachments/assets/4191d381-3dd8-44f7-befe-4c528d4d1b10)  
Duyệt từng vị trí hợp lệ, gọi đệ quy để thử tiếp quân hậu tiếp theo, sau đó xóa đi để thử các lựa chọn khác.  
![image](https://github.com/user-attachments/assets/34b2e96a-3894-41fa-99fd-da666db270a7)  
Tạo danh sách rỗng để chứa lời giải.  
![image](https://github.com/user-attachments/assets/87707f85-528d-408f-b248-d596b600c380)  
Nhập số quân hậu và in ra bàn cờ trống.    
![image](https://github.com/user-attachments/assets/80aed7e7-1692-48a6-b8d9-7c350271c5a5)  
Gọi hàm tìm lời giải và in tổng số lời giải.  
![image](https://github.com/user-attachments/assets/bf4200d3-1a64-431a-9a0e-1a9e1476098d)  
Tạo lại bàn cờ với Q là quân hậu, hiển thị thứ tự lời giải, vị trí, bàn cờ.  














