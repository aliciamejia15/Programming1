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
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.IndianRed
		self._button1.Font = System.Drawing.Font("Modern No. 20", 11.999999, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(27, 271)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(99, 31)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.IndianRed
		self._button2.Font = System.Drawing.Font("Modern No. 20", 11.999999, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(151, 271)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(93, 31)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.IndianRed
		self._button3.Font = System.Drawing.Font("Modern No. 20", 11.999999, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(273, 271)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(93, 31)
		self._button3.TabIndex = 2
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.Salmon
		self._label3.Font = System.Drawing.Font("Modern No. 20", 11.249999, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.ForeColor = System.Drawing.SystemColors.ControlText
		self._label3.Location = System.Drawing.Point(17, 113)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(144, 45)
		self._label3.TabIndex = 5
		self._label3.Text = "Perimeter"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label3.Click += self.Label3Click
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.Salmon
		self._label4.Font = System.Drawing.Font("Modern No. 20", 11.249999, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.ForeColor = System.Drawing.SystemColors.ControlText
		self._label4.Location = System.Drawing.Point(17, 184)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(144, 45)
		self._label4.TabIndex = 6
		self._label4.Text = "Area"
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label4.Click += self.Label4Click
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.Salmon
		self._label5.Font = System.Drawing.Font("Modern No. 20", 11.249999, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.ForeColor = System.Drawing.SystemColors.ControlText
		self._label5.Location = System.Drawing.Point(173, 113)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(183, 45)
		self._label5.TabIndex = 7
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.Salmon
		self._label6.Font = System.Drawing.Font("Modern No. 20", 11.249999, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.ForeColor = System.Drawing.SystemColors.ControlText
		self._label6.Location = System.Drawing.Point(173, 184)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(183, 45)
		self._label6.TabIndex = 8
		self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.Color.Transparent
		self._label8.Font = System.Drawing.Font("Modern No. 20", 11.249999, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label8.ForeColor = System.Drawing.SystemColors.ControlLightLight
		self._label8.Location = System.Drawing.Point(7, 34)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(173, 23)
		self._label8.TabIndex = 10
		self._label8.Text = "Width"
		self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label8.Click += self.Label8Click
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.Transparent
		self._label7.Font = System.Drawing.Font("Modern No. 20", 11.249999, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.ForeColor = System.Drawing.SystemColors.ControlLightLight
		self._label7.Location = System.Drawing.Point(193, 34)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(173, 23)
		self._label7.TabIndex = 11
		self._label7.Text = "Lenght"
		self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label7.Click += self.Label7Click
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.LightPink
		self._textBox1.Location = System.Drawing.Point(7, 60)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(173, 20)
		self._textBox1.TabIndex = 12
		self._textBox1.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.Color.LightPink
		self._textBox2.Location = System.Drawing.Point(195, 60)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(171, 20)
		self._textBox2.TabIndex = 13
		self._textBox2.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Maroon
		self.ClientSize = System.Drawing.Size(378, 318)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "AreaPerimeter"
		self.Load += self.MainFormLoad
		self.ResumeLayout(False)
		self.PerformLayout()


	def MainFormLoad(self, sender, e):
		pass

	def Button2Click(self, sender, e):
		self._label5.Text=" "
		self._label6.Text=" "
		self._textBox1.Text=" "
		self._textBox2.Text=" "

	def Label8Click(self, sender, e):
		pass

	def Label7Click(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		
		width = int(self._textBox1.Text)
		lenght = int(self._textBox2.Text)
		
		area = width*lenght
		perimeter = (2*width)+(2*lenght)
		
		self._label5.Text="The area of the rectangle is " + str(area)
		self._label6.Text="The perimeter of the rectangle is " + str(perimeter)

	def Label3Click(self, sender, e):
		pass

	def Label4Click(self, sender, e):
		pass

	def Button3Click(self, sender, e):
		Application.Exit()