#!/usr/bin/python3
from bs4 import BeautifulSoup
from sys import argv
from requests import exceptions
import requests
import re

mails = set(); links = set(); images = set()
a = ['.com', '.net', '.org', '.gov', 'http:', 'https:', 'www.']
b = ['.png', '.jpg', '.gif', '.svg', '.jpeg']
script = ''; url = ''
script, url = argv

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def mail_look(url):
	try:
		print(bcolors.OKBLUE + '\nProcurando e-mails em %s...' % url)
		emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", content.text, re.I))
		for mail in emails:
			mails.update(mail) if all(x not in mail for x in b) else 0	
		if mails == set():
			print(bcolors.FAIL + '\n\tNenhum e-mail encontrado.');
		else:
			for val in mails:
				print(bcolors.OKGREEN + '\n\tE-MAIL: ' + val)		
	except ValueError:
		print(bcolors.FAIL + '\nPágina inválida.')

def link_look(url):
	try:
		print(bcolors.OKBLUE + '\nProcurando links em %s...' % url)
		link = [x['href'] for x in soup.findAll('a')]
		links.update(link)
		if links == set():
			print(bcolors.FAIL + '\n\tNenhum link encontrado.');
		else:
			for val in links:
				if all(x not in str(val) for x in a):
					val = fix_link(val, url)
				print(bcolors.OKGREEN + '\n\t\t' + val)
	except:
		print(bcolors.FAIL + '\nPágina inválida.')

def image_look(url):
	try:
		print(bcolors.OKBLUE + '\nProcurando imagens em %s...' % url)
		image = [x['src'] for x in soup.findAll('img')]
		images.update(image)
		if images == set():
			print(bcolors.FAIL + '\n\tNenhuma imagem encontrada.');
		else:
			for val in images:
				if all(x not in str(val) for x in a):
					val = fix_link(val, url)
				print(bcolors.OKGREEN + '\n\t\t' + val)
		print('\n')
	except:
		print(bcolors.FAIL + '\nPágina inválida.\n')

def fix_link(val, url):
	print(bcolors.WARNING + '\n\tArrumando link quebrado ou incompleto %s...' % val)
	if str(val).startswith('../'):
		ct = url.count('/') - 2
		val = url.rsplit("/", ct)[0] + val[2:]
	elif str(val).startswith('/'):
		ct = url.count('/') - 2
		val = url.rsplit("/", ct)[0] + val
	else:
		ct = url.count('/') - 2
		val = url.rsplit("/", ct)[0] + '/' + val
	return val

def do(php):
	try:
		content = requests.get(php)
		soup = BeautifulSoup(content.text, 'lxml')
		mail_look(php)
		link_look(php)
		image_look(php)
	except exceptions.MissingSchema as err:
		print(bcolors.WARNING + '\nURL inválida, protocolo não fornecido. (você quis dizer \'http://%s\'?)\n' % url)

	except exceptions.ConnectionError as err:
		print(bcolors.WARNING + '\nErro de conexão (o site está disponível?)\n')

try:
	content = requests.get(url)
	soup = BeautifulSoup(content.text, 'lxml')
	mail_look(url)
	link_look(url)
	image_look(url)
	if images == set() and links == set() and mails == set():
		isphp = [x['src'] for x in soup.findAll('frame')]
		for php in isphp:
			print('PHP frame detected, redirecting...')
			do(php)
		
except exceptions.MissingSchema as err:
	print(bcolors.WARNING + '\nURL inválida, protocolo não fornecido. (você quis dizer \'http://%s\'?)\n' % url)

except exceptions.ConnectionError as err:
	print(bcolors.WARNING + '\nErro de conexão (o site está disponível?)\n')