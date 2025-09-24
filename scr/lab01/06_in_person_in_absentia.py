n = int(input())

on_campus = 0
online = 0

for _ in range(n):
    line = input().split()

    format_type = line[-1]
    
    if format_type == "True":
        on_campus += 1
    else :
        online += 1

print(on_campus, online)
