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
### Bài tập minh họa:  
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
Ví dụ: gọi số quân hậu là 4  
![image](https://github.com/user-attachments/assets/126d1fa2-167c-4784-aeb4-1a5bb4246074)  
Chú thích:  
Lời giải 1: [1, 3, 0, 2]  
- Hàng 0 -> Cột 1
- Hàng 1 -> Cột 3
- Hàng 2 -> Côt 0
- Hàng 3 -> Cột 2

Lời giải 2: [2, 0, 3, 1]  
- Hàng 0 -> Cột 2
- Hàng 1 -> Cột 0
- Hàng 2 -> Cột 3
- Hàng 3 -> Cột 1

### In theo tọa độ  
for index, solution in enumerate(solutions, start=1):  
- Duyệt qua từng lời giải trong danh sách solutions  
- solution là danh sách các cột mà quân hậu đã đứng sẵn  
- index là số thứ tự lời giải, bắt đầu là 1  
board = np.full((num_queens, num_queens), "-"): Tạo bảng có kích thước N x N  
coordinates = [(row, col) for row, col in enumerate(solution)]: coordinates chứa danh sách các tọa độ (row, col) của các quân hậu.  
![image](https://github.com/user-attachments/assets/c35eb255-6a64-45c5-9eb8-f976ac62c291)  
In lời giải và tọa độ các quân hậu  
![image](https://github.com/user-attachments/assets/a7e150bd-db8b-4bcc-a466-911ef7cf42df)  

Đặt kí hiệu 'Q' vào vị trí với tọa độ quân hậu và in ra bàn cờ.  
Ví dụ: có 4 quân hậu  
![image](https://github.com/user-attachments/assets/4b825ac8-5ba2-48f2-99e5-110d7564d3ff)  


## Thực hành 7: Bài toán 8-Queens  
Tương tự bài toán 4-Queens, nhưng bàn cờ được mở rộng lên 8x8 và cần đặt 8 quân hậu sao cho không quân nào tấn công nhau.  
### Bài tập minh họa  
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
![image](https://github.com/user-attachments/assets/cd64edb3-eb1f-410f-af6d-08b85d2305ca)  
Nhập số lượng quân hậu, biến i = 0 dùng để đánh số thứ tự lời giải  
![image](https://github.com/user-attachments/assets/700518d6-97b8-4a1c-b01e-cb392413770b)  
Vòng lặp:  
- Duyệt từng solution trong danh sách lời giải  
- Tạo một bảng N x N  
![image](https://github.com/user-attachments/assets/8e1878ab-a08b-4ab0-9b2f-623d34c4ae37)  

Đặt quân hậu vào bảng và in ra kết quả  
Ví dụ: gọi số quân hậu là 8  
![image](https://github.com/user-attachments/assets/34796019-b29d-4688-84f5-12a86a8bd441)  
Chúng ta sẽ có tổng cộng 92 lời giải tìm được. Ví dụ giải thích 1 lời giải:  
[0, 4, 7, 5, 2, 6, 1, 3]  
Hàng 0 -> Cột 0  
Hàng 1 -> Cột 4  
Hàng 2 -> Cột 7  
Hàng 3 -> Cột 5  
Hàng 4 -> Cột 2  
Hàng 5 -> Cột 6  
Hàng 6 -> Cột 1  
Hàng 7 -> Cột 3  

### In theo tọa độ  
for index, solution in enumerate(solutions, start=1):  
- Duyệt qua từng lời giải trong danh sách solutions  
- solution là danh sách các cột mà quân hậu đã đứng sẵn  
- index là số thứ tự lời giải, bắt đầu là 1  
board = np.full((num_queens, num_queens), "-"): Tạo bảng có kích thước N x N  
coordinates = [(row, col) for row, col in enumerate(solution)]: coordinates chứa danh sách các tọa độ (row, col) của các quân hậu.  
![image](https://github.com/user-attachments/assets/c35eb255-6a64-45c5-9eb8-f976ac62c291)  
In lời giải và tọa độ các quân hậu  
![image](https://github.com/user-attachments/assets/a7e150bd-db8b-4bcc-a466-911ef7cf42df)  

Đặt kí hiệu 'Q' vào vị trí với tọa độ quân hậu và in ra bàn cờ.  
Ví dụ: có 8 quân hậu  
![image](https://github.com/user-attachments/assets/15e32074-0fba-4a3c-a6f3-0abe92618f5b)  































