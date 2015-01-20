import os
from abc import ABCMeta, abstractmethod

class BaseRss(object):
	__metaclass__=ABCMeta


	@abstractmethod
	def send(self,message):
		pass
