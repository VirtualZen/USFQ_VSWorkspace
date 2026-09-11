"""Genera ventas.csv para la actividad del Dia 3.

1 500 000 filas x 10 columnas, unos 95 MB. Tarda ~17 s.
Semilla fija: a todos les sale exactamente el mismo archivo.

No se sube el CSV al aula virtual (95 MB): se sube este script y cada
quien genera sus datos. Se corre UNA vez.

    uv add pandas pyarrow
    uv run python generar_ventas.py
"""
import numpy as np
import pandas as pd

rng = np.random.default_rng(42)
N = 1_500_000

CIUDADES = ["Quito", "Guayaquil", "Cuenca", "Ambato", "Loja", "Manta"]
PRECIO_BASE = {"laptop": 950, "monitor": 205, "teclado": 45, "mouse": 16,
               "impresora": 180, "tablet": 320, "auriculares": 60}

producto = rng.choice(list(PRECIO_BASE), N)
precio = np.array([PRECIO_BASE[p] for p in producto]) * rng.normal(1, 0.10, N)
cantidad = rng.integers(1, 15, N)
descuento = np.clip(rng.normal(8, 5, N), 0, 40)

ventas = pd.DataFrame({
    "fecha": pd.to_datetime("2024-01-01")
             + pd.to_timedelta(rng.integers(0, 900, N), unit="D"),
    "ciudad": rng.choice(CIUDADES, N),
    "producto": producto,
    "canal": rng.choice(["web", "tienda", "telefono"], N),
    "cliente_id": rng.integers(1, 200_000, N),
    "vendedor_id": rng.integers(1, 500, N),
    "precio": precio.round(2),
    "cantidad": cantidad,
    "descuento": descuento.round(1),
})
ventas["total"] = (ventas.precio * ventas.cantidad
                   * (1 - ventas.descuento / 100)).round(2)

ventas.to_csv("ventas.csv", index=False)
print(f"ventas.csv  ->  {len(ventas):,} filas x {len(ventas.columns)} columnas")
