
def get_keywords(filename):
  '''
  This function returns a list with the lines in a file 
  '''
  with open(filename) as f:
    lines = f.readlines()
  # remove whitespace characters like `\n` at the end of each line
  lines = [x.strip() for x in lines]

  return lines
