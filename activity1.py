student_data={"id1":{"name":"Jake","class":"6S","subject":"english"},
              "id2":{"name":"Mike","class":"5A","subject":"math"},
              "id3":{"name":"Jake","class":"6S","subject":"english"},
              "id4":{"name":"riggy","class":"9B","subject":"Chemistry"},}
result={}
for key,value in student_data.items():
    if value not in result.values():
        result[key]=value
print(result)
