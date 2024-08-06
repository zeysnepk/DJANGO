from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Article(models.Model):
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, verbose_name = "Author")
    title = models.CharField(max_length=50)
    content = RichTextField()
    date = models.DateTimeField(auto_now_add=True)
    article_image = models.FileField(blank=True, null=True, verbose_name="Article Image")
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-date']
    
# Create your models here.
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name = "Article", related_name="comments")
    comment_name = models.ForeignKey("auth.User", on_delete=models.CASCADE, verbose_name="Name")
    comment_content = models.CharField(max_length=300, verbose_name="Comment")
    comment_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.comment_name)
    
    class Meta:
        ordering = ['-comment_date' ]
    