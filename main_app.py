# app de login
from tkinter import *
from tkinter import Tk, ttk, messagebox
import random, os, sys, time
import hashlib
import json
import sys

black = '#000000'
white = '#ffffff'
green = '#3fb5a3'
gray  = '#38576b'
letter = '#403d3d'


def random_number_chance(digite=10, n1=0, n2=9, roll=100, type_return=str):
	number = 0
	digites = ''
	for _ in range(digite):
		for e in range(roll):
			number = random.randint(n1, n2)
		digites += str(number)
	return type_return(digites)

def password_encry(text):
	r'''
		password_encry -> string a ser encriptado
	'''
	# encripta a string em sha256
	return (hashlib.sha256(str(text).encode('utf-8')).hexdigest())

def create_file(file, data=''):
	'''criar um arquivo em um diretorio se tiver algum dado ele vai prescrever aquele dado
	se já existir o arquivo ele so vai passar sem fazer nem uma ação'''
	try:
		# verifica se já existe
		file = open(file, 'r', encoding='utf-8')

	except:
		# se não existir ele vai ser criado um novo
		file = open(file, 'w', encoding='utf-8')
		# se data não for uma string
		if data != '':
			# escreve as infos
			file.write(data)
			
	finally:
		# e para não ter nem um problema ele fecha o arquivo
		file.close()

def write_file(file, data, new=True):
	'''se o arquivo não existir ele criar um novo e prescreve as informações 
	e se o new tiver true ele vai prescrever o novo dado encontrado se não ele vai adicionar'''
	
	# verifica se o fecha já foi criado se não foi ele vai criar um novo
	create_file(file)
	# se for pra criar um novo
	if new:
		# vai zera o fecha deixar sem nem um dado
		file = open(file, 'w', encoding='utf-8')
		# depois ele escrever o novo dado no arquivo
		file.write(data)
		# e para não ter nem um problema ele fecha o arquivo
		file.close()

	# se for pra adicionar informação
	else:
		# ele abri o arquivo para eeditar
		file = open(file, 'a', encoding='utf-8')
		# depois escreve as informações 
		file.write(data)
		# e para não ter nem um problema ele fecha o arquivo
		file.close()

def read_file(file):
	'''ler e retorna uma string'''
	try:
		# vai testar se tem o file pra ler
		file = open(file, 'r', encoding='utf-8')
		# se tiver ele vai pegar tudo que ta no arquivo
		# e armazenar em uma variavel
		read = file.read()
		# fechar o arquivo
		file.close()
		# depois retornar
		return read
	except Exception as e:
		# se não tiver ele so vai retornar
		return e

def clear_widget(*widgets):
	for frames in widgets:
		for widget in frames.winfo_children():
			widget.destroy()
#create_file(file, data='')
file_accounts = 'accounts.json'
default_info = {'000000':{'user':'admin', 'password':password_encry('admin'), 'infos':{'name':'Dev', 'age':24, 'gender':'m'}}}
create_file(file_accounts, json.dumps(default_info))
info = {}
try:
	info = json.loads(read_file(file_accounts))
except:
	info = default_info
base_data = info.copy()

class GAME_LOG(object):
	def __init__(self, title='Title Programmer', size='310x300', background=white):
		self.window = Tk()
		self.window.title(title)
		self.window.geometry(size)
		self.window.configure(background=background)
		self.window.resizable(width=FALSE, height=FALSE)

		self.frame_up = Frame(self.window, width=310, height=50, bg=white, relief='flat')
		self.frame_up.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

		self.frame_down = Frame(self.window, width=310, height=300, bg=white, relief='flat')
		self.frame_down.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)
		self.information_user = {}
		self.screen_login()
		# self.editor_profile()

	def editor_profile(self):
		self.clear_widget()
		def save_info():
			name = new_name.get()
			age = new_age.get()
			if (name != ''):
				self.information_user[1]['infos']['name'] = name
			if (age != ''):
				if (age.isnumeric()):
					self.information_user[1]['infos']["age"] = age
				else:
					messagebox.showinfo('Error', 'So pode numeros inteiros na idade')
			key = self.information_user[0]
			value = self.information_user[1]
			base_data[key] = value.copy()
			write_file(file=file_accounts, data=json.dumps(base_data), new=True)
			messagebox.showinfo('Concluido', 'As Informações Foram Salvas Com Sucesso!')
			self.screen_enter()
		
		button_back = Button(self.frame_up, text='Voltar', width=10, height=2, font=('Ivy 5'))
		button_back.place(x=300-50, y=25)
		
		l_title = Label(self.frame_up, text='Editor de Perfil', height=33, anchor=NE, font=('Ivy 25'), bg=white, fg=gray)
		l_title.place(x=5, y=5)

		l_name = Label(self.frame_down, text='Editar Nome', height=1, anchor=NE, font=('Ivy 15'), bg=white, fg=gray)
		l_name.place(x=5, y=5)

		new_name = Entry(self.frame_down, width=30, highlightthickness=0, relief='solid', font=('Ivy 10'))
		new_name.place(x=5, y=35)

		l_name = Label(self.frame_down, text='Editar Idade', height=1, anchor=NE, font=('Ivy 15'), bg=white, fg=gray)
		l_name.place(x=5, y=55)

		new_age = Entry(self.frame_down, width=30, highlightthickness=0, relief='solid', font=('Ivy 10'))
		new_age.place(x=5, y=85)

		button_save = Button(self.frame_down, text='Salvar', width=26, height=1, font=('Ivy 15'), command=save_info)
		button_save.place(x=5, y=155)

	def clear_widget(self):
		clear_widget(self.frame_down, self.frame_up)

	def screen_enter(self):
		# cria um nome
		self.clear_widget()
		name = self.information_user[1]["infos"]["name"]
		l_name = Label(self.frame_up, text=f'Usuario: {name}', height=1, anchor=NE, font=('Ivy 20'), bg=white, fg=gray)
		l_name.place(x=5, y=5)

		# cria uma linha
		l_line = Label(self.frame_up, width=275, text='', height=1, anchor=NW, font=('Ivy 1 '), bg=green)
		l_line.place(x=10, y=45)

		# cria uma mensagem de bem vindo
		l_name = Label(self.frame_down, text=f'Seja Bem Vindo {name.title()}', height=1, anchor=NE, font=('Ivy 15'), bg=white, fg=gray)
		l_name.place(x=5, y=105)

		b_e_user = Button(self.frame_down, text='Editar Perfil', command=self.editor_profile, width=10, height=1, anchor=NW, font=('Ivy 15'), bg=green)
		b_e_user.place(x=5, y=5)

	def check_password(self):
		name = str(self.e_name.get())
		password = password_encry(str(self.e_pass.get()))
		for key, value in base_data.items():
			if (value['user'] == name and value['password'] == password):
				messagebox.showinfo('Login', 'Seja Muito Bem Vindo')
				self.information_user = [key, value.copy()]
				clear_widget(self.frame_down, self.frame_up)
				self.screen_enter()
				return
			elif (value['user'] == name):
				messagebox.showinfo('Error', 'Nome de Usuario ou a senha não estão corretas')
				return
		else:
			messagebox.showinfo('Error', 'Nome não registrado')
	
	def register_user(self):
		global base_data
		user_name = str(self.e_name.get())
		password_name = str(self.e_pass.get())
		if (not (user_name in base_data)):
			id_gerator = random_number_chance(digite=9, n1=0, n2=9, roll=100, type_return=str)
			while(id_gerator in base_data):
				id_gerator = random_number_chance(digite=9, n1=0, n2=9, roll=100, type_return=str)
			base_data[id_gerator] = {'user':user_name, 'password':password_encry(password_name), 'infos':{'name':'unknown', 'age':None, 'gender':'unknown'}}
			write_file(file=file_accounts, data=json.dumps(base_data), new=True)
			self.clear_widget()
			messagebox.showinfo('Concluido', 'Registro Concluido')
		else:
			messagebox.showinfo('Error', 'Nome Já existente')
		self.screen_login()

	def register_screen(self):
		self.clear_widget()
		frame_up, frame_down = self.frame_up, self.frame_down
		name_1 = Label(frame_up, text='REGISTRAR-SE', height=1, anchor=NE, font=('ivy 25'), bg=white, fg=gray)
		name_1.place(x=5, y=5)

		line_1 = Label(frame_up, width=275, text='', height=1, anchor=NW, font=('Ivy 1 '), bg=green)
		line_1.place(x=10, y=45)

		l_name = Label(frame_down, text='Nome *', height=1, anchor=NW, font=('Ivy 10 bold'), bg=white, fg=gray)
		l_name.place(x=10, y=20)

		self.e_name = Entry(frame_down, width=25, justify='left', font=('', 15), highlightthickness=1, relief='solid')
		self.e_name.place(x=14, y=50)

		l_pass = Label(frame_down, text='password *', height=1, anchor=NW, font=('Ivy 10 bold'), bg=white, fg=gray)
		l_pass.place(x=10, y=95)

		self.e_pass = Entry(frame_down, show='*', width=25, justify='left', font=('', 15), highlightthickness=1, relief='solid')
		self.e_pass.place(x=15, y=130)

		button_confirm = Button(frame_down, text='submit', width=39, height=2, bg=white, command=self.register_user, fg=black, font=('Ivy 8 bold'), relief=RAISED, overrelief=RIDGE)
		button_confirm.place(x=15, y=180)
		
	def screen_login(self):
		self.clear_widget()
		frame_up, frame_down = self.frame_up, self.frame_down
		name_1 = Label(frame_up, text='LOGIN', height=1, anchor=NE, font=('Ivy 25 '), bg=white, fg=gray)
		name_1.place(x=5, y=5)

		button_register = Button(frame_up, text='register', width=10, height=2, bg=white, command=self.register_screen, fg=black, font=('Ivy 8 bold'), relief=RAISED, overrelief=RIDGE)
		button_register.place(x=180, y=5)

		line_1 = Label(frame_up, width=275, text='', height=1, anchor=NW, font=('Ivy 1 '), bg=green)
		line_1.place(x=10, y=45)

		l_name = Label(frame_down, text='Nome *', height=1, anchor=NW, font=('Ivy 10 bold'), bg=white, fg=gray)
		l_name.place(x=10, y=20)

		self.e_name = Entry(frame_down, width=25, justify='left', font=('', 15), highlightthickness=1, relief='solid')
		self.e_name.place(x=14, y=50)

		l_pass = Label(frame_down, text='password *', height=1, anchor=NW, font=('Ivy 10 bold'), bg=white, fg=gray)
		l_pass.place(x=10, y=95)

		self.e_pass = Entry(frame_down, show='*', width=25, justify='left', font=('', 15), highlightthickness=1, relief='solid')
		self.e_pass.place(x=15, y=130)

		button_confirm = Button(frame_down, text='submit', width=39, height=2, bg=white, command=self.check_password, fg=black, font=('Ivy 8 bold'), relief=RAISED, overrelief=RIDGE)
		button_confirm.place(x=15, y=180)


APP = GAME_LOG()
APP.window.mainloop()

