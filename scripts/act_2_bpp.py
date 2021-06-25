import pytest
import act_1_bpp

@pytest.fixture
def data_load():
    data = act_1_bpp.read_data()
    
    return data

# test para probar lectura correcta de datos, se devuelve 12 columnas
def test_read_data(data_load):
    ncol = 12

    assert len(data_load.columns) ==  ncol

# test para comprobar que se entrega el mes de mayor gasto
def test_mes_mayor_gasto(data_load):
    mes = 'Abril'
    monto = -34133.0
    mes_test, total = act_1_bpp.mayor_gasto_mensual(data_load)

    assert mes == mes_test
    assert monto == total

# test para comprobar que se entrega el mes de mayor ahorro
def test_mayor_ahorro_mensual(data_load):
    mes = 'Enero'
    monto = 12064.0
    mes_test, total = act_1_bpp.mayor_ahorro_mensual(data_load)

    assert mes == mes_test
    assert monto == total

# test para comprobar el correcto calculo del gasto medio y promedio del año
def test_gastos_media_mean_anual(data_load):
    
    total_promedio = -497.14
    total_medio = -497

    gasto_promedio, gasto_medio = act_1_bpp.gastos_media_mean_anual(data_load)

    assert total_promedio == gasto_promedio
    assert total_medio == gasto_medio

# test para comprobar el correcto calculo de ingresos y gastos del ano
def test_gastos_ingresos_ano(data_load):

    gastos = -296791
    ingresos = 280961

    gastos_ano, ingresos_ano = act_1_bpp.gastos_ingresos_ano(data_load)

    assert gastos == gastos_ano
    assert ingresos == ingresos_ano
