import os
from abc import ABC, abstractmethod


class EmailService:
    def send_email(self, provider_name, message):
        provider = EmailProvider.create(provider_name)
        return provider.send(message)


class EmailProvider(ABC):
    subclasses = {}

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.subclasses[cls._provider] = cls

    @property
    def provider(self):
        return self._provider

    @property
    def api_key(self):
        return self._api_key

    @abstractmethod
    def send(self, message):
        pass

    @classmethod
    def create(cls, provider):
        if provider not in cls.subclasses:
            raise ValueError(f"Not supported provider: {provider}")

        return cls.subclasses[provider]()

    def log_message_sending(self, message):
        print(
            f"Sending email via {self.provider} provider with content: {message}. api key: {self.api_key}"
        )


class SendEmailSendgrid(EmailProvider):
    _provider = "sendgrid"

    def __init__(self, api_key=os.getenv("SENDGRID_API_KEY")):
        self._api_key = api_key

    def send(self, message):
        # Some implementation
        self.log_message_sending(message)
        return True


class SendEmailMailgun(EmailProvider):
    _provider = "mailgun"

    def __init__(self, api_key=os.getenv("MAILGUN_API_KEY")):
        self._api_key = api_key

    def send(self, message):
        # Some implementation
        self.log_message_sending(message)
        return True
