s='AI is important for its potential to change how we live, work and play. It has been effectively used in business to automate tasks done by humans, including customer service work, lead generation, fraud detection and quality control. In a number of areas, AI can perform tasks much better than humans. Particularly when it comes to to repetitive, detail-oriented tasks, such as analyzing large numbers of legal documents ensure relevant fields are filled in properly, AI tools often complete jobs quickly and with relatively few errors. Because of the massive data sets it can process, AI can also give enterprises insights into their operations they might not have been aware of. The rapidly expanding population of generative AI tools will be important in fields ranging from education and marketing to product design.'
word_count=1
for i in range (len(s)):
    if s[i]==' ' or s[i]==', ' or s[i]=='. ':
        word_count+=1
print('Total words :',word_count)
sum_count=0
for i in range(65,90):
    letter_count=0
    for j in range(len(s)):
        if j==0 and s[0]==chr(i) or s[0]==chr(i+32):
            letter_count+=1
        elif s[j]==str(chr(i)) or s[j]==str(chr(i+32)):
            if s[j-1]==' ':
              letter_count+=1
    sum_count+=letter_count
    print(f'count of word {chr(i)} is {letter_count}')
print(f'Sum of total letter counts is {sum_count}')
