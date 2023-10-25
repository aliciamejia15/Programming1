import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._listBox1 = System.Windows.Forms.ListBox()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Papyrus", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(12, 223)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(134, 37)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Papyrus", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(161, 223)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(134, 37)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		# 
		# button3
		# 
		self._button3.Font = System.Drawing.Font("Papyrus", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(312, 223)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(134, 37)
		self._button3.TabIndex = 2
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		# 
		# listBox1
		# 
		self._listBox1.Font = System.Drawing.Font("Papyrus", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._listBox1.FormattingEnabled = True
		self._listBox1.ItemHeight = 25
		self._listBox1.Location = System.Drawing.Point(7, 5)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(468, 204)
		self._listBox1.TabIndex = 3
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.SpringGreen
		self.ClientSize = System.Drawing.Size(482, 272)
		self.Controls.Add(self._listBox1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Pro122i"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		heading = "Number\t\tCube Root\t\tCube"
		self._listBox1.Items.Add(heading)
		
		for num in range(-25,25+1): 
			cuberoot =  num ** (1. / 3) 
			cube = num*num*num
			
			
			msg = str(num) +"\t\t" + str(round(cuberoot, 4)) +  "\t\t" + str(cube) 
			self._listBox1.Items.Add(msg)
			