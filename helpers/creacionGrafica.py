import matplotlib.pyplot as plt
def generarGrafica(dataFrame):
    #Agrupar datos del dataframe segun el analisis de Filtro de arboles en Medellin
    '''
    promedioArboles=dataFrame.groupby('Vereda')['Arboles'].mean()
    #0. generando lista de colores
    colores=["#3D9637","#61DE59","#1BE80E"]
    #1. Generar una figura 
    plt.figure(figsize=(10,10))
    #2. Genero la grafica que deseo
    plt.bar(promedioArboles.index, promedioArboles.values, color=colores)
    #3. Agrego titulo a la gráfica
    plt.title("Promedios de arboles en Medellin")
    #4. Etiqueta o nombre del eje X
    plt.xlabel("Veredas")
    #5. Etiqueta o nombre del eje y
    plt.ylabel("Cantidad promedio")
    #6. Activar el grid
    plt.grid(True)
    #7. rotar los labels X
    plt.xticks(rotation=45)
    #7. Guardando nuestra grafica
    plt.savefig("./graphs/promedioArbolesMedellin.png")
    print(promedioArboles)
    '''
    '''
    #Grafica para el filtro de siembras en Santa fe de Antioquia
    promedioArbolesSFA = dataFrame.groupby('Vereda')['Arboles'].mean()
    colores = ["#3D9637", "#61DE59", "#1BE80E"]
    plt.figure(figsize=(8, 8))
    plt.pie(promedioArbolesSFA.values, labels=promedioArbolesSFA.index, colors=colores, autopct='%1.1f%%')
    plt.title("Distribución de árboles por vereda en Santa Fe de Antioquia")
    plt.savefig("./graphs/distribucion_arboles_SFA.png")
    '''
    ''' 
    #Grafica para el filtro de siembras en Santa fe de Antioquia
    promedioArbolesBagre=dataFrame.groupby('Vereda')['Arboles'].sum()
    #0. generando lista de colores
    colores=["#B68F27","#DAAD35","#977721","#8A6A14"]
    #1. Generar una figura 
    plt.figure(figsize=(10,10))
    #2. Genero la grafica que deseo
    plt.bar(promedioArbolesBagre.index, promedioArbolesBagre.values, color=colores)
    #3. Agrego titulo a la gráfica
    plt.title("Promedio de arboles en el bagre")
    #4. Etiqueta o nombre del eje X
    plt.xlabel("Vereda")
    #5. Etiqueta o nombre del eje y
    plt.ylabel("Promedio Total")
    #6. Activar el grid
    plt.grid(True)
    #7. rotar los labels X
    plt.xticks(rotation=45)
    #7. Guardando nuestra grafica
    plt.savefig("./graphs/promedioArbolesBagre.png")
    print(promedioArbolesBagre)
    '''

    '''
    #Grafica para el filtro de siembras en Santa fe de Antioquia
    promedioArbolesSRO = dataFrame.groupby('Vereda')['Arboles'].mean()
    colores = ["#3D9637", "#61DE59", "#1BE80E"]
    plt.figure(figsize=(8, 8))
    plt.pie(promedioArbolesSRO.values, labels=promedioArbolesSRO.index, colors=colores, autopct='%1.1f%%')
    plt.title("Distribución de árboles en Santa Rosa de Osos por vereda Mina Vieja y Las Cruces")
    plt.savefig("./graphs/distribucion_arboles_SantaRosa.png")
    '''

     #Grafica para el filtro de siembras en yondo
    promedioArbolesYondo=dataFrame.groupby('Vereda')['Arboles'].mean()
    #0. generando lista de colores
    colores=["#B68F27","#DAAD35","#977721","#8A6A14"]
    #1. Generar una figura 
    plt.figure(figsize=(10,10))
    #2. Genero la grafica que deseo
    plt.bar(promedioArbolesYondo.index, promedioArbolesYondo.values, color=colores)
    #3. Agrego titulo a la gráfica
    plt.title("Promedio de Siembras en Yondó")
    #4. Etiqueta o nombre del eje X
    plt.xlabel("Eventos")
    #5. Etiqueta o nombre del eje y
    plt.ylabel("Promedio de arboles")
    #6. Activar el grid
    plt.grid(True)
    #7. rotar los labels X
    plt.xticks(rotation=45)
    #7. Guardando nuestra grafica
    plt.savefig("./graphs/promedioArbolesYondo.png")
    print(promedioArbolesYondo)

    
    