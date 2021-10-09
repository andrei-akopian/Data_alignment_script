def import_graphs(filename):

  #get the data
  with open(filename,'r') as file:
    imported_data=file.readlines()
  #print(imported_data)
  ##convert the data
  offset_y=1
  #creates list of te right lenght
  size=len(imported_data[offset_y].split(','))
  graphs=[[] for _ in range(size//2)]

  #put the reworked data into the list
  for line in imported_data[offset_y:]:
    elements=line.strip('\n').split(',')
    for j in range(0,size,2):
      if elements[j]!='':
        graphs[j//2].append( (float(elements[j]), float(elements[j+1])) )
  print()
  print(graphs[0])
  print()
  graphs=[sorted(g, key=lambda p: p[0]) for g in graphs]
  print(graphs)
  return graphs

#applys the formulla
def formula(graph, t):
    for ((x1,y1), (x2, y2)) in zip(graph, graph[1:]):
        if x1<=t<=x2:
          slope=(y2-y1)/(x2-x1)
          return (t-x1)*slope+y1
    return None

def export(resoult_graphs):
  #get the lines ready
  lines=[]
  line=''
  Sum=0
  for i in range(len(resoult_graphs[0])):
    line=''
    Sum=[0,0]
    for point in resoult_graphs:
      if point[i][1]==None:
        line+=',,'
      else:
        line+=str(point[i][0])+','+str(point[i][1])+','
        Sum[0]+=point[i][1]
        Sum[1]+=1
    #put the sum at the end
    if Sum[1]!=0:
      line+=str(resoult_graphs[0][i][0])+','+str(Sum[0]/Sum[1])+'\n'
    else:
      line+='\n'
    lines.append(line)
    #write into a resoults.csv file
  with open('results.csv','w') as file:
    for line in lines:
      file.write(line)

#main part
def body(filename,times):
  graphs=import_graphs(filename)
  resoult_graphs=[]
  for i in range(len(graphs)):
    resoult_graphs.append([])
    for j in times:
      resoult_graphs[i].append((j, formula(graphs[i],j)))
  export(resoult_graphs)

#generate times
times=[]
for i in range(-44,33,2):
  times.append(i)
#filename
filename='data.csv'

#RUN
body(filename,times)


