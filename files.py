import os
from xml.dom import minidom
import xml.etree.cElementTree as ET
os.system('cls') 
currentDir=os.getcwd()
opciones = {}
#Create XML directory
try:
    os.mkdir(currentDir+"\XML")
except OSError:
    print ("Welcome back!")
else:
    print ("Welcome!")
#Logo
JP="      ## ########  \n      ## ##     ## \n      ## ##     ## \n      ## ########  \n##    ## ##        \n##    ## ##        \n ######  ##        "
print("File Viewer by:\n"+JP+"\n\n"+"R - Restart the search\nE - End the program\ntogFiles - Tog file's view \n\nReset XML paths deleting/modifying "+currentDir+"\XML\paths.xml\n")
ShowFiles=True
data = ET.Element("data")
items = ET.SubElement(data, "items")
tree = ET.ElementTree(data)
#Create XML document with current directory if doesnt exist
if os.path.isfile(currentDir+"/XML/paths.xml"):
    nt = ET.parse("XML/paths.xml") 
    PathsFile = minidom.parse('XML/paths.xml')
    paths = PathsFile.getElementsByTagName('item')
    for i in paths:
        ET.SubElement(items, "item", name="dir").text = i.firstChild.data
else: 
    ET.SubElement(items, "item", name="dir").text = currentDir
    tree.write("XML/paths.xml")
#Print function
def printFromPath(P,L,opciones,ShowFiles):
    Text=""
    for sd,dirs,files in os.walk(P): 
        if ShowFiles==True:
            for i in files:
                n=len(opciones)
                opciones[n] = str(sd)+"/"+str(i)
                Text=Text+L+"---"+str(n+1)+" File: "+str(i)+"\n"
        for i in dirs:
            n=len(opciones)
            opciones[n] = str(sd)+"/"+str(i)
            Text=Text+L+"---"+str(n+1)+" Folder: "+str(i)+":"+"\n"
            Text=Text+printFromPath(str(P)+"/"+str(i),L+"------",opciones,ShowFiles)
        break
    return Text
#Quit Function
def end():
    print("File Viewer closed\nThanks for using me. \n"+JP)
    exit()
#Logic
def openFolder(path):
    a=input("Open in explorer or cmd (e/c)...\n")
    if a=="e":
        os.startfile(path)
    elif a=="c":
        os.system("start cmd /K cd "+path )
def logic(ET,data,paths,opciones,ShowFiles):
    a=input("Select the number to open and press Enter...\n")
    if a.isnumeric():  
        if round(float(a)-1)<=len(opciones):
            print(str(opciones[round(float(a)-1)]))
            openFolder(str(opciones[round(float(a)-1)]))
            logic(ET,data,paths,opciones,ShowFiles)
        else:
            print(a+" no es una opcion valida")
            logic(ET,data,paths,opciones,ShowFiles)
    else:
        if a=="e" or a=="E":
            end()
        elif a=="togFiles":
            ShowFiles = not ShowFiles
            print("\nFile's view: "+str(ShowFiles))
            logic(ET,data,paths,opciones,ShowFiles) 
        elif a=="r" or a=="R":
            os.system('cls') 
            print("File Viewer by:\n"+JP+"\n\n"+"R - Restart the search\nE - End the program\ntogFiles - Tog file's view \n\nReset XML paths deleting/modifying "+currentDir+"\XML\paths.xml\n")
            read(ET,data,opciones,ShowFiles)
            selection(ET,data,paths,opciones,ShowFiles)
        else:
            print(a+" no es un numero")
            logic(ET,data,paths,opciones,ShowFiles) 
#Selection
def selection(ET,data,paths,opciones,ShowFiles):
    a=input("\nSelect the number of the path or add a new path...\n")
    if a.isnumeric():  
        if int(a):
            if (int(a)-1)<=len(paths) and round(float(a))!=0:
                path = paths[int(a)-1].firstChild.data
                opciones = {}
                opciones[0] = path
                print("---"+str(1)+" "+str(path)+": \n"+printFromPath(str(path),"---",opciones,ShowFiles))
                logic(ET,data,paths,opciones,ShowFiles)
            else:
                print(a+" is not a valid number")
                selection(ET,data,paths,opciones,ShowFiles)
    else:
        if a=="e" or a=="E":
            end()
        elif a=="togFiles":
            ShowFiles = not ShowFiles
            print("\nFile's view: "+str(ShowFiles))
            selection(ET,data,paths,opciones,ShowFiles)
        elif a=="r" or a=="R":
            os.system('cls') 
            print("File Viewer by:\n"+JP+"\n\n"+"R - Restart the search\nE - End the program\ntogFiles - Tog file's view \n\nReset XML paths deleting/modifying "+currentDir+"\XML\paths.xml\n")
            read(ET,data,opciones,ShowFiles)
            selection(ET,data,paths,opciones,ShowFiles)
        else:
            if os.path.isdir(a):
                ET.SubElement(items, "item", name="dir").text = a
                tree = ET.ElementTree(data)
                tree.write("XML/paths.xml")
                read(ET,data,opciones,ShowFiles)
            else:
                print(a+" is not a valid path")
                selection(ET,data,paths,opciones,ShowFiles)
#List the XML
def printPaths(p,ET,data,opciones,ShowFiles):
    c=1
    for i in p:
        print(str(c)+": "+i.firstChild.data)
        c=c+1
    selection(ET,data,p,opciones,ShowFiles)
#Read the XML
def read(ET,data,opciones,ShowFiles):
    PathsFile = minidom.parse('XML/paths.xml')
    paths = PathsFile.getElementsByTagName('item')
    printPaths(paths,ET,data,opciones,ShowFiles)
read(ET,data,opciones,ShowFiles)
