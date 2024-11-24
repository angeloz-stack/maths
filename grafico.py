import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

def f(z):
    # e^(z^2 - 1) - 1
    term1 = np.exp(z) + np.exp(-z) - 2
    # sin(pi/(z + 1))
    term2 = np.exp(2/z)
    term3 = (z**2 - 4)

    # (z^4 - 1)^2
    term4 = (z**2 + 9)
    # Funzione complessa
    return (term1 * term2) / (term3 * term4)

# Creazione della griglia nel piano complesso (x + iy)
x = np.linspace(-5, 5, 700)  # Ridotto il range per osservare meglio i dettagli
y = np.linspace(-5, 5, 700)
X, Y = np.meshgrid(x, y)
Z = X + 1j * Y  # La variabile complessa Z

# Calcolare il valore della funzione f(z)
F = f(Z)

# Calcolare il modulo |f(z)|
modulo = np.abs(F)

# **Scala logaritmica del modulo per evitare dominanza**
modulo_log = np.log10(modulo + 1e-10)  # Aggiunto un valore piccolo per evitare log(0)

# Calcolare la fase arg(f(z))
fase = np.angle(F)

# Creazione del grafico 3D per il modulo (con scala logaritmica)
fig_modulo = go.Figure(data=[go.Surface(z=modulo_log, x=X, y=Y, colorscale='Viridis')])
fig_modulo.update_layout(
    title="Modulo (scala log) di f(z)",
    scene=dict(
        xaxis_title='Parte Reale di z',
        yaxis_title='Parte Immaginaria di z',
        zaxis_title='log10(Modulo + 1e-10)'
    ),
    autosize=True
)

# Creazione del grafico 3D per la fase
fig_fase = go.Figure(data=[go.Surface(z=fase, x=X, y=Y, colorscale='hsv')])
fig_fase.update_layout(
    title="Fase di f(z)",
    scene=dict(
        xaxis_title='Parte Reale di z',
        yaxis_title='Parte Immaginaria di z',
        zaxis_title='Fase arg(f(z))'
    ),
    autosize=True
)

# Mostra i grafici
fig_modulo.show()
fig_fase.show()
