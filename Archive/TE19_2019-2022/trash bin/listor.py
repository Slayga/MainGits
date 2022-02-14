import xlsxwriter, xlrd
import pandas as pd

'''unused = [50,
          51,
          53,
          55,
          56,
          57,
          59,
          60,
          61,
          64,
          65,
          67,
          68,
          69,
          72,
          73,
          75,
          76,
          77,
          80,
          81,
          82,
          83,
          85,
          88,
          89,
          90,
          92,
          93,
          95,
          96,
          97,
          99,
          167,
          171,
          172,
          175,
          178,
          179,
          181,
          200,
          346,
          348,
          350,
          351,
          352,
          353,
          203,
          205,
          206,
          208,
          210,
          212,
          214,
          215,
          216,
          217,
          218,
          220,
          221,
          222,
          223,
          224,
          225,
          226,
          224,
          228,
          235,
          224,
          226,
          236,
          237,
          238,
          238,
          240,
          238,
          242,
          240,
          243,
          243,
          244,
          245,
          247,
          254,
          259,
          267,
          284,
          287,
          288,
          339,
          340,
          301,
          302,
          306,
          308,
          310,
          311,
          312,
          313,
          315,
          316,
          317,
          319,
          322,
          324,
          325,
          327,
          328,
          330,
          333,
          334,
          335,
          336
          ]
'''
# workbook = xlsxwriter.Workbook("lista.xlsx")
# worksheet = workbook.add_worksheet()

# # bold = workbook.add_format({"bold": 1})

# worksheet.write("A1", "Datornamn")

# row = 1


# for i in range(354):
#     if not i in unused:
#         string = "AD218" + ("0"*(3-len(str(i))) if len(str(i)) <= 3 else "") + str(i)
#         print(string)
#         worksheet.write_string(row, 0, string)
#         row += 1

# workbook.close()


# data = pd.ExcelFile("lista2021-2022.xlsx")
# print(data.parse(0))

# for dator in duppletter:
#     count = duppletter.count(dator)
    
#     if count > 1:
#         print(dator)

# gamla_namn = data["Namn2"].tolist()
# gamla_klass = data["Anskod"].tolist()

# nya_dict = dict(zip(nya_namn, nya_klass))
# gamla_dict = dict(zip(gamla_namn, gamla_klass))

# nya_namnlapp = dict()
# gammal_namnlapp = dict()

# index_to_pop = list()

# for index, (k, v) in enumerate(nya_dict.items()):
#     if k == None or v == None:
#         index_to_pop.append(index)

# for i in index_to_pop:
#     nya_dict.pop(None)

# index_to_pop = list()

# for index, (k, v) in enumerate(gamla_dict.items()):
#     if k == None or v == None:
#         index_to_pop.append(index)

# for i in index_to_pop:
#     gamla_dict.pop(None)

# print(len(nya_dict))
# print(len(gamla_dict))

# count = 0

# for e, k in nya_dict.items():
#     for g_e, g_k in gamla_dict.items():
#         if g_e == e and g_k[:2] == k[:2]:
#             count += 1
#             break
#     else:
#         nya_namnlapp[e] = k

# for g_e, g_k in gamla_dict.items():
#     for e, k in nya_dict.items():
#         if g_e == e and g_k[:2] == k[:2]:
#             count += 1
#             break
#     else:
#         gammal_namnlapp[g_e] = g_k

# print("NYA")
# for elev, klass in nya_namnlapp.items():
#     print(elev, "+", klass)
# input()
# print("GAMLA")
# for ele, kla in gammal_namnlapp.items():
#     print(ele, "+", kla)
# input()
# input(">> Exit...")


# workbook = xlsxwriter.Workbook("bok1.xlsx")
# worksheet = workbook.add_worksheet()

# bold = workbook.add_format({"bold": 1})

# worksheet.write("A1", "Nya")

# row = 1

# for namn, klass in nya_namnlapp.items():
#     worksheet.write_string(row, 0, namn, bold)
#     worksheet.write_string(row, 1, klass)
#     row += 1

# workbook.close()


data = pd.read_excel("lista2021-2022.xlsx")
data = data.where(pd.notnull(data), None)

data2 = pd.read_excel("GG.xlsx")
data2 = data2.where(pd.notnull(data2), None)
# print(data)

# nya_namn = data["Namn"].tolist()
# nya_klass = data["Klass"].tolist()

org_datorer = data["Datornamn"].tolist()
it_datorer = data2["Computer"].tolist()
it_serials = data2["Serial number bios"].tolist()

zip_dator = dict(zip(it_datorer, it_serials))

while None in org_datorer:
    org_datorer.remove(None)

column = 7

workbook = xlsxwriter.Workbook("lista2021-2022.xlsx")
worksheet = workbook.add_worksheet()

for k, v in zip_dator.items():
    if k in org_datorer:
        print(f"Found {k} in org_datorer at index {org_datorer.index(k)}. The serial is {v}" \
            f"Enter at row: {(org_datorer.index(k)+2)}")
        
        
        worksheet.write_string((org_datorer.index(k)+2), column, v)
        

workbook.close()

