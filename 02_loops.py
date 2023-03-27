count = 0

while count <= 5:
    print(count)
    count += 1

extern_count = 0
intern_count = 0

while extern_count < 5:
    while intern_count < 6:
        print(extern_count, intern_count)
        intern_count += 1

        if intern_count >= 3:
            break
        
    extern_count += 1
    intern_count = 0