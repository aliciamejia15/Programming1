import math
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
		self._listBox1.Font = System.Drawing.Font("Modern No. 20", 14.249999, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._listBox1.FormattingEnabled = True
		self._listBox1.ItemHeight = 21
		self._listBox1.Location = System.Drawing.Point(0, 0)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(423, 277)
		self._listBox1.TabIndex = 0
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Modern No. 20", 11.999999, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.RoyalBlue
		self._button1.Location = System.Drawing.Point(13, 303)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(90, 36)
		self._button1.TabIndex = 1
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Modern No. 20", 11.999999, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.Color.RoyalBlue
		self._button2.Location = System.Drawing.Point(143, 303)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(91, 36)
		self._button2.TabIndex = 2
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Font = System.Drawing.Font("Modern No. 20", 11.999999, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.Color.RoyalBlue
		self._button3.Location = System.Drawing.Point(295, 303)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(86, 36)
		self._button3.TabIndex = 3
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.LightSkyBlue
		self.ClientSize = System.Drawing.Size(420, 358)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._listBox1)
		self.Name = "MainForm"
		self.Text = "Square122a"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		heading = "Number\t\tSquare\t\tsquare\t\tSquare Root"
		self._listBox1.Items.Add(heading)
		
		for num in range(1,50+1): 
			nsqrd=num**2
			nsqrt = math.sqrt(num)
			
			msg = str(num) +"\t\t" + str(nsqrd) +  "\t\t" + str(round(nsqrt, 4))
			
			self._listBox1.Items.Add(msg)
 
	def Button2Click(self, sender, e):
		self._listBox1.Items.Clear()
		