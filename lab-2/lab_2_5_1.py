import os


example_dir = "./example"
word, counter = input(), 0

for filname in os.listdir(example_dir):
    if word in filname:
        counter += 1
print(counter)
