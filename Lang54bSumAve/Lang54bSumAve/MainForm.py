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
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._textBox4 = System.Windows.Forms.TextBox()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Modern No. 20", 11.999999, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(13, 266)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(85, 34)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Modern No. 20", 11.999999, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(132, 265)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(75, 34)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Font = System.Drawing.Font("Modern No. 20", 11.999999, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(240, 265)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(75, 34)
		self._button3.TabIndex = 2
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Modern No. 20", 11.249999, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(12, 43)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(128, 24)
		self._textBox1.TabIndex = 3
		self._textBox1.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
		# 
		# textBox2
		# 
		self._textBox2.Font = System.Drawing.Font("Modern No. 20", 11.249999, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(12, 97)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(128, 24)
		self._textBox2.TabIndex = 4
		self._textBox2.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
		# 
		# textBox3
		# 
		self._textBox3.Font = System.Drawing.Font("Modern No. 20", 11.249999, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox3.Location = System.Drawing.Point(12, 151)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(128, 24)
		self._textBox3.TabIndex = 5
		self._textBox3.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
		# 
		# textBox4
		# 
		self._textBox4.Font = System.Drawing.Font("Modern No. 20", 11.249999, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox4.Location = System.Drawing.Point(13, 209)
		self._textBox4.Name = "textBox4"
		self._textBox4.Size = System.Drawing.Size(128, 24)
		self._textBox4.TabIndex = 6
		self._textBox4.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.DarkRed
		self._label1.Font = System.Drawing.Font("Modern No. 20", 11.999999, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(194, 46)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 34)
		self._label1.TabIndex = 7
		self._label1.Text = "SUM"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Gainsboro
		self._label2.Font = System.Drawing.Font("Modern No. 20", 11.999999, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(170, 80)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(145, 34)
		self._label2.TabIndex = 8
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label2.Click += self.Label2Click
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.DarkRed
		self._label3.Font = System.Drawing.Font("Modern No. 20", 11.999999, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(194, 138)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 34)
		self._label3.TabIndex = 9
		self._label3.Text = "AVERAGE"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.Gainsboro
		self._label4.Font = System.Drawing.Font("Modern No. 20", 11.999999, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(170, 172)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(145, 34)
		self._label4.TabIndex = 10
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label4.Click += self.Label4Click
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.Transparent
		self._label5.Font = System.Drawing.Font("Modern No. 20", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.ForeColor = System.Drawing.SystemColors.Control
		self._label5.Location = System.Drawing.Point(13, 17)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(100, 23)
		self._label5.TabIndex = 11
		self._label5.Text = "Num1"
		self._label5.TextAlign = System.Drawing.ContentAlignment.BottomLeft
		self._label5.Click += self.Label5Click
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.Transparent
		self._label6.Font = System.Drawing.Font("Modern No. 20", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.ForeColor = System.Drawing.SystemColors.ButtonHighlight
		self._label6.Location = System.Drawing.Point(13, 71)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(100, 23)
		self._label6.TabIndex = 12
		self._label6.Text = "Num2"
		self._label6.TextAlign = System.Drawing.ContentAlignment.BottomLeft
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.Transparent
		self._label7.Font = System.Drawing.Font("Modern No. 20", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.ForeColor = System.Drawing.SystemColors.ControlLight
		self._label7.Location = System.Drawing.Point(13, 125)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(100, 23)
		self._label7.TabIndex = 13
		self._label7.Text = "Num3"
		self._label7.TextAlign = System.Drawing.ContentAlignment.BottomLeft
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.Color.Transparent
		self._label8.Font = System.Drawing.Font("Modern No. 20", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label8.ForeColor = System.Drawing.SystemColors.ControlLight
		self._label8.Location = System.Drawing.Point(12, 183)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(100, 23)
		self._label8.TabIndex = 14
		self._label8.Text = "Num4"
		self._label8.TextAlign = System.Drawing.ContentAlignment.BottomLeft
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.DarkRed
		self.ClientSize = System.Drawing.Size(343, 312)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._textBox4)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Lang54bSumAve"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Label5Click(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		
		num1 = int(self._textBox1.Text)
		num2 = int(self._textBox2.Text)
		num3 = int(self._textBox3.Text)
		num4 = int(self._textBox4.Text)
		
		Sum = num1+num2+num3+num4
		average = ((num1+num2+num3+num4)/4.0)
		
		self._label2.Text="The sum of the numbers is " + str(Sum)
		self._label4.Text="The average of the numbers is " + str(average)

	def Label2Click(self, sender, e):
		pass

	def Label4Click(self, sender, e):
		pass

	def Button2Click(self, sender, e):
		self._label4.Text=" "
		self._label2.Text=" "
		self._textBox1.Text=" "
		self._textBox2.Text=" "
		self._textBox3.Text=" "
		self._textBox4.Text=" "

	def Button3Click(self, sender, e):
		Application.Exit()