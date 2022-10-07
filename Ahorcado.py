from distutils.log import error
import random
import os
import time

def interfaz():
    print("""
    ██████████████████████████████████████████████████
    ██                                              ██
    ██       BIENVENIDO AL JUEGO DE AHORCADO        ██
    ██                                              ██
    ██████████████████████████████████████████████████
    
    """)

def dibujo(error):
    switcher={
        0:"""
    ░░░░░░░░░░░░░░░░░░░░░░
    ░    VAS MUY BIEN    ░
    ░                    ░
    ░░░░░░░░░░░░░░░░░░░░░░
    """,
        1:"""
    ╔
    ║
    ║
    ║
    ║
    ║
    ║
    ╩══════       
    """,
        2:"""
    ╔═════════╗
    ║         ║
    ║        
    ║        
    ║        
    ║
    ║
    ╩══════       
    """,
        3:"""
    ╔═════════╗
    ║         ║
    ║         ■
    ║        
    ║        
    ║
    ║
    ╩══════       
    """,
        4:"""
    ╔═════════╗
    ║         ║
    ║         ■
    ║         █
    ║        
    ║
    ║
    ╩══════       
    """,
        5:"""
    ╔═════════╗
    ║         ║
    ║         ■
    ║        ╚█
    ║        
    ║
    ║
    ╩══════       
    """,
        6:"""
    ╔═════════╗
    ║         ║
    ║         ■
    ║        ╚█╝
    ║        
    ║
    ║
    ╩══════       
    """,
        7:"""
    ╔═════════╗
    ║         ║
    ║         ■
    ║        ╚█╝
    ║        ║ 
    ║
    ║
    ╩══════       
    """,
        8:"""
    ╔═════════╗     ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
    ║         ║     ▓                          ▓
    ║         ■     ▓        AHORCADO!!        ▓
    ║        ╚█╝    ▓                          ▓
    ║        ║ ║    ▓                          ▓
    ║               ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
    ║
    ╩══════       
    """,
        9:"""
    ¤               ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
    ║               ▓                          ▓
    ║               ▓        GANASTE!!         ▓
    ║   ♥ ☻ ♥       ▓                          ▓
    ║   ╚═█═╝       ▓                          ▓
    ║     █         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
    ║    ║ ║
    ╩═══ ╝ ╚ ═════       
    """
    }

    # print("""
    # ╔═════════╗
    # ║         ║
    # ║         ▄
    # ║        ╚█╝
    # ║        ║ ║
    # ║
    # ║
    # ╩══════       
    # """)
    print(switcher.get(error,"No se encuentra este dibujo"))
    




def palabras(): #Con esta funcion extraemos las palabras del archivo y se escoge una palabra random
    datos=[]
    with open("./palabras_juego.txt","r",encoding="utf-8") as f:
    #with open("./Juego_Ahorcado/palabras_juego.txt","r",encoding="utf-8") as f:
        for line in f:
            datos.append(line)
    palabra=random.choice(datos)
    #print(palabra)
    return palabra

def juego():
    palabra=palabras().upper().strip()
    pal=[i for i in palabra]
    #print(list(enumerate(pal)))
    adivina=["_" for i in pal]
    print("█  "," ".join(adivina),"  █","      --contiene ",len(adivina),"letras--")
    letra=input("""
    ░░░░░░░░░░░░░░░░░░░░░░
    ░►Ingrese una letra: ░
    ░                    ░
    ░░░░░░░░░░░░░░░░░░░░░░
    
    -""")
    error=0
    while error<8:
        #print(adivina)
        #try:
        letra=letra.upper()
        cont=0
        aux=0
        if adivina.count(letra)!=0:
            print("►►►Letra repetida porfavor ingresar otra letra diferente◄◄◄\n")
            time.sleep(1)
        elif len(letra)>1:
            print("►►►Solo debe ingresar una letra◄◄◄\n")
            time.sleep(1)
        else:
            for letras in pal:
                if letra==letras:
                    adivina.pop(cont)
                    adivina.insert(cont,letra)
                else:
                    aux=aux+1
                cont=cont+1 
            if aux==len(pal):
                error=error+1   
        if adivina!=pal:
            os.system("cls") #limpia la pantalla  
            interfaz()
            dibujo(error)
            if error==8:
                print("".join(pal))
                continue
            print("█  "," ".join(adivina),"  █","      --contiene ",len(adivina),"letras--")
            letra=input("""
    ░░░░░░░░░░░░░░░░░░░░░░
    ░►Ingrese otra letra:░
    ░                    ░
    ░░░░░░░░░░░░░░░░░░░░░░
    
    -""")
            
            
            #print(adivina) 
        else:
            os.system("cls")
            print("""
    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
    ▓                            ▓
    ▓       ACERTASTE!!          ▓
    ▓                            ▓
    ▓       LA PALABRA ERA       ▓
    ▓       ""","".join(adivina),"""      ▓
    ▓                            ▓
    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
    """)
            #print("\t","".join(adivina),"\n")
            return True
            break
        #except ValueError as ve:
            #print(ve)
        


def run():
    os.system("cls") #limpia la pantalla
    interfaz()
    decision=input("Deseas Jugar(S/N): ")
    while (decision=='S') or (decision=='s'):
        if juego():
            print("Felicitaciones Juego terminado ")
            dibujo(9)
        decision=input("Deseas volver a jugar? (S/N): ")
    print("     Hasta la Proxima ♥")

if __name__=="__main__":
    run()