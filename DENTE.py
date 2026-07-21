PS4 = r"C:\Users\tania\OneDrive\Documenti\UniFi\fids\videogames\PS4_GamesSales.csv"
file_ps4 = open(PS4,'r', encoding="latin-1")  

xbox = r"C:\Users\tania\OneDrive\Documenti\UniFi\fids\videogames\XboxOne_GameSales.csv"
file_xbox = open(xbox,'r', encoding="latin-1")  

other = r"C:\Users\tania\OneDrive\Documenti\UniFi\fids\videogames\Video_Games_Sales_as_at_22_Dec_2016.csv"
file_other = open(other,'r', encoding="latin-1") 

def divisione(linea):
    index_virg=[]
    lista_finale=[]
    if "\"" in linea:
        for i in range(len(linea)):
            if linea[i]=="\"":
                index_virg.append(i)
        for indice_virgolette in range(len(index_virg)//2):
            if indice_virgolette == 0:
                prima_parte = linea[0:max(0,index_virg[indice_virgolette*2]-1)].split(",")
            else: 
                prima_parte = linea[index_virg[indice_virgolette*2-1]+2:index_virg[indice_virgolette*2]-1].split(",")
            if prima_parte == ['']:
                parziale=[linea[index_virg[indice_virgolette*2]:index_virg[indice_virgolette*2+1]+1]]
            else: 
                parziale = prima_parte + [linea[index_virg[indice_virgolette*2]:index_virg[indice_virgolette*2+1]+1]] 
            lista_finale+= parziale 
        resto = linea[index_virg[-1]+2:].split(",")
        lista_finale+= resto
    else:
        lista_finale = linea.split(",") 
    return lista_finale
    
def riempimento_fileA2(a,b,c,piattaforma_fissa):
    for linea in linee[1:]: 
        oggetto = divisione(linea)
        if piattaforma_fissa is not None:
            piattaforma = piattaforma_fissa
        else:
            piattaforma = oggetto[1]
        lettura = oggetto[a] + "," + oggetto[b] + "," + oggetto[c] + "," + piattaforma + '\n'
        finaleEU_JP.write(lettura)
    return finaleEU_JP.write(lettura)

def riempimento_fileB3(a,b):
    for linea in linee[1:]:
        oggetto = divisione(linea) 
        if oggetto[b]== "0":
            del linea
        else:
            lettura = oggetto[a] + "," + oggetto[b] + '\n'
            x = GenereNA.write(lettura)
    return x

def riempimento_fileC1(a,b):
    for linea in linee[1:]:
        oggetto = divisione(linea) 
        if oggetto[a]== "N/A":
            del linea
        else:
            lettura = oggetto[a] + "," + oggetto[b] + '\n'
            x = Anni_generi.write(lettura)
    return x


#  DOMANDA  A2: Il gioco che ha venduto di più in Europa e quello che ha venduto di più in Giappone


EU_JP = r"C:\Users\tania\OneDrive\Documenti\UniFi\fids\giochi_EU_JP.csv"
finaleEU_JP = open(EU_JP, 'w', encoding="latin-1")

linee = file_other.readlines()
c = riempimento_fileA2(0,6,7,piattaforma_fissa=None)

linee = file_ps4.readlines()
c = riempimento_fileA2(0,5,6,piattaforma_fissa="PS4")

linee = file_xbox.readlines()
c = riempimento_fileA2(1,6,7,piattaforma_fissa="XOne")

finaleEU_JP.close()
file_ps4.close()
file_xbox.close()
file_other.close()

finaleEU_JP = open(EU_JP, 'r', encoding="latin-1")

linea = finaleEU_JP.readline()
giocoEU={}
giocoJP={}
while linea: 
    valore = divisione(linea) 
    if float(valore[1]) > 0.1:
        giocoEU [(valore[0], valore[3])] = valore[1]
    if float(valore[2]) > 0.1:
        giocoJP [(valore[0], valore[3])] = valore[2]
    linea = finaleEU_JP.readline()

somme_per_oggettoEU = {}
somme_per_oggettoJP = {}

for (valore[0], valore[3]), valore[1] in giocoEU.items():
    if (valore[0], valore[3]) not in somme_per_oggettoEU:
        if valore[0] not in somme_per_oggettoEU:
            somme_per_oggettoEU[valore[0]] = 0
    somme_per_oggettoEU[valore[0]] += float(valore[1])
for (valore[0], valore[3]), valore[2] in giocoJP.items():
    if (valore[0], valore[3]) not in somme_per_oggettoJP:
        if valore[0] not in somme_per_oggettoJP:
            somme_per_oggettoJP[valore[0]] = 0
    somme_per_oggettoJP[valore[0]] += float(valore[2])

valore_massimoEU = max(somme_per_oggettoEU.values())
max_gioco_EU = max(somme_per_oggettoEU, key=somme_per_oggettoEU.get)

valore_massimoJP = max(somme_per_oggettoJP.values())
max_gioco_JP = max(somme_per_oggettoJP, key=somme_per_oggettoJP.get)

print("Il gioco che ha venduto di più in Europa e'", max_gioco_EU, "con", valore_massimoEU, "milioni di dollari") 

print("mentre il gioco che ha venduto di più in Giappone e'", max_gioco_JP, "con", valore_massimoJP, "milioni di dollari.", '\n')

finaleEU_JP.close()


# DOMANDA B3: Il genere che ha venduto di più in Nord America. Lo sviluppatore che ha sviluppato più giochi

# Il genere che ha venduto di più in Nord America.

genere_NA = r"C:\Users\tania\OneDrive\Documenti\UniFi\fids\genere_NA.csv"
GenereNA = open(genere_NA, 'w', encoding="latin-1")

file_ps4 = open(PS4,'r', encoding="latin-1")  
file_other = open(other,'r', encoding="latin-1")  
file_xbox = open(xbox,'r', encoding="latin-1")   


linee = file_other.readlines()
c = riempimento_fileB3(3,5)

linee = file_ps4.readlines()
c = riempimento_fileB3(2,4)

linee = file_xbox.readlines()
c = riempimento_fileB3(3,5)

file_ps4.close()
file_xbox.close()
file_other.close()
GenereNA.close()

GenereNA = open(genere_NA, 'r', encoding="latin-1")

NA_gen = {}
linea = GenereNA.readline()
while linea:
    oggetto = divisione(linea)
    if oggetto[0] not in NA_gen:
        NA_gen[oggetto[0]] = 0
    NA_gen[oggetto[0]] += float(oggetto[1])
    linea = GenereNA.readline()

genere= max(NA_gen, key=NA_gen.get)
max_venditaNA = max(NA_gen.values())

print("Il genere che ha venduto di più in Nord America è", genere, "con", max_venditaNA, "vendite.", '\n')

GenereNA.close()


# Lo sviluppatore che ha sviluppato più giochi

Svil_giochi = r"C:\Users\tania\OneDrive\Documenti\UniFi\fids\Sviluppatore_e_giochi.csv"
Sviluppatore = open(Svil_giochi, 'w', encoding="latin-1")
file_other = open(other,'r', encoding="latin-1")  

linee = file_other.readlines()
del linee[0]
for linea in linee:
    oggetto = divisione(linea)
    if oggetto[14] == "": 
        del linea
    else:
        lettura = oggetto[14] + "," + oggetto[0] + "," + oggetto[1] + '\n'
        Sviluppatore.write(lettura)

file_other.close()
Sviluppatore.close()

Sviluppatore = open(Svil_giochi, 'r', encoding="latin-1")

gioco_per_svil = {}

linea = Sviluppatore.readline()
while linea:
    valore = divisione(linea)
    gioco_per_svil[(valore[1], valore[2])] = valore[0]
    linea = Sviluppatore.readline()

riepilogo={}
for creatore in gioco_per_svil.values():
    if creatore in riepilogo:
        riepilogo[creatore] += 1
    else:
        riepilogo[creatore]=1

nome_creatore = max(riepilogo, key=riepilogo.get)
max_creatore = max(riepilogo.values())

print("Tra i giochi di cui abbiamo le info necessarie, lo sviluppatore che ha sviluppato più giochi e'", nome_creatore, "con", max_creatore, "giochi diversi.", '\n')

Sviluppatore.close()


# DOMANDA C1: L'anno in cui sono usciti più generi diversi

file_ps4 = open(PS4,'r', encoding="latin-1")  
file_other = open(other,'r', encoding="latin-1")  
file_xbox = open(xbox,'r', encoding="latin-1")  

anni = r"C:\Users\tania\OneDrive\Documenti\UniFi\fids\anno_con_più_generi.csv"
Anni_generi = open(anni,'w', encoding="latin-1") 

linee = file_other.readlines()
c = riempimento_fileC1(2,3)
linee = file_xbox.readlines()
c = riempimento_fileC1(2,3)
linee = file_ps4.readlines()
c = riempimento_fileC1(1,2)

file_ps4.close()
file_xbox.close()
file_other.close()
Anni_generi.close()

Anni_generi = open(anni,'r', encoding="latin-1")

diz_annogenere = {}
linea = Anni_generi.readline()
while linea:
    valore = linea.split(",")
    if valore[0] not in diz_annogenere.keys():
        diz_annogenere[valore[0]]=[valore[1]]
    else:
        diz_annogenere[valore[0]].append(valore[1])
    linea = Anni_generi.readline()

diz_annogenere_sistemato = {}
for valore[0], lista in diz_annogenere.items():
    lista = list(set(lista))
    diz_annogenere_sistemato[valore[0]] = lista

diz_anno_quantità = {}
chiavi = diz_annogenere_sistemato.keys()
for chiave in chiavi:
    numero_generi = len(diz_annogenere_sistemato[chiave])
    diz_anno_quantità[chiave]= numero_generi

max_anno = max(diz_anno_quantità, key=diz_anno_quantità.get)
max_generi = max(diz_anno_quantità.values())

print("L'anno in cui sono usciti più generi è il", max_anno, "con", max_generi, "generi diversi.")

Anni_generi.close()