# Open the input file in read mode
with open("merged.txt", "r") as infile:
  # Read the contents of the file
  contents = infile.read()

# Open the output file in write mode
with open("backup.txt", "w") as outfile:
  # Write the contents of the input file to the output file
  outfile.write(contents)
