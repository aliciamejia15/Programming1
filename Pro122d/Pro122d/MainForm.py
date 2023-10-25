import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._listBox1 = System.Windows.Forms.ListBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# listBox1
		# 
		self._listBox1.Font = System.Drawing.Font("Mongolian Baiti", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._listBox1.FormattingEnabled = True
		self._listBox1.ItemHeight = 16
		self._listBox1.Location = System.Drawing.Point(3, 2)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(301, 164)
		self._listBox1.TabIndex = 0
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Mongolian Baiti", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(5, 172)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(92, 37)
		self._button1.TabIndex = 1
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Mongolian Baiti", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(103, 172)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(92, 37)
		self._button2.TabIndex = 2
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Font = System.Drawing.Font("Mongolian Baiti", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(206, 172)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(92, 37)
		self._button3.TabIndex = 3
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.LightSkyBlue
		self.ClientSize = System.Drawing.Size(306, 217)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._listBox1)
		self.Name = "MainForm"
		self.Text = "Pro122d"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		
		
		for x in range(-12,16+1): 
			
			y = ((x*x*x*x*x*x) - (3*(x*x*x*x*x)) - (93*(x*x*x*x)) + (87*(x*x*x)) + 1596*(x**2) - (1380*x) - 2800)
			
			
			msg = str(x) +"\t\t" + str(y) 
			
			self._listBox1.Items.Add(msg)

	def Button2Click(self, sender, e):
		self._listBox1.Text = " " 

	def Button3Click(self, sender, e):
		Application.Exit()