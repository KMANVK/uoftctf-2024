# Hourglass : 

+ Check web history => file setting.txt có chứa base64 => decode ra flag

# No Grep : 

+ Check web history => File `update.ps1` : 

```
$String_Key = 'W0wMadeitthisfar'

$NewValue = '$(' + (([int[]][char[]]$String | ForEach-Object { "[char]$($_)" }) -join '+') + ')'

$chars = 34, 95, 17, 57, 2, 16, 3, 18, 68, 16, 12, 54, 4, 82, 24, 45, 35, 0, 40, 63, 20, 10, 58, 25, 3, 65, 0, 20

$keyAscii = $String_Key.ToCharArray() | ForEach-Object { [int][char]$_ }

$resultArray = $chars -bxor $keyAscii
```

=> Dựa vào đó viết code giải mã nó : 

```
string_key = 'W0wMadeitthisfar'
key_ascii = [ord(char) for char in string_key]

x = [34, 95, 17, 57, 2, 16, 3, 18, 68, 16, 12, 54, 4, 82, 24, 45, 35, 0, 40, 63, 20, 10, 58, 25, 3, 65, 0, 20]

flag = ""
c = 0
for n in range(len(x)):
    if c > len(key_ascii) - 1:
        c = 0
    flag += chr(x[n] ^ key_ascii[c])
    c += 1
print(flag)

# c2 : 

# String_Key = 'W0wMadeitthisfar'
# chars = [34, 95, 17, 57, 2, 16, 3, 18, 68, 16, 12, 54, 4, 82, 24, 45, 35, 0, 40, 63, 20, 10, 58, 25, 3, 65, 0, 20]

# keyAscii = [ord(char) for char in String_Key]
# resultArray = [char ^ keyAscii[index % len(keyAscii)] for index, char in enumerate(chars)]

# decoded_string = ''.join(chr(char) for char in resultArray)
# print(decoded_string)
```