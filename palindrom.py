# girilen değerin palidrom olup olmadığını döndürür
def is_palindrom(teststr):
    if teststr == teststr[::-1]:
        return True
    return False

run = True

while (run):
    teststr = input("Enter string to test for palindrom or 'exit': ")

# bütün yazıyı küçük harf yap
    teststr = teststr.lower()

# eğer kullanıcı 'exit' yazarsa programdan çık
    if teststr == 'exit':
        run = False
        break

# yeni bir diziye harfler ve sayılardan oluşan kısım aktarılır
    newstr = ""
    for x in teststr:
        if x.isalnum:
            newstr += x 

    print("Palindrome test: ", is_palindrom(newstr))
