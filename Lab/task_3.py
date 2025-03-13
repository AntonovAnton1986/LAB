# TODO Найдите количество книг, которое можно разместить на дискете
disc_in_bytes = 1.44 * 1024 * 1024
pages = 100
lines = 50
symbols = 25
total = pages * lines * symbols
storage = total * 4
books = int(disc_in_bytes) // int(storage)

print("Количество книг, помещающихся на дискету:", books)
