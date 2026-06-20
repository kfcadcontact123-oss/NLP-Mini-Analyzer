# TEXT ANALYZER USING REGEX AND BASIC NLP

(BẢN TIẾNG VIỆT Ở PHÍA TRÊN - ENGLISH VERSION BELOW)

## PHIÊN BẢN TIẾNG VIỆT

### GIỚI THIỆU

Đây là một mini project NLP được xây dựng bằng Python.

Chương trình đọc dữ liệu từ một file văn bản và thực hiện một số tác vụ xử lý ngôn ngữ tự nhiên cơ bản như:

* Đếm ký tự
* Đếm từ
* Đếm câu
* Trích xuất Email
* Trích xuất URL
* Trích xuất số điện thoại
* Thống kê các từ xuất hiện nhiều nhất

Mục tiêu của project là làm quen với Text Preprocessing, Regular Expression (Regex) và các thao tác xử lý văn bản cơ bản trong NLP.

### CẤU TRÚC THƯ MỤC

Mini_Project/

├── contacts.txt
├── results.txt
├── Mini_Analyzer.py
└── README.md
Trong đó:

* contacts.txt: dữ liệu đầu vào
* results.txt: kết quả phân tích
* Mini_Analyzer.py: chương trình chính

### THƯ VIỆN SỬ DỤNG

Project chỉ sử dụng các thư viện có sẵn của Python:

re
os

Không cần cài đặt thêm package bên ngoài.

### CÁC CHỨC NĂNG

#### Chuẩn hóa văn bản

* Chuyển toàn bộ ký tự thành chữ thường
* Loại bỏ ký tự đặc biệt
* Loại bỏ khoảng trắng dư thừa

#### Đếm ký tự

Sử dụng:
len(text)
#### Đếm từ

Sử dụng:
text.split()
#### Đếm câu: dựa theo ý tưởng đếm số dấu chấm, chấm hỏi, chấm than trong câu

Regex: r"[.?!]"

#### Trích xuất Email

Regex:
r"[A-Za-z0-9-+%_.]+@[A-Za-z0-9-.]+\.[A-Za-z]{2,}"

#### Trích xuất số điện thoại

Regex:
r"\d{10}"

#### Trích xuất URL

Regex:
r"https?://\S+"
#### Thống kê từ xuất hiện nhiều nhất

Chương trình sử dụng Dictionary để đếm số lần xuất hiện của từng từ, sau đó sắp xếp giảm dần theo tần suất.

### CÁCH CHẠY

Đặt dữ liệu cần phân tích vào file:

contacts.txt

Sau đó chạy:
"python Mini_Analyzer.py" trong bash hoặc terminal
Kết quả sẽ được ghi vào:

"results.txt"

### VÍ DỤ KẾT QUẢ

===== THỐNG KÊ =====

Số chữ: 532
Số từ: 96
Số câu: 8

===== EMAIL =====

johnsmith@gmail.com

===== URL =====

https://github.com

===== PHONE =====

0987654321

### NHỮNG GÌ MÌNH HỌC ĐƯỢC

* Đọc file
* Viết file
* Xử lý xâu
* Các hàm thông dụng
* Dictionary trong Python
* Sorting
* Hàm Lambda
* Phân tích tần suất từ
* Xử lý văn bản
* Tiền xử lý NLP

### HƯỚNG PHÁT TRIỂN

Trong tương lai mình muốn mở rộng project bằng cách:

* Hỗ trợ CSV và JSON
* Stop Word Removal
* Stemming
* Lemmatization
* Sentiment Analysis
* Named Entity Recognition
* Giao diện Streamlit
* API với FastAPI

### KẾT LUẬN

Mặc dù đây chỉ là một project NLP đơn giản, nó đã bao gồm nhiều bước quan trọng trong quá trình xử lý văn bản:

READ FILE → CLEAN TEXT → EXTRACT INFORMATION → ANALYZE → SAVE RESULT

Đây là nền tảng để tiếp tục học các chủ đề nâng cao hơn như Tokenization, Word Embeddings, Transformers và Large Language Models.

---

## ENGLISH VERSION

### INTRODUCTION

This is a beginner-friendly NLP project built with Python.

The program reads a text file and performs several basic Natural Language Processing tasks, including:

* Character counting
* Word counting
* Sentence counting
* Email extraction
* URL extraction
* Phone number extraction
* Word frequency analysis

The main goal of this project is to practice text preprocessing and Regular Expressions (Regex).

### PROJECT STRUCTURE

Mini_Project/

├── contacts.txt
├── results.txt
├── Mini_Analyzer.py
└── README.md

Files:

* contacts.txt: input text file
* results.txt: generated report
* Mini_Analyzer.py: main program

### TECHNOLOGIES USED

This project only uses Python standard libraries:
re
os

No external dependencies are required.

### FEATURES

#### Text Cleaning

* Convert text to lowercase
* Remove special characters
* Remove extra spaces

#### Character Counting

len(text)
#### Word Counting
text.split()
#### Sentence Counting

Regex:
r"[.?!]"

#### Email Extraction

Regex:
r"[A-Za-z0-9-+%_.]+@[A-Za-z0-9-.]+\.[A-Za-z]{2,}"

#### Phone Number Extraction

Regex:
r"\d{10}"

#### URL Extraction

Regex:
r"https?://\S+"

#### Word Frequency Analysis

The program counts word occurrences and sorts them by frequency in descending order.

### HOW TO RUN

Place your text inside:

contacts.txt

Run:

"python Mini_Analyzer.py" using bash or terminal


Results will be saved to:

results.txt

### SAMPLE OUTPUT

===== STATISTICS =====

Characters: 532
Words: 96
Sentences: 8

===== EMAIL =====

johnsmith@gmail.com

===== URL =====

https://github.com

===== PHONE =====

0987654321

### WHAT I LEARNED

* File Reading
* File Writing
* String Processing
* Regular Expressions
* Dictionaries
* Sorting
* Lambda Functions
* Word Frequency Analysis
* Text Cleaning
* NLP Preprocessing

### FUTURE IMPROVEMENTS

* CSV and JSON support
* Stop Word Removal
* Stemming
* Lemmatization
* Sentiment Analysis
* Named Entity Recognition
* Streamlit Interface
* FastAPI Deployment

### FINAL THOUGHTS

Although this is a simple NLP project, it already contains several important stages of a real-world text processing workflow:

READ FILE → CLEAN TEXT → EXTRACT INFORMATION → ANALYZE → SAVE RESULT

This project serves as a foundation for more advanced NLP topics such as Tokenization, Word Embeddings, Transformers, and Large Language Models.