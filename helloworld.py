import plugin_interface as plugintypes

class PluginPrint(plugintypes.IPluginExtended):
	def activate(self):
		print "Hello World activated"
	
	# called with each new sample
	def __call__(self, sample):
		if sample:
			print ("Channel 3: ")
			print (sample.channel_data[3])
			print ("Channel 4: ")
			print sample.channel_data[4]
			sample_string = "ID: %f\n%s" %(sample.id, str(sample.channel_data)[1:-1])
			print "---------------------------------"
			# if (sample.channel_data[4] > 4000):
			# 	print "hello world!"


				
		
		# DEBBUGING
		# try:
		#     sample_string.decode('ascii')
		# except UnicodeDecodeError:
		#     print "Not a ascii-encoded unicode string"
		# else:
		#     print sample_string
		