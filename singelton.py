def singelton(class_instance):
	"""Singelton method to instantiate only a single instance of a Class"""

	instances_dict = {}

	def get_instance(*args, **kwargs):
		if class_instance not in instances_dict:
			instances_dict[class_instance] = class_instance(*args, **kwargs)
		return instances_dict[class_instance]

	return get_instance
