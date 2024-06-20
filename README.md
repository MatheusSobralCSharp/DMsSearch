# DMs Searcher

### Esse script/código em python funciona de maneira com que busque as exatas mensagens que você quer, mesmo que você não se lembre da DMs ou Servidor em que se encontra, ele procura em todas utilizando sua token

<div style ="display: inline_block"><br/>
    <img align="center" alt="csharp" src=https://img.shields.io/badge/Discord-7289DA?style=for-the-badge&logo=discord&logoColor=white>
    <img align="center" alt="csharp" src=https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white>
</div>

# DMs Searcher

### This script/code in python works in a way that searches for the exact messages you want, even if you don't remember the DMs or Server you are in, it searches in all using your token

<div style ="display: inline_block"><br/>
    <img align="center" alt="csharp" src=https://img.shields.io/badge/Discord-7289DA?style=for-the-badge&logo=discord&logoColor=white>
    <img align="center" alt="csharp" src=https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white>
</div>

# How to run? Como usar:
### Insert the token in the end of code in the final line, Insira seu token no final do código:

`client.run('token')`

## Also change the settings in config.json, put your token, put if you wan't search only in dms or server's too / Também altere as configurações no config.json, coloque seu token, coloque também caso não queira procurar apenas no dms ou no servidor também. yes para sim, no para não, yes for true, and no for false

```{
"type": {
		"servers/servidores": "yes", 
		"dm": "yes"
	},
	"token": "seu token aqui / your token here",	
	"words/palavras": [
		"place a word here / insira uma palavra aqui",
		"place a word here / insira uma palvra aqui"
	],
	"regex": [
		"One Regex / Um Regex",
		"Another Regex / Outro Regex"
	]
}
```
### After that, run in cmd / Depois disso rode no cmd/prompt de comando:
`pip install discord && colorama`

## In the end of everything, run the script main.py / No final de tudo, rode o script main.py

`python main.py`

# As localizações ficam armazenados no .txt / The word files are stored in .txt
