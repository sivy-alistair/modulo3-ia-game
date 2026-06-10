import time
import re
import random

def evaluar_segmento_tiempo(texto_completo, marcador, instancia):
    """
    Calcula la entropía de hardware para una instancia específica del signo.
    Divide el texto de manera segura para aislar el procesamiento de ese nodo.
    """
    t_inicio = time.perf_counter_ns()
    
    # Fragmentamos el texto de forma controlada hasta la instancia deseada
    partes = texto_completo.split(marcador)
    texto_parcial = "".join(partes[:instancia])
    
    # Ciclo controlado de consumo de CPU para leer el micro-estado del procesador
    for _ in range(random.randint(100, 250)):
        _ = re.findall(r'\b\w+\b', texto_parcial)
        
    t_final = time.perf_counter_ns()
    return (t_final - t_inicio) % 3

def obtener_mano(codigo):
    mapeo = {0: "🪨 Piedra", 1: "📄 Papel", 2: "✂️ Tijeras"}
    return mapeo.get(codigo, "Desconocido")

def resolver_combate(p1_cod, p2_cod, name_p1="Usuario", name_p2="IA"):
    if p1_cod == p2_cod:
        return f"⚖️ Empate entre {name_p1} y {name_p2} ({obtener_mano(p1_cod)})."
    if (p1_cod == 0 and p2_cod == 2) or (p1_cod == 1 and p2_cod == 0) or (p1_cod == 2 and p2_cod == 1):
        return f"🎉 ¡Ganador: {name_p1}! Con {obtener_mano(p1_cod)} vence a {obtener_mano(p2_cod)}."
    return f"🤖 ¡Ganador: {name_p2}! Con {obtener_mano(p2_cod)} vence a {obtener_mano(p1_cod)}."

# --- LABORATORIO DE CONTROL ---
if __name__ == "__main__":
    print("=" * 65)
    print("🎮      BIENVENIDO AL JUEGO DE MÓDULO 3: EDICIÓN BLINDADA         🎮")
    print("=" * 65)
    print("Instrucciones: Elige un signo detonador y la cantidad de personajes.")
    print("El procesador medirá en nanosegundos la separación de tus palabras.")
    print("¡Advertencia!: El abuso del sistema detonará un escudo de protección.\n")
    
    # 1. Parámetros Iniciales de Control
    marcador = input("👉 Paso 1: Introduce tu signo o emoji detonador (ej: -, +, ⭐): ").strip()
    if not marcador:
        print("⚠️ Error: El marcador no puede estar vacío.")
        exit()
        
    try:
        total_pjs = int(input("👉 Paso 2: ¿Cuántos personajes participarán en total en el chat?: ").strip())
        if total_pjs < 1:
            raise ValueError
    except ValueError:
        print("⚠️ Número no válido. Se configurará 1 jugador contra la consola.")
        total_pjs = 1

    # 3. Captura del flujo de texto
    print(f"\nConfigurado. Escribe tu frase. Recuerda colocar el signo '{marcador}' para separar turnos.")
    entrada_texto = input("👉 Paso 3: Escribe tu párrafo aquí: ")
    
    # Contamos la cantidad de signos en el string de entrada
    conteo_signos = entrada_texto.count(marcador)
    
    # 🛡️ ESCUDO DE CONTINGENCIA: Si el usuario intenta saturar con 4 o más signos
    if conteo_signos >= 4:
        print("\n🚨 AUTOMATIC SAFE RESET: Se detectó un intento de desbordamiento (4+ signos).")
        print("⚠️ Riesgo de sobrecarga física de RAM/CPU bloqueado de inmediato.")
        print("🤖 Modo Contingencia Activado: Desplegando matrices aleatorias de bajo consumo...\n")
        
        # Resolución instantánea de bajo impacto (cero uso de ciclos de CPU intensivos)
        for i in range(total_pjs + 1):
            nombre = "Tú (Usuario)" if i == 0 else f"Personaje {i}"
            print(f"-> {nombre}: {obtener_mano(random.randint(0, 2))} [Matriz Básica de Resguardo]")
        print("\n♻️ El programa se ha ejecutado de forma segura sin estresar el hardware.")
        exit()

    # 4. PROCESAMIENTO ESTABLE (1 a 3 Signos Detectados)
    if conteo_signos == 0:
        print(f"\n❌ Error: No se localizó el signo '{marcador}' en la frase. Ejecución abortada.")
        exit()
        
    # Fase de cálculo única: Evaluamos solo los signos reales presentes (máximo 3)
    pool_codigos_calculados = []
    for inst in range(1, conteo_signos + 1):
        codigo_derivado = evaluar_segmento_tiempo(entrada_texto, marcador, inst)
        pool_codigos_calculados.append(codigo_derivado)
        
    # 5. RESOLUCIÓN POR RECICLAJE (ROUND-ROBIN)
    print("\n📊 --- DESPLIEGUE DEL TABLERO RELACIONAL ---")
    
    # Asignamos jugadas a la lista total de personajes sin volver a encender el cronómetro de CPU
    jugadas_totales = []
    for idx in range(total_pjs + 1): # +1 para contar al Usuario principal
        nombre_entidad = "Tú (Usuario)" if idx == 0 else f"Pj {idx}"
        
        # Mapeo Cíclico: El residuo de la posición hereda el código pre-calculado
        codigo_asignado = pool_codigos_calculados[idx % len(pool_codigos_calculados)]
        jugadas_totales.append((nombre_entidad, codigo_asignado))
        
        print(f"👉 {nombre_entidad} utiliza el Nodo {idx % len(pool_codigos_calculados)}: {obtener_mano(codigo_asignado)}")

    # Mostramos los enfrentamientos en cascada contra el Usuario
    print("\n⚔️ --- RESOLUCIÓN EN CADENA DEL MULTIVERSO ---")
    user_name, user_cod = jugadas_totales[0]
    for name, cod in jugadas_totales[1:]:
        print(resolver_combate(user_cod, cod, user_name, name))