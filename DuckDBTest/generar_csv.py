import csv, random
from pathlib import Path
random.seed(11)

MODELOS = [
    (1, "regresion_logistica", "lineal"),
    (2, "random_forest",       "arboles"),
    (3, "xgboost",             "arboles"),
    (4, "mlp_pequena",         "redes"),
    (5, "mlp_grande",          "redes"),
    (6, "svm_rbf",             "kernel"),
]
DATASETS = [
    (1, "clientes",   12000, 18),
    (2, "ventas",     45000, 12),
    (3, "imagenes",    8000, 64),
    (4, "sensores",  120000,  9),
]
# accuracy tipica por familia: da variedad y hace que Reto 1 devuelva algo
BASE = {"lineal": .78, "arboles": .88, "redes": .86, "kernel": .83}
COSTO = {"lineal": 3, "arboles": 40, "redes": 95, "kernel": 60}

filas, i = [], 1
for m_id, m_nom, fam in MODELOS:
    for d_id, d_nom, d_filas, _ in DATASETS:
        for k in range(random.choice([1, 2, 2, 3])):     # varias corridas por par
            acc = min(.99, max(.55, random.gauss(BASE[fam], .045)))
            seg = COSTO[fam] * (d_filas / 20000) * random.uniform(.7, 1.4)
            filas.append((i, m_id, d_id, f"2026-0{random.randint(1,6)}-{random.randint(10,28)}",
                          round(acc, 3), round(seg, 1)))
            i += 1

Path(".").mkdir(exist_ok=True)
def escribir(nombre, cab, datos):
    with open(nombre, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f); w.writerow(cab); w.writerows(datos)
    print(f"{nombre:18s} {len(datos):3d} filas")

escribir("modelos.csv",      ["id_modelo","nombre","familia"], MODELOS)
escribir("datasets.csv",     ["id_dataset","nombre","filas","columnas"], DATASETS)
escribir("experimentos.csv", ["id","id_modelo","id_dataset","fecha","accuracy","segundos"], filas)
