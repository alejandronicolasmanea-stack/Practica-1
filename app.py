import streamlit as st

# 1. Configuración de la página
st.set_page_config(page_title="Salud 3º ESO", page_icon="🏥")

# Título y Descripción
st.title("Calculadora de rebajas")
st.markdown("Bienvenido. Introduce tus datos para calcular el precio después del descuento.")
st.write("---") # Línea separadora

# 2. Entrada de Datos (Barra Lateral)
st.sidebar.header("Tus Datos")
precio original = st.sidebar.number_input("Tu capital ()", min_value=0, max_value=5000, value=150)
el descuento = st.sidebar.slider("El descuento (%)", 0, 100, 50 )

# 3. Botón de Cálculo y Lógica
if st.button("Calcular ahora"):
    
    # Fórmula Matemática: precio original por descuento entre 100
    ahorro = precio_original * (descuento / 100)
precio_final = precio_original - ahorro
    
    # 4. Mostrar Resultado con Diseño
    col1, col2 = st.columns(2)
    
    with col1:
        # Usamos metric para que el número se vea grande
        st.metric(label="Tu precio final es:", value=f"{imc:.2f}")
        
    with col2:
        # Usamos condicionales (if/elif/else) para el diagnóstico
        elif 18.5 <= imc < 25:
            st.success("¡Menudo Chollo!")
            st.balloons() # ¡Premio!
            
    # Extra: Mostrar la fórmula usada (LaTeX)
    st.write("---")
    st.info("Fórmula matemática utilizada:")
    st.latex(r''' precio final = precio original * (descuento / 100) ''')
