def generation(n):
    for i in range(1, n + 1, 2):
        yield i


generation_to_5 = generation(5)
print(next(generation_to_5))
print(next(generation_to_5))
print(next(generation_to_5))
print(next(generation_to_5))
print(next(generation_to_5))
