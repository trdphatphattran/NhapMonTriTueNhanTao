# LAB 4: THUẬT TOÁN DI TRUYỀN (GENETIC ALGORITHM)  
## Thông tin:  
Sinh viên: Trần Đại Phát  
MSSV: 2374802010379  
Môn học: Nhập môn Trí tuệ nhân tạo  
GVHD: Nguyễn Thái Anh  
Năm học: 2024 - 2025  
## Mục tiêu bài học:  
- Hiểu rõ nguyên lý hoạt động của thuật toán di truyền.
- Áp dụng thuật toán để giải các bài toán tối ưu hóa.
- Phân tích và trực quan hóa kết quả.
- Thực hành với các bài tập mở rộng và nâng cao kỹ năng.
## Giới thiệu:  
Thuật toán di truyền (Genetic Algorithm - GA) là một phương pháp tìm kiếm dựa trên cơ chế tiến hóa tự nhiên, lấy cảm hứng từ thuyết tiến hóa của Darwin. GA được sử dụng để tìm lời giải gần tối ưu cho các bài toán tối ưu hóa phức tạp.  
## Các bước chính của thuật toán:  
1. Khởi tạo quần thể: Tạo ngẫu nhiên một tập hợp các cá thể (giải pháp tiềm năng).
2. Đánh giá độ thích nghi (Fitness Evaluation): Tính giá trị hàm mục tiêu cho mỗi cá thể.
3. Lựa chọn (Selection): Chọn các cá thể tốt nhất để lai ghép (thường sử dụng các phương pháp như Tournament Selection hoặc Roulette Wheel).
4. Lai ghép (Crossover): Kết hợp cả hai cá thể để tạo ra cá thể mới.
5. Đột biến (Mutation): Thay đổi ngẫu nhiên một số gen để duy trì tính đa dạng.
6. Lặp lại: Quay lại bước 2 cho đến khi đạt điều kiện dừng (số thế hệ hoặc giá trị Fitness mong muốn).

## Công thức tổng quát:  
![image](https://github.com/user-attachments/assets/68570270-fe39-480b-b221-244e637fc086) hoặc ![image](https://github.com/user-attachments/assets/35ea920c-1349-43d7-8602-ac6de9e9cfff)  

## Ví dụ 1: Tối ưu hóa hàm 1 biến  
### Bài toán  
Tìm x sao cho f(x) = -(x^2) + 10x + 50 đạt GTLN trong khoảng x ∈ [0, 10].  
#### Giải thích:  
![image](https://github.com/user-attachments/assets/89050164-637b-4141-9cc5-2ce9f737dfcf)  
Khởi tạo hàm mục tiêu.  
![image](https://github.com/user-attachments/assets/d6dc0e3e-b464-460e-ba52-ef63e53cce0c)  
Khởi tạo quần thể, mỗi cá thể là một giá trị ngẫu nhiên trong đoạn [min_val, max_val].  
![image](https://github.com/user-attachments/assets/dc08272e-027b-4438-99d1-aad53c858bcf)  
Lựa chọn cha mẹ, chọn ngẫu nhiên tournament_size cá thể từ quần thể, lấy cá thể có fitness cao nhất làm cha mẹ.  
![image](https://github.com/user-attachments/assets/e67036b2-7126-41d1-a6e1-fb3924b237f2)  
Đây là lai ghép. Với xác suất 80%, tạo con bằng cách lấy trung bình hai cha mẹ. 20% còn lại thì con giống hệt cha mẹ đầu tiên.  
![image](https://github.com/user-attachments/assets/6bc8f342-6780-4f6e-bef6-5069739298d7)  
Đây là đột biến. Với xác suất 10%, cá thể đột biến thành giá trị ngẫu nhiên từ [0, 10].  
![image](https://github.com/user-attachments/assets/42fc49fd-f8d4-4a44-87c3-73368bc5caa8)  
Khởi tạo quần thể ban đầu gồm pop_size cá thể và một danh sách lưu giá trị f(x) tốt nhất của mỗi thế hệ.  
![image](https://github.com/user-attachments/assets/af094dbb-48f6-409b-aa52-dcc633ab7654)  
Vòng lặp chạy qua từng thế hệ tiến hóa, tính fitness cho tất cả cá thể, lấy giá trị tốt nhất và lưu lại để vẽ đồ thị.  
![image](https://github.com/user-attachments/assets/2aa7ae35-4138-44d9-89f7-b40be747f875)  
Tạo quần thể mới gồm 2 cha mẹ tốt nhất -> lai ghép tạo con -> đột biến con -> thêm con vào thế hệ mới.  
![image](https://github.com/user-attachments/assets/4597a6fb-1e3e-41bc-8f83-4d007226fe88)  
Cập nhật quần thể mới cho thế hệ tiếp theo và in ra cá thể tốt nhất của thế hệ hiện tại.  

## Ví dụ 2: Tối ưu hóa hàm 2 biến  
### Bài toán  
Tìm x, y sao cho g(x, y) = x^2 + y^2 đạt GTNN trong khoảng x ∈ [-5, 5].  
#### Giải thích:  
![image](https://github.com/user-attachments/assets/3c5df443-51d0-4878-8ded-89ff26e7751d)  
Khởi tạo hàm mục tiêu.  
![image](https://github.com/user-attachments/assets/adb8e549-6d63-43b4-8d6c-a1bfb87a675d)  
Khởi tạo quần thể, mỗi cá thể là một giá trị ngẫu nhiên trong đoạn [min_val, max_val].  
![image](https://github.com/user-attachments/assets/cbb8a9a6-2435-4854-b04d-5a11e8366582)  
Lựa chọn cha mẹ, chọn ngẫu nhiên tournament_size cá thể từ quần thể, lấy cá thể có fitness cao nhất làm cha mẹ.  
![image](https://github.com/user-attachments/assets/e429decc-ac66-4926-acf2-2d2faf817c58)  
Lai ghép:  
- Xác suất 80%: Tạo con bằng trung bình các tọa độ 2 cha mẹ.  
- Xác suất 20%: Con giống cha mẹ 1.

![image](https://github.com/user-attachments/assets/cca891b8-6c3f-476c-9d5b-320e47618cd3)  
Đột biến: Với xác suất 10%, mỗi biến x hoặc y có thể thay đổi ngẫu nhiên từ [-5, 5].
![image](https://github.com/user-attachments/assets/44a0a754-938b-4568-99d8-1056567168c8)  
Khởi tạo quần thể ban đầu gồm pop_size cá thể và một danh sách lưu giá trị f(x) tốt nhất của mỗi thế hệ.  
![image](https://github.com/user-attachments/assets/55063444-2460-4c9b-9470-fd9fbd06515c)  
Vòng lặp chạy qua từng thế hệ tiến hóa, tính fitness cho tất cả cá thể, lấy giá trị tốt nhất và lưu lại để vẽ đồ thị.  
![image](https://github.com/user-attachments/assets/f20f71cc-f3b1-4617-be76-d4cf4bce7038)  
Tạo quần thể mới gồm 2 cha mẹ tốt nhất -> lai ghép tạo con -> đột biến con -> thêm con vào thế hệ mới. 
![image](https://github.com/user-attachments/assets/f5e70e30-e90b-4bea-8fc4-f221cb80daf3)  
Cập nhật quần thể mới cho thế hệ tiếp theo và in ra cá thể tốt nhất của thế hệ hiện tại.  

## Bài tập  
### Bài toán 1:  
Tối ưu hàm h(x) = sin(x) + cos(x) trong miền x ∈ [0, 2π].  

Ta có: h(x) = sin(x) + cos(x) = √2.sin(x + π/4) -> max h(x) = √2 ≈ 1,1412.  
Xảy ra khi: x = π/4.  
Phương pháp chọn lọc: Roulette Wheel Selection.  

#### Code chính:  
![image](https://github.com/user-attachments/assets/5c14fec5-9a16-486a-b4b1-852abd7f2e32)  
- Lấy fitness nhỏ nhất trong quần thể (trong đoạn code có thể là -1,1412).  
- Nếu có giá trị âm, ta dịch tất cả fitness về dương.

![image](https://github.com/user-attachments/assets/86ce6a06-9d02-4244-a68f-9320f26e7ca1)  
- total_fitness: tổng độ thích nghi của quần thể.  
- pick: chọn ngẫu nhiên 1 giá trị trong đoạn [0, total_fitness].  
- current: biến cộng dồn, xác định vị trí rơi của pick.

![image](https://github.com/user-attachments/assets/153ee70d-a43f-49af-9648-4598ddd1d940)  
- Vòng lặp sẽ cộng dồn từng giá trị fitness.
- Khi current vượt qua pick, tức là roulette đã được chọn.






## Hướng dẫn  
### 1. Cài đặt môi trường  
Cài python, sau đó cài các thư viện:  
Dùng tổ hợp phím: Windows + R + cmd.  
- pip install numpy matplotlib.

### 2. Chạy notebook  
- Mở jupyter notebook trên VSCode.
- Code từng bài chạy và xem kết quả.
- Nếu xảy ra lỗi: code sai, chưa cài thư viện, ... -> Không hiển thị kết quả.

### 3. Tùy chỉnh tham số  
Có thể thay đổi vài thứ sau:  
- Hàm mục tiêu.
- Tỉ lệ lai ghép.
- Giá trị nhỏ nhất và lớn nhất.
- Kích thước quần thể
- Các phương pháp chọn lọc: Tournament Selection, Roulette Wheel Selection, ...
- ...

## Tài liệu hướng dẫn  
- Slide bài tập thực hành - Van Lang University.
- An Introduction to Genetic Algorithms – Melanie Mitchell.  




















































