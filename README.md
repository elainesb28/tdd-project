# 🧪 Aprendendo e Aplicando TDD (Test-Driven Development)

Bem-vindo(a)! Este espaço foi criado para documentar meus estudos e práticas sobre **TDD**, uma abordagem de desenvolvimento que transforma a forma de construir softwares robustos e confiáveis.

---

## 🔄 O Ciclo de Desenvolvimento

O funcionamento do TDD segue a regra clássica de três passos simples:

1. **🔴 RED:** Escrevo um teste para algo que ainda não existe. O teste falha.
2. **🟢 GREEN:** Escrevo apenas o código necessário para fazer o teste passar.
3. **🔵 REFACTOR:** Limpo e otimizo o código, mantendo os testes passando.

---

## 🚀 Por que uso TDD?

* **Menos bugs:** Encontro falhas antes mesmo do código ir para a aplicação.
* **Design limpo:** Escrever o teste primeiro obriga o código a ser simples e modular.
* **Confiança:** Posso refatorar qualquer trecho sem medo de quebrar o sistema.
* **Documentação rápida:** Os testes mostram exatamente como cada função deve se comportar.

---

## 🛠️ Como rodar os testes por aqui

```bash
# Clone o projeto
git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)

# Entre na pasta
cd seu-repositorio

# Instale as dependências
npm install

# Rode os testes
npm test
