MOD_ADLER = 65521  # найбільше просте число менше ніж 65536


def adler32(data):
    # якщо передали рядок, перетворюємо його у байти
    if isinstance(data, str):
        data = data.encode("utf-8")

    a = 1
    b = 0

    # проходимо по кожному байту
    for byte in data:
        a = (a + byte) % MOD_ADLER
        b = (b + a) % MOD_ADLER

    # об'єднуємо b і a в одне 32-бітне число
    return (b << 16) | a


# тест
if __name__ == "__main__":
    text = "Hello"

    result = adler32(text)

    print("Text:", text)
    print("Adler-32:", hex(result))
