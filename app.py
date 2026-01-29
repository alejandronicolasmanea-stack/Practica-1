import streamlit as st  # 1. Corregido el import

# Configuración de la página
st.set_page_config(page_title="Calculadora de Rebajas", page_icon="🏷️")

# Título y Descripción
st.title("Calculadora de rebajas")
st.markdown("Bienvenido. Introduce tus datos para calcular el precio después del descuento.")
st.write("---")

# 2. Entrada de Datos (Barra Lateral)
st.sidebar.header("Tus Datos")

# Corregido: Nombres de variables sin espacios (precio_original, descuento)
precio_original = st.sidebar.number_input("Precio original (€)", min_value=0.0, value=150.0)
descuento = st.sidebar.slider("El descuento (%)", 0, 100, 50)

# 3. Botón de Cálculo y Lógica
if st.button("Calcular ahora"):
    
    # Cálculo
    ahorro = precio_original * (descuento / 100)
    precio_final = precio_original - ahorro
    
    # 4. Mostrar Resultado
    col1, col2 = st.columns(2)
    
    with col1:
        # Corregido: Ahora mostramos precio_final, no imc
        st.metric(label="Tu precio final es:", value=f"{precio_final:.2f} €", delta=f"-{ahorro:.2f} €")
        
    with col2:
        # Lógica adaptada a rebajas (en vez de IMC)
        if descuento >= 50:
            st.success("¡Menudo Chollo! (Más del 50%)")
            st.balloons()
        elif descuento >= 20:
            st.info("Es una buena oferta.")
        else:
            st.warning("El descuento es bajito.")
            
    # Extra: Mostrar la fórmula usada
    st.write("---")
    st.info("Fórmula matemática utilizada:")
    # Corregido: La fórmula LaTeX para que coincida con la realidad
    st.latex(r''' P_{final} = P_{original} - (P_{original} \times \frac{Descuento}{100}) ''')
