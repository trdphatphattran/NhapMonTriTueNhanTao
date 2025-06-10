# LAB 1: THUẬT TOÁN TÌM KIẾM MÙ  
## Mục tiêu  
1. Hiểu rõ khái niệm và cơ chế hoạt động của các thuật toán tìm kiếm mù trong trí tuệ nhân tạo.
2. Thành thạo triển khai BFS và DFS trên các đồ thị vô hướng, bao gồm đồ thị không trọng số và có trọng số.
3. Phân tích hạn chế của BFS và DFS khi áp dụng trên đồ thị có trọng số.
4. Thực hiện minh họa thủ công và lập trình với chú thích rõ ràng để kiểm chứng kết quả tìm kiếm.

## Thuật toán sử dụng  
Trong bài lab này sử dụng 2 thuật toán: tìm kiếm theo chiều rộng BFS và tìm kiếm theo chiều sau DFS.  
Ngoài ra, còn làm quen với các loại đồ thị: không trọng số (các cạnh có trọng số ngầm định bằng 1, BFS tối ưu theo số cạnh) và có trọng số (các cạnh có trọng số khác nhau, BFS và DFS không được thiết kế để tối ưu hóa tổng trọng số, dẫn đến kết quả không tối ưu).  

## Bài tập minh họa  
### Bài tập về nhà  
#### Bài 1: Viết mã Python để chạy BFS và DFS trên **Đồ thị mẫu 6** và **Đồ thị mẫu 7**. Định nghĩa đồ thị dưới dạng từ điển và thêm chú thích chi tiết.  
Đồ thị mẫu 6:  
```mermaid
graph TD
    S -->|2| A
    S -->|5| C
    A -->|3| B
    A -->|4| D
    B -->|6| E
    C -->|7| D
    C -->|9| F
    D -->|8| E
    E -->|10| H
    F -->|12| G
    G -->|15| H
```
- **Các cạnh và trọng số**:
  - S-A: 2, S-C: 5, A-B: 3, A-D: 4, B-E: 6, C-D: 7, C-F: 9, D-E: 8, E-H: 10, F-G: 12, G-H: 15.
- **Đặc điểm**: Nhiều đường đi từ S đến H, có chu trình (A-D-E-B-A).

##### Đồ thị BFS trên đồ thị mẫu 6:  

Hàm BFS chính:  
![image](https://github.com/user-attachments/assets/a8c6a965-02be-407c-8378-79a32eeafb4b)  
graph: đồ thị với các cạnh có trọng số  
start: nút bắt đầu tìm kiếm  
goal: nút đích đến  

Khởi tạo hàng đợi và tập visited:  
![image](https://github.com/user-attachments/assets/3976395b-6414-4a17-9edb-aba5f0aaa6dd)  
Hàng đợi gồm có: node, path, total_weight.  

Vòng lặp chính:  
![image](https://github.com/user-attachments/assets/4d5c5f67-c444-42f9-b0f0-c9ef2067369e)  
Nếu tìm được đích thì trả về đường đi và tổng trọng số  
![image](https://github.com/user-attachments/assets/58d0f744-bd6d-4e68-88e5-c278eecb530e)    

Duyệt các nút kề của node hiện tại, nếu neighbour chưa được thăm thì thêm vào visited và xếp vào hàng đợi với đường đi mới và tổng trọng số mới.  
![image](https://github.com/user-attachments/assets/97d87895-9915-4007-a31e-40e87716b46b)  
1. Khởi tạo: Hàng đợi = [(S, [S], 0)], Đã thăm = {S}
2. Lấy S, thêm A, C: Hàng đợi = [(A, [S, A], 2), (C, [S, C], 5)], Đã thăm = {S, A, C}
3. Lấy A, thêm B, D: Hàng đợi = [(B, [S, A, B], 5), (C, [S, C], 5), (D, [S, A, D], 6)], Đã thăm = {S, A, C, B, D}
4. Lấy C, thêm F: Hàng đợi = [(B, [S, A, B], 5), (F, [S, C, F], 14), (D, [S, A, D], 6)], Đã thăm = {S, A, C, B, D, F}
5. Lấy B, thêm E: Hàng đợi = [(E, [S, A, B, E], 11), (F, [S, C, F], 14), (D, [S, A, D], 6)], Đã thăm = {S, A, C, B, D, F, E}
6. Lấy D, không có kề mới: Hàng đợi = [(F, [S, C, F], 14), (E, [S, A, B, E], 11)]
7. Lấy F, thêm G: Hàng đợi = [(E, [S, A, B, E], 11), (G, [S, C, F, G], 26)], Đã thăm = {S, A, C, B, D, F, E, G}
8. Lấy E, thêm H: Hàng đợi = [(G, [S, C, F, G], 26), (H, [S, A, B, E, H], 21)], Đã thăm = {S, A, C, B, D, F, E, G, H}
9. Lấy H: H là đích, trả về [S, A, B, E, H], trọng số 21  

Nếu không tìm thấy đường đi, trả về "return None, 0".  

Gọi đồ thị mẫu 6 có trọng số, mỗi đỉnh liên kết với các cặp (nút kề, trọng số)  
![image](https://github.com/user-attachments/assets/316e6cb2-2937-4df0-a3fd-7929ca926e09)  

Tìm đường đi BFS từ S đến H và in ra kết quả:  
![image](https://github.com/user-attachments/assets/ec60585f-5992-42bb-a68b-13eb3be78c94)  

##### Đồ thị DFS trên đồ thị mẫu 6  

Hàm DFS chính:  
![image](https://github.com/user-attachments/assets/5dbd6b7c-6c65-47f6-9cad-0ba658f06aaf)  
graph: đồ thị với các cạnh có trọng số  
start: nút bắt đầu tìm kiếm  
goal: nút đích đến  
visited: các nút đã thăm  
path: các nút đi qua  
total_weight: tổng trọng số  

Khởi tạo tập đã thăm và đường đi nếu chưa có:  
![image](https://github.com/user-attachments/assets/fda1f8f4-5ef1-4c18-b9bb-631a75ce66fa)  

Thêm đỉnh hiện tại vào tập đã thăm "visited.add(start)".  

Nếu hiện tại là đích cần đến thì trả về đường đi và tổng trọng số:  
![image](https://github.com/user-attachments/assets/48846b37-c6c1-482c-8905-a51259384621)  

Duyệt các nút kề:  
![image](https://github.com/user-attachments/assets/6a3a72f6-010f-452a-907b-db990c8164de)  
Duyệt các nút kề chưa được thăm, gọi đệ quy để tiếp tục DFS. Nếu tìm thấy đường đi thì trả về luôn.  
1. Khởi tạo: Ngăn xếp = [(S, [S], 0)], Đã thăm = {S}
2. Lấy S, thêm A: Ngăn xếp = [(A, [S, A], 2)], Đã thăm = {S, A}
3. Lấy A, thêm B: Ngăn xếp = [(B, [S, A, B], 5)], Đã thăm = {S, A, B}
4. Lấy B, thêm E: Ngăn xếp = [(E, [S, A, B, E], 11)], Đã thăm = {S, A, B, E}
5. Lấy E, thêm H: Ngăn xếp = [(H, [S, A, B, E, H], 21)], Đã thăm = {S, A, B, E, H}
6. Lấy H: H là đích, trả về [S, A, B, E, H], trọng số 21

Nếu không tìm thấy đường đi, trả về "return None, 0".  

Gọi đồ thị mẫu 6 có trọng số, mỗi đỉnh liên kết với các cặp (nút kề, trọng số)  
![image](https://github.com/user-attachments/assets/316e6cb2-2937-4df0-a3fd-7929ca926e09)  

Tìm đường đi DFS từ S đến H và in ra kết quả:  
![image](https://github.com/user-attachments/assets/c049cb37-488b-4cc2-b057-51464967693e)  

##### Kết quả khi chạy BFS và DFS:  
![image](https://github.com/user-attachments/assets/72151019-c646-4478-ab5a-33880e2f1ff8)  

Đồ thị mẫu 7:  
```mermaid
graph TD
    S --> A
    S --> D
    S --> E
    A --> B
    A --> D
    A --> E
    B --> C
    B --> E
    B --> F
    C --> F
    C --> G
    D --> E
    E --> F
    E --> H
    F --> G
    F --> H
    G --> H

```
- **Các cạnh**: S-A, S-D, S-E, A-B, A-D, A-E, B-C, B-E, B-F, C-F, C-G, D-E, E-F, E-H, F-G, F-H, G-H.
- **Đặc điểm**: Mật độ cạnh cao, nhiều chu trình, nhiều đường đi từ S đến H.

##### Đồ thị BFS trên đồ thị mẫu 7  

Hàm BFS chính:  
![image](https://github.com/user-attachments/assets/a8c6a965-02be-407c-8378-79a32eeafb4b)  
graph: đồ thị với các cạnh có trọng số  
start: nút bắt đầu tìm kiếm  
goal: nút đích đến  

Khởi tạo hàng đợi và tập visited:  
![image](https://github.com/user-attachments/assets/3976395b-6414-4a17-9edb-aba5f0aaa6dd)  
Hàng đợi gồm có: node, path, total_weight.  

Vòng lặp chính:  
![image](https://github.com/user-attachments/assets/4d5c5f67-c444-42f9-b0f0-c9ef2067369e)  
Nếu tìm được đích thì trả về đường đi và tổng trọng số  
![image](https://github.com/user-attachments/assets/58d0f744-bd6d-4e68-88e5-c278eecb530e)    

Duyệt các nút kề của node hiện tại, nếu neighbour chưa được thăm thì thêm vào visited và xếp vào hàng đợi với đường đi mới và tổng trọng số mới.  
![image](https://github.com/user-attachments/assets/97d87895-9915-4007-a31e-40e87716b46b)  
1. Khởi tạo: Hàng đợi = [(S, [S])], Đã thăm = {S}
2. Lấy S, thêm A, D, E: Hàng đợi = [(A, [S, A]), (D, [S, D]), (E, [S, E])], Đã thăm = {S, A, D, E}
3. Lấy A, thêm B: Hàng đợi = [(D, [S, D]), (E, [S, E]), (B, [S, A, B])], Đã thăm = {S, A, D, E, B}
4. Lấy D, không có kề mới (A, E đã thăm): Hàng đợi = [(E, [S, E]), (B, [S, A, B])]
5. Lấy E, thêm F, H: Hàng đợi = [(B, [S, A, B]), (F, [S, E, F]), (H, [S, E, H])], Đã thăm = {S, A, D, E, B, F, H}
6. Lấy B, thêm C: Hàng đợi = [(F, [S, E, F]), (H, [S, E, H]), (C, [S, A, B, C])], Đã thăm = {S, A, D, E, B, F, H, C}
7. Lấy F, không có kề mới (G, H đã thăm hoặc chưa tới): Hàng đợi = [(H, [S, E, H]), (C, [S, A, B, C])]
8. Lấy H: H là đích, trả về [S, E, H] 

Nếu không tìm thấy đường đi, trả về "return None, 0".  

Gọi đồ thị mẫu 6 có trọng số, mỗi đỉnh liên kết với các cặp (nút kề, trọng số)  
![image](https://github.com/user-attachments/assets/316e6cb2-2937-4df0-a3fd-7929ca926e09)  

Tìm đường đi BFS từ S đến H và in ra kết quả:  
![image](https://github.com/user-attachments/assets/ec60585f-5992-42bb-a68b-13eb3be78c94)  

##### Đồ thị DFS trên đồ thị mẫu 6  

Hàm DFS chính:  
![image](https://github.com/user-attachments/assets/5dbd6b7c-6c65-47f6-9cad-0ba658f06aaf)  
graph: đồ thị với các cạnh có trọng số  
start: nút bắt đầu tìm kiếm  
goal: nút đích đến  
visited: các nút đã thăm  
path: các nút đi qua  
total_weight: tổng trọng số  

Khởi tạo tập đã thăm và đường đi nếu chưa có:  
![image](https://github.com/user-attachments/assets/fda1f8f4-5ef1-4c18-b9bb-631a75ce66fa)  

Thêm đỉnh hiện tại vào tập đã thăm "visited.add(start)".  

Nếu hiện tại là đích cần đến thì trả về đường đi và tổng trọng số:  
![image](https://github.com/user-attachments/assets/48846b37-c6c1-482c-8905-a51259384621)  

Duyệt các nút kề:  
![image](https://github.com/user-attachments/assets/6a3a72f6-010f-452a-907b-db990c8164de)  
Duyệt các nút kề chưa được thăm, gọi đệ quy để tiếp tục DFS. Nếu tìm thấy đường đi thì trả về luôn.  
1. Khởi tạo: Ngăn xếp = [(S, [S])], Đã thăm = {S}
2. Lấy S, thêm A: Ngăn xếp = [(A, [S, A])], Đã thăm = {S, A}
3. Lấy A, thêm B: Ngăn xếp = [(B, [S, A, B])], Đã thăm = {S, A, B}
4. Lấy B, thêm C: Ngăn xếp = [(C, [S, A, B, C])], Đã thăm = {S, A, B, C}
5. Lấy C, thêm F: Ngăn xếp = [(F, [S, A, B, C, F])], Đã thăm = {S, A, B, C, F}
6. Lấy F, thêm G: Ngăn xếp = [(G, [S, A, B, C, F, G])], Đã thăm = {S, A, B, C, F, G}
7. Lấy G, thêm H: Ngăn xếp = [(H, [S, A, B, C, F, G, H])], Đã thăm = {S, A, B, C, F, G, H}
8. Lấy H: H là đích, trả về [S, A, B, C, F, G, H]

Nếu không tìm thấy đường đi, trả về "return None, 0".  

Gọi đồ thị mẫu 6 có trọng số, mỗi đỉnh liên kết với các cặp (nút kề, trọng số)  
![image](https://github.com/user-attachments/assets/316e6cb2-2937-4df0-a3fd-7929ca926e09)  

Tìm đường đi DFS từ S đến H và in ra kết quả:  
![image](https://github.com/user-attachments/assets/c049cb37-488b-4cc2-b057-51464967693e)  

##### Kết quả khi chạy BFS và DFS:  
![image](https://github.com/user-attachments/assets/943497ed-16a9-4077-8707-4256ce99b958)  

#### Bài 2  


  



































