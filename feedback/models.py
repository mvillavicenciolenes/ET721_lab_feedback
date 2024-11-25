from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)

class Feedback(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="feedbacks")
    comment = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    # Ensure rating is between 1 and 5
    def save(self, *args, **kwargs):
        if self.rating < 1:
            self.rating = 1
        elif self.rating > 5:
            self.rating = 5
        super().save(*args, **kwargs)
