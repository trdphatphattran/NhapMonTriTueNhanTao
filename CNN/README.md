# LAB 5: THUẬT TOÁN CONVOLUTIONAL NEURAL NETWORK (CNN)  
## Thông tin:  
Sinh viên: Trần Đại Phát  
MSSV: 2374802010379  
Môn học: Nhập môn Trí tuệ nhân tạo  
GVHD: Nguyễn Thái Anh  
Năm học: 2024 - 2025  
## 1. CNN là gì?  
CNN (Convolutional Neural Network) là một loại mạng nơ-ron nhân tạo giúp máy tính "nhìn" và hiểu ảnh, tương tự cách con người nhận diện vật thể trong đời thực. Thay vì xem toàn bộ ảnh một lúc như mạng nơ-ron thông thường (fully connected), CNN chia nhỏ ảnh ra, tìm các đặc trưng như đường thẳng, góc, vòng tròn, rồi ghép lại để đoán xem ảnh đó là gì.  
Ví dụ: Khi ta nhìn một con mèo, không cần xem hết cả ảnh ngay lập tức. Ta nhận ra tai mèo (hình tam giác), mắt mèo (hình tròn), ria mèo (đường thẳng), rồi kết luận "Đây là mèo". CNN cũng làm như vậy bằng cách dùng các "kính lúp" nhỏ quét qua ảnh từng phần một.  

## 2. Các thành phần chính của CNN  
### 2.1 Tầng tích chập (Convolution Layer)  
Đây là bước quan trọng nhất, giống như "đôi mắt" của CNN, giúp tìm các đặc trưng nhỏ trong ảnh như cạnh, góc, hoặc đường cong.  
Ý tưởng cơ bản  
- Chúng ta có 1 ảnh, giả sử kích thước là 6x6 pixel.
- Dùng 1 bộ lọc (filter/kernel), ví dụ 3x3, như một "kính lúp" nhỏ để quét qua ảnh.
- Kết quả là 1 feature map, cho biết chỗ nào trong ảnh có đặc trưng mà bộ lọc tìm được.
#### Công thức tích chập  
![image](https://github.com/user-attachments/assets/cbe1bfc9-70cc-4ff5-8ec8-4613e3dad611)  
Trong đó:  
- I: Ảnh đầu vào.
- K: Bộ lọc (kernel/filter).
- F: Kích thước bộ lọc (ví dụ F = 3 nếu là 3x3).
- S(i, j): Gía trị tại vị trí (j, j) trong feature map.

### 2.2 Hàm kích hoạt (ReLU)  
Sau khi có feature map từ tầng tích chập, ta dùng hàm ReLU để "lọc" nó, giữ lại các đặc trưng rõ ràng và loại bỏ những phần không quan trọng.  
#### Công thức ReLU  
![image](https://github.com/user-attachments/assets/4e00e067-cb5a-41e4-96e9-c048bf034400)  
Trong đó:  
- Nếu số lớn hơn 0, giữ nguyên.
- Nếu số nhỏ hơn hoặc bằng 0, biến thành 0.

### 2.3 Tầng Pooling (Pooling Layer)  
Pooling giống như "tóm tắt" feature map, giảm kích thước để tiết kiệm tính toán nhưng vẫn giữ được thông tin quan trọng.  
Loại phố biến: Max Pooling  
- Lấy giá trị lớn nhất trong một vùng nhỏ, thường là 2x2.
#### Công thức Max Pooling  
![image](https://github.com/user-attachments/assets/0cfe5f3b-2d2d-45e4-afa1-e2a851d3f907)  
Giải thích đơn giản: Chia feature map thành các ô 2x2, chọn số lớn nhất trong mỗi ô để tạo feature map nhỏ hơn.  

### 2.4 Tầng Fully Connected (FC Layer)  
Đây là bước cuối cùng, nơi CNN ghép tất cả đặc trưng lại để đoán xem ảnh là gì.  
#### Công thức của FC Layer  
![image](https://github.com/user-attachments/assets/eb6c1dd1-051b-4c36-911c-029e8f513f63)  
Trong đó:  
x: Vector từ feature map duỗi ra.  
W: Ma trận trọng số.  
b: Bias (độ lệch).  
Giải thích đơn giản: Lấy feature map cuối, "duỗi" thành một hàng số, rồi nhân với trọng số để ra kết quả phân loại.  

## 3. Tổng hợp CNN  
1. Tích chập: Tìm đặc trưng như đường ngang --> Feature map S.
2. ReLU: Lọc bỏ các nét mờ (giá trị âm) --> Feature map Srelu.
3. Pooling: Tóm tắt, giảm kích thước --> Feature map Spooled.
4. Fully Connected: Ghép các đặc trưng, đoán xem là gì.

## 4. Ứng dụng thực tế  
CNN dùng trong nhiều lĩnh vực:  
- Nhận diện khuôn mặt: Facebook dùng CNN để gắn thẻ bạn bè trong ảnh.
- Xe tự lái: Phát hiện biển báo, người đi bộ qua camera.
- Y khoa: Phân tích ảnh X-quang để tìm bệnh.

## Bài tập về nhà  
### Câu 1:  
- Yêu cầu: Tăng số lượng epoch từ 5 lên 10.
- Chạy lại code và ghi nhận.
- Viết ngắn gọn về lý do epoch ảnh hưởng đến kết quả.

![image](https://github.com/user-attachments/assets/86cd0ebc-c37e-47e6-93c1-a788d0e6367a)  

##### Độ chính xác trên tập test có sự thay đổi tăng lên:  
- Vì trong 5 epoch đầu tiên (1 -> 5) thì độ chính xác accuracy thường có sự chênh lệch lớn (bởi vì mô hình đang học các đặc trưng cơ bản).
- Trong 5 epoch còn lại (6 -> 10) thì mô hình đã học hiệu quả, nên chênh lệch giữa các accuracy thường là rất nhỏ.

##### Biểu đồ mất mát (loss) giảm mạnh, sau đó là giảm đều, cụ thể:  
- Giai đoạn 1 -> 2: loss giảm rất mạnh vì mô hình học được các đặc trưng cơ bản từ ảnh (góc, cạnh, ...).
- Giai đoạn 3 -> 7: loss giảm chậm lại vì mô hình bắt đầu có thể nhận diện tốt hơn.
- Giai đoạn 8 -> 10: loss có thể chững lại hoặc dao động nhẹ, chứng tỏ mô hình đã nhận diện gần như hoàn hảo.

##### Số epoch ảnh hưởng đến kết quả vì:  
- Ít epoch: Mô hình học chưa đủ -> accuracy thấp, loss cao.
- Vừa epoch: Mô hình học tốt các đặc trưng -> accuracy cao, loss thấp.
- Nhiều epoch: Mô hình học cả nhiễu của dữ liệu -> accuracy trên test giảm, dù train accuracy tăng.

### Câu 2:  
- Yêu cầu: Thêm một tầng tích chập thứ ba (conv3) vào mô hình MNIST_CNN.  
- Viết ngắn gọn về tác dụng của việc tăng tầng tích chập.  

![image](https://github.com/user-attachments/assets/3be2df1a-bbcd-4a1d-9917-cde8f8ae7f71)  

##### Biếu đồ mất mát (loss) giảm mạnh, sau đó là giảm đều, cụ thể:  
- Giai đoạn 1 -> 2: loss giảm mạnh vì mô hình học được các đặc trưng cơ bản từ ảnh (góc, cạnh, ...).
- Giai đoạn 3 -> 5: loss giảm đều với tốc độ chậm, mô hình đã có thể nhận diện tốt hơn và sắp hoàn hảo.

##### Tác dụng của việc tăng tầng tích chập:  
- conv1: Học các đặc trưng như cạnh, đường thẳng.
- conv2: Học các đặc trưng như góc, nét căng.
- conv3: Học các đặc trưng như cấu trúc số, ...  
Tầng conv3 giúp mô hình hiểu sâu hơn về hình ảnh, phân biệt rõ hơn giữa các con số.
- Độ chính xác có thể tăng lên vì mạng có khả năng học mối quan hệ phức tạp hơn.

### Câu 3:  
- Yêu cầu: Thử 2 giá trị learning rate khác nhau: 0.001 và 0.1.  
- Chạy lại code và ghi nhận.  
- Viết ngắn gọn về cách learning rate ảnh hưởng đến quá trình học của hình.

#### Với lr = 0.001:  
![image](https://github.com/user-attachments/assets/99ce93e1-6ad2-498b-847f-b4f5b1213e36)  

##### Độ chính xác trên tập test với learning rate 0.001 sẽ giảm rõ rệt, cụ thể:  
- Chênh lệch giữa các accuracy là rất lớn.
- Với lr = 0.001 thì mô hình sẽ học rất chậm và lâu nhận diện.

##### Biểu đồ mất mát (loss) giảm mạnh, sau đó giảm dần đều, cụ thể:  
- Giai đoạn 1: loss giảm mạnh, mô hình bắt đầu học được đáng kể.
- Giai đoạn 2 -> 3: loss giảm khá chậm, mô hình đã có thể nhận diện được một số đặc trưng cơ bản.
- Giai đoạn 4 -> 5: loss giảm chậm, mô hình đã học gần như hoàn hảo các đặc trưng.

#### Với lr = 0.1:  
![image](https://github.com/user-attachments/assets/ff0c80e1-bc28-4f40-8fd8-74bb22c38564)  

##### Độ chính xác trên tập test với learning rate = 0.1 sẽ giảm rõ rệt, cụ thể:  
- Chênh lệch giữa các accuracy là lớn.
- Với lr = 0.1, mô hình không hội tụ tốt dẫn đến không chính xác trên tập test.

##### Biểu đồ mất mát (loss) giảm mạnh, sau đó giảm không đều, cụ thể:  
- Giai đoạn 1: loss giảm mạnh, mô hình đang học tốt.
- Giai đoạn 2 -> 5: loss giảm đều nhưng chậm hơn, mô hình có thể gần như hoàn hảo nhưng hơi chậm.

##### Cách learning rate ảnh hưởng đến quá trình học của mô hình:  
- lr nhỏ: Mô hình học rất chậm, cần nhiều epoch để hội tụ, nhưng quá trình học khá ổn định.
- lr phù hợp: Mô hình học nhanh và ổn định, loss giảm đều, dễ đạt độ chính xác cao.
- lr lớn: Mô hình học không ổn định, loss dao động bất thường, có thể không hội tụ.

### Câu 4:  
- Yêu cầu: Sửa hàm visualize_feature_map để vẽ thêm hai feature map từ tầng conv2.
- Chạy lại mô hình và mô tả sự khác biệt giữa feature map từ conv1 và conv2
- Viết ngắn gọn về sự khác biệt giữa feature map từ các tầng khác nhau.

![image](https://github.com/user-attachments/assets/6a320283-4b80-4174-bbdb-8bd2cb7fc561)  

##### Sau khi chạy lại mô hình, chúng ta sẽ thấy có 5 ảnh:  
- 1 ảnh gốc.
- 2 ảnh feature map conv1.
- 2 ảnh feature map conv2.

##### Mô tả sự khác biệt:  
###### Conv1:  
- Hiển thị rõ viền và nét của số 7 gồm đường chéo và đường ngang rõ ràng, độ cong và mép nét đều được giữ lại.
- Feature map vẫn giữ nhiều chi tiết không gian của ảnh gốc.
###### Conv2:  
- Hiển thị các vùng chính của số 7 bao gồm vùng đầu số 7 được nhấn mạnh, các vùng còn lại mờ hơn.
- Ảnh trở nên thô hơn, tập trung vào hình dạng tổng quát.

## Hướng dẫn  
### 1. Cài đặt môi trường  
Cài python, sau đó cài các thư viện:  
Dùng tổ hợp phím: Win + R + cmd:  
- pip install torch torchvision torchaudio.
- pip install numpy matplotlib.

### 2. Chạy notebook  
- Mở jupyter notebook trên VSCode.
- Code từng bài chạy và xem kết quả.
- Nếu xảy ra lỗi: code sai, chưa cài thư viện... --> Không chạy được code.

### 3. Tùy chỉnh tham số  
Thay đổi các tham số như:  
- epoch tăng hoặc giảm.
- Thêm các tầng tích chập.
- Thay đổi learning rate.
- Vẽ thêm feature map.
- ...

## Tài liệu hướng dẫn  
- Slide thực hành - Van Lang University.
- An Introduction to Convolutional Neural Networks (CNNs).
- GeeksforGeeks – “Introduction to Convolution Neural Network.







 




























