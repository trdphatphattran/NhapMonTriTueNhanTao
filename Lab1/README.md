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

### Đồ thị mẫu 2  

```mermaid
graph TD
    S --> A
    S --> B
    A --> B
    A --> C
    B --> D
    C --> D
    D --> G
```
- **Các cạnh**: S-A, S-B, A-B, A-C, B-D, C-D, D-G.

#### Đồ thị BFS trên đồ thị mẫu 2  

Hàm BFS chính:  
![image](https://github.com/user-attachments/assets/7222627e-0e11-4e42-b838-da1cbfe63a0e)  
graph: đồ thị với các cạnh có trọng số  
start: nút bắt đầu tìm kiếm  
goal: nút đích đến  

Khởi tạo hàng đợi và tập visited:  
![image](https://github.com/user-attachments/assets/3976395b-6414-4a17-9edb-aba5f0aaa6dd)  
Hàng đợi gồm có: node, path.  

Vòng lặp chính:  
![image](https://github.com/user-attachments/assets/887f732f-60d5-48e2-a9ac-cb49b4510a94)  
Nếu tìm được đích thì trả về đường đi  
![image](https://github.com/user-attachments/assets/7522cb34-9111-4cef-91f6-04a1a7e189bf)
 
Duyệt các nút kề của node hiện tại, nếu neighbour chưa được thăm thì thêm vào visited và xếp vào hàng đợi với đường đi mới.  
![image](https://github.com/user-attachments/assets/9881e200-faa5-401d-a05d-250b014d8b75)  
1. Khởi tạo: Hàng đợi = [(S, [S])], Đã thăm = {S}
2. Lấy S, thêm A, B: Hàng đợi = [(A, [S, A]), (B, [S, B])], Đã thăm = {S, A, B}
3. Lấy A, thêm C: Hàng đợi = [(B, [S, B]), (C, [S, A, C])], Đã thăm = {S, A, B, C}
4. Lấy B, thêm D: Hàng đợi = [(C, [S, A, C]), (D, [S, B, D])], Đã thăm = {S, A, B, C, D}
5. Lấy C, không có kề mới: Hàng đợi = [(D, [S, B, D])]
6. Lấy D, thêm G: Hàng đợi = [(G, [S, B, D, G])], Đã thăm = {S, A, B, C, D, G}
7. Lấy G: G là đích, trả về [S, B, D, G]

Nếu không tìm thấy đường đi, trả về "return None, 0".  

Gọi đồ thị mẫu 2    
![image](https://github.com/user-attachments/assets/3cdd1d7e-9af0-468b-b7cf-af8e35a22dc1)  

Tìm đường đi BFS từ S đến G và in ra kết quả:  
![image](https://github.com/user-attachments/assets/ef733b1a-3ce4-4269-9191-fd43b0abf1f1)  

Kết quả khi chạy:  
![image](https://github.com/user-attachments/assets/ed873f25-7c56-4abe-b9a4-b1cb8aa65792)  

#### Đồ thị DFS trên đồ thị mẫu 2  

Hàm DFS chính:  
![image](https://github.com/user-attachments/assets/1b08fb78-c7e4-4465-866f-0ad63fcda493)  
graph: đồ thị với các cạnh có trọng số  
start: nút bắt đầu tìm kiếm  
goal: nút đích đến  
visited: các nút đã thăm  
path: các nút đi qua  

Khởi tạo tập đã thăm và đường đi nếu chưa có:  
![image](https://github.com/user-attachments/assets/fda1f8f4-5ef1-4c18-b9bb-631a75ce66fa)  

Thêm đỉnh hiện tại vào tập đã thăm "visited.add(start)".  

Nếu hiện tại là đích cần đến thì trả về đường đi:  
![image](https://github.com/user-attachments/assets/20607bfe-5e12-4cbf-945c-5db336838b6f)

Duyệt các nút kề:  
![image](https://github.com/user-attachments/assets/93d7e092-e6d9-4cef-b1b6-96822a9d24e2)  
Duyệt các nút kề chưa được thăm, gọi đệ quy để tiếp tục DFS. Nếu tìm thấy đường đi thì trả về luôn.  
1. Khởi tạo: Ngăn xếp = [(S, [S])], Đã thăm = {S}
2. Lấy S, thêm A: Ngăn xếp = [(A, [S, A])], Đã thăm = {S, A}
3. Lấy A, thêm B: Ngăn xếp = [(B, [S, A, B])], Đã thăm = {S, A, B}
4. Lấy B, thêm D: Ngăn xếp = [(D, [S, A, B, D])], Đã thăm = {S, A, B, D}
5. Lấy D, thêm G: Ngăn xếp = [(G, [S, A, B, D, G])], Đã thăm = {S, A, B, D, G}
8. Lấy G: G là đích, trả về [S, A, B, D, G]  

Nếu không tìm thấy đường đi, trả về "return None, 0".  

Gọi đồ thị mẫu 2     
![image](https://github.com/user-attachments/assets/c0a2dab7-310b-460c-9367-f8e51eef3db6)  

Tìm đường đi DFS từ S đến G và in ra kết quả:  
![image](https://github.com/user-attachments/assets/d164a0ce-bdb0-4d57-aec9-557fdd570022)  

Kết quả khi chạy:  
![image](https://github.com/user-attachments/assets/81f7752c-b029-4c26-a4e2-935d1bd0d177)  

### Sửa mã BFS để đếm số nút đã thăm trên đồ thị mẫu 4.  
```mermaid
graph TD
    S --> A
    S --> C
    A --> B
    A --> D
    B --> E
    C --> D
    C --> F
    D --> E
    E --> G
    F --> G
```

- **Các cạnh**: S-A, S-C, A-B, A-D, B-E, C-D, C-F, D-E, E-G, F-G.

Hàm BFS chính:  
![image](https://github.com/user-attachments/assets/7222627e-0e11-4e42-b838-da1cbfe63a0e)  
graph: đồ thị với các cạnh có trọng số  
start: nút bắt đầu tìm kiếm  
goal: nút đích đến  

Khởi tạo hàng đợi và tập visited:  
![image](https://github.com/user-attachments/assets/3976395b-6414-4a17-9edb-aba5f0aaa6dd)  
Hàng đợi gồm có: node, path.  

Đếm số nút đã thăm, bắt đầu với 1: "count = 1".  

Vòng lặp chính:  
![image](https://github.com/user-attachments/assets/f956cbb5-3043-4904-884b-67d03b7c775c)  
Nếu tìm được đích, thì trả về đường đi và in ra các nút đã thăm  
![image](https://github.com/user-attachments/assets/bd442cec-41de-497f-ade5-7f1fcd2b5168)  

Duyệt qua các nút kề của nút hiện tại, nếu nút kề chưa được thăm thì thêm nút kề vào tập đã thăm và thêm nút kề và đường đi mới vào hàng đợi, tăng count vì đã tăng thêm một nút.  
![image](https://github.com/user-attachments/assets/6eceeeb0-5df2-48ff-88c3-58ac4f37ce2b)  
1. Khởi tạo: Hàng đợi = [(S, [S])], Đã thăm = {S}  
2. Lấy S, thêm A, C: Hàng đợi = [(A, [S, A]), (C, [S, C])], Đã thăm = {S, A, C}  
3. Lấy A, thêm B, D: Hàng đợi = [(B, [S, A, B]), (D, [S, A, D]), (C, [S, C])], Đã thăm = {S, A, C, B, D} 
4. Lấy C, thêm F: Hàng đợi = [(B, [S, A, B]), (D, [S, A, D]), (F, [S, C, F])], Đã thăm = {S, A, C, B, D, F}  
5. Lấy B, thêm E: Hàng đợi = [(E, [S, A, B, E]), (D, [S, A, D]), (F, [S, C, F])], Đã thăm = {S, A, C, B, D, F, E}  
6. Lấy D không có kề mới: Hàng đợi = [(E, [S, A, B, E]), (F, [S, C, F])]
7. Lấy F, thêm G: G là đích, trả về (G, [S, C, F, G])

Nếu không tìm thấy đường đi, thì trả về None và in ra tất cả các nút đã thăm.  
![image](https://github.com/user-attachments/assets/47df3bd3-f057-4ea6-a620-c9c8728f7a8c)  

Gọi đồ thị mẫu 4  
![image](https://github.com/user-attachments/assets/21ad340f-3bb8-4e41-bfb9-1ecd01b68c94)  

Chạy và in ra kết quả  
![image](https://github.com/user-attachments/assets/55768504-20da-42c2-8bb6-a653ba4a6bf8)  

Kết quả khi chạy:  
![image](https://github.com/user-attachments/assets/6418191d-5261-4c45-8709-05b8adc10565)  

#### Vẽ đồ thị hiển thị đường đi  

Hàm BFS chính:  
![image](https://github.com/user-attachments/assets/7222627e-0e11-4e42-b838-da1cbfe63a0e)  
graph: đồ thị với các cạnh có trọng số  
start: nút bắt đầu tìm kiếm  
goal: nút đích đến  

Khởi tạo hàng đợi và tập visited:  
![image](https://github.com/user-attachments/assets/3976395b-6414-4a17-9edb-aba5f0aaa6dd)  
Hàng đợi gồm có: node, path.  

Đếm số nút đã thăm, bắt đầu với 1: "count = 1".  

Vòng lặp chính:  
![image](https://github.com/user-attachments/assets/f956cbb5-3043-4904-884b-67d03b7c775c)  
Nếu tìm được đích, thì trả về đường đi và in ra các nút đã thăm  
![image](https://github.com/user-attachments/assets/bd442cec-41de-497f-ade5-7f1fcd2b5168)  

Duyệt qua các nút kề của nút hiện tại, nếu nút kề chưa được thăm thì thêm nút kề vào tập đã thăm và thêm nút kề và đường đi mới vào hàng đợi, tăng count vì đã tăng thêm một nút.  
![image](https://github.com/user-attachments/assets/6eceeeb0-5df2-48ff-88c3-58ac4f37ce2b)  
1. Khởi tạo: Hàng đợi = [(S, [S])], Đã thăm = {S}  
2. Lấy S, thêm A, C: Hàng đợi = [(A, [S, A]), (C, [S, C])], Đã thăm = {S, A, C}  
3. Lấy A, thêm B, D: Hàng đợi = [(B, [S, A, B]), (D, [S, A, D]), (C, [S, C])], Đã thăm = {S, A, C, B, D} 
4. Lấy C, thêm F: Hàng đợi = [(B, [S, A, B]), (D, [S, A, D]), (F, [S, C, F])], Đã thăm = {S, A, C, B, D, F}  
5. Lấy B, thêm E: Hàng đợi = [(E, [S, A, B, E]), (D, [S, A, D]), (F, [S, C, F])], Đã thăm = {S, A, C, B, D, F, E}  
6. Lấy D không có kề mới: Hàng đợi = [(E, [S, A, B, E]), (F, [S, C, F])]
7. Lấy F, thêm G: G là đích, trả về (G, [S, C, F, G])

Nếu không tìm thấy đường đi, thì trả về None và in ra tất cả các nút đã thăm.  
![image](https://github.com/user-attachments/assets/47df3bd3-f057-4ea6-a620-c9c8728f7a8c)  

Gọi đồ thị mẫu 4  
![image](https://github.com/user-attachments/assets/21ad340f-3bb8-4e41-bfb9-1ecd01b68c94)  

Chạy và in ra kết quả  
![image](https://github.com/user-attachments/assets/55768504-20da-42c2-8bb6-a653ba4a6bf8)  

Khai báo thư viện:  
![image](https://github.com/user-attachments/assets/b9f285e1-22f1-44cc-b8b6-a27f447a0e03)  

Tạo đồ thị có hướng, sử dụng DiGraph().  

Thêm các cạnh:  
![image](https://github.com/user-attachments/assets/1740396c-e491-4b4e-89d1-e6015b8fa964)  
Mỗi cặp (node, neighbor) được thêm vào đồ thị G dưới dạng cạnh có hướng từ node đến neighbor.  

Tạo layout:  "pos = nx.spring_layout(G, seed=42)"  
Dùng thuật toán spring_layout để bố trí nút, seed = 42 để đảm bảo bố cục ổn định.  

Vẽ đồ thị:  
![image](https://github.com/user-attachments/assets/883824d4-857b-423b-8996-f5609474d7a8)  
with_labels=True: hiện nhãn các đỉnh.  
node_color='lightblue': màu của các đỉnh mặc định.  
edge_color='gray': màu các cạnh bình thường.  
node_size, font_size, arrowsize: điều chỉnh kích cỡ nút, chữ, mũi tên.  

Các cộng trong đường đi sẽ có màu đỏ  
![image](https://github.com/user-attachments/assets/4ab53b2a-5a41-4221-a88f-5f75a8ee33d2)  
Các đỉnh thuộc đường đi được tô màu cam  
![image](https://github.com/user-attachments/assets/f2c29233-91fc-48ce-b061-adf9fb13a7e1)  

Đặt tiêu đề và hiển thị hình ảnh  
![image](https://github.com/user-attachments/assets/a62d0fd6-7870-4f41-8412-07b71a28cca3)  

Kết quả khi chạy:  
![image](https://github.com/user-attachments/assets/3a038317-30da-442f-823a-b9fb1539b1ab)  

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
![image](https://github.com/user-attachments/assets/7222627e-0e11-4e42-b838-da1cbfe63a0e)  
graph: đồ thị với các cạnh có trọng số  
start: nút bắt đầu tìm kiếm  
goal: nút đích đến  

Khởi tạo hàng đợi và tập visited:  
![image](https://github.com/user-attachments/assets/3976395b-6414-4a17-9edb-aba5f0aaa6dd)  
Hàng đợi gồm có: node, path.  

Vòng lặp chính:  
![image](https://github.com/user-attachments/assets/887f732f-60d5-48e2-a9ac-cb49b4510a94)  
Nếu tìm được đích thì trả về đường đi  
![image](https://github.com/user-attachments/assets/7522cb34-9111-4cef-91f6-04a1a7e189bf)
 
Duyệt các nút kề của node hiện tại, nếu neighbour chưa được thăm thì thêm vào visited và xếp vào hàng đợi với đường đi mới.  
![image](https://github.com/user-attachments/assets/9881e200-faa5-401d-a05d-250b014d8b75)
1. Khởi tạo: Hàng đợi = [(S, [S])], Đã thăm = {S}
2. Lấy S, thêm A, D, E: Hàng đợi = [(A, [S, A]), (D, [S, D]), (E, [S, E])], Đã thăm = {S, A, D, E}
3. Lấy A, thêm B: Hàng đợi = [(D, [S, D]), (E, [S, E]), (B, [S, A, B])], Đã thăm = {S, A, D, E, B}
4. Lấy D, không có kề mới (A, E đã thăm): Hàng đợi = [(E, [S, E]), (B, [S, A, B])]
5. Lấy E, thêm F, H: Hàng đợi = [(B, [S, A, B]), (F, [S, E, F]), (H, [S, E, H])], Đã thăm = {S, A, D, E, B, F, H}
6. Lấy B, thêm C: Hàng đợi = [(F, [S, E, F]), (H, [S, E, H]), (C, [S, A, B, C])], Đã thăm = {S, A, D, E, B, F, H, C}
7. Lấy F, không có kề mới (G, H đã thăm hoặc chưa tới): Hàng đợi = [(H, [S, E, H]), (C, [S, A, B, C])]
8. Lấy H: H là đích, trả về [S, E, H] 

Nếu không tìm thấy đường đi, trả về "return None, 0".  

Gọi đồ thị mẫu 7  
![image](https://github.com/user-attachments/assets/8afd4dcd-e685-4a0c-b71f-99ca6f9f5455)

Tìm đường đi BFS từ S đến H và in ra kết quả:  
![image](https://github.com/user-attachments/assets/805d0707-5916-4955-a968-efdb26b44cf8)  

##### Đồ thị DFS trên đồ thị mẫu 7  

Hàm DFS chính:  
![image](https://github.com/user-attachments/assets/1b08fb78-c7e4-4465-866f-0ad63fcda493)  
graph: đồ thị với các cạnh có trọng số  
start: nút bắt đầu tìm kiếm  
goal: nút đích đến  
visited: các nút đã thăm  
path: các nút đi qua  

Khởi tạo tập đã thăm và đường đi nếu chưa có:  
![image](https://github.com/user-attachments/assets/fda1f8f4-5ef1-4c18-b9bb-631a75ce66fa)  

Thêm đỉnh hiện tại vào tập đã thăm "visited.add(start)".  

Nếu hiện tại là đích cần đến thì trả về đường đi:  
![image](https://github.com/user-attachments/assets/20607bfe-5e12-4cbf-945c-5db336838b6f)

Duyệt các nút kề:  
![image](https://github.com/user-attachments/assets/93d7e092-e6d9-4cef-b1b6-96822a9d24e2)  
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

Gọi đồ thị mẫu 7   
![image](https://github.com/user-attachments/assets/de01fb96-258d-4329-89dd-f3a21b390480)  
 
Tìm đường đi DFS từ S đến H và in ra kết quả:  
![image](https://github.com/user-attachments/assets/352fa980-535f-4fc1-8e6b-1e32780416de)

##### Kết quả khi chạy BFS và DFS:  
![image](https://github.com/user-attachments/assets/943497ed-16a9-4077-8707-4256ce99b958)  

#### Bài 2  
Hàm BFS chính:  
![image](https://github.com/user-attachments/assets/e7f26471-0a5b-4b7f-87c6-bd96d6861012)  
graph: đồ thị với các cạnh có trọng số  
start: nút bắt đầu tìm kiếm  
goal: nút đích đến  

Khởi tạo hàng đợi và danh sách các đường đi từ start đến goal:  
![image](https://github.com/user-attachments/assets/74c7a0a1-48df-4534-811f-52f71db995b4)  

Vòng lặp chính:  
![image](https://github.com/user-attachments/assets/4e2113bf-c147-4341-ac15-d6b161bff22a)  
Nếu tìm được đích thì thêm vào danh sách  
![image](https://github.com/user-attachments/assets/6f2ec599-c076-45cd-8a70-d3a0fe5be2d7)  
Không return vì phải tìm tất cả đường đi, nên sẽ tiếp tục duyệt các phần tử còn lại
   
Duyệt các nút kề của node hiện tại, nếu neighbour không có đường đi hiện tại thì thêm nút kề và đường đi mới vào hàng đợi.  
![image](https://github.com/user-attachments/assets/0ebeafe7-c960-415c-b66c-8de481a2a9bf)  

Sau khi tìm thấy đường đi thì trả về "return all_paths".  

Gọi đồ thị mẫu 7 không trọng số  
![image](https://github.com/user-attachments/assets/544e0f01-f553-4e55-ad0a-082a81784614)  

Tìm tất cả đường đi BFS từ S đến H và in ra kết quả:  
![image](https://github.com/user-attachments/assets/ae9ede55-ff53-4c97-9c36-84c70a6d1897)  

##### Kết quả:  
![image](https://github.com/user-attachments/assets/b4264dce-5eaa-4eea-87a5-87be02b7a8ba)  

#### Bài 3  
```mermaid
graph TD
    S -->|2| A
    S -->|5| C
    A -->|3| B
    A -->|4| D
    B -->|6| E
    B -->|20| H
    C -->|7| D
    C -->|9| F
    D -->|8| E
    E -->|10| H
    F -->|12| G
    G -->|15| H
```
- **Các cạnh và trọng số**:
  - S-A: 2, S-C: 5, A-B: 3, A-D: 4, B-E: 6, B-H: 20, C-D: 7, C-F: 9, D-E: 8, E-H: 10, F-G: 12, G-H: 15.
 
##### Đồ thị BFS  

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
5. Lấy B, thêm E, H: Hàng đợi = [(E, [S, A, B, E], 11), (H, [S, A, B, H], 25), (F, [S, C, F], 14), (D, [S, A, D], 6)], Đã thăm = {S, A, C, B, D, F, E, H}
6. Lấy D, không có kề mới: Hàng đợi = [(F, [S, C, F], 14), (E, [S, A, B, E], 11)]
7. Lấy F, thêm G: Hàng đợi = [(E, [S, A, B, E], 11), (H, [S, A, B, H], 25), (G, [S, C, F, G], 26)], Đã thăm = {S, A, C, B, D, F, E, H, G}
8. Lấy E, thêm H: H là đích, trả về [S, A, B, H], 25  

Nếu không tìm thấy đường đi, trả về "return None, 0".  

Gọi đồ thị mẫu 6 có trọng số, mỗi đỉnh liên kết với các cặp (nút kề, trọng số)  
![image](https://github.com/user-attachments/assets/bb5269a4-3c1a-470f-9b6a-88c885935936)  
  
Tìm đường đi BFS từ S đến H và in ra kết quả:  
![image](https://github.com/user-attachments/assets/571e516c-9c4b-433f-8e52-ea30df592837)  

##### Đồ thị DFS  
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
![image](https://github.com/user-attachments/assets/9a1fe046-574f-48fa-b327-45fd0bf73bcf)  
  
Tìm đường đi DFS từ S đến H và in ra kết quả:  
![image](https://github.com/user-attachments/assets/96697dc2-1a3d-46b4-ae73-909f87dc9979)  

##### Kết quả khi chạy BFS và DFS:  
![image](https://github.com/user-attachments/assets/f0d63db4-aa46-436b-9074-3f4b33042b54)  

#### Phân tích sự thay đổi  
- Đường đi BFS thay đổi từ [S, A, B, E, H] thành [S, A, B, H], tổng trọng số thay đổi từ 21 sang 25. Vì BFS không quan tâm đến trọng số, nó chỉ quan tâm đến số cạnh nên dù thêm B --> |20| H có thêm trọng số, nhưng [S, A, B, H] vẫn là đường đi ngắn nhất (dù trọng số lớn hơn).
- Đường đi DFS không thay đổi, vẫn là [S, A, B, E, H] trọng số 21. Vì DFS tìm kiếm sâu theo nhánh nên các nút kề sẽ được duyệt thoe thứ tự trong danh sách. Vì E nằm trước H trong danh sách, nên DFS sẽ đi qua E trước rồi sau đó mới tới H.


### Bài tập nâng cao  
#### Câu 1  
##### Đo thời gian chạy của BFS trên đồ thị mẫu 6  

Gọi hàm time bằng câu lệnh "import time".  
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

Đo thời gian chạy của BFS  
start_bfs: thời điểm bắt đầu chạy của thuật toán, ở đây sử dụng hàm time.perf_counter() vì hàm này cho độ chính xác cao khi đo thời gian.  

path_bfs, weight_bfs: trả về các đỉnh được tạo trên đường đi từ S -> H và tổng trọng số của nó.  

end_bfs: thời điểm kết thúc của thuật toám, ở đây cũng sử dụng hàm time.perf_counter().  

time_bfs = end_bfs - start_bfs: thời gian chạy thực tế = thời gian kết thúc = thời gian bắt đầu.  

Sau cùng, in ra thời gian chạy thực tế và làm tròn đến 5 chữ số thập phân {time_bfs:.5f}.  

##### Đo thời gian chạy của DFS trên đồ thị mẫu 6  

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

Đo thời gian chạy của DFS  
start_dfs: thời điểm bắt đầu chạy của thuật toán, ở đây sử dụng hàm time.perf_counter() vì hàm này cho độ chính xác cao khi đo thời gian.  

path_dfs, weight_dfs: trả về các đỉnh được tạo trên đường đi từ S -> H và tổng trọng số của nó.  

end_dfs: thời điểm kết thúc của thuật toám, ở đây cũng sử dụng hàm time.perf_counter().  

time_dfs = end_dfs - start_dfs: thời gian chạy thực tế = thời gian kết thúc = thời gian bắt đầu.  

Sau cùng, in ra thời gian chạy thực tế và làm tròn đến 5 chữ số thập phân {time_bds:.5f}.  

So sánh thời gian của BFS và DFS:  
![image](https://github.com/user-attachments/assets/c64f737f-05a0-495f-95df-0eda98a27259)  

Kết quả khi chạy:  
![image](https://github.com/user-attachments/assets/ac833505-6311-4da1-8bc0-543ed71637b0)  

BFS chạy chậm hơn DFS vì lí do sau:  
- BFS phải duyệt tất cả các đỉnh cùng mức, có nghĩa là nó sẽ thăm nhiều đỉnh hơn trước khi đến đích -> tốn nhiều thời gian.
- DFS đi sâu theo nhánh mà không cần duyệt các đỉnh cùng mức, nên nó sẽ chỉ đi qua một vài đỉnh trước khi đến đích -> tốn ít thời gian.

##### Đo thời gian chạy của BFS trên đồ thị mẫu 7  

Gọi hàm time bằng câu lệnh "import time".  

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
Nếu tìm được đích thì trả về đường đi  
![image](https://github.com/user-attachments/assets/7522cb34-9111-4cef-91f6-04a1a7e189bf)
 
Duyệt các nút kề của node hiện tại, nếu neighbour chưa được thăm thì thêm vào visited và xếp vào hàng đợi với đường đi mới.  
![image](https://github.com/user-attachments/assets/9881e200-faa5-401d-a05d-250b014d8b75)
1. Khởi tạo: Hàng đợi = [(S, [S])], Đã thăm = {S}
2. Lấy S, thêm A, D, E: Hàng đợi = [(A, [S, A]), (D, [S, D]), (E, [S, E])], Đã thăm = {S, A, D, E}
3. Lấy A, thêm B: Hàng đợi = [(D, [S, D]), (E, [S, E]), (B, [S, A, B])], Đã thăm = {S, A, D, E, B}
4. Lấy D, không có kề mới (A, E đã thăm): Hàng đợi = [(E, [S, E]), (B, [S, A, B])]
5. Lấy E, thêm F, H: Hàng đợi = [(B, [S, A, B]), (F, [S, E, F]), (H, [S, E, H])], Đã thăm = {S, A, D, E, B, F, H}
6. Lấy B, thêm C: Hàng đợi = [(F, [S, E, F]), (H, [S, E, H]), (C, [S, A, B, C])], Đã thăm = {S, A, D, E, B, F, H, C}
7. Lấy F, không có kề mới (G, H đã thăm hoặc chưa tới): Hàng đợi = [(H, [S, E, H]), (C, [S, A, B, C])]
8. Lấy H: H là đích, trả về [S, E, H] 

Nếu không tìm thấy đường đi, trả về "return None, 0".  

Gọi đồ thị mẫu 7  
![image](https://github.com/user-attachments/assets/8afd4dcd-e685-4a0c-b71f-99ca6f9f5455)

Tìm đường đi BFS từ S đến H và in ra kết quả:  
![image](https://github.com/user-attachments/assets/805d0707-5916-4955-a968-efdb26b44cf8)  

Đo thời gian chạy của BFS  
start_bfs: thời điểm bắt đầu chạy của thuật toán, ở đây sử dụng hàm time.perf_counter() vì hàm này cho độ chính xác cao khi đo thời gian.  

path_bfs: trả về các đỉnh được tạo trên đường đi từ S -> H.  

end_bfs: thời điểm kết thúc của thuật toám, ở đây cũng sử dụng hàm time.perf_counter().  

time_bfs = end_bfs - start_bfs: thời gian chạy thực tế = thời gian kết thúc = thời gian bắt đầu.  

Sau cùng, in ra thời gian chạy thực tế và làm tròn đến 7 chữ số thập phân {time_bfs:.7f}.  

##### Đo thời gian chạy của DFS trên đồ thị mẫu 7  

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

Nếu hiện tại là đích cần đến thì trả về đường đi:  
![image](https://github.com/user-attachments/assets/20607bfe-5e12-4cbf-945c-5db336838b6f)

Duyệt các nút kề:  
![image](https://github.com/user-attachments/assets/93d7e092-e6d9-4cef-b1b6-96822a9d24e2)  
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

Gọi đồ thị mẫu 7   
![image](https://github.com/user-attachments/assets/de01fb96-258d-4329-89dd-f3a21b390480)  
 
Tìm đường đi DFS từ S đến H và in ra kết quả:  
![image](https://github.com/user-attachments/assets/352fa980-535f-4fc1-8e6b-1e32780416de)  

start_dfs: thời điểm bắt đầu chạy của thuật toán, ở đây sử dụng hàm time.perf_counter() vì hàm này cho độ chính xác cao khi đo thời gian.  

path_dfs: trả về các đỉnh được tạo trên đường đi từ S -> H.  

end_dfs: thời điểm kết thúc của thuật toám, ở đây cũng sử dụng hàm time.perf_counter().  

time_dfs = end_dfs - start_dfs: thời gian chạy thực tế = thời gian kết thúc = thời gian bắt đầu.  

Sau cùng, in ra thời gian chạy thực tế và làm tròn đến 7 chữ số thập phân {time_dfs:.7f}.  

Kết quả khi chạy:  
![image](https://github.com/user-attachments/assets/bd16aa81-f6dc-4cb4-acb1-9430b894c64f)  
![image](https://github.com/user-attachments/assets/4a5aec34-34a5-4bb7-9ba7-8df1e2a6053c)  

Ở đây, có thể xảy ra 2 trường hợp:
- BFS đi chậm hơn DFS vì BFS phải duyệt tất cả các đỉnh cùng mức, có nghĩa là nó sẽ thăm nhiều đỉnh hơn trước khi đến đích -> tốn nhiều thời gian. DFS đi sâu theo nhánh mà không cần duyệt các đỉnh cùng mức, nên nó sẽ chỉ đi qua một vài đỉnh trước khi đến đích -> tốn ít thời gian.
- DFS đi chậm hơn BFS vì DFS đôi khi có thể đi sai nhánh thì phải quay lại đi từ đầu để tiếp tục thử nhánh khác -> tốn nhiều thời gian. BFS duyệt theo mức nên nếu đích nằm gần điểm bắt đầu thì BFS sẽ tìm thấy nhanh hơn -> tốn ít thời gian.

#### Câu 2  
```mermaid
graph TD
    S --> |2| A
    S --> |4| B
    S --> |5| C
    A --> |3| C
    A --> |6| D
    B --> |7| D
    B --> |9| E
    C --> |10| F
    C --> |8| G
    D --> |12| H
    E --> |14| F
    E --> |15| H
    F --> |11| I
    G --> |9| H
    H --> |14| I
```

Các cạnh: S-A: 2, S-B: 4, S-C: 5, A-C: 3, A-B: 7, B-D: 9, B-C: 12, C-E: 10, C-G: 8, D-G: 15, E-H: 7, E-I: 5, F-G: 8, F-H: 16, G-F: 11, G-I: 7.  
Đường đi: Từ S -> I.  

##### Đồ thị BFS  

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
2. Lấy S, thêm A, B, C: Hàng đợi = [(A, [S, A], 2), (B, [S, B], 4), (C, [S, C], 5)], Đã thăm = {S, A, B, C}  
3. Lấy A, thêm D: Hàng đợi = [(B, [S, A, B], 4), (C, [S, C], 5), (D, [S, A, D], 8)], Đã thăm = {S, A, B, C, D}  
4. Lấy B, thêm E: Hàng đợi = [(E, [S, B, E], 13), (C, [S, C], 5), (D, [S, A, D], 8)], Đã thăm = {S, A, B, C, D, E}  
5. Lấy C, thêm F, G: Hàng đợi = [(E, [S, B, E], 13), (F, [S, C, F], 15), (G, [S, C, G], 13), (D, [S, A, D], 8)], Đã thăm = {S, A, B, C, D, E, F, G}  
6. Lấy D, thêm H: Hàng đợi = [(E, [S, B, E], 13), (F, [S, C, F], 15), (G, [S, C, G], 13), (H, [S, A, D, H], 20)], Đã thăm = {S, A, B, C, D, E, F, G, H}  
7. Lấy E, không có kề mới: Hàng đợi = [(F, [S, C, F], 15), (G, [S, C, G], 13), (H, [S, A, D, H], 20)]
8. Lấy F, thêm I: I là đích, trả về [S, C, F, I], trọng số: 26.  

Nếu không tìm thấy đường đi, trả về "return None, 0".  

Gọi đồ thị có trọng số, mỗi đỉnh liên kết với các cặp (nút kề, trọng số)  
![image](https://github.com/user-attachments/assets/e5337010-f4a5-4c43-ac14-b31612b28e25)  

Tìm đường đi BFS từ S đến I và in ra kết quả:  
![image](https://github.com/user-attachments/assets/8b603998-a962-4632-b532-6089bdfb6608)  

##### Đồ thị DFS   

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
3. Lấy A, thêm C: Ngăn xếp = [(C, [S, A, C], 5)], Đã thăm = {S, A, C}
4. Lấy C, thêm F: Ngăn xếp = [(F, [S, A, C, F], 15)], Đã thăm = {S, A, C, F}
5. Lấy F, thêm I: I là đích, trả về [S, A, C, F, I], trọng số: 26  

Nếu không tìm thấy đường đi, trả về "return None, 0".  

Gọi đồ thị có trọng số, mỗi đỉnh liên kết với các cặp (nút kề, trọng số)  
![image](https://github.com/user-attachments/assets/df88fe1c-b193-4f42-82c3-031a1224ede4)  

Tìm đường đi DFS từ S đến H và in ra kết quả:  
![image](https://github.com/user-attachments/assets/47730851-59e8-47cf-9991-42118ca6f95e)

##### Kết quả khi chạy BFS và DFS:  
![image](https://github.com/user-attachments/assets/fd2cb138-ebc2-4db0-9107-bd47c80d8535)







































 

 
  








  



































