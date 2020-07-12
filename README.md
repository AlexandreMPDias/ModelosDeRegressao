# Trabalho de Modelos de Regressão - 2020.1 - PUC-Rio
# Grupo:
	> Alexandre Dias - 1413183
# Objetivo
Encontrar a probabilidade de uma pessoa ter uma doença arterial coronária, dadas as características (demográficas, comportamentais e biológicas) dela.
## Variável Dependente
Uma variável boolean que vale 1 se o indíviduo tiver tido uma doença arterial coronária ao longo de 10 anos de vida após fazer esses exames.
## Variáveis Independentes
|       Escopo        |    Varíavel     |                             Descrição                             |      ...      |
| :-----------------: | :-------------: | :---------------------------------------------------------------: | :-----------: |
|     Demográfico     |       sex       |              Sexo do paciente. 1 se Masculino, 0 se feminino      |    Nominal    |
|     Demográfico     |       age       |                     Idade do paciente em anos                     | Contínuo *(1) |
|   Comportamental    |  currentSmoker  |                 1 se o paciente é fumante, 0 se não               |    Nominal    |
|   Comportamental    |   cigsPerDay    |   Número de cigarros que o paciente fuma, em média, em um dia     | Contínuo *(2) |
|  Histórico Médico   |     BPMeds      | 1 se o Paciente estava sob influência de remédios para pressão sanguínea, 0 se não |    Nominal    |
|  Histórico Médico   | prevalentSmoker |         1 se o Paciente já teve um derrame, 0 se não              |    Nominal    |
|  Histórico Médico   |  prevalentHyp   |             1 se Paciente estava hipertenso, 0 se não             |    Nominal    |
|  Histórico Médico   |    diabetes     |                  1 se o Paciente teve diabetes, 0 se não          |    Nominal    |
| Perfil Médico Atual |     totChol     |          Nível total de Colesterol no sangue em mg/dL             |   Contínuo    |
| Perfil Médico Atual |      sysBP      |             Pressão Sanguínea Sistólica em mmHg                   |   Contínuo    |
| Perfil Médico Atual |      diaBP      |                   Pressão sanguínea diastólica em mmHg            |   Contínuo    |
| Perfil Médico Atual |       BMI       |                     Índice de Massa Corpórea em kg/m^2            |   Contínuo    |
| Perfil Médico Atual |    heartRate    |                 Frequência Cardíaca Média (min^(-1))              |   Contínuo    |
| Perfil Médico Atual |     glucose     |                 Nível de Glucose no sangue em mg/dL               |   Contínuo    |

*(1) - Embora os valores de idades tenham sido arredondados para valores inteiros, o conceito de idade é contínuo.  
*(2) - Pois uma pessoa pode fumar um número qualquer de cigarros, até mesmo meio cigarro.