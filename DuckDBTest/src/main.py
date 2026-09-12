import duckdb  # type: ignore[import-not-found]
import pandas as pd  # type: ignore[import-not-found]

duckdb.sql("SELECT * FROM 'experimentos.csv' LIMIT 5").show()
## 1. Corridas con accuracy > 0.85
duckdb.sql("""SELECT *
FROM 'experimentos.csv'
WHERE accuracy > 0.85;""").show()
duckdb.sql("SELECT COUNT(*) FROM 'experimentos.csv'").show()

## 2. Accuracy promedio por modelo
duckdb.sql("""SELECT
    m.nombre        AS modelo,
    AVG(e.accuracy) AS accuracy_promedio,
    COUNT(*)        AS num_corridas
FROM 'experimentos.csv' e
JOIN 'modelos.csv' m ON e.id_modelo = m.id_modelo
GROUP BY m.nombre
ORDER BY accuracy_promedio DESC;
""").show()


duckdb.sql("""SELECT
    m.nombre    AS modelo,
    d.nombre    AS dataset,
    e.accuracy
FROM 'experimentos.csv' e
JOIN 'modelos.csv'  m ON e.id_modelo  = m.id_modelo
JOIN 'datasets.csv' d ON e.id_dataset = d.id_dataset;
""").show()

