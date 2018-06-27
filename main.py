from controladores.controlador_menu_principal import ControladorMenuPrincipal
from PyQt5.QtWidgets import QApplication
from controladores.controlador_simulacion import ControladorSimulacion
import sys,time
from PyQt5 import QtTest

import numpy as np
from modelo.Reloj import Reloj
from modelo.Taller import Taller
from modelo.Evento import Evento
from modelo.Vehiculo import Vehiculo
from modelo.Reparacion import Reparacion
import bisect


#60 mintos por hora * las 10 horas laborales.
AUTOS_POR_DIA = 15
MINUTOS_DE_SIMULACION_POR_DIA = 600
PORCENTAJE_DE_AUTOS_CON_ELEVADOR = 70

# Eventos
LLEGA_VEHICULO = 1  #cuando llega un vehiculo al taller
FINALIZA_REPARACION = 2 #cuando finaliza la reparacion de un vehiculo
SALE_VEHICULO = 3   #cuando un vehiculo sale del taller


def calcular_exponencial(valor_promedio,tiempo_reparacion):
    if tiempo_reparacion: 
        aux = np.random.exponential(valor_promedio)
        if aux < 30:
            return 30
        elif aux > 120:
            return 120
        else:
            return aux
    else:#Es tiempo de permanencia
        aux = np.random.exponential(valor_promedio)
        if aux < 300:
            return 300
        elif aux > 900:
            return 900
        else:
            return aux

def generar_cola_eventos_ordenada(dias_simulacion):
    lista_eventos = []
    """
    Variables necesarias de generar:
    * Eventos de llegadas de los autos(15 por dia con dist. Poisson y 70% requieren elevador)
    * A cada auto que llega le tengo que poner:
        * patente
        * usa_elevador * tiempo_reparacion(1hr Dist. Exponencial)
        * tiempo_total (1dia Dist. Exponencial)
    """

    for dia in range(dias_simulacion):
        """
        Por cada dia debo generar los 15~ eventos teniendo en cuenta el los minutos de ese día
        """
        minutos_diarios_usados = []
        #Caluclo la cantidad de autos para este día
        cantidad_de_autos = int(np.random.poisson(AUTOS_POR_DIA))
        #De esa cantidad utilizando el PORCENTAJE (70%) me quedo con la cantidad de autos que no requieren elevador
        cant_autos_usan_elevador = int((cantidad_de_autos * PORCENTAJE_DE_AUTOS_CON_ELEVADOR)/100)
        #Itereo por la cantidad de autos que NO requieren elevador
        for auto in range(cantidad_de_autos - cant_autos_usan_elevador):
            #Primero le asigo un minuto del dia
            minuto_de_ocurrencia_evento = np.random.randint(0,MINUTOS_DE_SIMULACION_POR_DIA) + (dia * MINUTOS_DE_SIMULACION_POR_DIA)
            #Mientras el numero sea repetido genero un nuevo
            while minuto_de_ocurrencia_evento in minutos_diarios_usados:
                minuto_de_ocurrencia_evento = np.random.randint(0,MINUTOS_DE_SIMULACION_POR_DIA) + (dia * MINUTOS_DE_SIMULACION_POR_DIA)
            #Cuando encuentro un minuto nuevo lo agrego a la lista para futuras comparaciones
            minutos_diarios_usados.append(minuto_de_ocurrencia_evento)
            #Calculamos el tiempo de permanencia del auto
            tiempo_permanencia = calcular_exponencial(600,False)
            #Genero el Vehiculo
            vehiculo = Vehiculo(minuto_de_ocurrencia_evento,False,tiempo_total=tiempo_permanencia)
            #Genereo el evento
            evento = Evento(LLEGA_VEHICULO,minuto_de_ocurrencia_evento,None,vehiculo)
            lista_eventos.append(evento)
        for auto in range(cant_autos_usan_elevador):
            #Primero le asigo un minto del dia
            minuto_de_ocurrencia_evento = np.random.randint(0,MINUTOS_DE_SIMULACION_POR_DIA) + (dia * MINUTOS_DE_SIMULACION_POR_DIA)
            #Mientras el numero sea repetido genero un nuevo
            while minuto_de_ocurrencia_evento in minutos_diarios_usados:
                minuto_de_ocurrencia_evento = np.random.randint(0,MINUTOS_DE_SIMULACION_POR_DIA) + (dia * MINUTOS_DE_SIMULACION_POR_DIA)
            #Cuando encuentro un minuto nuevo lo agrego a la lista para futuras comparaciones
            minutos_diarios_usados.append(minuto_de_ocurrencia_evento)
            #Calculamos el tiempo de permanencia del auto
            tiempo_permanencia = calcular_exponencial(600,False)
            #Calculamos el tiempo de uso del elvador del auto
            tiempo_reparacion = calcular_exponencial(60,True)
            #Genero el Vehiculo
            vehiculo = Vehiculo(minuto_de_ocurrencia_evento,True,reparacion=tiempo_reparacion,tiempo_total=tiempo_permanencia)
            #Genereo el evento
            evento = Evento(LLEGA_VEHICULO,minuto_de_ocurrencia_evento,None,vehiculo)
            lista_eventos.append(evento)
    lista_eventos = sorted(lista_eventos, key=lambda evento: evento.tiempo)
    print("Tamaño de la lista de Eventos Iniciales:{}".format(len(lista_eventos)))
    for evento in lista_eventos:
        print(evento)
    return lista_eventos

def get_evento_proximo(cola_eventos):
    if (len(cola_eventos) > 0):
        proximo_evento = cola_eventos[0]
        cola_eventos.remove(proximo_evento)
        return proximo_evento
    else:
        return None
    
def agregar_evento(cola_eventos, nuevo_evento):
    bisect.insort(cola_eventos, nuevo_evento)

def procesar_evento(un_evento, taller, reloj, cola_eventos): # tambien puede llamarse ocurre_evento. No me convence ninguno de los 2 como nombre. piensen otro
    if (un_evento.get_tipo() == LLEGA_VEHICULO):
        if(not taller.get_galpon().esta_lleno()):
            vehiculo = un_evento.get_vehiculo()
            vehiculo.set_tiempo_llegada(reloj.get_valor())
            taller.ingresar_vehiculo(vehiculo)
            mecanico = taller.get_mecanico_libre()
            if mecanico:
                if(vehiculo.get_usa_elevador()):
                    elevador = taller.get_elevador_libre()
                    if elevador:
                        vehiculo.set_tiempo_espera(0)
                        reparacion = taller.iniciar_reparacion(vehiculo, mecanico, elevador)
                        evento_nuevo = Evento(FINALIZA_REPARACION, reloj.get_valor() + vehiculo.get_tiempo_reparacion(), reparacion, vehiculo) 
                        agregar_evento(cola_eventos, evento_nuevo)
                        #Agrego el evento de Salida del auto cuando termine su tiempo de estadia
                        #evento_nuevo = Evento(SALE_VEHICULO, reloj.get_valor() + vehiculo.get_tiempo_total(),un_vehiculo=vehiculo) 
                        #agregar_evento(cola_eventos, evento_nuevo)
                else:
                    vehiculo.set_tiempo_espera(0)
                    reparacion = taller.iniciar_reparacion(vehiculo, mecanico)

                    t_reparacion = vehiculo.get_tiempo_total()
                    vehiculo.set_tiempo_reparacion(t_reparacion)

                    tiempo_finalizacion_reparacion = reloj.get_valor() + vehiculo.get_tiempo_reparacion()
                    evento_nuevo = Evento(FINALIZA_REPARACION, tiempo_finalizacion_reparacion, reparacion, vehiculo) 

                    agregar_evento(cola_eventos, evento_nuevo)
        else:
            taller.aumentar_autos_rechazados()

        
    elif(un_evento.get_tipo() == FINALIZA_REPARACION):
        reparacion = un_evento.get_reparacion()
        if (reparacion.get_elevador()):
            taller.finalizar_reparacion(reparacion)
            #Vuelvo al Taller hasta que pase el evento de SALE_VEHICULO
            vehiculo = reparacion.get_vehiculo()
            t_de_salida = (vehiculo.get_tiempo_llegada() + vehiculo.get_tiempo_total())
            if t_de_salida > reloj.get_valor():
                evento = Evento(SALE_VEHICULO, t_de_salida, None, vehiculo)
                agregar_evento(cola_eventos,evento)
            else:
                taller.egresar_vehiculo(un_evento.get_vehiculo())


            # INICIO DATOS GRAFICO ELEVADOR
            dias_horas = calcular_dias_transcurridos(reloj) - 1
            vehiculo = reparacion.get_vehiculo()
            horas_reparacion = vehiculo.get_tiempo_reparacion()
            elevador = reparacion.get_elevador()
            
            elevador.set_valor_arreglo(dias_horas,horas_reparacion)

            #FIN GRAFICO

        else:
            taller.finalizar_reparacion(reparacion)
            taller.egresar_vehiculo(reparacion.get_vehiculo())
        
        # INICIO DATOS GRAFICO MECANICO
        dias_horas = calcular_dias_transcurridos(reloj) - 1
        vehiculo = reparacion.get_vehiculo()
        horas_reparacion = vehiculo.get_tiempo_reparacion()
        mecanico = reparacion.get_mecanico()
        
        mecanico.set_valor_arreglo(dias_horas,horas_reparacion)

        #FIN GRAFICO
        
        #Tomo otro auto y creo nuevo evento de reparacion
        vehiculo = taller.get_vehiculo_libre()
        if vehiculo:
            mecanico = taller.get_mecanico_libre()
            if mecanico:
                if(vehiculo.get_usa_elevador()):
                    elevador = taller.get_elevador_libre()
                    if elevador:
                        vehiculo.set_tiempo_espera(reloj.get_valor() - vehiculo.get_tiempo_llegada())
                        reparacion = taller.iniciar_reparacion(vehiculo, mecanico, elevador)
                        evento_nuevo = Evento(FINALIZA_REPARACION, reloj.get_valor() + vehiculo.get_tiempo_reparacion(), reparacion, vehiculo) 
                        agregar_evento(cola_eventos, evento_nuevo)
                else:
                    vehiculo.set_tiempo_espera(reloj.get_valor() - vehiculo.get_tiempo_llegada())
                    reparacion = taller.iniciar_reparacion(vehiculo, mecanico)

                    t_reparacion = vehiculo.get_tiempo_total() - vehiculo.get_tiempo_espera()
                    if t_reparacion > 0:
                        vehiculo.set_tiempo_reparacion(t_reparacion)
                    else: # es para envitar error en caso de que su reparacion inicie despues de finalizado su tiempo de estadia
                        vehiculo.set_tiempo_reparacion(1)

                    tiempo_finalizacion_reparacion = reloj.get_valor() + vehiculo.get_tiempo_reparacion()
                    evento_nuevo = Evento(FINALIZA_REPARACION, tiempo_finalizacion_reparacion, reparacion, vehiculo) 

                    agregar_evento(cola_eventos, evento_nuevo)

    else:
        taller.egresar_vehiculo(un_evento.get_vehiculo())

    #NOTA: Cualquiera sea el evento, actualizo el estado en la interfaz grafica, llamando a Taller.actualizarEstadoGUI()
    #NOTA2: Deberia ser el main quien actualice los datos de la GUI ya que los dias transcurridos y eso los sabe el main.


def actualizar_pantalla(pantalla,dias_transcurridos,taller,finalizo_simulacion):
    pantalla.cant_dias_transcurridos_val_label.setText(str(dias_transcurridos))
    pantalla.lcdNumber.display(dias_transcurridos)
    pantalla.cant_autos_reparados_val_label.setText(str(taller.get_autos_reparados_con_elevador()+taller.get_autos_reparados_sin_elevador()))
    pantalla.con_elevador_val_label.setText(str(taller.get_autos_reparados_con_elevador()))
    pantalla.sin_elevador_val_label.setText(str(taller.get_autos_reparados_sin_elevador()))
    pantalla.cant_autos_rechazados_val_label.setText(str(taller.get_autos_rechazados()))
    pantalla.cant_autos_galpon_val_label.setText(str(taller.get_galpon().get_espacio_ocupado()))
    pantalla.cant_mecanicos_utilizados_val_label.setText(str(taller.get_cant_mecanicos_ocupados()))
    pantalla.cant_mecanicos_libres_val_label.setText(str(taller.get_cant_mecanicos_disponibles()))
    pantalla.cant_elevadores_utilizados_val_label.setText(str(taller.get_cant_elevadores_disponibles()))
    pantalla.cant_elevadores_libres_val_label.setText(str(taller.get_cant_elevadores_ocupados()))
    if finalizo_simulacion:
        pantalla.ver_grafico_uno_button.setEnabled(True)
        pantalla.ver_grafico_dos_button.setEnabled(True)
        pantalla.ver_grafico_tres_button.setEnabled(True)

def calcular_dias_transcurridos(reloj):
    return int(reloj.get_valor()/ MINUTOS_DE_SIMULACION_POR_DIA)+1

def main(controlador_simulacion, pantalla,cantidad_elevadores,cantidad_mecanicos,dias_simulacion):
    dias_transcurridos = 0
    #Se genera el reloj que guiará toda la simulación.
    reloj = Reloj()
    #Se genera la instancia de Taller.
    taller = Taller(dias_simulacion,cantidad_mecanicos,cantidad_elevadores)
    #Generar la cola de eventos.
    cola_eventos = generar_cola_eventos_ordenada(dias_simulacion)
    
    while (True):
        #Calculo los dias transcurridos
        dias_transcurridos = calcular_dias_transcurridos(reloj)

        #Obtenemos el evento correspondiente
        evento = get_evento_proximo(cola_eventos)
        if evento:
            #Adelantamos el reloj hasta el tiempo del proximo evento
            reloj.set_valor(evento.get_tiempo())
            #Procesamos el evento
            if (reloj.get_valor() < dias_simulacion * MINUTOS_DE_SIMULACION_POR_DIA):
                procesar_evento(evento, taller,reloj,cola_eventos)
                #Dada la respuesta definimos si hay que agregar
                #otro evento en la cola de eventos
                #if respuesta:
                #    agregar_evento(cola_eventos,respuesta)
                
                actualizar_pantalla(pantalla,dias_transcurridos, taller,False)
                
            else:
                print("No Hay mas tiempo, tiempo reloj: ", reloj.get_valor())
                print(evento)
                break
        else:
            print("No Hay mas eventos, tiempo reloj: ", reloj.get_valor())
            break
        #QtTest.QTest.qWait(1000)
    #Aca hariamos calculos para armar el grafico 
    controlador_simulacion.set_elevadores(taller.get_elevadores())
    controlador_simulacion.set_mecanicos(taller.get_mecanicos())
    #controlador_simulacion.mostrar_graficos()
    #controlador_simulacion.mostrarTodosLosGraficos()
    print("Termine la simulación")
    actualizar_pantalla(pantalla,dias_transcurridos, taller,True)
    
    
    #elevador_1 = elevadores[0]
    #for i in range(0,30):
     #   print("Elevador_1: " + str(elevador_1.get_valor_arreglo(i)))

def mostrar_ventana():
    app = QApplication(sys.argv)
    ventana_inicial = ControladorMenuPrincipal()
    ventana_inicial.exec_()
    ventana_simulacion = ControladorSimulacion(ventana_inicial.cantidad_elevadores,ventana_inicial.cantidad_mecanicos,ventana_inicial.dias_simulacion,[1,2,3],[4,5,6])
    ventana_simulacion.show()
    main(ventana_simulacion, ventana_simulacion.pantalla_simulacion,ventana_simulacion.cantidad_elevadores,ventana_simulacion.cantidad_mecanicos,ventana_simulacion.dias_simulacion)
    sys.exit(app.exec_())

if __name__ == '__main__':
    mostrar_ventana()