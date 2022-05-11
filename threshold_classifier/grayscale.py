from PIL import Image

# import required module
from pathlib import Path
from datetime import datetime
 
# assign directory
directory = 'images'
dir_no_contact = '../../classifier/data/Train/0/'
dir_contact = '../../classifier/data/Train/1/'
dir_collision = '../../classifier/data/Train/2/'
 
# iterate over files in
# that directory
#files = Path(dir_no_contact).glob('*.png')
#files = Path(dir_contact).glob('*.png')
files = Path(dir_collision).glob('*.png')

i = 0
no_co = 0
cont = 0
coll = 0
unknown = 0


#fw = open("0_gray_predictions_" + datetime.now().strftime("%Y%m%d-%H%M%S") + ".md", "a")
#fw = open("1_gray_predictions_" + datetime.now().strftime("%Y%m%d-%H%M%S") + ".md", "a")
fw = open("2_gray_predictions_" + datetime.now().strftime("%Y%m%d-%H%M%S") + ".md", "a")

for file in files:

	i = i+1

	image = Image.open(file) # Can be many different formats.
	pix = image.load()
	
	r1, g1, b1, a1 = pix[280,32]
	r2, g2, b2, a2 = pix[280,280]
	r3, g3, b3, a3 = pix[280,400]

	# Grayscale  = 0.299R + 0.587G + 0.114B
	grayscale1 = 0.299 * r1 + 0.587 * g1 + 0.114 * b1
	grayscale2 = 0.299 * r2 + 0.587 * g2 + 0.114 * b2
	grayscale3 = 0.299 * r3 + 0.587 * g3 + 0.114 * b3

	# no contact
	#if ((grayscale1 >= 44 and grayscale1 <= 56) and (grayscale2 >= 74 and grayscale2 <= 81) and (grayscale3 >= 132 and grayscale3 <= 149)):
	#if (grayscale1 >= 44 and grayscale1 <= 56):
	#if (grayscale2 >= 74 and grayscale2 <= 81):
	if (grayscale3 >= 132 and grayscale3 <= 149):

		fw.write("The image " + str(i) + " shows no contact.\n")
		fw.write("#1 RGB: " + str(r1) + ", " + str(g1) + ", " + str(b1) + ", grayscale: " + str(grayscale1) + "\n")
		fw.write("#2 RGB: " + str(r2) + ", " + str(g2) + ", " + str(b2) + ", grayscale: " + str(grayscale2) + "\n")
		fw.write("#3 RGB: " + str(r3) + ", " + str(g3) + ", " + str(b3) + ", grayscale: " + str(grayscale3) + "\n")
		fw.write("![](" + str(file) + ")\n")
		no_co = no_co +1


	# contact
	#elif ((grayscale1 >= 81 or grayscale1 <= 39) and (grayscale2 <= 69 or (grayscale2 >= 82 and grayscale2 <= 102)) and (grayscale3 <= 131)):
	#elif (grayscale1 >= 81 or grayscale1 <= 39):
	#elif (grayscale2 <= 69 or (grayscale2 >= 82 and grayscale2 <= 102)):
	elif (grayscale3 <= 131):

		fw.write("The image " + str(i) + " shows a contact.\n")
		fw.write("#1 RGB: " + str(r1) + ", " + str(g1) + ", " + str(b1) + ", grayscale: " + str(grayscale1) + "\n")
		fw.write("#2 RGB: " + str(r2) + ", " + str(g2) + ", " + str(b2) + ", grayscale: " + str(grayscale2) + "\n")
		fw.write("#3 RGB: " + str(r3) + ", " + str(g3) + ", " + str(b3) + ", grayscale: " + str(grayscale3) + "\n")
		fw.write("![](" + str(file) + ")\n")
		cont = cont + 1


	# collision
	#elif (((grayscale1 >= 40 and grayscale1 <= 43) or (grayscale1 >= 57 and grayscale1 <= 80)) and ((grayscale2 >= 70 and grayscale2 <= 73) or (grayscale2 >= 103)) and (grayscale3 >= 150)):
	#elif ((grayscale1 >= 40 and grayscale1 <= 43) or (grayscale1 >= 57 and grayscale1 <= 80)):
	#elif ((grayscale2 >= 70 and grayscale2 <= 73) or (grayscale2 >= 103)):
	elif (grayscale3 >= 150):
		
		fw.write("The image " + str(i) + " shows a collision.\n")
		fw.write("#1 RGB: " + str(r1) + ", " + str(g1) + ", " + str(b1) + ", grayscale: " + str(grayscale1) + "\n")
		fw.write("#2 RGB: " + str(r2) + ", " + str(g2) + ", " + str(b2) + ", grayscale: " + str(grayscale2) + "\n")
		fw.write("#3 RGB: " + str(r3) + ", " + str(g3) + ", " + str(b3) + ", grayscale: " + str(grayscale3) + "\n")
		fw.write("![](" + str(file) + ")\n")
		coll = coll + 1


	else:
		
		fw.write("It cannot be determined what the image " + str(i) + " shows.\n")
		fw.write("#1 RGB: " + str(r1) + ", " + str(g1) + ", " + str(b1) + ", grayscale: " + str(grayscale1) + "\n")
		fw.write("#2 RGB: " + str(r2) + ", " + str(g2) + ", " + str(b2) + ", grayscale: " + str(grayscale2) + "\n")
		fw.write("#3 RGB: " + str(r3) + ", " + str(g3) + ", " + str(b3) + ", grayscale: " + str(grayscale3) + "\n")
		fw.write("![](" + str(file) + ")\n")
		unknown = unknown + 1


#Accuracy
no_acc = (no_co/i)*100
con_acc = (cont/i)*100
col_acc = (coll/i)*100
un_acc = (unknown/i)*100

fw.write("\n")
fw.write("no contact: " + str(no_co) + " ==> " + str(no_acc) + "% \n")
fw.write("contact: " + str(cont) + " ==> " + str(con_acc) + "% \n")
fw.write("collision: " + str(coll) + " ==> " + str(col_acc) + "% \n")
fw.write("unknown: " + str(unknown) + " ==> " + str(un_acc) + "% \n")

fw.close()