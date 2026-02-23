"""Módulo de conducción en estado estacionario (SI).

Este módulo implementa ecuaciones de conducción unidimensional en:
- Pared plana.
- Coordenadas cilíndricas.
- Coordenadas esféricas.

Diseñado para ser parte de una aplicación modular de transferencia de calor,
separando la lógica matemática de cualquier interfaz.
"""

from math import exp, log, pi


def _is_missing(value):
    """Devuelve True si la variable requerida no fue proporcionada."""
    return value is None


def _validate_knowns(variables, required_missing_count=1):
    """Valida que exactamente una variable sea desconocida (None)."""
    missing = [name for name, value in variables.items() if _is_missing(value)]
    if len(missing) != required_missing_count:
        raise ValueError(
            "Debe proporcionarse exactamente una variable desconocida (None). "
            f"Variables desconocidas recibidas: {missing}."
        )
    return missing[0]


def _validate_positive(name, value):
    """Valida que una magnitud física sea estrictamente positiva."""
    if value <= 0:
        raise ValueError(f"{name} debe ser > 0 en unidades SI. Valor recibido: {value}.")


def conduction_plane_wall(Q=None, k=None, A=None, L=None, delta_T=None):
    """Resuelve conducción 1D en pared plana en estado estacionario.

    Ecuación base (sin simplificar):
        Q = k * A * delta_T / L

    Donde:
        Q: Tasa de transferencia de calor [W]
        k: Conductividad térmica [W/(m·K)]
        A: Área normal al flujo de calor [m²]
        L: Espesor de la pared [m]
        delta_T: Diferencia de temperatura (T1 - T2) [K]

    Debe dejarse exactamente una variable como None para calcularla.

    Returns:
        float: Valor de la variable despejada.

    Raises:
        ValueError: Si faltan/ sobran incógnitas o hay datos no físicos.
    """
    unknown = _validate_knowns({"Q": Q, "k": k, "A": A, "L": L, "delta_T": delta_T})

    # Validaciones físicas de entradas conocidas.
    if k is not None:
        _validate_positive("k", k)
    if A is not None:
        _validate_positive("A", A)
    if L is not None:
        _validate_positive("L", L)

    if unknown == "Q":
        return k * A * delta_T / L
    if unknown == "k":
        if A * delta_T == 0:
            raise ValueError("No se puede despejar k: A * delta_T no puede ser 0.")
        return Q * L / (A * delta_T)
    if unknown == "A":
        if k * delta_T == 0:
            raise ValueError("No se puede despejar A: k * delta_T no puede ser 0.")
        return Q * L / (k * delta_T)
    if unknown == "L":
        if Q == 0:
            raise ValueError("No se puede despejar L: Q no puede ser 0.")
        return k * A * delta_T / Q
    if unknown == "delta_T":
        if k * A == 0:
            raise ValueError("No se puede despejar delta_T: k * A no puede ser 0.")
        return Q * L / (k * A)

    raise RuntimeError("Error interno: variable desconocida no contemplada.")


def conduction_cylinder(Q=None, k=None, L=None, r1=None, r2=None, delta_T=None):
    """Resuelve conducción radial en cilindro hueco en estado estacionario.

    Ecuación base (sin simplificar):
        Q = 2 * pi * k * L * delta_T / ln(r2 / r1)

    Donde:
        Q: Tasa de transferencia de calor [W]
        k: Conductividad térmica [W/(m·K)]
        L: Longitud del cilindro [m]
        r1: Radio interno [m]
        r2: Radio externo [m]
        delta_T: Diferencia de temperatura (T1 - T2) [K]

    Debe dejarse exactamente una variable como None para calcularla.
    Nota: para despejar r1 o r2 se usa inversión exponencial exacta de la ecuación.

    Returns:
        float: Valor de la variable despejada.

    Raises:
        ValueError: Si faltan/ sobran incógnitas o hay datos no físicos.
    """
    unknown = _validate_knowns(
        {"Q": Q, "k": k, "L": L, "r1": r1, "r2": r2, "delta_T": delta_T}
    )

    if k is not None:
        _validate_positive("k", k)
    if L is not None:
        _validate_positive("L", L)
    if r1 is not None:
        _validate_positive("r1", r1)
    if r2 is not None:
        _validate_positive("r2", r2)

    # Relación geométrica necesaria cuando ambos radios son conocidos.
    if r1 is not None and r2 is not None and r2 <= r1:
        raise ValueError("Debe cumplirse r2 > r1 para un cilindro hueco.")

    if unknown == "Q":
        denominator = log(r2 / r1)
        if denominator == 0:
            raise ValueError("ln(r2/r1) no puede ser 0.")
        return 2 * pi * k * L * delta_T / denominator

    if unknown == "k":
        denominator = 2 * pi * L * delta_T
        if denominator == 0:
            raise ValueError("No se puede despejar k: 2*pi*L*delta_T no puede ser 0.")
        return Q * log(r2 / r1) / denominator

    if unknown == "L":
        denominator = 2 * pi * k * delta_T
        if denominator == 0:
            raise ValueError("No se puede despejar L: 2*pi*k*delta_T no puede ser 0.")
        return Q * log(r2 / r1) / denominator

    if unknown == "delta_T":
        denominator = 2 * pi * k * L
        if denominator == 0:
            raise ValueError("No se puede despejar delta_T: 2*pi*k*L no puede ser 0.")
        return Q * log(r2 / r1) / denominator

    if unknown == "r2":
        if Q == 0:
            raise ValueError("No se puede despejar r2: Q no puede ser 0.")
        exponent = (2 * pi * k * L * delta_T) / Q
        r2_calc = r1 * exp(exponent)
        if r2_calc <= r1:
            raise ValueError("Resultado no físico: r2 calculado debe ser > r1.")
        return r2_calc

    if unknown == "r1":
        if Q == 0:
            raise ValueError("No se puede despejar r1: Q no puede ser 0.")
        exponent = (2 * pi * k * L * delta_T) / Q
        r1_calc = r2 / exp(exponent)
        if r1_calc <= 0 or r1_calc >= r2:
            raise ValueError("Resultado no físico: debe cumplirse 0 < r1 < r2.")
        return r1_calc

    raise RuntimeError("Error interno: variable desconocida no contemplada.")


def conduction_sphere(Q=None, k=None, r1=None, r2=None, delta_T=None):
    """Resuelve conducción radial en esfera hueca en estado estacionario.

    Ecuación base (sin simplificar):
        Q = 4 * pi * k * delta_T / ((1/r1) - (1/r2))

    Donde:
        Q: Tasa de transferencia de calor [W]
        k: Conductividad térmica [W/(m·K)]
        r1: Radio interno [m]
        r2: Radio externo [m]
        delta_T: Diferencia de temperatura (T1 - T2) [K]

    Debe dejarse exactamente una variable como None para calcularla.

    Returns:
        float: Valor de la variable despejada.

    Raises:
        ValueError: Si faltan/ sobran incógnitas o hay datos no físicos.
    """
    unknown = _validate_knowns({"Q": Q, "k": k, "r1": r1, "r2": r2, "delta_T": delta_T})

    if k is not None:
        _validate_positive("k", k)
    if r1 is not None:
        _validate_positive("r1", r1)
    if r2 is not None:
        _validate_positive("r2", r2)

    if r1 is not None and r2 is not None and r2 <= r1:
        raise ValueError("Debe cumplirse r2 > r1 para una esfera hueca.")

    if unknown == "Q":
        denominator = (1 / r1) - (1 / r2)
        if denominator == 0:
            raise ValueError("(1/r1 - 1/r2) no puede ser 0.")
        return 4 * pi * k * delta_T / denominator

    if unknown == "k":
        denominator = 4 * pi * delta_T
        if denominator == 0:
            raise ValueError("No se puede despejar k: 4*pi*delta_T no puede ser 0.")
        return Q * ((1 / r1) - (1 / r2)) / denominator

    if unknown == "delta_T":
        denominator = 4 * pi * k
        if denominator == 0:
            raise ValueError("No se puede despejar delta_T: 4*pi*k no puede ser 0.")
        return Q * ((1 / r1) - (1 / r2)) / denominator

    if unknown == "r2":
        denominator = (1 / r1) - (4 * pi * k * delta_T / Q)
        if denominator <= 0:
            raise ValueError("Resultado no físico: 1/r2 debe ser > 0.")
        r2_calc = 1 / denominator
        if r2_calc <= r1:
            raise ValueError("Resultado no físico: r2 calculado debe ser > r1.")
        return r2_calc

    if unknown == "r1":
        denominator = (1 / r2) + (4 * pi * k * delta_T / Q)
        if denominator <= 0:
            raise ValueError("Resultado no físico: 1/r1 debe ser > 0.")
        r1_calc = 1 / denominator
        if r1_calc <= 0 or r1_calc >= r2:
            raise ValueError("Resultado no físico: debe cumplirse 0 < r1 < r2.")
        return r1_calc

    raise RuntimeError("Error interno: variable desconocida no contemplada.")


if __name__ == "__main__":
    # Ejemplo 1: pared plana, calcular Q.
    q_wall = conduction_plane_wall(k=45.0, A=0.8, L=0.05, delta_T=60.0, Q=None)
    print(f"Pared plana -> Q = {q_wall:.3f} W")

    # Ejemplo 2: cilindro, calcular k.
    k_cyl = conduction_cylinder(Q=950.0, L=2.0, r1=0.03, r2=0.06, delta_T=75.0, k=None)
    print(f"Cilindro -> k = {k_cyl:.3f} W/(m·K)")

    # Ejemplo 3: esfera, calcular delta_T.
    dt_sphere = conduction_sphere(Q=1200.0, k=16.0, r1=0.05, r2=0.09, delta_T=None)
    print(f"Esfera -> delta_T = {dt_sphere:.3f} K")
