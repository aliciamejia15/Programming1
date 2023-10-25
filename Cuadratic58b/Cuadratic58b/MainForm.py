import math
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label8 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._button3 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button1 = System.Windows.Forms.Button()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label1 = System.Windows.Forms.Label()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._label2 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.LightPink
		self._textBox1.Location = System.Drawing.Point(2, 43)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(128, 20)
		self._textBox1.TabIndex = 23
		self._textBox1.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.Color.Transparent
		self._label8.Font = System.Drawing.Font("Modern No. 20", 11.249999, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label8.ForeColor = System.Drawing.SystemColors.ControlLightLight
		self._label8.Location = System.Drawing.Point(2, 17)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(128, 23)
		self._label8.TabIndex = 21
		self._label8.Text = "A"
		self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.Salmon
		self._label6.Font = System.Drawing.Font("Modern No. 20", 11.249999, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.ForeColor = System.Drawing.SystemColors.ControlText
		self._label6.Location = System.Drawing.Point(181, 172)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(189, 56)
		self._label6.TabIndex = 20
		self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter

		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.Salmon
		self._label5.Font = System.Drawing.Font("Modern No. 20", 11.249999, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.ForeColor = System.Drawing.SystemColors.ControlText
		self._label5.Location = System.Drawing.Point(181, 101)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(189, 56)
		self._label5.TabIndex = 19
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter

		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.Salmon
		self._label4.Font = System.Drawing.Font("Modern No. 20", 11.249999, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.ForeColor = System.Drawing.SystemColors.ControlText
		self._label4.Location = System.Drawing.Point(25, 172)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(150, 56)
		self._label4.TabIndex = 18
		self._label4.Text = "Root 2"
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter

		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.Salmon
		self._label3.Font = System.Drawing.Font("Modern No. 20", 11.249999, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.ForeColor = System.Drawing.SystemColors.ControlText
		self._label3.Location = System.Drawing.Point(25, 101)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(150, 56)
		self._label3.TabIndex = 17
		self._label3.Text = "Root 1"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter

		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.IndianRed
		self._button3.Font = System.Drawing.Font("Modern No. 20", 11.999999, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(271, 260)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(99, 42)
		self._button3.TabIndex = 16
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.IndianRed
		self._button2.Font = System.Drawing.Font("Modern No. 20", 11.999999, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(149, 260)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(99, 42)
		self._button2.TabIndex = 15
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.IndianRed
		self._button1.Font = System.Drawing.Font("Modern No. 20", 11.999999, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(25, 260)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(105, 42)
		self._button1.TabIndex = 14
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.Color.LightPink
		self._textBox2.Location = System.Drawing.Point(136, 43)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(128, 20)
		self._textBox2.TabIndex = 25
		self._textBox2.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Transparent
		self._label1.Font = System.Drawing.Font("Modern No. 20", 11.249999, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.SystemColors.ControlLightLight
		self._label1.Location = System.Drawing.Point(136, 17)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(128, 23)
		self._label1.TabIndex = 24
		self._label1.Text = "B"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textBox3
		# 
		self._textBox3.BackColor = System.Drawing.Color.LightPink
		self._textBox3.Location = System.Drawing.Point(270, 43)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(128, 20)
		self._textBox3.TabIndex = 27
		self._textBox3.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Transparent
		self._label2.Font = System.Drawing.Font("Modern No. 20", 11.249999, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.ForeColor = System.Drawing.SystemColors.ControlLightLight
		self._label2.Location = System.Drawing.Point(270, 17)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(128, 23)
		self._label2.TabIndex = 26
		self._label2.Text = "C"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Maroon
		self.ClientSize = System.Drawing.Size(403, 331)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Cuadratic58b"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Label3Click(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		A = float(self._textBox1.Text)
		B = float(self._textBox2.Text)
		C = float(self._textBox3.Text)
		
		root1 = (-B + math.sqrt(B**2 - 4*A*C))/(2.0*A)
		root2 = (-B - math.sqrt(B**2 - 4*A*C))/(2.0*A)
		
		self._label5.Text="The positive root is " +str(root1)
		self._label6.Text="The negative root is " +str(root2)
		

	def Button3Click(self, sender, e):
		Application.Exit()

	def Button2Click(self, sender, e):
		self._label5.Text=" "
		self._label6.Text=" "
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._textBox3.Text = ""