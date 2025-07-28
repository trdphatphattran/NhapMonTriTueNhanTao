# ĐỀ THI THỬ  
## Thông tin sinh viên  
- Sinh viên: Trần Đại Phát
- MSSV: 2374802010379
- Môn học: Nhập môn Trí tuệ nhân tạo  
- GVHD: Nguyễn Thái Anh  
- Năm học: 2024 - 2025
## Mục đích  
- Ôn lại các kiến thức về DFS, BFS, CNN, Naive Bayes, Thuật toán di truyền.
- Chuẩn bị cho bài thi cuối kì.
## Câu 1: Tìm DFS theo đồ thị bên dưới bằng python  
<img width="688" height="365" alt="image" src="https://github.com/user-attachments/assets/d8ae9827-90b8-419a-af12-a41af86cb6eb" />  

### Code chính  

<img width="881" height="122" alt="image" src="https://github.com/user-attachments/assets/f45e2847-f89e-424e-9b4b-ca5bfe6ea0b1" />  

Duyệt các đỉnh kề của đỉnh hiện tại và thực hiện tìm kiếm đệ quy theo chiều sâu để tìm đường đi đến đỉnh đích, đồng thời tính tổng trọng số trên đường đi. Nếu tìm thấy đường đến đích, nó trả về đường đi và tổng trọng số; nếu không thì trả về None, 0.  

## Câu 2: Tối ưu hóa hàm một biến  
<img width="750" height="159" alt="image" src="https://github.com/user-attachments/assets/647e11f0-3eea-492a-bd21-8c11739ddbea" />  

### Code chính  

<img width="719" height="415" alt="image" src="https://github.com/user-attachments/assets/3dd8c082-02ac-46c8-b802-86d8335ad263" />  

Tìm giá trị của x trong khoảng từ min_val đến max_val sao cho hàm f(x) = -x² + 10x + 50 đạt giá trị lớn nhất, bằng cách sử dụng thuật toán di truyền (genetic algorithm). Hàm này mô phỏng quá trình tiến hóa sinh học gồm: khởi tạo quần thể, chọn lọc, lai ghép, đột biến, lặp lại qua nhiều thế hệ để tìm nghiệm tối ưu.  

## Câu 3: Sử dụng mô hình CNN để phân loại dữ liệu chó và mèo từ data  
[Kaggle](https://www.kaggle.com/c/dogs-vs-cats/data)  

### Phần dùng để huấn luyện mô hình  
#### Tạo dataset và dataloader  
<img width="572" height="139" alt="image" src="https://github.com/user-attachments/assets/a10ddc31-e252-49ab-b7ef-4cab4f94ed2c" />  

#### Định nghĩa mô hình CNN  
<img width="630" height="347" alt="image" src="https://github.com/user-attachments/assets/a985ea4f-5d67-430e-bdef-7f2eb943eed0" />  

#### Cấu hình optimizer, loss  
<img width="476" height="43" alt="image" src="https://github.com/user-attachments/assets/05a96044-cef4-40e9-8842-fb2f8aacb2f9" />  

#### Huấn luyện  
<img width="651" height="423" alt="image" src="https://github.com/user-attachments/assets/bfc4bbda-aa23-4783-872a-6f022e130070" />  


## Câu 4: Sử dụng Naive Bayes cho tập dữ liệu sau  
<img width="445" height="432" alt="image" src="https://github.com/user-attachments/assets/cc57b58d-e2b1-4cea-82ef-5b84ba1d1cf0" />  

### Code chính  

<img width="342" height="97" alt="image" src="https://github.com/user-attachments/assets/beeaff86-2756-4c9b-8b0e-c948333b2983" />  

- Mã hóa các biến phân loại thành số.

<img width="203" height="46" alt="image" src="https://github.com/user-attachments/assets/f9d37db7-22ed-4195-86ec-63dde28e9467" />  

- Tách dữ liệu thành đặc trưng và nhãn.

<img width="649" height="64" alt="image" src="https://github.com/user-attachments/assets/17ed212b-8805-4683-9c53-d37d634f2346" />  

- Chia thành tập huấn luyện và kiểm tra, sau đó huấn luyện Naive Bayes.  




## Tài liệu tham khảo  
- Lab DFS, thuật toán di truyền, CNN, Naive Bayes lý thuyết + thực hành - Van Lang University.  











