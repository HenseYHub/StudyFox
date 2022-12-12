def reverse_str(text):
    return text[::-1]

def main():
    cases = [
        ("abcd efgh", "dcba hgfe"),
        ("a1bcd efg!h", "d1cba hgf!e"),
        ("", ""),

    ]

    for text in cases:
        reversed_text = reverse_str(text)
        print(reversed_text)

if __name__ =='__main__':
    main()