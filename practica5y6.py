import statsmodels.api as sm
from statsmodels.formula.api import ols
import pandas as pd

df = pd.read_csv('nba_modificado.csv')

modelo = ols('Puntos ~ Abreviacion_del_equipo', data=df).fit()

# Realizar el análisis de varianza (ANOVA)
anova_resultado = sm.stats.anova_lm(modelo)

# Imprimir la tabla ANOVA
print("Tabla ANOVA:")
print(anova_resultado)