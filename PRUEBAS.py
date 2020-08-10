import os
from os import path
import shutil

archivo_1 = "lista_crop.txt"
archivo_2 = "sujetos.txt"

direccion_1 = path.abspath(archivo_1)
direccion_2 = path.abspath(archivo_2)
direccion_3 = os.path.split(direccion_1) 
direccion_3 = direccion_3[0] 
direccion_4 = os.path.split(direccion_3) 
direccion_4 = direccion_4[0] +"/frames" #Direccion de imagenes .jpg
direccion_5 = os.path.split(direccion_3) 
direccion_5 = direccion_5[0] +"/segment_five" #Direccion de imagenes .png (mask)
print(direccion_2)

fichero = open(direccion_1,"r")
lineas_1 = fichero.readlines()
fichero.close()

fichero = open(direccion_2,"r")
lineas_2 = fichero.readlines()
fichero.close()
m=0
for m in range (len(lineas_2)):
	lineas_2[m] = lineas_2[m][0:len(lineas_2[m])-1] 


#print(lineas_2)
nombre= ["po1","po2","rg1","rg2"]
try:
	os.stat(direccion_3 + "/" + nombre[0])
	os.stat(direccion_3 + "/" + nombre[0] + "_mask")
	os.stat(direccion_3 + "/" + nombre[1])
	os.stat(direccion_3 + "/" + nombre[1] + "_mask")
	os.stat(direccion_3 + "/" + nombre[2])
	os.stat(direccion_3 + "/" + nombre[2] + "_mask")
	os.stat(direccion_3 + "/" + nombre[3])
	os.stat(direccion_3 + "/" + nombre[3] + "_mask")
except:
	os.mkdir(direccion_3 + "/" + nombre[0])
	os.mkdir(direccion_3 + "/" + nombre[0] + "_mask")
	os.mkdir(direccion_3 + "/" + nombre[1])
	os.mkdir(direccion_3 + "/" + nombre[1] + "_mask")
	os.mkdir(direccion_3 + "/" + nombre[2])
	os.mkdir(direccion_3 + "/" + nombre[2] + "_mask")
	os.mkdir(direccion_3 + "/" + nombre[3])
	os.mkdir(direccion_3 + "/" + nombre[3] + "_mask")
#print("carpeta")

lista_sujeto=["hola"]
po1_f = ["po1_f"]
po2_f = ["po2_f"]
rg1_f = ["rg1_f"]
rg2_f = ["rg2_f"]

for elemento in lineas_2:#---------FOR "GLOBAL" DE LOS SUJETO (10 DEL TXT PERSONALIZADO)
	m=0
	for m in range (len(lineas_1)) :
		captura = lineas_1[m].find(elemento)
		if (captura != -1):
			lista_sujeto.append(lineas_1[m])#---FILTRACION DE FRAMES POR SUJETO
	del lista_sujeto[0]		
	
	#print(lista_sujeto)	
	#print("\n\n\n")
	#-------------------OBTENCION DE LOS FRAMES DIVIDIDOS POR LABELS-----------------------------
	po1=["po1"]
	po2=["po2"]
	rg1=["rg1"]
	rg2=["rg2"]
	n=0
	for n in range (len(lista_sujeto)):
		a = lista_sujeto[n].find("B0A")
		b = lista_sujeto[n].find("G01")
		if(a != -1 or b != -1):
			po1.append(lista_sujeto[n])
	n=0
	for n in range (len(lista_sujeto)):
		a = lista_sujeto[n].find("B0B")
		b = lista_sujeto[n].find("G02")
		if(a != -1 or b != -1):
			po2.append(lista_sujeto[n])
	n=0
	for n in range (len(lista_sujeto)):
		a = lista_sujeto[n].find("G03")
		b = lista_sujeto[n].find("G04")
		c = lista_sujeto[n].find("G05")
		d = lista_sujeto[n].find("G06")
		e = lista_sujeto[n].find("G07")
		f = lista_sujeto[n].find("G10")
		g = lista_sujeto[n].find("G11")
		if(a != -1 or b != -1 or c != -1 or d != -1 or e != -1 or f != -1 or g != -1):
			rg1.append(lista_sujeto[n])
	n=0
	for n in range (len(lista_sujeto)):
		a = lista_sujeto[n].find("D0X")
		if(a != -1):
			rg2.append(lista_sujeto[n])		
	n=0		

	del po1[0]
	del po2[0]
	del rg1[0]
	del rg2[0]
#-------------------OBTENCION DE LOS FRAMES DIVIDIDOS POR LABELS-----------------------------


#-------------------CONSEGUIR BORDES DE LA IMAGENES-----------------------------
#---------------------PO1_F-------------------------------
	for i in range (len(po1)):
		print(po1[i])
		m=0
		n=0
		for n in range (5):
			buscador = po1[i][m:len(po1[i])].find(",")
			m=m+buscador+1
			if(n == 0):
				name_img = m-1
			if(n==2): 
				dato_1=m
			if(n==3):
				dato_2=m
			if(n==4):
				dato_3=m
		
		
		borde_1 = po1[i][dato_1:dato_2-1]
		borde_2 = po1[i][dato_2:dato_3-1]
		ID = ["24"]
		for l in range (int(borde_1),int(borde_2)):
			if((l-int(borde_1) == 0 or (l-int(borde_1)) % 10 == 0)):
				ID.append(str(l))	
		del ID[0]

		for l in range (len(ID)):
			for x in range(6-len(ID[l])):
				ID[l] = "0" + ID[l]
			ID[l] = po1[i][0:name_img] + "_" + ID[l]
			shutil.copy(direccion_4 + "/" +po1[i][0:name_img]+"/"+ ID[l] +".jpg" , direccion_3 + "/" + nombre[0]+"/" + ID[l] + ".jpg")
			shutil.copy(direccion_5 + "/" +po1[i][0:name_img]+"/"+ ID[l] +".png" , direccion_3 + "/" + nombre[0]+"_mask"+"/" + ID[l] + ".png")

			
		for l in ID:
			po1_f.append(l + "\n")
		n=0
#---------------------PO1_F-------------------------------
#---------------------PO2_F-------------------------------
	for i in range (len(po2)):
		print(po2[i])
		m=0
		n=0
		for n in range (5):
			buscador = po2[i][m:len(po2[i])].find(",")
			m=m+buscador+1
			if(n == 0):
				name_img = m-1
			if(n==2): 
				dato_1=m
			if(n==3):
				dato_2=m
			if(n==4):
				dato_3=m
		

		
		borde_1 = po2[i][dato_1:dato_2-1]
		borde_2 = po2[i][dato_2:dato_3-1]
		ID = ["24"]
		for l in range (int(borde_1),int(borde_2)):
			if((l-int(borde_1) == 0 or (l-int(borde_1)) % 10 == 0)):
				ID.append(str(l))	
		del ID[0]

		for l in range (len(ID)):
			for x in range(6-len(ID[l])):
				ID[l] = "0" + ID[l]
			ID[l] = po2[i][0:name_img] + "_" + ID[l]
			shutil.copy(direccion_4 + "/" +po2[i][0:name_img]+"/"+ ID[l] +".jpg" , direccion_3 + "/" + nombre[1]+"/" + ID[l] + ".jpg")
			shutil.copy(direccion_5 + "/" +po2[i][0:name_img]+"/"+ ID[l] +".png" , direccion_3 + "/" + nombre[1] + "_mask"+ "/" + ID[l] + ".png")
			
		for l in ID:
			po2_f.append(l + "\n")
			
		n=0
#---------------------PO2_F-------------------------------

#---------------------RG1_F-------------------------------
	for i in range (len(rg1)):
		print(rg1[i])
		m=0
		n=0
		for n in range (5):
			buscador = rg1[i][m:len(rg1[i])].find(",")
			m=m+buscador+1
			if(n == 0):
				name_img = m-1
			if(n==2): 
				dato_1=m
			if(n==3):
				dato_2=m
			if(n==4):
				dato_3=m
		
		
		borde_1 = rg1[i][dato_1:dato_2-1]
		borde_2 = rg1[i][dato_2:dato_3-1]
		ID = ["24"]
		for l in range (int(borde_1),int(borde_2)):
			if((l-int(borde_1) == 0 or (l-int(borde_1)) % 10 == 0)):
				ID.append(str(l))	
		del ID[0]

		for l in range (len(ID)):
			for x in range(6-len(ID[l])):
				ID[l] = "0" + ID[l]
			ID[l] = rg1[i][0:name_img] + "_" + ID[l]
			shutil.copy(direccion_4 + "/" +rg1[i][0:name_img]+"/"+ ID[l] +".jpg" , direccion_3 + "/" + nombre[2]+"/" + ID[l] + ".jpg")
			shutil.copy(direccion_5 + "/" +rg1[i][0:name_img]+"/"+ ID[l] +".png" , direccion_3 + "/" + nombre[2] + "_mask"+ "/" + ID[l] + ".png")
			
		for l in ID:
			rg1_f.append(l + "\n")
		n=0

#---------------------RG1_F-------------------------------

#---------------------RG2_F-------------------------------
	for i in range (len(rg2)):
		print(rg2[i])
		m=0
		n=0
		for n in range (5):
			buscador = rg2[i][m:len(rg2[i])].find(",")
			m=m+buscador+1
			if(n == 0):
				name_img = m-1
			if(n==2): 
				dato_1=m
			if(n==3):
				dato_2=m
			if(n==4):
				dato_3=m
		
		
		borde_1 = rg2[i][dato_1:dato_2-1]
		borde_2 = rg2[i][dato_2:dato_3-1]
		ID = ["24"]
		for l in range (int(borde_1),int(borde_2)):
			if((l-int(borde_1) == 0 or (l-int(borde_1)) % 30 == 0)):
				ID.append(str(l))	
		del ID[0]

		for l in range (len(ID)):
			for x in range(6-len(ID[l])):
				ID[l] = "0" + ID[l]
			ID[l] = rg2[i][0:name_img] + "_" + ID[l]
			shutil.copy(direccion_4 + "/" +rg2[i][0:name_img]+"/"+ ID[l] +".jpg" , direccion_3 + "/" + nombre[3]+"/" + ID[l] + ".jpg")
			shutil.copy(direccion_5 + "/" +rg2[i][0:name_img]+"/"+ ID[l] +".png" , direccion_3 + "/" + nombre[3] + "_mask"+ "/" + ID[l] + ".png")
			
		for l in ID:
			rg2_f.append(l + "\n")
		n=0
#---------------------RG2_F-------------------------------


#-------------------CONSEGUIR BORDES DE LA IMAGENES-----------------------------
	

	print("lista total: "+ str(len(lista_sujeto)))	
	print("po1: "+ str(len(po1)))	
	print("po2: "+ str(len(po2)))
	print("rg1: "+ str(len(rg1)))
	print("rg2: "+ str(len(rg2)))

	lista_sujeto=["hola"]


del po1_f[0]
del po2_f[0]
del rg1_f[0]
del rg2_f[0]


"""
file = open(direccion_3 +"/"+"po1"+".txt", "w")
for i in po1_f:
	file.write(i)
file.close()
print(len(po1_f))

file = open(direccion_3 +"/"+"po2"+".txt", "w")
for i in po2_f:
	file.write(i)
file.close()
print(len(po2_f))

file = open(direccion_3 +"/"+"rg1"+".txt", "w")
for i in rg1_f:
	file.write(i)
file.close()
print(len(rg1_f))

file = open(direccion_3 +"/"+"rg2"+".txt", "w")
for i in rg2_f:
	file.write(i)
file.close()
print(len(rg2_f))
"""
"""
original = "4CM11_11_R_#1,G04,7,3993,4021,29"
m=0
n=0

for n in range (3):
	buscador = original[m:len(original)].find(",")
	m=m+buscador+1

dato_1=m
buscador = original[m:len(original)].find(",")
m=m+buscador+1
dato_2=m
buscador = original[m:len(original)].find(",")
m=m+buscador
dato_3
print(original[dato_1:dato_2-1])
print(original[dato_2:m])

borde_1 = original[dato_1:dato_2-1]
borde_2 = original[dato_2:dato_3]
"""

