
class User:
	def __init__(self, fabric_user, app, server, vault):
		self.fabuser = fabric_user
		self.app = app
		self.server = server
		self.vault = vault


	def response(self, resp):
		self.update_death_time()

		return {'status': True}


	def loop(self):
		pass