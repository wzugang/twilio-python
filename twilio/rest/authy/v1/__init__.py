# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base.version import Version
from twilio.rest.authy.v1.form import FormList
from twilio.rest.authy.v1.service import ServiceList


class V1(Version):

    def __init__(self, domain):
        """
        Initialize the V1 version of Authy

        :returns: V1 version of Authy
        :rtype: twilio.rest.authy.v1.V1.V1
        """
        super(V1, self).__init__(domain)
        self.version = 'v1'
        self._services = None
        self._forms = None

    @property
    def services(self):
        """
        :rtype: twilio.rest.authy.v1.service.ServiceList
        """
        if self._services is None:
            self._services = ServiceList(self)
        return self._services

    @property
    def forms(self):
        """
        :rtype: twilio.rest.authy.v1.form.FormList
        """
        if self._forms is None:
            self._forms = FormList(self)
        return self._forms

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Authy.V1>'
