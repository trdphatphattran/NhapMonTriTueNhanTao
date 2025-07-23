# THỰC HÀNH: REINFORCEMENT LEARNING - ĐƯỜNG ĐI MÊ CUNG & DẠNG LƯỚI 6X6  
## Thông tin  
- Sinh viên: Trần Đại Phát
- MSSV: 2374802010379
- Môn học: Nhập môn Xử lý ảnh số
- GVHD: Đỗ Hữu Quân
- Năm học: 2024 - 2025
## Thuật toán Reinforcement Learning là gì?  
Thuật toán Reinforcement Learning (học tăng cường) là một nhánh của học máy mà trong đó có một tác nhân học cách tối ưu hành vi thông qua thử-sai trong một môi trường nhằm tối đa hóa phần thưởng tích lũy.  
## Nguyên lý hoạt động  
1. Agent quan sát trạng thái hiện tại của môi trường.
2. Agent chọn một hành động để thực hiện.
3. Môi trường phản hồi lại với:
- Trạng thái mới.
- Phần thưởng.
4. Agent cập nhật chính sách dựa trên phần thưởng nhận đươc.
5. Quá trình lặp lại để học ra quá trình tối ưu.

## Các ví dụ  
### Thực hành 20  
#### Code chính:
<img width="455" height="240" alt="image" src="https://github.com/user-attachments/assets/34be6922-59ca-42ca-a27b-b2a90de14e34" />  

- Đây là đoạn code đi sâu vào mê cung (theo một nhánh) cho đến khi tìm thấy đích hoặc hết đường.  
- Thu thập ngược đường đi thành công qua path.append(current) theo thứ tự ngược (từ đích trở về gốc).  
- Tránh lặp lại nhờ visited.
- Sinh ra các bước đi kế tiếp nhờ vào moves (lên, xuống, trái, phải).
- Với mỗi ô lân cận và hợp lệ chưa thăm, đệ quy gọi lại DFS.
- Nếu từ ô đó dẫn đến đích được, thì thêm vào current vào path và trả về True.
- Khi tất cả hướng đều không trả về đích -> False.

### Thực hành 21
#### Code chính:  
<img width="449" height="240" alt="image" src="https://github.com/user-attachments/assets/ebddb162-5a94-4525-80d9-00d765f6d108" />  

- Đây là đoạn code đi sâu vào mê cung (theo một nhánh) cho đến khi tìm thấy đích hoặc hết đường.   
- Thu thập ngược đường đi thành công qua path.append(current) theo thứ tự ngược (từ đích trở về gốc).  
- Tránh lặp lại nhờ visited.  
- Sinh ra các bước đi kế tiếp nhờ vào moves (lên, xuống, trái, phải).  
- Với mỗi ô lân cận và hợp lệ chưa thăm, đệ quy gọi lại DFS.  
- Nếu từ ô đó dẫn đến đích được, thì thêm vào current vào path và trả về True.  
- Khi tất cả hướng đều không trả về đích -> False.

### Thực hành 22  
#### Code chính:  
<img width="582" height="334" alt="image" src="https://github.com/user-attachments/assets/e5623e9a-9568-4f25-93dc-173a599b6361" />  

- Khởi tạo: dùng hàng đợi queue để lưu các vị trí cần kiểm tra và đường đi tương ứng, visited tập hợp các vị trí đã đi qua, tránh lặp lại.

Duyệt BFS:  
- Lấy một điểm current từ hàng đợi và kiểm tra.
- Nếu là đích thì trả về đường đi.
- Nếu không thì tính các điểm có thể đi tiếp từ current.
- Kiểm tra nếu next_position hợp lệ và chưa thăm.
- Thêm vào hàng đợi để duyệt tiếp, đồng thời cập nhật đường đi.

### Thực hành 23  
#### Code chính:  
<img width="586" height="295" alt="image" src="https://github.com/user-attachments/assets/4a931d78-af70-4d4d-8730-aa4b9f5ea8c6" />  

- Khởi tạo: dùng hàng đợi queue để lưu các vị trí cần kiểm tra và đường đi tương ứng, visited tập hợp các vị trí đã đi qua, tránh lặp lại.  

Duyệt BFS:  
- Lấy một điểm current từ hàng đợi và kiểm tra.  
- Nếu là đích thì trả về đường đi.  
- Nếu không thì tính các điểm có thể đi tiếp từ current.  
- Kiểm tra nếu next_position hợp lệ và chưa thăm.  
- Thêm vào hàng đợi để duyệt tiếp, đồng thời cập nhật đường đi.

### Thực hành 24  
#### Code chính:  
<img width="974" height="441" alt="image" src="https://github.com/user-attachments/assets/b868878e-b097-42db-b00c-ea177e10d375" />  

- Mô phỏng một môi trường có 16 trạng thái (từ 0 đến 15).  
- Trạng thái 15 là đích đến (goal).  
- Tại mỗi bước:  
  + Agent chọn hành động ngẫu nhiên (20%) hoặc chọn hành động tốt nhất từ Q-table (80%).  
  + Luôn chuyển sang trạng thái kế tiếp (next_state = current_state + 1).  
  + Nếu đến trạng thái 15 thì nhận phần thưởng = 1, còn lại là 0.  
  + Cập nhật Q-value theo công thức Q-learning.  
- Sau 1000 vòng lặp (epochs), agent học được chiến lược để đi tới đích.

## Hướng dẫn  
### 1. Cài đặt môi trường  
- Cài python
- Cài thư viện matplotlib

### 2. Thay đổi tham số  
- Có thể thay đổi tùy ý các tham số như ma trận, đường đi, ... để xem các kết quả khác nhau của bài.

## Tài liệu hướng dẫn  
- Bài tập thực hành - Van Lang University.










