import distorm3
#Taken from there https://www.youtube.com/watch?v=iwRSFlZoSCM

FILE = "input_file"
FILE_OFF_START = 0x1000
FILE_OFF_END = 0x8e32c

VA = 0x401000 - 0x1000
UNIQ = {}

def DecodeAsm(pc, d):

  dis = distorm3.Decode(pc, d, distorm3.Decode64Bits) #change 64 with 32 if binary is 32 bit

  k = []
  l = ""
  ist = ""
  for d in dis:
    addr = d[0]
    size = d[1]
    inst = d[2].lower()
    t = "0x%x   %s" % (addr, inst)
    l+= t+ "\n"
    ist += "%s\n" % (inst)
    k.append((addr,inst))

    if inst.find('ret') != -1:
      break

  return (l,k,ist)

d = open(FILE,"rb").read()

for i in range(FILE_OFF_START, FILE_OFF_END):
  (cc, kk, ist) = DecodeAsm(VA+i, d[i:i+40])
  
  if cc.find('ret') == -1:
    continue

  if cc.find('db ') != -1:
    continue

  if ist in UNIQ:
    continue

  UNIQ[ist] = True

  print("-------> offset: 0x%x"%(i+VA))
  for k in kk:
    print("0x%x   %s"%(k[0],k[1]))
    if k[1].find('ret') != -1:
      break

  print("\n")
