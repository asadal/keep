from pydantic import BaseModel


class WebhookSettings(BaseModel):
    webhookApi: str
    apiKey: str


class ProviderWebhookSettings(BaseModel):
    webhookDescription: str | None = None
    webhookTemplate: str