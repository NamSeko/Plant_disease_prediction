# AI_in_agriculture
## I. Cài đặt môi trường
Chạy lệnh `pip install -r requirements.txt` để cài đặt các thư viện cần thiết cho việc huấn luyện, dự đoán.
## II. Huấn luyện model
1. Chạy file `train-model.ipynb` để huấn luyện mô hình trên bộ dữ liệu `Train` và `Test`. Sau khi huấn luyện model sẽ được một file `best_model.pth` để sử dụng cho quá trình dự đoán.
2. Để dự đoán cần load model `best_model.pth` để lấy trọng số cho việc dự đoán.

Để phục vụ cho việc chạy app trên web local. Ta cần chuyển file `best_model.pth` vào thư mục `Seminar_app/seminar/media/`.
## III. Docker
### 1. Chạy server
1. Tài và cài đặt docker desktop.
2. Chỉnh sửa các enviroment của từng services trong file `docker_compose.yaml`.
3. Mở cửa sổ dòng lệnh tại thư mục `Seminar_app` và chạy dòng lệnh `docker-compose up --build` để đóng gói khởi động các container phuc vụ cho việc chạy app.
### 2. Sử dụng
1. Truy cập `http://localhost:8000/serminar` để truy cập vào giao diện web dự đoán.