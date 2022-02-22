def generation(i_1, i_2):
    remains = len(i_1) - len(i_2)
    if remains > 0:
        for _ in range(remains):
            i_2.append(None)
    for tutors, klass in zip(i_1, i_2):
        yield tutors, klass


tutors = [
    'Иван', 'Алексей', 'Борис', 'Мария', 'Анастасия', 'Никита', 'Максим', 'Илья'
]
klass = [
    '7B', '6A', '9E', '8C', '9A', '10B'
]
print(*generation(tutors, klass))
