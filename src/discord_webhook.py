import requests

class DiscordWebhook:
    def __init__(self, webhook_url: str):
        """
        Inicializa a classe com a URL do Webhook do Discord.
        """
        self.webhook_url = webhook_url

    def send_message(self, content: str, username: str = "Bot", avatar_url: str = None):
        """
        Envia uma mensagem para o canal do Discord via Webhook.
        
        :param content: Conteúdo da mensagem a ser enviada.
        :param username: Nome do bot que enviará a mensagem (opcional).
        :param avatar_url: URL do avatar do bot (opcional).
        """

        payload = {
            "content": content[:2000], # content precisa ser no maximo 2000 caracteres.
            "username": username
        }
        if avatar_url:
            payload["avatar_url"] = avatar_url

        response = requests.post(self.webhook_url, json=payload)
        
        if response.status_code != 204:
            raise Exception(f"Erro ao enviar mensagem: {response.status_code} - {response.text}")
        
        return response