# THỰC HÀNH: GIẢI THUẬT MINIMAX  
## Thông tin  
- Sinh viên: Trần Đại Phát  
- MSSV: 2374802010379  
- Môn học: Nhập môn Trí tuệ nhân tạo  
- GVHD: Nguyễn Thái Anh  
- Năm học: 2024 - 2025
## Thuật toán Minimax là gì?  
Thuật toán Minimax là một kỹ thuật trong trí tuệ nhân tạo, thường được sử dụng trong các trò chơi đối kháng 2 người như cờ vua, cờ caro, ...  
### Ý tưởng chính  
Minimax dựa trên giả định:  
- Một người chơi cố tối đa hóa điểm số (MAX).
- Người chơi còn lại cố tối thiểu hóa điểm số (MIN).
Minimax sẽ:
- Xem xét mọi nước đi có thể của cả 2 người chơi.
- Mô phỏng toàn bộ cây trò chơi.
- Chọn nước đi mang lại kết quả tốt nhất cho MAX, giả sử MIN cũng chơi tối ưu.

## Ví dụ về bài toán Caro 4x4  
### 1. Khởi tạo chương trình và biến
<img width="239" height="153" alt="image" src="https://github.com/user-attachments/assets/3335c65f-d15b-4b65-b978-5b90d858593f" />

- Tạo cửa số chính root với tiêu đề "Game XO 4x4".
- clicked: luôn đổi giữa True và False để xác định lượt chơi (True (X) và False (O)).
- count: đếm số lượt chơi đã chơi.

### 2. Hàm disableButtons() - Khóa tất cả các nút  
<img width="290" height="320" alt="image" src="https://github.com/user-attachments/assets/700702dd-746c-47ef-87ed-8b21b0c8990e" />  

- Khóa toàn bộ 16 nút lại sau khi có người thắng, không cho nhấn tiếp.

### 3. Hàm checkWinner() - Kiểm tra điều kiện thắng  
- Lần lượt kiểm tra các tổ hợp thắng:
   + 4 hàng ngang.
   + 4 cột dọc.
   + 2 đường chéo.
- Với mỗi tổ hợp, dùng điều kiện if hoặc elif để kiểm tra xem có phải cả 4 ô cùng có giá trị "X" hay "O" không.

### 4. Hàm checkDraw() - Kiểm tra hòa  
<img width="374" height="102" alt="image" src="https://github.com/user-attachments/assets/15cfffcf-770a-47db-b353-2bb12069cbeb" />  

- Nếu tất cả 16 ô đã được choi mà không ai thắng thì hiển thị thông báo hòa và khởi động lại.

### 5. Hàm buttonClicked(button) - Xử lý khi nhấn vào nút  
<img width="499" height="294" alt="image" src="https://github.com/user-attachments/assets/ff163dc3-8e55-435a-bc7b-52cc00a6c9df" />  

- Nếu ô đang nhấn còn trống " ":
  + Nếu đang là lượt chơi của người chơi 1 (clicked == True) --> gán X, ngược là là O.
- Tăng count lên 1.
- Gọi checkWinner() và checkDraw() sau mỗi lần đi.
- Nếu người chơi đã ấn vào ô đã chọn rồi thì hiện thông báo lỗi.

### 6. Hàm start() - Khởi động lại game  
- Tạo lại 16 nút mới.
- Reset lại clicked = True, count = 0.
- Mỗi nút là 1 button riêng biệt.
- Gán từng nút vào lưới grid(row, column) để tạo bàn 4x4.

### 7. Menu Game  
<img width="466" height="150" alt="image" src="https://github.com/user-attachments/assets/f0ce4791-aea9-4f49-84f1-541e634ef1eb" />  

- Tạo menu "Options" với lựa chọn là "Restart Game" để khởi động lại trò chơi bằng tay.  
- Sau đó chạy trò chơi.

### Nhận xét tính đúng đắn  
- Giao diện: hiển thị đầy đủ 16 nút theo dạng lưới 4x4.
- Xử lý lượt chơi: chương trình lần lượt phân chia lượt chơi giữa người chơi X và O dựa trên biến clicked, đảm bảo đúng logic luân phiên.
- Xử lý thắng cuộc: viết đầy đủ các trường hợp để kiểm tra 4 dấu liên tiếp nhau trên các hàng, cột và hai đường chéo chính, đảm bảo phát hiện đúng người chiến thắng.
- Dừng trò chơi khi có người thắng: hàm disableButtons() được gọi để vô hiệu hóa toàn bộ các nút sau khi có người thắng hoặc hòa.
- Tái khởi động ván mới: hàm start() được thiết kế để khởi tạo lại toàn bộ nút bấm và đặt lại các biến trạng thái, cho phép chơi nhiều ván liên tục.

## Code theo cách khác  
### 1. Hàm disableButtons() - Khóa tất cả các nút  
<img width="288" height="83" alt="image" src="https://github.com/user-attachments/assets/425701db-c8af-4ce2-ad1a-94296e228a89" />  

- Vô hiệu hóa tất cả các nút khi kết thúc ván đấu.

### 2. Hàm checkLines(player)  
<img width="513" height="224" alt="image" src="https://github.com/user-attachments/assets/07407991-5d3f-4efa-8ba2-691b7d1f7e85" />  

- Kiểm tra người chơi hiện tại (X hoặc O) có 4 dấu liên tiếp theo hàng ngang hay dọc hay không.
- Sử dụng all(..) để kiểm tra từng hàng và từng cột.

### 3. Hàm checkDiagonals(player)  
- Kiểm tra hai đường chéo chính xem có toàn bộ là ký hiệu của người chơi không.

### 4. Hàm checkWinner()  
<img width="691" height="132" alt="image" src="https://github.com/user-attachments/assets/e876d4d7-4342-4f6e-aa2b-b1728a6d5119" />  

- Gọi checkLines() và checkDiagonals() cho cả 2 người chơi. Nếu tìm thấy người thắng, hiển thị thông báo và khởi động lại ván mới.
- Sau khi có người thắng, gọi start() để tạo bàn cờ mới.

### 5. Hàn checkDraw()  
<img width="382" height="90" alt="image" src="https://github.com/user-attachments/assets/bba0175a-9e7d-4c54-8280-d2921f94cf69" />  

- Kiểm tra nếu đã đánh đủ 16 nước mà chưa có ai thắng thì thông báo hòa và khởi động lại trò chơi mới.

### 6. Hàm buttonClicked(button)  
<img width="543" height="189" alt="image" src="https://github.com/user-attachments/assets/440b26d2-9091-4f05-beb6-7cc58dd852b6" />  

- Nếu ô trống: đánh dấu X hoặc O tùy theo lượt chơi.
- Tăng count và kiểm tra thắng hoặc hòa.
- Nếu đánh vào ô đã chọn trước đó thì thông báo lỗi.

### 7. Hàm start()  
<img width="779" height="261" alt="image" src="https://github.com/user-attachments/assets/df02785f-ba9c-4b57-bfc7-2309f0ca9efa" />  

- Khởi tạo lại toàn bộ trạng thái game.

### 8. Menu game  
<img width="779" height="261" alt="image" src="https://github.com/user-attachments/assets/346ebffa-425b-4bd6-b91c-a3dd3b492aa0" />  

- Tạo thanh menu cho người dùng nhấn vào nút "Restart Game" để chơi lại.

## So sánh với đoạn code trên  
### 1. Đoạn code đầu tiên (viết tay, từng nút từ button1 đến button16)  
#### Ưu điểm:  
- Tính thủ công: mỗi nút được khai báo và xử lý riêng biệt, giúp hình dung rõ vị trị từng nút và từng điều kiện thắng.
- Dễ sửa nhanh từng nút: nếu chỉ thay đổi 1 nút cụ thể, bạn có thể chỉnh đúng tên nút đó mà không ảnh hưởng đến toàn bộ.

#### Nhược điểm:  
- Mã dài dòng: viết từng dòng khiến code trở nên rườm rà, dễ mắc lỗi.
- Khó mở rộng: nếu muốn chuyển sang dạng lớn hơn, phải viết lại hoặc thêm các nút mới, tốn thời gian.

### 2. Đoạn code thứ hai (dùng từng danh sách buttons[i][j])  
#### Ưu điểm:  
- Ngắn gọn, dễ mở rộng: code chỉ viết 1 lần cho phần khởi tạo và kiểm tra, có thể dẽ dàng nâng lên ma trận cao hơn.
- Tính linh hoạt cao: các hàm như checkLines() và checkDiagonals() được tổ chức tốt, dễ tái sử dụng lại.
#### Nhược điểm:  
- Code phức tạp: với người mới học có thể gây ra khó hiểu.






















