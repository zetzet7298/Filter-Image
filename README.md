# Filter-Image
*Yêu cầu:
- Python3 --version=3.8.10, installed pip
- Các thư viện cần thiết: fitz, io, PIL, cv2, numpy. Chạy các lệnh sau để cài:
+ pip install --upgrade pip
+ pip install --upgrade pymupdf
+ pip install pillow
+ pip install opencv-python
+ pip install numpy

*Cấu trúc thư mục:
- album/ (Chứa bộ ảnh cần so sánh)
- album-pdf/ (Chứa bộ ảnh xuất từ file pdf)
- pdf.pdf (File pdf để scan ảnh)
- extract_image.py
- compare.py
- result/ (Chứa bộ ảnh sau khi so sánh)

*Các bước thực hiện chương trình
- Đưa ảnh từ thư viện bỏ vào thư mục "album"
- Chạy lệnh: python3 extract_pdf.py (Xuất ảnh từ file pdf)
- Chạy lệnh: python3 compare.py (So sánh ảnh trong "album" với ảnh trong "album-pdf")
