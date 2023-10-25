import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._button4 = System.Windows.Forms.Button()
		self._button5 = System.Windows.Forms.Button()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Modern No. 20", 21.7499981, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.SystemColors.ControlLight
		self._label1.Location = System.Drawing.Point(28, 35)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(330, 33)
		self._label1.TabIndex = 0
		self._label1.Text = "Phone Numbers List"
		self._label1.Click += self.Label1Click
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("Mongolian Baiti", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.ForeColor = System.Drawing.Color.White
		self._label2.Location = System.Drawing.Point(182, 102)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(142, 21)
		self._label2.TabIndex = 1
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Modern No. 20", 11.999999, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(43, 100)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(116, 23)
		self._button1.TabIndex = 2
		self._button1.Text = "McDonald's"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Modern No. 20", 11.999999, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(43, 149)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(116, 23)
		self._button2.TabIndex = 3
		self._button2.Text = "Starbucks"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Font = System.Drawing.Font("Modern No. 20", 11.999999, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(43, 194)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(116, 23)
		self._button3.TabIndex = 4
		self._button3.Text = "Chick-fil-A"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# button4
		# 
		self._button4.Font = System.Drawing.Font("Modern No. 20", 11.999999, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button4.Location = System.Drawing.Point(43, 236)
		self._button4.Name = "button4"
		self._button4.Size = System.Drawing.Size(116, 23)
		self._button4.TabIndex = 5
		self._button4.Text = "LongHorn "
		self._button4.UseVisualStyleBackColor = True
		self._button4.Click += self.Button4Click
		# 
		# button5
		# 
		self._button5.Font = System.Drawing.Font("Modern No. 20", 11.999999, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button5.Location = System.Drawing.Point(43, 282)
		self._button5.Name = "button5"
		self._button5.Size = System.Drawing.Size(116, 23)
		self._button5.TabIndex = 6
		self._button5.Text = "KFC "
		self._button5.UseVisualStyleBackColor = True
		self._button5.Click += self.Button5Click
		# 
		# label3
		# 
		self._label3.Font = System.Drawing.Font("Mongolian Baiti", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.ForeColor = System.Drawing.Color.White
		self._label3.Location = System.Drawing.Point(182, 150)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(142, 23)
		self._label3.TabIndex = 7
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label3.Click += self.Label3Click
		# 
		# label4
		# 
		self._label4.Font = System.Drawing.Font("Mongolian Baiti", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.ForeColor = System.Drawing.Color.White
		self._label4.Location = System.Drawing.Point(182, 194)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(142, 23)
		self._label4.TabIndex = 8
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label5
		# 
		self._label5.Font = System.Drawing.Font("Mongolian Baiti", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.ForeColor = System.Drawing.Color.White
		self._label5.Location = System.Drawing.Point(182, 236)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(142, 23)
		self._label5.TabIndex = 9
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label6
		# 
		self._label6.Font = System.Drawing.Font("Mongolian Baiti", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.ForeColor = System.Drawing.Color.White
		self._label6.Location = System.Drawing.Point(182, 282)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(142, 23)
		self._label6.TabIndex = 10
		self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Maroon
		self.ClientSize = System.Drawing.Size(512, 328)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._button5)
		self.Controls.Add(self._button4)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "PhoneNumbers"
		self.ResumeLayout(False)


	def Label1Click(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		self._label2.Text="(608) 752-0100"

	def Button2Click(self, sender, e):
		self._label3.Text="(608) 754-8331"

	def Label3Click(self, sender, e):
		pass

	def Button3Click(self, sender, e):
		self._label4.Text="(608) 531-1991"

	def Button5Click(self, sender, e):
		self._label6.Text="(608) 754-0811"

	def Button4Click(self, sender, e):
		self._label5.Text="(608) 836-1830"