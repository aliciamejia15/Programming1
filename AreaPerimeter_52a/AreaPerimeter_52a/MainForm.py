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
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(30, 252)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 23)
		self._button1.TabIndex = 0
		self._button1.Text = "button1"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(134, 251)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(75, 23)
		self._button2.TabIndex = 1
		self._button2.Text = "button2"
		self._button2.UseVisualStyleBackColor = True
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(242, 250)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(75, 23)
		self._button3.TabIndex = 2
		self._button3.Text = "button3"
		self._button3.UseVisualStyleBackColor = True
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.IndianRed
		self._label1.Location = System.Drawing.Point(30, 29)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(118, 23)
		self._label1.TabIndex = 3
		self._label1.Text = "label1"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.IndianRed
		self._label2.Location = System.Drawing.Point(171, 29)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(121, 23)
		self._label2.TabIndex = 4
		self._label2.Text = "label2"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.Brown
		self._label3.Font = System.Drawing.Font("Modern No. 20", 11.999999, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(30, 92)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 35)
		self._label3.TabIndex = 5
		self._label3.Text = "label3"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.Firebrick
		self._label4.Font = System.Drawing.Font("Modern No. 20", 11.999999, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(30, 148)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 34)
		self._label4.TabIndex = 6
		self._label4.Text = "label4"
		# 
		# label5
		# 
		self._label5.Location = System.Drawing.Point(152, 92)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(100, 23)
		self._label5.TabIndex = 7
		self._label5.Text = "label5"
		# 
		# label6
		# 
		self._label6.Location = System.Drawing.Point(152, 159)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(100, 23)
		self._label6.TabIndex = 8
		self._label6.Text = "label6"
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Maroon
		self.ClientSize = System.Drawing.Size(345, 297)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "AreaPerimeter_52a"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		pass