sum_numb = 0
for dis_numb in range(123, 567):
    if (dis_numb/5 == dis_numb//5) or (dis_numb/6 == dis_numb//6):
        sum_numb += dis_numb

print(sum_numb)
