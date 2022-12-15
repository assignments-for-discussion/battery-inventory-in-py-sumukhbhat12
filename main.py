
def count_batteries_by_usage(cycles):
  #dictionary to count the batteries with lowcount, mediumcount and highcount
  dic = {
    "lowCount": 0,
    "mediumCount": 0,
    "highCount": 0
  }
  for battery in cycles:
    if battery < 0:
      #if any of the battery is negative ignore as it is an illegal input
      
    #if the battery is below 310, increase the lowcount by 1
    elif battery < 310:
      dic["lowCount"] += 1
    #if the battery is between 310 and 930 increase the midcount by 1
    elif battery >= 310 and battery < 930:
      dic["mediumCount"] += 1
    #if the battery is more than 930, increase the highcount by 1
    elif battery >= 930:
      dic["highCount"] += 1
  return dic


def test_bucketing_by_number_of_cycles():
  print("Counting batteries by usage cycles...\n");
  counts = count_batteries_by_usage([100, 300, 500, 600, 900, 1000])
  assert(counts["lowCount"] == 2)
  assert(counts["mediumCount"] == 3)
  assert(counts["highCount"] == 1)
  
  #If the input is empty
  counts = count_batteries_by_usage([])
  assert(counts["lowCount"] == 0)
  assert(counts["mediumCount"] == 0)
  assert(counts["highCount"] == 0)
  
  #Boundary cases
  counts = count_batteries_by_usage([310,930])
  assert(counts["lowCount"] == 0)
  assert(counts["mediumCount"] == 1)
  assert(counts["highCount"] == 1)
  print("Done counting :)")
  
  #Invalid input
  counts = count_batteries_by_usage([-5])
  assert(counts["lowCount"] == 0)
  assert(counts["mediumCount"] == 0)
  assert(counts["highCount"] == 0)
  print("Done counting :)")

if __name__ == '__main__':
  test_bucketing_by_number_of_cycles()
