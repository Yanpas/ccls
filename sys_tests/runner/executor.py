import asyncio
from asyncio.subprocess import create_subprocess_exec, PIPE
import sys

class Executor:
	def __init__(self, executable, project):
		self.executable = executable
		self.project = project
		self.module = None

	def run(self):
		self.loadTest()
		asyncio.run(self._runSuite())

	def loadTest(self):
		sys.path.append(self.project)
		self.module = __import__("cclstest")

	async def _runSuite(self):
		proc = await create_subprocess_exec(self.executable, "-log-file=/dev/stderr",
				stdin=PIPE,
				stdout=PIPE,
				#stderr=PIPE,
				cwd=self.project)
		try:
			req = '''{
				"jsonrpc": "2.0",
				"id": 0,
				"method": "exit",
			}'''
			proc.stdin.write(f"Content-Length: {len(req.encode())}\r\n\r\n{req}".encode())
			resp = await proc.stdout.read()
			print(resp)
			await self.module.run()
		finally:
			try:
				proc.kill()
			except Exception:
				pass
			await proc.wait()
