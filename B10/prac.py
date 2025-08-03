import string


# dem so lan tu xuat hien trong 1 doan van ban
def count_words(paragraph):
    # thay doi thanh chu thuong
    paragraph = paragraph.lower()
    
    # loai dau cau
    for char in string.punctuation:
        paragraph = paragraph.replace(char, "")
        
    # tach tu
    words = paragraph.split()
    
    # dem tan suat
    word_count = {} # dict
    for word in words:
        if word in word_count:
            word_count[word] += 1 # cong 1 lan dem
        else:
            word_count[word] = 1 # dem 1 lan
            
    return word_count

p= "They rushed out the door, grabbing anything and everything they could think of they might need. There was no time to double-check to make sure they weren't leaving something important behind. Everything was thrown into the car and they sped off. Thirty minutes later they were safe and that was when it dawned on them that they had forgotten the most important thing of all."
result = count_words(pảagraph=p)
# hien thi danh sach theo thu tu chu cai
max = 0
word_count_max = ""
for word, counter in sorted(result.items()):
    print(f"{word}: {counter}")
    if counter > max:
        max = counter
        word_count_max = word
        
print(f"Tu voi so lan lap cao nhat:{word_count_max}, lap {max} lan")

    