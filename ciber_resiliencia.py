import random

# ============================================================
# Simulacion de Ciber Resiliencia Empresarial
# Basado en: "Ciberseguridad: brechas criticas que aun desafian
# la proteccion de la informacion empresarial"
# Lima, Peru - Abril 2026 | Kyndryl Readiness Report 2025
# ============================================================

SEPARATOR = "=" * 60


# -----------------------------------------------------------
# PILAR 1: Visibilidad integrada de riesgos
# -----------------------------------------------------------
def evaluar_riesgo_organizacion(nombre, nivel_preparacion):
    """Evalua el nivel de preparacion de una organizacion (0-100)."""
    if nivel_preparacion >= 70:
        estado = "PREPARADA"
    elif nivel_preparacion >= 40:
        estado = "PARCIALMENTE PREPARADA"
    else:
        estado = "VULNERABLE"
    return {"organizacion": nombre, "nivel": nivel_preparacion, "estado": estado}


def simular_visibilidad_riesgos(organizaciones):
    print("\n[PILAR 1] Visibilidad integrada de riesgos")
    print(SEPARATOR)
    resultados = [evaluar_riesgo_organizacion(n, p) for n, p in organizaciones]
    preparadas = sum(1 for r in resultados if r["estado"] == "PREPARADA")
    porcentaje = (preparadas / len(resultados)) * 100
    for r in resultados:
        print(f"  {r['organizacion']:30s} | Nivel: {r['nivel']:3d}% | {r['estado']}")
    print(f"\n  >> Solo el {porcentaje:.0f}% de organizaciones esta completamente preparada.")
    print(f"     (Referencia real: 31% segun Kyndryl Readiness Report 2025)")
    return resultados


# -----------------------------------------------------------
# PILAR 2: Modernizacion de sistemas
# -----------------------------------------------------------
SISTEMAS = [
    {"nombre": "ERP Legacy v2.3",     "actualizado": False, "vulnerabilidades": 14},
    {"nombre": "CRM Cloud v5.1",       "actualizado": True,  "vulnerabilidades": 1},
    {"nombre": "BD Oracle 11g",        "actualizado": False, "vulnerabilidades": 22},
    {"nombre": "Portal Web React",     "actualizado": True,  "vulnerabilidades": 0},
    {"nombre": "Servidor FTP antiguo", "actualizado": False, "vulnerabilidades": 31},
]

def simular_modernizacion():
    print("\n[PILAR 2] Modernizacion de sistemas")
    print(SEPARATOR)
    total_vuln_antes = sum(s["vulnerabilidades"] for s in SISTEMAS)
    for s in SISTEMAS:
        estado = "OK" if s["actualizado"] else "REQUIERE ACTUALIZACION"
        print(f"  {s['nombre']:30s} | Vulnerabilidades: {s['vulnerabilidades']:2d} | {estado}")
    for s in SISTEMAS:
        if not s["actualizado"]:
            s["vulnerabilidades"] = max(0, s["vulnerabilidades"] // 5)
            s["actualizado"] = True
    total_vuln_despues = sum(s["vulnerabilidades"] for s in SISTEMAS)
    reduccion = ((total_vuln_antes - total_vuln_despues) / total_vuln_antes) * 100
    print(f"\n  >> Tras modernizacion: vulnerabilidades reducidas en {reduccion:.0f}%")
    print(f"     ({total_vuln_antes} -> {total_vuln_despues} vulnerabilidades totales)")


# -----------------------------------------------------------
# PILAR 3: Backup inmutable y recuperacion orquestada
# -----------------------------------------------------------
def simular_backup_y_recuperacion():
    print("\n[PILAR 3] Backup inmutable y recuperacion orquestada")
    print(SEPARATOR)
    archivos = ["clientes.db", "transacciones.db", "contratos.pdf", "config.yaml"]
    backups = {}
    print("  Creando backups inmutables...")
    for archivo in archivos:
        backups[archivo] = f"BACKUP_INMUTABLE_{archivo.upper()}_v1"
        print(f"  Backup creado: {backups[archivo]}")

    print("\n  Simulando ransomware: archivos cifrados...")
    archivos_cifrados = {a: "[CIFRADO]" for a in archivos}
    for a, v in archivos_cifrados.items():
        print(f"  {a}: {v}")

    print("\n  Recuperando desde backups inmutables...")
    recuperados = 0
    for archivo in archivos:
        if archivo in backups:
            print(f"  Restaurado: {archivo} desde {backups[archivo]}")
            recuperados += 1
    print(f"\n  >> Recuperacion exitosa: {recuperados}/{len(archivos)} archivos restaurados (100%)")


# -----------------------------------------------------------
# PILAR 4: Zero Trust en accesos e identidades
# -----------------------------------------------------------
USUARIOS = [
    {"nombre": "ana.garcia",   "rol": "admin",       "mfa": True,  "contexto_valido": True},
    {"nombre": "juan.perez",   "rol": "usuario",     "mfa": False, "contexto_valido": True},
    {"nombre": "atacante_ext", "rol": "desconocido", "mfa": False, "contexto_valido": False},
    {"nombre": "carlos.lopez", "rol": "auditor",     "mfa": True,  "contexto_valido": False},
]

def verificar_zero_trust(usuario):
    if not usuario["mfa"]:
        return "DENEGADO (sin MFA)"
    if not usuario["contexto_valido"]:
        return "DENEGADO (contexto invalido)"
    return "ACCESO PERMITIDO"

def simular_zero_trust():
    print("\n[PILAR 4] Zero Trust - Gestion de accesos e identidades")
    print(SEPARATOR)
    for u in USUARIOS:
        resultado = verificar_zero_trust(u)
        print(f"  {u['nombre']:20s} | Rol: {u['rol']:12s} | MFA: {str(u['mfa']):5s} | {resultado}")
    bloqueados = sum(1 for u in USUARIOS if verificar_zero_trust(u) != "ACCESO PERMITIDO")
    print(f"\n  >> Zero Trust bloqueo {bloqueados}/{len(USUARIOS)} accesos no autorizados o inseguros.")


# -----------------------------------------------------------
# PILAR 5: IA para deteccion de amenazas
# -----------------------------------------------------------
def detectar_amenaza_ia(evento):
    """Modelo simple basado en reglas que simula deteccion por IA."""
    score = 0
    if evento.get("intentos_fallidos", 0) > 5:   score += 40
    if evento.get("hora_inusual", False):          score += 30
    if evento.get("ip_desconocida", False):        score += 20
    if evento.get("volumen_datos_alto", False):    score += 25
    if score >= 60:
        return "AMENAZA DETECTADA", score
    elif score >= 30:
        return "ACTIVIDAD SOSPECHOSA", score
    else:
        return "NORMAL", score

def simular_ia_deteccion():
    print("\n[PILAR 5] Inteligencia Artificial - Deteccion de amenazas")
    print(SEPARATOR)
    eventos = [
        {"id": "EVT-001", "intentos_fallidos": 0,  "hora_inusual": False, "ip_desconocida": False, "volumen_datos_alto": False},
        {"id": "EVT-002", "intentos_fallidos": 3,  "hora_inusual": True,  "ip_desconocida": False, "volumen_datos_alto": False},
        {"id": "EVT-003", "intentos_fallidos": 10, "hora_inusual": True,  "ip_desconocida": True,  "volumen_datos_alto": True},
        {"id": "EVT-004", "intentos_fallidos": 0,  "hora_inusual": False, "ip_desconocida": True,  "volumen_datos_alto": False},
        {"id": "EVT-005", "intentos_fallidos": 7,  "hora_inusual": True,  "ip_desconocida": True,  "volumen_datos_alto": False},
    ]
    for e in eventos:
        clasificacion, score = detectar_amenaza_ia(e)
        print(f"  {e['id']} | Score IA: {score:3d} | {clasificacion}")
    amenazas = sum(1 for e in eventos if detectar_amenaza_ia(e)[0] == "AMENAZA DETECTADA")
    print(f"\n  >> IA detecto {amenazas} amenaza(s) critica(s) de {len(eventos)} eventos analizados.")


# -----------------------------------------------------------
# PILAR 6: Arquitectura resiliente - simulacion de fallo controlado
# -----------------------------------------------------------
def simular_arquitectura_resiliente():
    print("\n[PILAR 6] Arquitectura resiliente - Fallo controlado y recuperacion")
    print(SEPARATOR)
    servicios = [
        {"nombre": "Servicio de Pagos",     "replicas": 3, "activas": 3},
        {"nombre": "API Gateway",            "replicas": 2, "activas": 2},
        {"nombre": "Servicio de Reportes",   "replicas": 2, "activas": 2},
        {"nombre": "Base de Datos Principal","replicas": 3, "activas": 3},
    ]
    print("  Estado inicial:")
    for s in servicios:
        print(f"  {s['nombre']:30s} | Replicas activas: {s['activas']}/{s['replicas']}")

    print("\n  Simulando fallo en un nodo por servicio...")
    for s in servicios:
        s["activas"] -= 1
    for s in servicios:
        disponible = s["activas"] > 0
        estado = "OPERATIVO (failover activo)" if disponible else "CAIDO"
        print(f"  {s['nombre']:30s} | Replicas activas: {s['activas']}/{s['replicas']} | {estado}")

    print("\n  Orquestador re-levantando nodos caidos...")
    for s in servicios:
        s["activas"] = s["replicas"]
    for s in servicios:
        print(f"  {s['nombre']:30s} | Replicas activas: {s['activas']}/{s['replicas']} | RESTAURADO")
    print("\n  >> Todos los servicios recuperados sin perdida de disponibilidad.")


# -----------------------------------------------------------
# RESUMEN FINAL
# -----------------------------------------------------------
def resumen_final():
    print("\n" + SEPARATOR)
    print("RESUMEN: Evaluacion de Ciber Resiliencia")
    print(SEPARATOR)
    pilares = [
        ("Visibilidad integrada de riesgos",   "Completado"),
        ("Modernizacion de sistemas",           "Completado"),
        ("Backup inmutable y recuperacion",     "Completado"),
        ("Zero Trust - Accesos e identidades",  "Completado"),
        ("IA para deteccion de amenazas",       "Completado"),
        ("Arquitectura resiliente",             "Completado"),
    ]
    for i, (pilar, estado) in enumerate(pilares, 1):
        print(f"  Pilar {i}: {pilar:40s} [{estado}]")
    print("\n  Conclusion: La ciber resiliencia no es un producto, es una estrategia.")
    print("  'La pregunta ya no es SI ocurriran los ataques, sino cuan preparadas")
    print("  estan las empresas para responder y recuperarse.' - Kyndryl, 2026")
    print(SEPARATOR)


# -----------------------------------------------------------
# MAIN
# -----------------------------------------------------------
if __name__ == "__main__":
    print(SEPARATOR)
    print("SIMULACION DE CIBER RESILIENCIA EMPRESARIAL")
    print("Basado en noticia: Lima, Peru - Abril 2026")
    print("Kyndryl Readiness Report 2025")
    print(SEPARATOR)

    organizaciones = [
        ("Banco Nacional SAC",        85),
        ("MiniMarket Online SAC",     25),
        ("Hospital Central",          45),
        ("Telefonica Peru",           78),
        ("PyME Textil Lima",          18),
        ("Gobierno Regional Lima",    55),
        ("Startup Fintech",           72),
        ("Distribuidora Mayorista",   30),
        ("Universidad Nacional",      60),
        ("Clinica Privada",           40),
    ]

    simular_visibilidad_riesgos(organizaciones)
    simular_modernizacion()
    simular_backup_y_recuperacion()
    simular_zero_trust()
    simular_ia_deteccion()
    simular_arquitectura_resiliente()
    resumen_final()
