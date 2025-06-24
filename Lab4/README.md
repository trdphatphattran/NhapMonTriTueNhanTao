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

## Ví dụ 1: Tối ưu hóa hàm 1 biến  
### Bài toán  
Tìm $x$ sao cho  
$$
f(x) = -(x^2) + 10x + 50
$$  
đạt giá trị lớn nhất trong khoảng  
$$
x \in [0, 10].
$$


