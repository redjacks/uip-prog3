
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import StringProperty
import random

pregResp = [ ("Panama tiene mas de cien distritos.", 0), ("Panama cuenta con 5 comarcas indigenas.", 1), 
			("Presidente actual: Ricardo Martinelli", 0), ("Fundacion de la ciudad de Panama: 15 de agosto de 1519.", 1),
			("Panama tiene frontera con Colombia y Nicaragua.", 0) ]
			

pts = 0
i = 0


		
class YourWidget(Widget):
	pregunta = StringProperty()

	def __init__(self, **kwargs):
		global i
		i = random.randint(0, 4)
		super(YourWidget, self).__init__(**kwargs)
		self.pregunta = str(pregResp[i][0])
	
	def sumarPts(self,resp):
		global pts
		
		if resp == pregResp[i][1]:
		
			print("correcto")
			pts += 10 
			print("total de puntos: " + str(pts))
			
		else:
			print("equivocado")
			print("total de puntos: " + str(pts))
			

	def change_text(self):
		global i
		i = random.randint(0, 4)
		self.pregunta = str(pregResp[i][0])
		return i

class YourApp(App):
	def build(self):
		return YourWidget()
	
	

if __name__ == '__main__':
	YourApp().run()