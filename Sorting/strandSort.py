def strand_sort(inp):
  output = strand(inp)
  while len(inp):
    output = merge(output, strand(inp))
  return output
   
   
def strand(inp):
  element, sub = 0, [inp.pop(0)]
  while element < len(inp):
    if inp[element] > sub[-1]:
      sub.append(inp.pop(element))
    else:
      element += 1
  return sub
  
def merge(a, b):
  output = []
  while len(a) and len(b):
    if a[0] < b[0]:
      output.append(a.pop(0))
    else:
      output.append(b.pop(0))
  output += a
  output += b
  return output
  
inputs = [9,2,0,4,1,8,2,3,7]
print("Input List:")
print(inputs)
 
output = strand_sort(inputs)
print("Output List:")
print(output)
