from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def hello():
    html = '''<form action="/" method="post">
                <div class="Cozinha">
                    <p>Quantas vezes voce cozinha por dia:
                     <select  name="cozinha">
                        <option value="1">1</option> 
                        <option value="2">2</option>
                        <option value="3">3</option>
                        <option value="4">4</option>
                    </select>
                    </p>

                    <p>Qual metodo voce utiliza (Eletrico, Gas natural ou Gas GLP):
                     <select class="form-control" name="tipoCozinha">
                        <option value="eletrico">Eletrico</option> 
                        <option value="gas_nat">Gas natural</option>
                        <option value="glp">GLP</option>
                    </select>
                    </p>
                </div>
                <div class="Carro">
                    <label for="pwd">Quantos km voce anda?:</label>
                    <input type="text" class="form-control" id="pwd" name="km">
                    <p>Meio de transporte:
                    <select class="form-control" id="sel2" name="transporte">
                        <option value="carro">Carro</option> 
                        <option value="onibus">Onibus</option>
                        <option value="outros">Outros</option>
                        
                    </select>
                    </p>
                    <p>Motor do carro:
                    <select class="form-control" id="sel2" name="motor">
                        <option value="1.0">1.0</option> 
                        <option value="1.4">1.4</option>
                        <option value="1.6">1.6</option>
                        <option value="2.0">2.0</option>
                        <option value="onibus">Onibus</option> 
                    </select>
                    </p>
                    <p>Gasolina ou alcool?:
                    <select class="form-control" id="sel2" name="combustivel">
                        <option value="gasolina">Gasolina</option> 
                        <option value="alcool">Alcool</option>
                        <option value="flex">Flex</option>
                    </select>
                    </p>
                </div>  
                
                <div class="banho">
                    <p>Quantos banhos voce toma por dia?:
                    <select class="form-control" id="sel3" name="banho">
                        <option value="1">1</option> 
                        <option value="2">2</option>
                        <option value="3">3</option>
                        <option value="4">4</option>
                    </select>
                    </p>
                    <p>Quantos tempo de banhos?:
                    <select class="form-control" id="sel4" name="tempoBanho">
                        <option value="5">5 minutos</option> 
                        <option value="10">10 minutos</option>
                        <option value="15">15 minutos</option>
                        <option value="20">20 minutos</option>
                    </select>
                    </p>
                     <p>Seu chuveiro e eletrico ou a gas?:
                    <select class="form-control" id="sel3" name="tipoBanho">
                        <option value="eletrico">Eletrico</option> 
                        <option value="gas">Gas</option>
                        
                    </select>
                    </p>
                </div>
                <div class="Lampadas">
                    <p>Quantas lampadas ligadas voce tem em casa?:
                    <input type="text" name="numeroLamp">
                    </p>
                    <p>Quanto tempo, em media, por dia, elas ficam ligadas?:
                    <select class="form-control" id="sel3" name="tempoLamp">
                        <option value="1">1 hr</option> 
                        <option value="2">2 hr</option>
                        <option value="3">3 hr</option>
                        <option value="4">4 hr</option>
                        <option value="5">5 hr</option> 
                        <option value="6">6 hr</option>
                        <option value="7">7 hr</option>
                        <option value="8">8 hr</option>
                        <option value="9">9 hr</option> 
                        <option value="10">10 hr</option>
                        <option value="11">11 hr</option>
                        <option value="12">12 hr</option>
                    </select>
                    </p>
                    <p>Qual tipo de lampada?:
                    <select class="form-control" id="sel3" name="tipoLampada">
                        <option value="incandescente">Incandescente</option> 
                        <option value="fluorescente">Fluorescente</option>
                        <option value="led">LED</option>

                        
                    </select>
                    </p>
                </div>
                 <div class="Eletrodomestico">
                    <p>Quantas geladeiras voce tem?:
                    <input type="text" name="numeroGeladeira">
                    </p>
                    <p>Quantas portas ?:
                    <select class="form-control" id="sel3" name="numeroPortaGeladeira">
                        <option value="1">1 porta</option> 
                        <option value="2">2 portas</option>
                    </select>
                    </p>
                    <p>Quantos freezers?:
                    <select class="form-control" id="sel3" name="numeroFreezer">
                        <option value="1">1</option> 
                        <option value="2">2</option>
                        <option value="3">3</option>
                    </select>
                    </p>
                    <label for="pwd">Quantas vezes voce lava roupa por semana?:</label>
                    <input type="text" class="form-control" id="pwd" name="vezesLavaRoupa">
                    <p>Voce usa uma secadora?:
                    <select class="form-control" id="sel2" name="secadoraBool">
                        <option value="1">Sim</option> 
                        <option value="0">Nao</option>
                    </select>
                    </p>
                    <label for="pwd">Quantos minutos voce seca a roupa?:</label>
                    <input type="text" class="form-control" id="pwd" name="vezesSecaRoupa">
                    <p>Voce usa uma secadora?:

                    <select class="form-control" id="sel2" name="passaRoupaBool">
                        <option value="1">Sim</option> 
                        <option value="0">Nao</option>
                        </select>
                    </p>
                    <label for="pwd">Quantos minutos voce usa o ferro de passar roupa?:</label>
                    <input type="text" class="form-control" id="pwd" name="vezesPassaRoupa">
                        
                        
                    </select>
                    </p>

                </div>
                <input type="submit" value="Calcular">
                </form>'''
    
    
    return (html)

@app.route("/", methods=['POST'])
def equation():
    cozinha = float(request.form.get("cozinha")) 
    tipo_cozinha = request.form.get("tipoCozinha")
    km = float(request.form.get("km"))
    meio = request.form.get("transporte")
    motor = request.form.get("motor")
    combustivel = request.form.get("combustivel")
    banho =  float(request.form.get("banho"))
    tempoBanho = float(request.form.get("tempoBanho"))
    tipoBanho = request.form.get("tipoBanho")
    numeroLamp = float(request.form.get("numeroLamp"))
    tipoLampada = request.form.get("tipoLampada")
    tempoLampada = float(request.form.get("tempoLamp"))
    numeroGeladeira =  float(request.form.get("numeroGeladeira"))
    numeroPortaGeladeira = request.form.get("numeroPortaGeladeira")
    numeroFreezer = float(request.form.get("numeroFreezer"))
    vezesLavaRoupa = float(request.form.get("vezesLavaRoupa"))
    secadoraBool = float(request.form.get("secadoraBool"))
    if secadoraBool:
        vezesSecaRoupa = float(request.form.get("vezesSecaRoupa"))
    passaRoupaBool = float(request.form.get("passaRoupaBool"))
    if passaRoupaBool:
        vezesPassaRoupa = float(request.form.get("vezesPassaRoupa"))


    
    motores_gasolina = {"1.0": 12.9,"1.4": 11.62,".1.6": 11.6, "2.0": 11.5} 

    cozinhada = {"eletrico": [6, 0.0871], "glp": [0.1125, 0.8275], "gas_nat": [0.09, 0.75]}

    lampadaEnerg = {"incandescente": 60/1000, "fluorescente":15/1000, "led":7/1000}

    banho_energia_eletric = 0.08/1000.0 #Mwh por banho 
    banho_energia_gas = (0.567 * 0.85) * (11/3)

    geladeiraTipo = {"1": 2, "2": 3}
 
    constEletric = 0.0871

    emissao = 0

    if (meio == "carro" and combustivel == 'alcool' and combustivel =!'onibus'):
        emissao += ((0.1029) * (km / ((motores_gasolina[motor]) * (11/3)))) 
    
    elif (meio == "carro" and combustivel =!'onibuss'):
        emissao += ((0.4673625 + 0.1029) * (km / ((motores_gasolina[motor])* (11/3)))) 

    elif (meio == 'onibus'):
        emissao += (0.73008 * (km / (144/(11/3)))) 
    
    if (tipo_cozinha == 'eletrico'):
        emissao += cozinha/2 * (cozinhada[tipo_cozinha][0] * cozinhada[tipo_cozinha][1]) 

    elif (tipo_cozinha == 'glp'):
        emissao += (cozinha * (cozinhada[tipo_cozinha][0] * cozinhada[tipo_cozinha][1]) ) * (11/3)
    
    elif (tipo_cozinha == 'gas_nat'):
        emissao += (cozinha * (cozinhada[tipo_cozinha][0] * cozinhada[tipo_cozinha][1]))*(11/3) 

    if (tipoBanho == "eletrico"):
        emissao += tempoBanho * banho_energia_eletric * constEletric
    elif (tipoBanho == 'gas'):
        emissao += tempoBanho * banho_energia_gas * constEletric

    emissao +=( (numeroGeladeira * geladeiraTipo[numeroPortaGeladeira]) +( numeroFreezer * 4)) * constEletric

    if (secadoraBool and passaRoupaBool):
        emissao += (1.5 * vezesLavaRoupa + 3.5 * vezesSecaRoupa + vezesPassaRoupa * 0.0166) * constEletric

    elif (secadoraBool and not passaRoupaBool):
        emissao += (1.5 * vezesLavaRoupa + 3.5 * vezesSecaRoupa)  * constEletric

    elif (not secadoraBool and passaRoupaBool):
        emissao += (1.5 * vezesLavaRoupa + vezesPassaRoupa * 0.0166) * constEletric

    else:
        emissao += (1.5 * vezesLavaRoupa) * constEletric
    

    emissao += numeroLamp * lampadaEnerg[tipoLampada] * tempoLampada * constEletric

    return("{:.3f} kg de Co2 em 1 mes". format(emissao * 30))
    

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)

