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


class ParticipantList(ListResource):

    def __init__(self, version, conversation_sid):
        """
        Initialize the ParticipantList
        
        :param Version version: Version that contains the resource
        :param conversation_sid: The conversation_sid
        
        :returns: ParticipantList
        :rtype: ParticipantList
        """
        super(ParticipantList, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'conversation_sid': conversation_sid,
        }
        self._uri = '/Conversations/{conversation_sid}/Participants'.format(**self._kwargs)

    def stream(self, limit=None, page_size=None, **kwargs):
        """
        Streams ParticipantInstance records from the API as a generator stream.
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
            ParticipantInstance,
            self._kwargs,
            'GET',
            self._uri,
            limits['limit'],
            limits['page_limit'],
            params=params,
        )

    def read(self, limit=None, page_size=None, **kwargs):
        """
        Reads ParticipantInstance records from the API as a list.
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
        Retrieve a single page of ParticipantInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50
        
        :returns: Page of ParticipantInstance
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
            ParticipantInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def create(self, to, from_):
        """
        Create a new ParticipantInstance
        
        :param str to: The to
        :param str from_: The from
        
        :returns: Newly created ParticipantInstance
        :rtype: ParticipantInstance
        """
        data = values.of({
            'To': to,
            'From': from_,
        })
        
        return self._version.create(
            ParticipantInstance,
            self._kwargs,
            'POST',
            self._uri,
            data=data,
        )

    def get(self, sid):
        """
        Constructs a ParticipantContext
        
        :param sid: Contextual sid
        
        :returns: ParticipantContext
        :rtype: ParticipantContext
        """
        return ParticipantContext(self._version, sid=sid, **self._kwargs)

    def __call__(self, sid):
        """
        Constructs a ParticipantContext
        
        :param sid: Contextual sid
        
        :returns: ParticipantContext
        :rtype: ParticipantContext
        """
        return ParticipantContext(self._version, sid=sid, **self._kwargs)

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Conversations.V1.ParticipantList>'


class ParticipantContext(InstanceContext):

    def __init__(self, version, conversation_sid, sid):
        """
        Initialize the ParticipantContext
        
        :param Version version
        :param conversation_sid: Contextual conversation_sid
        :param sid: Contextual sid
        
        :returns: ParticipantContext
        :rtype: ParticipantContext
        """
        super(ParticipantContext, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'conversation_sid': conversation_sid,
            'sid': sid,
        }
        self._uri = '/Conversations/{conversation_sid}/Participants/{sid}'.format(**self._kwargs)

    def fetch(self):
        """
        Fetch a ParticipantInstance
        
        :returns: Fetched ParticipantInstance
        :rtype: ParticipantInstance
        """
        params = values.of({})
        
        return self._version.fetch(
            ParticipantInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._kwargs.items())
        return '<Twilio.Conversations.V1.ParticipantContext {}>'.format(context)


class ParticipantInstance(InstanceResource):

    def __init__(self, version, payload, conversation_sid, sid=None):
        """
        Initialize the ParticipantInstance
        
        :returns: ParticipantInstance
        :rtype: ParticipantInstance
        """
        super(ParticipantInstance, self).__init__(version)
        
        # Marshaled Properties
        self._properties = {
            'sid': payload['sid'],
            'address': payload['address'],
            'status': payload['status'],
            'conversation_sid': payload['conversation_sid'],
            'date_created': deserialize.iso8601_datetime(payload['date_created']),
            'start_time': deserialize.iso8601_datetime(payload['start_time']),
            'end_time': deserialize.iso8601_datetime(payload['end_time']),
            'duration': deserialize.integer(payload['duration']),
            'account_sid': payload['account_sid'],
            'url': payload['url'],
        }
        
        # Context
        self._instance_context = None
        self._kwargs = {
            'conversation_sid': conversation_sid,
            'sid': sid or self._properties['sid'],
        }

    @property
    def _context(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context
        
        :returns: ParticipantContext for this ParticipantInstance
        :rtype: ParticipantContext
        """
        if self._instance_context is None:
            self._instance_context = ParticipantContext(
                self._version,
                self._kwargs['conversation_sid'],
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
    def address(self):
        """
        :returns: The address
        :rtype: str
        """
        return self._properties['address']

    @property
    def status(self):
        """
        :returns: The status
        :rtype: participant.status
        """
        return self._properties['status']

    @property
    def conversation_sid(self):
        """
        :returns: The conversation_sid
        :rtype: str
        """
        return self._properties['conversation_sid']

    @property
    def date_created(self):
        """
        :returns: The date_created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def start_time(self):
        """
        :returns: The start_time
        :rtype: datetime
        """
        return self._properties['start_time']

    @property
    def end_time(self):
        """
        :returns: The end_time
        :rtype: datetime
        """
        return self._properties['end_time']

    @property
    def duration(self):
        """
        :returns: The duration
        :rtype: str
        """
        return self._properties['duration']

    @property
    def account_sid(self):
        """
        :returns: The account_sid
        :rtype: str
        """
        return self._properties['account_sid']

    @property
    def url(self):
        """
        :returns: The url
        :rtype: str
        """
        return self._properties['url']

    def fetch(self):
        """
        Fetch a ParticipantInstance
        
        :returns: Fetched ParticipantInstance
        :rtype: ParticipantInstance
        """
        return self._context.fetch()

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._kwargs.items())
        return '<Twilio.Conversations.V1.ParticipantInstance {}>'.format(context)
