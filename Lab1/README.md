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

Duyệt các nút kề (DFS đệ quy):  
![image](https://github.com/user-attachments/assets/6a3a72f6-010f-452a-907b-db990c8164de)  
Duyệt các nút kề chưa được thăm, gọi đệ quy để tiếp tục DFS. Nếu tìm thấy đường đi thì trả về luôn.  

Nếu không tìm thấy đường đi, trả về "return None, 0".  

Gọi đồ thị mẫu 6 có trọng số, mỗi đỉnh liên kết với các cặp (nút kề, trọng số)  
![image](https://github.com/user-attachments/assets/316e6cb2-2937-4df0-a3fd-7929ca926e09)  

Tìm đường đi DFS từ S đến H và in ra kết quả:  
![image](https://github.com/user-attachments/assets/c049cb37-488b-4cc2-b057-51464967693e)































