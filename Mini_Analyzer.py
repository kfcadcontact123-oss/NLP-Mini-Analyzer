import re
import os

INPUT = "contacts.txt"
OUTPUT = "results.txt"

base_dir = os.path.dirname(__file__)
in_path = os.path.join(base_dir, INPUT)
out_path = os.path.join(base_dir, OUTPUT)

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    text = text.strip()
    return text
def count_characters(text):
    return len(text)
def count_words(text):
    words = text.strip()
    return(len(words))
def count_sentences(text):
    sentences = re.findall(r"[.?!]", text)
    return len(sentences)
def extract_email(text):
    email = re.findall(r"[A-Za-z0-9-+%_.]+@[A-Za-z0-9-.]+\.[A-Za-z]{2,}", text)
    for e in email:
        print(e+"\n")
    return
def extract_phones(text):
    phone = re.findall(r"\d{10}", text)
    for p in phone:
        print(p+"\n")
    return
def extract_url(text):
    url = re.findall(r"https?://\S+", text)
    for u in url:
        print(u +"\n")
    return
def top_words(text): #một từ xuất hiện mấy lần
    counter = {}
    words = text.split()
    for word in words:
        if word not in counter:
            counter[word] = 0
        counter[word]+= 1
    sorted_words = sorted(#sorted xếp tăng dần nên reverse = True nghĩa là xếp giảm dần
        counter.items(),
        #counter.items() sẽ có dạng (word, counter[word])
        key = lambda x:x[1], 
        #lambda này đang làm việc lấy phần tử thứ hai trong mỗi x, hay là counter.items()
        reverse = True
    )
    for i in range(10):
        the_word, count = sorted_words[i]
        print(f"{the_word}: {count}")
    return
def main(text):
    output = f'''===== THỐNG KÊ =====
Số chữ: {count_characters(text)}
Số từ: {count_words(text)}
Số câu: {count_sentences(text)}

===== EMAIL =====
{extract_email(text)}

===== URL =====
{extract_url(text)}

===== PHONE =====
{extract_phones(text)}

===== TOP WORDS ===== 
{top_words(text)}
'''
    return output
with open(in_path, "r", encoding = "utf-8") as file:
    text = file.read()
with open(out_path, "w", encoding = "utf-8") as file:
    file.write(main(text))