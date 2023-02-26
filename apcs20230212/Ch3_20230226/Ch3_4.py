dictScores = {'Ch':95,'En':80,'Ma':70,'Ch':10}
print(dictScores)

dictScores['En'] = 91
print(dictScores)
# key不在給值新增
dictScores['Sc'] = 25
print(dictScores)
# key不在取值拋出錯誤
#if 'Gg' in dictScores:
print(dictScores['Gg'])
