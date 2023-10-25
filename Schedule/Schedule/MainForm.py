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
		self._button1.Font = System.Drawing.Font("Modern No. 20", 14.249999, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(294, 231)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 36)
		self._button1.TabIndex = 0
		self._button1.Text = "Show"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Modern No. 20", 14.249999, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(294, 274)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(75, 36)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Modern No. 20", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.Color.White
		self._label1.Location = System.Drawing.Point(12, 36)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(276, 46)
		self._label1.TabIndex = 2
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label1.Click += self.Label1Click
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("Modern No. 20", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.ForeColor = System.Drawing.Color.White
		self._label2.Location = System.Drawing.Point(12, 64)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(276, 41)
		self._label2.TabIndex = 3
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label3
		# 
		self._label3.Font = System.Drawing.Font("Modern No. 20", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.ForeColor = System.Drawing.Color.White
		self._label3.Location = System.Drawing.Point(12, 91)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(276, 41)
		self._label3.TabIndex = 4
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label4
		# 
		self._label4.Font = System.Drawing.Font("Modern No. 20", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.ForeColor = System.Drawing.Color.White
		self._label4.Location = System.Drawing.Point(12, 118)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(276, 41)
		self._label4.TabIndex = 5
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label5
		# 
		self._label5.Font = System.Drawing.Font("Modern No. 20", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.ForeColor = System.Drawing.Color.White
		self._label5.Location = System.Drawing.Point(12, 145)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(276, 41)
		self._label5.TabIndex = 6
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label6
		# 
		self._label6.Font = System.Drawing.Font("Modern No. 20", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.ForeColor = System.Drawing.Color.White
		self._label6.Location = System.Drawing.Point(12, 172)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(276, 41)
		self._label6.TabIndex = 7
		self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label6.Click += self.Label6Click
		# 
		# label7
		# 
		self._label7.Font = System.Drawing.Font("Modern No. 20", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.ForeColor = System.Drawing.Color.White
		self._label7.Location = System.Drawing.Point(12, 199)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(276, 41)
		self._label7.TabIndex = 8
		self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label8
		# 
		self._label8.Font = System.Drawing.Font("Modern No. 20", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label8.ForeColor = System.Drawing.Color.White
		self._label8.Location = System.Drawing.Point(12, 226)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(276, 41)
		self._label8.TabIndex = 9
		self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Maroon
		self.ClientSize = System.Drawing.Size(381, 322)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Schedule"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		self._label1.Text="Block1: Writing through Film "
		self._label2.Text="Block2: Biomed "
		self._label3.Text="Block3: Computer Programming "
		self._label4.Text="Block4: Precalculus "
		self._label5.Text="Block5: English"
		self._label6.Text="Block6: International Seminar "
		self._label7.Text="Block7: PE"
		self._label8.Text="Block8: Forensic Science "

	def Label1Click(self, sender, e):
		pass

	def Button2Click(self, sender, e):
		self._label1.Text=" "
		self._label2.Text=" "
		self._label3.Text=" "
		self._label4.Text=" "
		self._label5.Text=" "
		self._label6.Text=" "
		self._label7.Text=" "
		self._label8.Text=" "

	def Label6Click(self, sender, e):
		pass