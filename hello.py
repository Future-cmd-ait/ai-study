import sys
print("Hello, AI Job Sprint!")
print("Python:", sys.version.split()[0])

names = ["Python", "Git", "LLM"]
for i, n in enumerate(names, 1):
    print(f"{i}. {n}")
