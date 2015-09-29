# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from twilio import values
from twilio.rest import deserialize
from twilio.rest.base import InstanceContext
from twilio.rest.base import InstanceResource
from twilio.rest.base import ListResource


class CredentialList(ListResource):

    def __init__(self, version, account_sid, credential_list_sid):
        """
        Initialize the CredentialList
        
        :param Version version: Version that contains the resource
        :param account_sid: The account_sid
        :param credential_list_sid: The credential_list_sid
        
        :returns: CredentialList
        :rtype: CredentialList
        """
        super(CredentialList, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'account_sid': account_sid,
            'credential_list_sid': credential_list_sid,
        }
        self._uri = '/Accounts/{account_sid}/SIP/CredentialLists/{credential_list_sid}/Credentials.json'.format(**self._kwargs)

    def stream(self, limit=None, page_size=None, **kwargs):
        """
        Streams CredentialInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)
        
        :returns: Generator that will yield up to limit results
        :rtype: generator
        """
        limits = self._version.read_limits(limit, page_size)
        
        params = values.of({
            'PageSize': limits['page_size'],
        })
        params.update(kwargs)
        
        return self._version.stream(
            self,
            CredentialInstance,
            self._kwargs,
            'GET',
            self._uri,
            limits['limit'],
            limits['page_limit'],
            params=params,
        )

    def read(self, limit=None, page_size=None, **kwargs):
        """
        Reads CredentialInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. read() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, read() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)
        
        :returns: Generator that will yield up to limit results
        :rtype: generator
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
            **kwargs
        ))

    def page(self, page_token=None, page_number=None, page_size=None, **kwargs):
        """
        Retrieve a single page of CredentialInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50
        
        :returns: Page of CredentialInstance
        :rtype: Page
        """
        params = values.of({
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })
        params.update(kwargs)
        
        return self._version.page(
            self,
            CredentialInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def create(self, username, password):
        """
        Create a new CredentialInstance
        
        :param str username: The username
        :param str password: The password
        
        :returns: Newly created CredentialInstance
        :rtype: CredentialInstance
        """
        data = values.of({
            'Username': username,
            'Password': password,
        })
        
        return self._version.create(
            CredentialInstance,
            self._kwargs,
            'POST',
            self._uri,
            data=data,
        )

    def get(self, sid):
        """
        Constructs a CredentialContext
        
        :param sid: Contextual sid
        
        :returns: CredentialContext
        :rtype: CredentialContext
        """
        return CredentialContext(self._version, sid=sid, **self._kwargs)

    def __call__(self, sid):
        """
        Constructs a CredentialContext
        
        :param sid: Contextual sid
        
        :returns: CredentialContext
        :rtype: CredentialContext
        """
        return CredentialContext(self._version, sid=sid, **self._kwargs)

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.CredentialList>'


class CredentialContext(InstanceContext):

    def __init__(self, version, account_sid, credential_list_sid, sid):
        """
        Initialize the CredentialContext
        
        :param Version version
        :param account_sid: Contextual account_sid
        :param credential_list_sid: Contextual credential_list_sid
        :param sid: Contextual sid
        
        :returns: CredentialContext
        :rtype: CredentialContext
        """
        super(CredentialContext, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'account_sid': account_sid,
            'credential_list_sid': credential_list_sid,
            'sid': sid,
        }
        self._uri = '/Accounts/{account_sid}/SIP/CredentialLists/{credential_list_sid}/Credentials/{sid}.json'.format(**self._kwargs)

    def fetch(self):
        """
        Fetch a CredentialInstance
        
        :returns: Fetched CredentialInstance
        :rtype: CredentialInstance
        """
        params = values.of({})
        
        return self._version.fetch(
            CredentialInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def update(self, username, password):
        """
        Update the CredentialInstance
        
        :param str username: The username
        :param str password: The password
        
        :returns: Updated CredentialInstance
        :rtype: CredentialInstance
        """
        data = values.of({
            'Username': username,
            'Password': password,
        })
        
        return self._version.update(
            CredentialInstance,
            self._kwargs,
            'POST',
            self._uri,
            data=data,
        )

    def delete(self):
        """
        Deletes the CredentialInstance
        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete('delete', self._uri)

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._kwargs.items())
        return '<Twilio.Api.V2010.CredentialContext {}>'.format(context)


class CredentialInstance(InstanceResource):

    def __init__(self, version, payload, account_sid, credential_list_sid,
                 sid=None):
        """
        Initialize the CredentialInstance
        
        :returns: CredentialInstance
        :rtype: CredentialInstance
        """
        super(CredentialInstance, self).__init__(version)
        
        # Marshaled Properties
        self._properties = {
            'sid': payload['sid'],
            'account_sid': payload['account_sid'],
            'credential_list_sid': payload['credential_list_sid'],
            'username': payload['username'],
            'friendly_name': payload['friendly_name'],
            'date_created': deserialize.rfc2822_datetime(payload['date_created']),
            'date_updated': deserialize.rfc2822_datetime(payload['date_updated']),
            'uri': payload['uri'],
        }
        
        # Context
        self._instance_context = None
        self._kwargs = {
            'account_sid': account_sid,
            'credential_list_sid': credential_list_sid,
            'sid': sid or self._properties['sid'],
        }

    @property
    def _context(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context
        
        :returns: CredentialContext for this CredentialInstance
        :rtype: CredentialContext
        """
        if self._instance_context is None:
            self._instance_context = CredentialContext(
                self._version,
                self._kwargs['account_sid'],
                self._kwargs['credential_list_sid'],
                self._kwargs['sid'],
            )
        return self._instance_context

    @property
    def sid(self):
        """
        :returns: The sid
        :rtype: str
        """
        return self._properties['sid']

    @property
    def account_sid(self):
        """
        :returns: The account_sid
        :rtype: str
        """
        return self._properties['account_sid']

    @property
    def credential_list_sid(self):
        """
        :returns: The credential_list_sid
        :rtype: str
        """
        return self._properties['credential_list_sid']

    @property
    def username(self):
        """
        :returns: The username
        :rtype: str
        """
        return self._properties['username']

    @property
    def friendly_name(self):
        """
        :returns: The friendly_name
        :rtype: str
        """
        return self._properties['friendly_name']

    @property
    def date_created(self):
        """
        :returns: The date_created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The date_updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def uri(self):
        """
        :returns: The uri
        :rtype: str
        """
        return self._properties['uri']

    def fetch(self):
        """
        Fetch a CredentialInstance
        
        :returns: Fetched CredentialInstance
        :rtype: CredentialInstance
        """
        return self._context.fetch()

    def update(self, username, password):
        """
        Update the CredentialInstance
        
        :param str username: The username
        :param str password: The password
        
        :returns: Updated CredentialInstance
        :rtype: CredentialInstance
        """
        return self._context.update(
            username,
            password,
        )

    def delete(self):
        """
        Deletes the CredentialInstance
        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._context.delete()

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._kwargs.items())
        return '<Twilio.Api.V2010.CredentialInstance {}>'.format(context)
