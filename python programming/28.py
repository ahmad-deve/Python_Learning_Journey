words = ["ahmad","ali","ameen","hassan"]
def word_count(word):
    return len(word) >= 5
res = list(filter(word_count,words))
print(res)