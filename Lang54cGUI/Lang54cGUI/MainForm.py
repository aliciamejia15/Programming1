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
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Modern No. 20", 11.999999, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(4, 172)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(114, 41)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Modern No. 20", 11.999999, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(123, 171)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(114, 41)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Font = System.Drawing.Font("Modern No. 20", 11.999999, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(243, 171)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(114, 41)
		self._button3.TabIndex = 2
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Modern No. 20", 11.249999, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(169, 39)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(152, 24)
		self._textBox1.TabIndex = 3
		self._textBox1.TextChanged += self.TextBox1TextChanged
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Modern No. 20", 15.749999, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.SystemColors.Control
		self._label1.Location = System.Drawing.Point(10, 84)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(165, 57)
		self._label1.TabIndex = 4
		self._label1.Text = "Area"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Snow
		self._label2.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
		self._label2.Font = System.Drawing.Font("Modern No. 20", 11.249999, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(169, 94)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(152, 44)
		self._label2.TabIndex = 5
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label3
		# 
		self._label3.Font = System.Drawing.Font("Modern No. 20", 15.749999, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.ForeColor = System.Drawing.SystemColors.Control
		self._label3.ImageAlign = System.Drawing.ContentAlignment.BottomCenter
		self._label3.Location = System.Drawing.Point(42, 27)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(121, 44)
		self._label3.TabIndex = 6
		self._label3.Text = "Radius "
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.DarkRed
		self.ClientSize = System.Drawing.Size(362, 238)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Lang54cGUI"
		self.ResumeLayout(False)
		self.PerformLayout()


	def TextBox1TextChanged(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		radius = float(self._textBox1.Text)
		
		radius = round(radius, 3)
		
		pi = 3.14159
		
		area = (pi * (radius**2))
		
		area = round(area, 3)  
		
		self._label2.Text="The area is " + str(area)
		
		

	def Button2Click(self, sender, e):
		self._label2.Text= " "
		self._textBox1.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()