from difflib import SequenceMatcher

with open("1.txt") as file1, open("2.txt") as file2:
  file1data = file1.read()
  file2data = file2.read()
  similarityRatio = SequenceMatcher(None, file1data, file2data).ratio()
  print("Similarity between two files is :", similarityRatio*100, "per cent")
