#Part 1
##import hashlib
##
##code = "bgvyzdsv"
##number = 0
##result = hashlib.md5(code.encode())
##md5hash = ""
##
##while md5hash[0:5] != '00000':
##    result = code + str(number)
##    md5hash=(hashlib.md5(result.encode())).hexdigest()
##    number += 1
##print(number - 1)


#Part 2
import hashlib

code = "bgvyzdsv"
number = 0
result = hashlib.md5(code.encode())
md5hash = ""

while md5hash[0:6] != '000000':
    result = code + str(number)
    md5hash=(hashlib.md5(result.encode())).hexdigest()
    number += 1
print(number - 1)
