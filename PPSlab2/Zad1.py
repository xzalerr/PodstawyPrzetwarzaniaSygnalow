def palindrome(s):
    s = s.lower()
    s_reversed = s[::-1]
    if s == s_reversed:
        print("Podany wyraz jest palindromem.")
    else:
        print("Podany wyraz nie jest palindromem.")


string = input("Podaj wyraz, ktory chcesz sprawdzic: ")
palindrome(string)


