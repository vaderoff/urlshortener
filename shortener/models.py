from django.db import models
import binascii


class UrlModel(models.Model):
    origin_url = models.URLField()
    hash_url = models.IntegerField(unique=True)

    def generate_hash(self):
        return binascii.crc32(self.origin_url.encode())

    def save(self, *args, **kwargs):
        if not self.hash_url:
            self.hash_url = self.generate_hash()
        super(UrlModel, self).save(*args, **kwargs)
