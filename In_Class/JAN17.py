string = "CPEN 333 || FRI 13:00 - 15:00 || CEME 2002 \n CPEN 333 || MON 13:00 - 15:00 || CEME 2002"
string = string.replace("\n", "||")

info = string.split("||")

print(info)