# Altox

# Ambiente de desenvolvimento
 Linux Mint 18
# Ide
ATOM
# Anaconda
python 3.6.6
# Métodos de testes
## Utilizando Postman
Para testar utilize o Postman: https://www.getpostman.com/

### Use o method Post

link: localhost:5000/drawMolecule

#### body: raw.json

exemplo:
```
{
	"drawMolecule":"CC(=O)Nc1ccc(O)cc1"
}
```

#usando url
exemplos de urls, este método achei estranho, mas não conheço muito bem o formato:

http://localhost:5000/drawMolecule/CC(=O)Nc1ccc(O)cc1
http://localhost:5000/drawMolecule/CN1C=NC2=C1C(=O)N(C(=O)N2C)C
http://localhost:5000/drawMolecule/O=C(C)Oc1ccccc1C(=O)O
http://localhost:5000/drawMolecule/CC(=O)Nc1ccc(O)cc1
