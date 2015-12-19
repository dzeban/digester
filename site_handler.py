from importlib import import_module

def get_content(site):
	"""Dynamically invoke site handler depending on 'type' in config"""
	handler = import_module(site['type'])
	return handler.get_content(site['data'])