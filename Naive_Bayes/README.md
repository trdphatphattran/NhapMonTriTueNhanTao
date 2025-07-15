# LAB 6: NAIVE BAYES
## Thông tin:  
Sinh viên: Trần Đại Phát  
MSSV: 2374802010379  
Môn học: Nhập môn Trí tuệ nhân tạo  
GVHD: Nguyễn Thái Anh  
Năm học: 2024 - 2025  
## Mục tiêu bài học  
- Phân phối Bernoulli và phân phối Multinomial.  
- Phân phối Gaussian.
## 1. Naive Bayes là gì?  
Naive Bayes là một thuật toán học máy đơn giản nhưng mạnh mẽ, dùng cho phân loại (classification). Nó dựa trên định lý Bayes trong xác suất thống kê và giả định “naive” rằng các đặc trưng (features) là độc lập với nhau – điều này hiếm đúng trong thực tế, nhưng vẫn cho kết quả rất tốt trong nhiều bài toán thực tế như lọc thư rác, phân loại văn bản, nhận diện cảm xúc, ...  
## 2. Định lý  
<img width="263" height="112" alt="image" src="https://github.com/user-attachments/assets/c258d671-31de-402f-8448-f6f145ced929" />  

Trong đó:  
- A: nhãn lớp (labels).  
- B: tập các đặc trưng (features).  
## 3. Các loại Naive Bayes  
- Gaussian: dùng cho dữ liệu liên tục, giả định phân phối chuẩn.  
- Multinomial: phổ biến trong phân loại văn bản.  
- Bernoulli: Dùng khi đặc trưng là nhị phân.  
## 4. Ví dụ  
### Xây dựng trang web theo yêu cầu sau:  
Cho tệp dữ liệu: Education.csv và drug200.csv.  
Trong đó:  
- Text: chứa đoạn văn bản liên quan đến chủ đề giáo dục.  
- Label: chứa nhãn cảm xúc của văn bản (positive và negative).  
Yêu cầu: Áp dụng thuật toán Naive Bayes (phân phối bernoulli và phân phối Multinomial) để dự đoán cảm xúc của văn bản là tích cực hay tiêu cực và so sánh kết quả của hai phân phối đó.  
- Age: Tuổi của bệnh nhân  
- Sex: Giới tính của bệnh nhân  
- BP: Mức huyết áp  
- Cholesterol: Mức cholesterol trong máu  
- Na_to_K: Tỷ lệ Natri và Kali trong máu  
- Drug: Loại thuốc [A/B/C/X/Y]  
Yêu cầu: Áp dụng thuật toán Naive Bayes (phân phối Gaussian) để dự đoán kết quả loại thuốc phù hợp với bệnh nhân.  

#### Bài làm  
<img width="300" height="152" alt="image" src="https://github.com/user-attachments/assets/4b851ea1-1045-473f-9c4b-ea4ecfdc1f88" />  

Đây là hàm load dữ liệu từ 2 tệp education.csv và drug200.csv.  

##### Mô hình 1: Phân loại văn bản với Bernoulli  

###### Chia tập train  

<img width="555" height="158" alt="image" src="https://github.com/user-attachments/assets/7dc8351b-1b96-4c70-ad3d-502292249ee9" />  

Giúp tránh dùng train_test_split của sklearn nếu muốn kiểm soát logic chia bằng permute.  

###### Huấn luyện với Bernoulli  

<img width="677" height="259" alt="image" src="https://github.com/user-attachments/assets/a3cf13ad-fc91-4af7-9c5e-98a542a9c814" />  

- Dữ liệu văn bản được chuyển sang nhị phân bằng CountVectorizer(binary=True).  
- Ánh xạ label thành nhị phân: positive --> 1, negative --> 0.  
- Dùng BernoulliNB() để train.  
- Tính đường cong ROC từ tập test.  
###### Hàm dự đoán cả xúc văn bản  
<img width="646" height="754" alt="image" src="https://github.com/user-attachments/assets/50809f76-b24d-4c24-a104-90616479f9f4" />  
- Nhận diện một chuỗi văn bản.
- Dự đoán nhãn và xác suất.
- Vẽ biểu đồ ROC: đo độ phân biệt mô hình.
- Biểu đồ thanh: cho thấy xác suất positive và negative.

##### Mô hình 2: Dự đoán thuốc với GaussianNB  
###### Encode với dữ liệu định tính  
<img width="446" height="239" alt="image" src="https://github.com/user-attachments/assets/85fe1e07-0014-45f5-a602-f93ceac83266" />  

- Encode các cột dạng text về số.  
- Dùng GaussianNB() vì dữ liệu đầu vào dạng liên tục hoặc gần liên tục.

###### Hàm dự đoán thuốc  
<img width="528" height="535" alt="image" src="https://github.com/user-attachments/assets/58ed0624-6b42-4823-920b-7b4e6deebd1e" />  
- Dự đoán thuốc phù hợp với các đặc trưng đầu vào.
- Trả về tên thuốc dự đoán (A/B/C/X/Y) và biểu đồ thanh xác suất từng loại thuốc.

##### Tạo giao diện với Gradio  
###### Tạo giao diện cho education.csv  
<img width="760" height="223" alt="image" src="https://github.com/user-attachments/assets/d1773fc4-bcce-47c5-a04a-319ed0141a16" />  
- Nhập văn bản.
- Trả cảm xúc + ROC + bar chart.
###### Ví dụ:  
- Input: The impact of educational reforms remains uncertain despite extensive research.  
- Output:  
<img width="1253" height="726" alt="image" src="https://github.com/user-attachments/assets/98e008b4-cd2a-42a6-8c40-0c58bfaf71b8" />
Giao diện toàn bộ web:
<img width="1253" height="726" alt="image" src="https://github.com/user-attachments/assets/04bb9e04-08a4-4c80-baf7-f8f99e147b6c" />

###### Tạo giao diện cho grug20.csv  
<img width="682" height="310" alt="image" src="https://github.com/user-attachments/assets/fd5b083f-9a2c-44e9-aad1-1f3dce3dc02a" />  
- Nhập thông tin bệnh nhân.
- Trả về loại thuốc phù hợp và biểu đồ xác suất.
###### Ví dụ:  
- Input: 23,F,HIGH,HIGH,25.355.
- Output:
<img width="617" height="356" alt="image" src="https://github.com/user-attachments/assets/ab15e233-0205-4bdf-8e3d-e8905abd9b71" />
Giao diện toàn bộ web:
<img width="1248" height="424" alt="image" src="https://github.com/user-attachments/assets/d9461e2c-33f8-4f26-ac8e-d3ce2115ddf3" />




















