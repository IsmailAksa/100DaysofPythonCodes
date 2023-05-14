import re
pattern=r"[A-Z]+uslim"
text= ''' During the periodic renovations undertaken, the ruling Islamic dynasties constructed additions to the mosque and its precincts, such as its dome, façade, minarets, and minbar and interior structure. Upon its capture by the Crusaders in 1099, the mosque was used as a palace; it was also the headquarters of the religious order of the Knights Templar. After the area was conquered by Saladin in 1187, the structure's function as a mosque was restored. More renovations, repairs, and expansion projects were undertaken in later centuries by the Ayyubid Sultanate, the Mamluk Sultanate, the Ottoman Empire, the Supreme Muslim Council of British Palestine, and during the Jordanian occupation of the West Bank. Since the beginning of the ongoing Israeli occupation of the West Bank, the mosque has remained under the independent administration of the Jerusalem Islamic Waqf Muslim.[11] '''
# match= re.search(pattern,text)
# print(match)
matches= re.finditer(pattern,text)
for match in matches:
  print(match)
  print(match.span())