def analice_Sentence(sentence):
    sentence = sentence.upper()
    aux = 0
    for leter in sentence:
        if leter == "\n":
            break
        aux += 1
    print(aux)
    sentence = sentence.replace("NOM ", "NAME_INGREDIENT ")
    sentence = sentence.replace("ENE ", "ENERGY ")
    sentence = sentence.replace("PRO ", "PROTEINS ")
    sentence = sentence.replace("GRS ", "SATURED_FATS ")
    sentence = sentence.replace("GRP ", "POLIUNSATURED_FATS ")
    sentence = sentence.replace("GRM", "MONOUNSATURED_FATS")
    sentence = sentence.replace("COL ", "CHOLESTEROL ")
    sentence = sentence.replace("H20 ", "WATHER ")
    sentence = sentence.replace("GRA ", "FATS ")
    sentence = sentence.replace("FIB ", "FIBRE ")
    sentence = sentence.replace("AZ ", "SUGGAR ")
    sentence = sentence.replace("CHO ", "CARBOHYDRATES ")
    sentence = sentence.replace("NA ", "SODIUM ")
    sentence = sentence.replace("K ", "POTASSIUM ")
    sentence = sentence.replace("CA ", "CALCIUM ")
    sentence = sentence.replace("P ", "PHOSPHORUS ")
    sentence = sentence.replace("MG ", "MAGNESIUM ")
    sentence = sentence.replace("CL ", "PHOSPHORUS ")
    sentence = sentence.replace("S ", "SULFUR ")
    sentence = sentence.replace("FE ", "IRON ")
    sentence = sentence.replace("F ", "FLUORINE ")
    sentence = sentence.replace("I ", "IODINE ")
    sentence = sentence.replace("MN ", "MANGANNESE ")
    sentence = sentence.replace("CO ", "COBALT ")
    sentence = sentence.replace("CU ", "COPPER ")
    sentence = sentence.replace("ZN ", "ZINC ")
    sentence = sentence.replace("SI ", "SILICE ")
    sentence = sentence.replace("NI ", "NICKEL ")
    sentence = sentence.replace("CR ", "CHROMR ")
    sentence = sentence.replace("LI ", "LITHIUM ")
    sentence = sentence.replace("MO ", "MOLYBDENUM ")
    sentence = sentence.replace("SE ", "SELENIUM ")
    sentence = sentence.replace("VA ", "VITAMIN_A ")
    sentence = sentence.replace("VB1 ", "VITAMIN_B1 ")
    sentence = sentence.replace("VB2 ", "VITAMIN_B2 ")
    sentence = sentence.replace("VB3 ", "VITAMIN_B3 ")
    sentence = sentence.replace("VB6 ", "VITAMIN_B6 ")
    sentence = sentence.replace("VB12 ", "VITAMIN_B12 ")
    sentence = sentence.replace("VC ", "VITAMIN_C ")
    sentence = sentence.replace("VD ", "VITAMIN_D ")
    sentence = sentence.replace("VE ", "VITAMIN_E ")
    sentence = sentence.replace("VK ", "VITAMIN_K ")
    sentence = sentence.replace("VB2 ", "VITAMIN_ ")
    sentence = sentence.replace("ACP ", "PANTOTHECNIC_ACID ")
    sentence = sentence.replace("ACF ", "FOLIC_ACID ")
    sentence = sentence.replace("BIO ", "BIOTIN ")
    print(sentence)

    """mylist = sentence.split('\n')
    mylist.remove('')
    for x in range(0, len(mylist)):
        if 'nombre' in mylist[x]:
            mylist[x] = ['NAME', mylist[x][6:]]
        else:
            aux = mylist[x].split(' ')
            mylist[x] = [aux[0], aux[1]]"""

    return " "

