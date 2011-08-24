from django.db import models


class Category(models.Model):
    """
    Category model to be used for categorization of content. Categories are
    high level constructs to be used for grouping and organizing content,
    thus creating a site's table of contents.
    """
    title = models.CharField(
        max_length=200,
        help_text='Short descriptive name for this category.',
    )
    slug = models.SlugField(
        max_length=255,
        db_index=True,
        unique=True,
        help_text='Short descriptive unique name for use in urls.',
    )

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ('title',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class Tag(models.Model):
    """
    Tag model to be used for tagging content. Tags are to be used to describe
    your content in more detail, in essence providing keywords associated with
    your content. Tags can also be seen as micro-categorization of a site's
    content.
    """
    title = models.CharField(
        max_length=200,
        help_text='Short descriptive name for this tag.',
    )
    slug = models.SlugField(
        max_length=255,
        db_index=True,
        unique=True,
        help_text='Short descriptive unique name for use in urls.',
    )
    categories = models.ManyToManyField(
        'category.Category',
        blank=True,
        null=True,
        help_text='Categories to which this tag belongs.'
    )

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ('title',)
        verbose_name = 'tag'
        verbose_name_plural = 'tags'
