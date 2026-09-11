try:
	# Preferred when used as a package: `python -m src.mi_proyecto.estadistica`
	from .main import crear_dataframe
except Exception:
	# Fallbacks for other execution contexts (script run or different PYTHONPATH)
	try:
		from mi_proyecto.main import crear_dataframe
	except Exception:
		from src.mi_proyecto.main import crear_dataframe

from .logging_utils import log_start, log_end

log_start("estadistica.py")

df = crear_dataframe()

print("Estadísticas del DataFrame:")
print(df.describe())

log_end("estadistica.py")