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
		self._listBox1.FormattingEnabled = True
		self._listBox1.Location = System.Drawing.Point(0, 2)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(298, 186)
		self._listBox1.TabIndex = 0
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(13, 214)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 23)
		self._button1.TabIndex = 1
		self._button1.Text = "button1"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(115, 214)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(75, 23)
		self._button2.TabIndex = 2
		self._button2.Text = "button2"
		self._button2.UseVisualStyleBackColor = True
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(223, 214)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(75, 23)
		self._button3.TabIndex = 3
		self._button3.Text = "button3"
		self._button3.UseVisualStyleBackColor = True
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(299, 249)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._listBox1)
		self.Name = "MainForm"
		self.Text = "Pro122c"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
				
		for num in range(2,10+1,2): 
			num1 = num + 2
			num2=num1+1
			num3=num1*2
			num4=num1**2
			
			msg = str(num1) +"\t\t" + str(num2) +  "\t\t" + str(num3) + "\t\t" + str(num4)
			
			self._listBox1.Items.Add(msg)