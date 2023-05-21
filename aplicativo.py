import streamlit as st
import pandas as pd
import numpy as np



def calcular_porcentagem_do_numero():
    valor = st.text_input("Digite o valor:", key="valor")
    porcentagem = st.text_input("Digite a porcentagem:", key="porcentagem")

    if valor and porcentagem:
        try:
            valor = float(valor)
            porcentagem = float(porcentagem)

            resultado = (valor * porcentagem) / 100
            st.success("A porcentagem de {}% de {} é igual a {}".format(porcentagem, valor, resultado))
        except ValueError:
            st.error("Valores inválidos!")

def calcular_porcentagem_do_total():
    valor = st.text_input("Digite o valor:", key="valor")
    total = st.text_input("Digite o valor total:", key="total")

    if valor and total:
        try:
            valor = float(valor)
            total = float(total)

            resultado = (valor * 100) / total
            st.success("{} é {}% de {}".format(valor, resultado, total))
        except ValueError:
            st.error("Valores inválidos!")

def calcular_valor_da_porcentagem():
    porcentagem = st.text_input("Digite a porcentagem:", key="porcentagem")
    total = st.text_input("Digite o total:", key="total")

    if porcentagem and total:
        try:
            porcentagem = float(porcentagem)
            total = float(total)

            resultado = (porcentagem * total) / 100
            st.success("{}% de {} é igual a {}".format(porcentagem, total, resultado))
        except ValueError:
            st.error("Valores inválidos!")

def calcular_valor_menos_porcentagem():
    valor_com_porcentagem = st.text_input("Digite o valor com porcentagem:", key="valor_com_porcentagem")
    porcentagem = st.text_input("Digite a porcentagem:", key="porcentagem")

    if valor_com_porcentagem and porcentagem:
        try:
            valor_com_porcentagem = float(valor_com_porcentagem)
            porcentagem = float(porcentagem)

            resultado = valor_com_porcentagem / (1 + (porcentagem / 100))
            st.success("O valor original após subtrair {}% de {} é igual a {}".format(porcentagem, valor_com_porcentagem, resultado))
        except ValueError:
            st.error("Valores inválidos!")

def main():
    st.title("Calculadora de Porcentagem")
    opcoes = ["Porcentagem do próprio número", "Porcentagem de um valor total", "Valor da porcentagem", "Valor menos a porcentagem"]
    escolha = st.selectbox("Escolha o tipo de cálculo:", opcoes)

    if escolha == "Porcentagem do próprio número":
        calcular_porcentagem_do_numero()
    elif escolha == "Porcentagem de um valor total":
        calcular_porcentagem_do_total()
    elif escolha == "Valor da porcentagem":
        calcular_valor_da_porcentagem()
    elif escolha == "Valor menos a porcentagem":
        calcular_valor_menos_porcentagem()

if __name__ == "__main__":
   main()