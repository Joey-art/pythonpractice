import wikipedia
Naruto = wikipedia.page("Naruto", auto_suggest=False)
print(Naruto.summary)
print(Naruto.section("Part 1"))
print(Naruto.images)
print(len(Naruto.images))
print(Naruto.content)